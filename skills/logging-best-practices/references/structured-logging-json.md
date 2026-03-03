# Structured Logging (JSON)

## Structured Logging (JSON)

### Node.js with Winston

```typescript
// winston-logger.ts
import winston from "winston";

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || "info",
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json(),
  ),
  defaultMeta: {
    service: "user-service",
    environment: process.env.NODE_ENV,
  },
  transports: [
    // Write to console
    new winston.transports.Console({
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple(),
      ),
    }),
    // Write to file
    new winston.transports.File({
      filename: "logs/error.log",
      level: "error",
      maxsize: 5242880, // 5MB
      maxFiles: 5,
    }),
    new winston.transports.File({
      filename: "logs/combined.log",
      maxsize: 5242880,
      maxFiles: 5,
    }),
  ],
});

// Usage
logger.info("User created", {
  userId: user.id,
  email: user.email,
  requestId: req.id,
});

logger.error("Payment processing failed", {
  error: error.message,
  stack: error.stack,
  orderId: order.id,
  amount: order.total,
  userId: user.id,
});
```

### Python with structlog

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

### Go with zap

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
