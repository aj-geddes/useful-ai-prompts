---
name: health-check-endpoints
description: Implement comprehensive health check endpoints for liveness, readiness, and dependency monitoring. Use when deploying to Kubernetes, implementing load balancer health checks, or monitoring service availability.
---

# Health Check Endpoints

## Overview

Implement health check endpoints to monitor service health, dependencies, and readiness for traffic.

## When to Use

- Kubernetes liveness and readiness probes
- Load balancer health checks
- Service discovery and registration
- Monitoring and alerting systems
- Circuit breaker decisions
- Auto-scaling triggers
- Deployment verification

## Health Check Types

| Type | Purpose | Failure Action |
|------|---------|----------------|
| **Liveness** | Process is running | Restart container |
| **Readiness** | Ready for traffic | Remove from load balancer |
| **Startup** | Application started | Delay other probes |
| **Deep** | Dependencies healthy | Alert/Circuit break |

## Implementation Examples

### 1. **Express.js Health Checks**

```typescript
import express from 'express';
import { Pool } from 'pg';
import Redis from 'ioredis';

interface HealthStatus {
  status: 'healthy' | 'degraded' | 'unhealthy';
  timestamp: string;
  uptime: number;
  checks: Record<string, CheckResult>;
  version?: string;
  environment?: string;
}

interface CheckResult {
  status: 'pass' | 'fail' | 'warn';
  time: number;
  output?: string;
  error?: string;
}

class HealthCheckService {
  private startTime = Date.now();
  private version = process.env.APP_VERSION || '1.0.0';
  private environment = process.env.NODE_ENV || 'development';

  constructor(
    private db: Pool,
    private redis: Redis
  ) {}

  async liveness(): Promise<{ status: string }> {
    // Simple check: is the process alive?
    return { status: 'alive' };
  }

  async readiness(): Promise<HealthStatus> {
    const checks = await Promise.all([
      this.checkDatabase(),
      this.checkRedis()
    ]);

    const results = {
      database: checks[0],
      redis: checks[1]
    };

    const status = this.determineStatus(results);

    return {
      status,
      timestamp: new Date().toISOString(),
      uptime: Date.now() - this.startTime,
      checks: results,
      version: this.version,
      environment: this.environment
    };
  }

  async deep(): Promise<HealthStatus> {
    const checks = await Promise.all([
      this.checkDatabase(),
      this.checkRedis(),
      this.checkExternalAPI(),
      this.checkDiskSpace(),
      this.checkMemory()
    ]);

    const results = {
      database: checks[0],
      redis: checks[1],
      external_api: checks[2],
      disk_space: checks[3],
      memory: checks[4]
    };

    const status = this.determineStatus(results);

    return {
      status,
      timestamp: new Date().toISOString(),
      uptime: Date.now() - this.startTime,
      checks: results,
      version: this.version,
      environment: this.environment
    };
  }

  private async checkDatabase(): Promise<CheckResult> {
    const startTime = Date.now();

    try {
      const result = await this.db.query('SELECT 1');
      const time = Date.now() - startTime;

      if (time > 1000) {
        return {
          status: 'warn',
          time,
          output: 'Database response slow'
        };
      }

      return {
        status: 'pass',
        time,
        output: 'Database connection healthy'
      };
    } catch (error: any) {
      return {
        status: 'fail',
        time: Date.now() - startTime,
        error: error.message
      };
    }
  }

  private async checkRedis(): Promise<CheckResult> {
    const startTime = Date.now();

    try {
      await this.redis.ping();
      const time = Date.now() - startTime;

      return {
        status: 'pass',
        time,
        output: 'Redis connection healthy'
      };
    } catch (error: any) {
      return {
        status: 'fail',
        time: Date.now() - startTime,
        error: error.message
      };
    }
  }

  private async checkExternalAPI(): Promise<CheckResult> {
    const startTime = Date.now();

    try {
      const response = await fetch('https://api.example.com/health', {
        signal: AbortSignal.timeout(5000)
      });

      const time = Date.now() - startTime;

      if (!response.ok) {
        return {
          status: 'warn',
          time,
          output: `API returned ${response.status}`
        };
      }

      return {
        status: 'pass',
        time,
        output: 'External API healthy'
      };
    } catch (error: any) {
      return {
        status: 'warn',
        time: Date.now() - startTime,
        error: error.message
      };
    }
  }

  private async checkDiskSpace(): Promise<CheckResult> {
    const startTime = Date.now();

    try {
      const { execSync } = require('child_process');
      const output = execSync('df -h /').toString();
      const lines = output.split('\n');
      const stats = lines[1].split(/\s+/);
      const usagePercent = parseInt(stats[4]);

      const time = Date.now() - startTime;

      if (usagePercent > 90) {
        return {
          status: 'fail',
          time,
          output: `Disk usage at ${usagePercent}%`
        };
      }

      if (usagePercent > 80) {
        return {
          status: 'warn',
          time,
          output: `Disk usage at ${usagePercent}%`
        };
      }

      return {
        status: 'pass',
        time,
        output: `Disk usage at ${usagePercent}%`
      };
    } catch (error: any) {
      return {
        status: 'warn',
        time: Date.now() - startTime,
        error: error.message
      };
    }
  }

  private async checkMemory(): Promise<CheckResult> {
    const startTime = Date.now();

    try {
      const used = process.memoryUsage();
      const heapUsedMB = used.heapUsed / 1024 / 1024;
      const heapTotalMB = used.heapTotal / 1024 / 1024;
      const usagePercent = (heapUsedMB / heapTotalMB) * 100;

      const time = Date.now() - startTime;

      if (usagePercent > 90) {
        return {
          status: 'warn',
          time,
          output: `Memory usage at ${usagePercent.toFixed(2)}%`
        };
      }

      return {
        status: 'pass',
        time,
        output: `Memory usage at ${usagePercent.toFixed(2)}%`
      };
    } catch (error: any) {
      return {
        status: 'warn',
        time: Date.now() - startTime,
        error: error.message
      };
    }
  }

  private determineStatus(
    checks: Record<string, CheckResult>
  ): 'healthy' | 'degraded' | 'unhealthy' {
    const results = Object.values(checks);

    if (results.some(c => c.status === 'fail')) {
      return 'unhealthy';
    }

    if (results.some(c => c.status === 'warn')) {
      return 'degraded';
    }

    return 'healthy';
  }
}

// Setup routes
const app = express();
const db = new Pool({ connectionString: process.env.DATABASE_URL });
const redis = new Redis(process.env.REDIS_URL);
const healthCheck = new HealthCheckService(db, redis);

// Liveness probe (lightweight)
app.get('/health/live', async (req, res) => {
  const result = await healthCheck.liveness();
  res.status(200).json(result);
});

// Readiness probe (checks critical dependencies)
app.get('/health/ready', async (req, res) => {
  const result = await healthCheck.readiness();

  if (result.status === 'unhealthy') {
    return res.status(503).json(result);
  }

  res.status(200).json(result);
});

// Deep health check (checks all dependencies)
app.get('/health', async (req, res) => {
  const result = await healthCheck.deep();

  const statusCode =
    result.status === 'healthy' ? 200 :
    result.status === 'degraded' ? 200 :
    503;

  res.status(statusCode).json(result);
});

// Startup probe
app.get('/health/startup', async (req, res) => {
  // Check if application has fully started
  const isReady = true; // Check actual startup conditions

  if (isReady) {
    res.status(200).json({ status: 'started' });
  } else {
    res.status(503).json({ status: 'starting' });
  }
});
```

