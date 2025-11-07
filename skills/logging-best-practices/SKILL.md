---
name: logging-best-practices
description: Implement structured logging with JSON formats, log levels (DEBUG, INFO, WARN, ERROR), contextual logging, PII handling, and centralized logging. Use for logging, observability, log levels, structured logs, or debugging.
---

# Logging Best Practices

## Overview

Comprehensive guide to implementing structured, secure, and performant logging across applications. Covers log levels, structured logging formats, contextual information, PII protection, and centralized logging systems.

## When to Use

- Setting up application logging infrastructure
- Implementing structured logging
- Configuring log levels for different environments
- Managing sensitive data in logs
- Setting up centralized logging
- Implementing distributed tracing
- Debugging production issues
- Compliance with logging regulations

## Instructions

### 1. **Log Levels**

#### Standard Log Levels
```typescript
// logger.ts
enum LogLevel {
  DEBUG = 0,   // Detailed information for debugging
  INFO = 1,    // General informational messages
  WARN = 2,    // Warning messages, potentially harmful
  ERROR = 3,   // Error messages, application can continue
  FATAL = 4    // Critical errors, application must stop
}

class Logger {
  constructor(private minLevel: LogLevel = LogLevel.INFO) {}

  debug(message: string, context?: object) {
    if (this.minLevel <= LogLevel.DEBUG) {
      this.log(LogLevel.DEBUG, message, context);
    }
  }

  info(message: string, context?: object) {
    if (this.minLevel <= LogLevel.INFO) {
      this.log(LogLevel.INFO, message, context);
    }
  }

  warn(message: string, context?: object) {
    if (this.minLevel <= LogLevel.WARN) {
      this.log(LogLevel.WARN, message, context);
    }
  }

  error(message: string, error?: Error, context?: object) {
    if (this.minLevel <= LogLevel.ERROR) {
      this.log(LogLevel.ERROR, message, {
        ...context,
        error: {
          message: error?.message,
          stack: error?.stack,
          name: error?.name
        }
      });
    }
  }

  fatal(message: string, error?: Error, context?: object) {
    this.log(LogLevel.FATAL, message, {
      ...context,
      error: {
        message: error?.message,
        stack: error?.stack,
        name: error?.name
      }
    });
    process.exit(1);
  }

  private log(level: LogLevel, message: string, context?: object) {
    const logEntry = {
      timestamp: new Date().toISOString(),
      level: LogLevel[level],
      message,
      ...context
    };
    console.log(JSON.stringify(logEntry));
  }
}

// Usage
const logger = new Logger(
  process.env.NODE_ENV === 'production' ? LogLevel.INFO : LogLevel.DEBUG
);

logger.debug('Processing request', { userId: '123', requestId: 'abc' });
logger.info('User logged in', { userId: '123' });
logger.warn('Rate limit approaching', { userId: '123', count: 95 });
logger.error('Database connection failed', dbError, { query: 'SELECT ...' });
```

### 2. **Structured Logging (JSON)**

#### Node.js with Winston
```typescript
// winston-logger.ts
import winston from 'winston';

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: {
    service: 'user-service',
    environment: process.env.NODE_ENV
  },
  transports: [
    // Write to console
    new winston.transports.Console({
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple()
      )
    }),
    // Write to file
    new winston.transports.File({
      filename: 'logs/error.log',
      level: 'error',
      maxsize: 5242880, // 5MB
      maxFiles: 5
    }),
    new winston.transports.File({
      filename: 'logs/combined.log',
      maxsize: 5242880,
      maxFiles: 5
    })
  ]
});

// Usage
logger.info('User created', {
  userId: user.id,
  email: user.email,
  requestId: req.id
});

logger.error('Payment processing failed', {
  error: error.message,
  stack: error.stack,
  orderId: order.id,
  amount: order.total,
  userId: user.id
});
```

#### Python with structlog
```python
# logger.py
import structlog
import logging

# Configure structlog
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

# Usage
logger.info("user_created",
    user_id=user.id,
    email=user.email,
    request_id=request.id
)

logger.error("payment_failed",
    error=str(error),
    order_id=order.id,
    amount=order.total,
    user_id=user.id
)
```

