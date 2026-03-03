# Express.js Health Checks

## Express.js Health Checks

```typescript
import express from "express";
import { Pool } from "pg";
import Redis from "ioredis";

interface HealthStatus {
  status: "healthy" | "degraded" | "unhealthy";
  timestamp: string;
  uptime: number;
  checks: Record<string, CheckResult>;
  version?: string;
  environment?: string;
}

interface CheckResult {
  status: "pass" | "fail" | "warn";
  time: number;
  output?: string;
  error?: string;
}

class HealthCheckService {
  private startTime = Date.now();
  private version = process.env.APP_VERSION || "1.0.0";
  private environment = process.env.NODE_ENV || "development";

  constructor(
    private db: Pool,
    private redis: Redis,
  ) {}

  async liveness(): Promise<{ status: string }> {
    // Simple check: is the process alive?
    return { status: "alive" };
  }

  async readiness(): Promise<HealthStatus> {
    const checks = await Promise.all([this.checkDatabase(), this.checkRedis()]);

    const results = {
      database: checks[0],
      redis: checks[1],
    };

    const status = this.determineStatus(results);

    return {
      status,
      timestamp: new Date().toISOString(),
      uptime: Date.now() - this.startTime,
      checks: results,
      version: this.version,
      environment: this.environment,
    };
  }

  async deep(): Promise<HealthStatus> {
    const checks = await Promise.all([
      this.checkDatabase(),
      this.checkRedis(),
      this.checkExternalAPI(),
      this.checkDiskSpace(),
      this.checkMemory(),
    ]);

    const results = {
      database: checks[0],
      redis: checks[1],
      external_api: checks[2],
      disk_space: checks[3],
      memory: checks[4],
    };

    const status = this.determineStatus(results);

    return {
      status,
      timestamp: new Date().toISOString(),
      uptime: Date.now() - this.startTime,
      checks: results,
      version: this.version,
      environment: this.environment,
    };
  }

  private async checkDatabase(): Promise<CheckResult> {
    const startTime = Date.now();

    try {
      const result = await this.db.query("SELECT 1");
      const time = Date.now() - startTime;

      if (time > 1000) {
        return {
          status: "warn",
          time,
          output: "Database response slow",
        };
      }

      return {
        status: "pass",
        time,
        output: "Database connection healthy",
      };
    } catch (error: any) {
      return {
        status: "fail",
        time: Date.now() - startTime,
        error: error.message,
      };
    }
  }

  private async checkRedis(): Promise<CheckResult> {
    const startTime = Date.now();

    try {
      await this.redis.ping();
      const time = Date.now() - startTime;

      return {
        status: "pass",
        time,
        output: "Redis connection healthy",
      };
    } catch (error: any) {
      return {
        status: "fail",
        time: Date.now() - startTime,
        error: error.message,
      };
    }
  }

  private async checkExternalAPI(): Promise<CheckResult> {
    const startTime = Date.now();

    try {
      const response = await fetch("https://api.example.com/health", {
        signal: AbortSignal.timeout(5000),
      });

      const time = Date.now() - startTime;

      if (!response.ok) {
        return {
          status: "warn",
          time,
          output: `API returned ${response.status}`,
        };
      }

      return {
        status: "pass",
        time,
        output: "External API healthy",
      };
    } catch (error: any) {
      return {
        status: "warn",
        time: Date.now() - startTime,
        error: error.message,
      };
    }
  }

  private async checkDiskSpace(): Promise<CheckResult> {
    const startTime = Date.now();

    try {
      const { execSync } = require("child_process");
      const output = execSync("df -h /").toString();
      const lines = output.split("\n");
      const stats = lines[1].split(/\s+/);
      const usagePercent = parseInt(stats[4]);

      const time = Date.now() - startTime;

      if (usagePercent > 90) {
        return {
          status: "fail",
          time,
          output: `Disk usage at ${usagePercent}%`,
        };
      }

      if (usagePercent > 80) {
        return {
          status: "warn",
          time,
          output: `Disk usage at ${usagePercent}%`,
        };
      }

      return {
        status: "pass",
        time,
        output: `Disk usage at ${usagePercent}%`,
      };
    } catch (error: any) {
      return {
        status: "warn",
        time: Date.now() - startTime,
        error: error.message,
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
          status: "warn",
          time,
          output: `Memory usage at ${usagePercent.toFixed(2)}%`,
        };
      }

      return {
        status: "pass",
        time,
        output: `Memory usage at ${usagePercent.toFixed(2)}%`,
      };
    } catch (error: any) {
      return {
        status: "warn",
        time: Date.now() - startTime,
        error: error.message,
      };
    }
  }

  private determineStatus(
    checks: Record<string, CheckResult>,
  ): "healthy" | "degraded" | "unhealthy" {
    const results = Object.values(checks);

    if (results.some((c) => c.status === "fail")) {
      return "unhealthy";
    }

    if (results.some((c) => c.status === "warn")) {
      return "degraded";
    }

    return "healthy";
  }
}

// Setup routes
const app = express();
const db = new Pool({ connectionString: process.env.DATABASE_URL });
const redis = new Redis(process.env.REDIS_URL);
const healthCheck = new HealthCheckService(db, redis);

// Liveness probe (lightweight)
app.get("/health/live", async (req, res) => {
  const result = await healthCheck.liveness();
  res.status(200).json(result);
});

// Readiness probe (checks critical dependencies)
app.get("/health/ready", async (req, res) => {
  const result = await healthCheck.readiness();

  if (result.status === "unhealthy") {
    return res.status(503).json(result);
  }

  res.status(200).json(result);
});

// Deep health check (checks all dependencies)
app.get("/health", async (req, res) => {
  const result = await healthCheck.deep();

  const statusCode =
    result.status === "healthy"
      ? 200
      : result.status === "degraded"
        ? 200
        : 503;

  res.status(statusCode).json(result);
});

// Startup probe
app.get("/health/startup", async (req, res) => {
  // Check if application has fully started
  const isReady = true; // Check actual startup conditions

  if (isReady) {
    res.status(200).json({ status: "started" });
  } else {
    res.status(503).json({ status: "starting" });
  }
});
```