### 2. **Spring Boot Actuator-Style (Java)**

```java
@RestController
@RequestMapping("/actuator")
public class HealthController {

    @Autowired
    private DataSource dataSource;

    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> health() {
        Map<String, Object> health = new HashMap<>();
        health.put("status", "UP");
        health.put("timestamp", Instant.now().toString());

        Map<String, Object> components = new HashMap<>();

        // Check database
        components.put("db", checkDatabase());

        // Check Redis
        components.put("redis", checkRedis());

        health.put("components", components);

        boolean anyDown = components.values().stream()
            .anyMatch(c -> "DOWN".equals(((Map) c).get("status")));

        if (anyDown) {
            health.put("status", "DOWN");
            return ResponseEntity.status(503).body(health);
        }

        return ResponseEntity.ok(health);
    }

    @GetMapping("/health/liveness")
    public ResponseEntity<Map<String, String>> liveness() {
        Map<String, String> response = new HashMap<>();
        response.put("status", "UP");
        return ResponseEntity.ok(response);
    }

    @GetMapping("/health/readiness")
    public ResponseEntity<Map<String, Object>> readiness() {
        Map<String, Object> readiness = new HashMap<>();

        // Check critical dependencies
        Map<String, Object> dbCheck = checkDatabase();
        readiness.put("database", dbCheck);

        boolean isReady = "UP".equals(dbCheck.get("status"));

        if (isReady) {
            readiness.put("status", "UP");
            return ResponseEntity.ok(readiness);
        } else {
            readiness.put("status", "DOWN");
            return ResponseEntity.status(503).body(readiness);
        }
    }

    private Map<String, Object> checkDatabase() {
        Map<String, Object> result = new HashMap<>();
        long startTime = System.currentTimeMillis();

        try {
            Connection conn = dataSource.getConnection();
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT 1");

            long duration = System.currentTimeMillis() - startTime;

            result.put("status", "UP");
            result.put("responseTime", duration + "ms");

            rs.close();
            stmt.close();
            conn.close();
        } catch (Exception e) {
            result.put("status", "DOWN");
            result.put("error", e.getMessage());
        }

        return result;
    }

    private Map<String, Object> checkRedis() {
        Map<String, Object> result = new HashMap<>();
        long startTime = System.currentTimeMillis();

        try {
            redisTemplate.opsForValue().get("health-check");
            long duration = System.currentTimeMillis() - startTime;

            result.put("status", "UP");
            result.put("responseTime", duration + "ms");
        } catch (Exception e) {
            result.put("status", "DOWN");
            result.put("error", e.getMessage());
        }

        return result;
    }
}
```

