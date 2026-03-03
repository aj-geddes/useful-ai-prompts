---
name: logging-best-practices
description: >
  Implement structured logging with JSON formats, log levels (DEBUG, INFO, WARN,
  ERROR), contextual logging, PII handling, and centralized logging. Use for
  logging, observability, log levels, structured logs, or debugging.
---

# Logging Best Practices

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

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

## Quick Start

Minimal working example:

```typescript
// logger.ts
enum LogLevel {
  DEBUG = 0, // Detailed information for debugging
  INFO = 1, // General informational messages
  WARN = 2, // Warning messages, potentially harmful
  ERROR = 3, // Error messages, application can continue
  FATAL = 4, // Critical errors, application must stop
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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Log Levels](references/log-levels.md) | Log Levels |
| [Structured Logging (JSON)](references/structured-logging-json.md) | Structured Logging (JSON) |
| [Contextual Logging](references/contextual-logging.md) | Contextual Logging |
| [PII and Sensitive Data Handling](references/pii-and-sensitive-data-handling.md) | PII and Sensitive Data Handling |
| [Performance Logging](references/performance-logging.md) | Performance Logging |
| [Centralized Logging](references/centralized-logging.md) | Centralized Logging |
| [Distributed Tracing](references/distributed-tracing.md) | Distributed Tracing |
| [Log Sampling (High-Volume Services)](references/log-sampling-high-volume-services.md) | Log Sampling (High-Volume Services) |

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