#### Go with zap
```go
// logger.go
package main

import (
    "go.uber.org/zap"
    "go.uber.org/zap"
)

func main() {
    // Production config (JSON)
    logger, _ := zap.NewProduction()
    defer logger.Sync()

    // Development config (human-readable)
    // logger, _ := zap.NewDevelopment()

    logger.Info("User created",
        zap.String("userId", user.ID),
        zap.String("email", user.Email),
        zap.String("requestId", req.ID),
    )

    logger.Error("Payment processing failed",
        zap.Error(err),
        zap.String("orderId", order.ID),
        zap.Float64("amount", order.Total),
        zap.String("userId", user.ID),
    )

    // Sugared logger for less structured logs
    sugar := logger.Sugar()
    sugar.Infow("User login",
        "userId", user.ID,
        "ip", req.IP,
    )
}
```

### 3. **Contextual Logging**

#### Request Context Middleware
```typescript
// request-logger.ts
import { v4 as uuidv4 } from 'uuid';
import { AsyncLocalStorage } from 'async_hooks';

const asyncLocalStorage = new AsyncLocalStorage();

// Middleware to add request context
export function requestLogger(req, res, next) {
  const requestId = req.headers['x-request-id'] || uuidv4();
  const context = {
    requestId,
    method: req.method,
    path: req.path,
    ip: req.ip,
    userAgent: req.headers['user-agent'],
    userId: req.user?.id
  };

  asyncLocalStorage.run(context, () => {
    logger.info('Request started', context);

    // Log response when finished
    res.on('finish', () => {
      logger.info('Request completed', {
        ...context,
        statusCode: res.statusCode,
        duration: Date.now() - req.startTime
      });
    });

    req.startTime = Date.now();
    next();
  });
}

// Logger wrapper that includes context
export function getLogger() {
  const context = asyncLocalStorage.getStore();
  return {
    info: (message: string, meta?: object) =>
      logger.info(message, { ...context, ...meta }),
    error: (message: string, error: Error, meta?: object) =>
      logger.error(message, { ...context, error, ...meta }),
    warn: (message: string, meta?: object) =>
      logger.warn(message, { ...context, ...meta }),
    debug: (message: string, meta?: object) =>
      logger.debug(message, { ...context, ...meta })
  };
}

// Usage in route handler
app.get('/api/users/:id', async (req, res) => {
  const log = getLogger();

  log.info('Fetching user', { userId: req.params.id });

  try {
    const user = await userService.findById(req.params.id);
    log.info('User found', { userId: user.id });
    res.json(user);
  } catch (error) {
    log.error('Failed to fetch user', error, { userId: req.params.id });
    res.status(500).json({ error: 'Internal server error' });
  }
});
```

#### Correlation IDs
```typescript
// correlation-id.ts
export class CorrelationIdManager {
  private static storage = new AsyncLocalStorage<string>();

  static run<T>(correlationId: string, callback: () => T): T {
    return this.storage.run(correlationId, callback);
  }

  static get(): string | undefined {
    return this.storage.getStore();
  }
}

// Middleware
app.use((req, res, next) => {
  const correlationId = req.headers['x-correlation-id'] || uuidv4();
  res.setHeader('x-correlation-id', correlationId);

  CorrelationIdManager.run(correlationId, () => {
    next();
  });
});

// Enhanced logger
const enhancedLogger = {
  info: (message: string, meta?: object) =>
    logger.info(message, {
      correlationId: CorrelationIdManager.get(),
      ...meta
    })
};
```

### 4. **PII and Sensitive Data Handling**

#### Data Sanitization
```typescript
// sanitizer.ts
const SENSITIVE_FIELDS = [
  'password',
  'token',
  'apiKey',
  'ssn',
  'creditCard',
  'email',  // depending on regulations
  'phone'   // depending on regulations
];

function sanitize(obj: any): any {
  if (typeof obj !== 'object' || obj === null) {
    return obj;
  }

  if (Array.isArray(obj)) {
    return obj.map(sanitize);
  }

  const sanitized = {};
  for (const [key, value] of Object.entries(obj)) {
    if (SENSITIVE_FIELDS.some(field =>
      key.toLowerCase().includes(field.toLowerCase())
    )) {
      sanitized[key] = '[REDACTED]';
    } else if (typeof value === 'object') {
      sanitized[key] = sanitize(value);
    } else {
      sanitized[key] = value;
    }
  }
  return sanitized;
}

// Usage
logger.info('User data', sanitize({
  userId: '123',
  email: 'user@example.com',  // Will be redacted
  password: 'secret123',       // Will be redacted
  name: 'John Doe'             // Will be logged
}));

// Output:
// {
//   "userId": "123",
//   "email": "[REDACTED]",
//   "password": "[REDACTED]",
//   "name": "John Doe"
// }
```