### 3. **Python Flask Health Checks**

```python
from flask import Flask, jsonify
from typing import Dict, Any
import psycopg2
import redis
import time

app = Flask(__name__)

class HealthCheck:
    def __init__(self):
        self.start_time = time.time()
        self.db_pool = None  # Initialize your DB pool
        self.redis_client = redis.Redis(host='localhost', port=6379)

    def liveness(self) -> Dict[str, str]:
        """Simple liveness check."""
        return {"status": "alive"}

    def readiness(self) -> Dict[str, Any]:
        """Readiness check with dependencies."""
        checks = {
            "database": self.check_database(),
            "redis": self.check_redis()
        }

        status = "ready" if all(
            c["status"] == "pass" for c in checks.values()
        ) else "not_ready"

        return {
            "status": status,
            "checks": checks,
            "timestamp": time.time()
        }

    def check_database(self) -> Dict[str, Any]:
        """Check database connection."""
        start_time = time.time()

        try:
            conn = psycopg2.connect("dbname=test user=postgres")
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            cursor.close()
            conn.close()

            duration = (time.time() - start_time) * 1000

            return {
                "status": "pass",
                "time": f"{duration:.2f}ms"
            }
        except Exception as e:
            return {
                "status": "fail",
                "error": str(e)
            }

    def check_redis(self) -> Dict[str, Any]:
        """Check Redis connection."""
        start_time = time.time()

        try:
            self.redis_client.ping()
            duration = (time.time() - start_time) * 1000

            return {
                "status": "pass",
                "time": f"{duration:.2f}ms"
            }
        except Exception as e:
            return {
                "status": "fail",
                "error": str(e)
            }

health_checker = HealthCheck()

@app.route('/health/live')
def liveness():
    return jsonify(health_checker.liveness()), 200

@app.route('/health/ready')
def readiness():
    result = health_checker.readiness()
    status_code = 200 if result["status"] == "ready" else 503
    return jsonify(result), status_code

@app.route('/health')
def health():
    result = health_checker.readiness()
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Best Practices

### ✅ DO
- Implement separate liveness and readiness probes
- Keep liveness probes lightweight
- Check critical dependencies in readiness
- Return appropriate HTTP status codes
- Include response time metrics
- Set reasonable timeouts
- Cache health check results briefly
- Include version and environment info
- Monitor health check failures

### ❌ DON'T
- Make liveness probes check dependencies
- Return 200 for failed health checks
- Take too long to respond
- Skip important dependency checks
- Expose sensitive information
- Ignore health check failures

## Kubernetes Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
      - name: app
        livenessProbe:
          httpGet:
            path: /health/live
            port: 3000
          initialDelaySeconds: 15
          periodSeconds: 10
          timeoutSeconds: 3
          failureThreshold: 3

        readinessProbe:
          httpGet:
            path: /health/ready
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 3

        startupProbe:
          httpGet:
            path: /health/startup
            port: 3000
          initialDelaySeconds: 0
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 30
```

## Resources

- [Kubernetes Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- [Health Check Response Format](https://tools.ietf.org/id/draft-inadarei-api-health-check-06.html)
