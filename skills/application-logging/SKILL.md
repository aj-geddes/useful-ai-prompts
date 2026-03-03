---
name: application-logging
description: >
  Implement structured logging across applications with log aggregation and
  centralized analysis. Use when setting up application logging, implementing
  ELK stack, or analyzing application behavior.
---

# Application Logging

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive structured logging with proper levels, context, and centralized aggregation for effective debugging and monitoring.

## When to Use

- Application debugging
- Audit trail creation
- Performance analysis
- Compliance requirements
- Centralized log aggregation

## Quick Start

Minimal working example:

```javascript
// logger.js
const winston = require("winston");

const logFormat = winston.format.combine(
  winston.format.timestamp({ format: "YYYY-MM-DD HH:mm:ss" }),
  winston.format.errors({ stack: true }),
  winston.format.json(),
);

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || "info",
  format: logFormat,
  defaultMeta: {
    service: "api-service",
    environment: process.env.NODE_ENV || "development",
  },
  transports: [
    new winston.transports.Console({
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple(),
      ),
    }),
    new winston.transports.File({
      filename: "logs/error.log",
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Node.js Structured Logging with Winston](references/nodejs-structured-logging-with-winston.md) | Node.js Structured Logging with Winston |
| [Express HTTP Request Logging](references/express-http-request-logging.md) | Express HTTP Request Logging |
| [Python Structured Logging](references/python-structured-logging.md) | Python Structured Logging |
| [Flask Integration](references/flask-integration.md) | Flask Integration |
| [ELK Stack Setup](references/elk-stack-setup.md) | ELK Stack Setup |
| [Logstash Configuration](references/logstash-configuration.md) | Logstash Configuration |

## Best Practices

### ✅ DO

- Use structured JSON logging
- Include request IDs for tracing
- Log at appropriate levels
- Add context to error logs
- Implement log rotation
- Use timestamps consistently
- Aggregate logs centrally
- Filter sensitive data

### ❌ DON'T

- Log passwords or secrets
- Log at INFO for every operation
- Use unstructured messages
- Ignore log storage limits
- Skip context information
- Log to stdout in production
- Create unbounded log files