#### Email/PII Masking
```typescript
// masking.ts
function maskEmail(email: string): string {
  const [local, domain] = email.split('@');
  const maskedLocal = local[0] + '*'.repeat(local.length - 2) + local[local.length - 1];
  return `${maskedLocal}@${domain}`;
}

function maskPhone(phone: string): string {
  return phone.replace(/\d(?=\d{4})/g, '*');
}

function maskCreditCard(cc: string): string {
  return cc.replace(/\d(?=\d{4})/g, '*');
}

// Usage
logger.info('User registered', {
  userId: user.id,
  email: maskEmail(user.email),           // u***r@example.com
  phone: maskPhone(user.phone),            // ******1234
  creditCard: maskCreditCard(user.card)    // ************1234
});
```

### 5. **Performance Logging**

```typescript
// performance-logger.ts
class PerformanceLogger {
  private timers = new Map<string, number>();

  start(operation: string) {
    this.timers.set(operation, Date.now());
  }

  end(operation: string, metadata?: object) {
    const startTime = this.timers.get(operation);
    if (!startTime) return;

    const duration = Date.now() - startTime;
    this.timers.delete(operation);

    logger.info(`Performance: ${operation}`, {
      operation,
      duration,
      durationMs: duration,
      ...metadata
    });

    // Alert if slow
    if (duration > 1000) {
      logger.warn(`Slow operation: ${operation}`, {
        operation,
        duration,
        threshold: 1000,
        ...metadata
      });
    }
  }

  async measure<T>(operation: string, fn: () => Promise<T>, metadata?: object): Promise<T> {
    this.start(operation);
    try {
      return await fn();
    } finally {
      this.end(operation, metadata);
    }
  }
}

// Usage
const perfLogger = new PerformanceLogger();

// Manual timing
perfLogger.start('database-query');
const users = await db.query('SELECT * FROM users');
perfLogger.end('database-query', { count: users.length });

// Automatic timing
const result = await perfLogger.measure(
  'complex-operation',
  async () => await processData(),
  { userId: '123' }
);
```

### 6. **Centralized Logging**

#### ELK Stack (Elasticsearch, Logstash, Kibana)
```yaml
# docker-compose.yml
version: '3'
services:
  elasticsearch:
    image: elasticsearch:8.0.0
    environment:
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ports:
      - "9200:9200"

  logstash:
    image: logstash:8.0.0
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    ports:
      - "5000:5000"
    depends_on:
      - elasticsearch

  kibana:
    image: kibana:8.0.0
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch
```

```conf
# logstash.conf
input {
  tcp {
    port => 5000
    codec => json
  }
}

filter {
  # Parse timestamp
  date {
    match => ["timestamp", "ISO8601"]
  }

  # Add geo-location if IP present
  if [ip] {
    geoip {
      source => "ip"
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "app-logs-%{+YYYY.MM.dd}"
  }
}
```

#### Ship Logs to ELK
```typescript
// winston-elk.ts
import winston from 'winston';
import 'winston-logstash';

const logger = winston.createLogger({
  transports: [
    new winston.transports.Logstash({
      port: 5000,
      host: 'logstash',
      node_name: 'user-service',
      max_connect_retries: -1
    })
  ]
});
```

#### AWS CloudWatch Logs
```typescript
// cloudwatch-logger.ts
import winston from 'winston';
import WinstonCloudWatch from 'winston-cloudwatch';

const logger = winston.createLogger({
  transports: [
    new WinstonCloudWatch({
      logGroupName: '/aws/lambda/user-service',
      logStreamName: () => {
        const date = new Date().toISOString().split('T')[0];
        return `${date}-${process.env.LAMBDA_VERSION}`;
      },
      awsRegion: 'us-east-1',
      jsonMessage: true
    })
  ]
});
```

### 7. **Distributed Tracing**

