# Log Levels

## Log Levels

### Standard Log Levels

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
          name: error?.name,
        },
      });
    }
  }

  fatal(message: string, error?: Error, context?: object) {
    this.log(LogLevel.FATAL, message, {
      ...context,
      error: {
        message: error?.message,
        stack: error?.stack,
        name: error?.name,
      },
    });
    process.exit(1);
  }

  private log(level: LogLevel, message: string, context?: object) {
    const logEntry = {
      timestamp: new Date().toISOString(),
      level: LogLevel[level],
      message,
      ...context,
    };
    console.log(JSON.stringify(logEntry));
  }
}

// Usage
const logger = new Logger(
  process.env.NODE_ENV === "production" ? LogLevel.INFO : LogLevel.DEBUG,
);

logger.debug("Processing request", { userId: "123", requestId: "abc" });
logger.info("User logged in", { userId: "123" });
logger.warn("Rate limit approaching", { userId: "123", count: 95 });
logger.error("Database connection failed", dbError, { query: "SELECT ..." });
```