```typescript
// tracing.ts
import opentelemetry from '@opentelemetry/api';
import { NodeTracerProvider } from '@opentelemetry/node';
import { SimpleSpanProcessor } from '@opentelemetry/tracing';
import { JaegerExporter } from '@opentelemetry/exporter-jaeger';

// Setup tracer
const provider = new NodeTracerProvider();
provider.addSpanProcessor(
  new SimpleSpanProcessor(
    new JaegerExporter({
      serviceName: 'user-service',
      endpoint: 'http://jaeger:14268/api/traces'
    })
  )
);
provider.register();

const tracer = opentelemetry.trace.getTracer('user-service');

// Usage in application
app.get('/api/users/:id', async (req, res) => {
  const span = tracer.startSpan('get-user', {
    attributes: {
      'http.method': req.method,
      'http.url': req.url,
      'user.id': req.params.id
    }
  });

  try {
    const user = await fetchUser(req.params.id, span);
    span.setStatus({ code: opentelemetry.SpanStatusCode.OK });
    res.json(user);
  } catch (error) {
    span.setStatus({
      code: opentelemetry.SpanStatusCode.ERROR,
      message: error.message
    });
    res.status(500).json({ error: 'Internal server error' });
  } finally {
    span.end();
  }
});

async function fetchUser(userId: string, parentSpan: Span) {
  const span = tracer.startSpan('database-query', {
    parent: parentSpan,
    attributes: { 'db.statement': 'SELECT * FROM users WHERE id = ?' }
  });

  try {
    const user = await db.query('SELECT * FROM users WHERE id = ?', [userId]);
    return user;
  } finally {
    span.end();
  }
}
```

### 8. **Log Sampling (High-Volume Services)**

```typescript
// log-sampler.ts
class SamplingLogger {
  constructor(
    private logger: Logger,
    private sampleRate: number = 0.1 // 10% sampling
  ) {}

  info(message: string, meta?: object) {
    if (this.shouldSample()) {
      this.logger.info(message, meta);
    }
  }

  // Always log warnings and errors
  warn(message: string, meta?: object) {
    this.logger.warn(message, meta);
  }

  error(message: string, error: Error, meta?: object) {
    this.logger.error(message, error, meta);
  }

  private shouldSample(): boolean {
    return Math.random() < this.sampleRate;
  }

  // Sample based on user ID (consistent sampling)
  infoSampled(userId: string, message: string, meta?: object) {
    const hash = this.hashUserId(userId);
    if (hash % 100 < this.sampleRate * 100) {
      this.logger.info(message, { ...meta, sampled: true });
    }
  }

  private hashUserId(userId: string): number {
    let hash = 0;
    for (let i = 0; i < userId.length; i++) {
      hash = ((hash << 5) - hash) + userId.charCodeAt(i);
      hash |= 0;
    }
    return Math.abs(hash);
  }
}
```

## Best Practices

### ✅ DO
- Use structured logging (JSON) in production
- Include correlation/request IDs in all logs
- Log at appropriate levels (don't overuse DEBUG)
- Redact sensitive data (PII, passwords, tokens)
- Include context (userId, requestId, etc.)
- Log errors with full stack traces
- Use centralized logging in distributed systems
- Set up log rotation to manage disk space
- Monitor log volume and costs
- Use async logging for performance
- Include timestamps in ISO 8601 format
- Log business events (user actions, transactions)
- Set up alerts for error patterns

### ❌ DON'T
- Log passwords, tokens, or sensitive data
- Use console.log in production
- Log at DEBUG level in production by default
- Log inside tight loops (use sampling)
- Include PII without anonymization
- Ignore log rotation (disk will fill up)
- Use synchronous logging in hot paths
- Log to multiple transports without need
- Forget to include error stack traces
- Log binary data or large objects
- Use string concatenation (use structured fields)
- Log every single request in high-volume APIs

## Common Patterns

### Pattern 1: Error Boundary Logging
```typescript
class ErrorBoundary {
  static async handle(fn: () => Promise<void>) {
    try {
      await fn();
    } catch (error) {
      logger.error('Unhandled error', error, {
        function: fn.name,
        stack: error.stack
      });
      throw error;
    }
  }
}
```

### Pattern 2: Audit Logging
```typescript
function auditLog(action: string, resource: string) {
  return function(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;

    descriptor.value = async function(...args: any[]) {
      const result = await originalMethod.apply(this, args);

      logger.info('Audit', {
        action,
        resource,
        userId: this.userId,
        timestamp: new Date().toISOString(),
        result: sanitize(result)
      });

      return result;
    };

    return descriptor;
  };
}

// Usage
class UserService {
  @auditLog('DELETE', 'user')
  async deleteUser(userId: string) {
    // ...
  }
}
```

## Tools & Resources

- **Winston**: Versatile Node.js logger
- **Pino**: Fast JSON logger for Node.js
- **structlog**: Structured logging for Python
- **zap**: Fast structured logging for Go
- **Logback**: Java logging framework
- **ELK Stack**: Elasticsearch, Logstash, Kibana
- **Splunk**: Enterprise log management
- **Datadog**: Cloud monitoring and logging
- **CloudWatch**: AWS log management
- **Jaeger**: Distributed tracing
