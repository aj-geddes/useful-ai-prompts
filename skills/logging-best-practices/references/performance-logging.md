# Performance Logging

## Performance Logging

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
      ...metadata,
    });

    // Alert if slow
    if (duration > 1000) {
      logger.warn(`Slow operation: ${operation}`, {
        operation,
        duration,
        threshold: 1000,
        ...metadata,
      });
    }
  }

  async measure<T>(
    operation: string,
    fn: () => Promise<T>,
    metadata?: object,
  ): Promise<T> {
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
perfLogger.start("database-query");
const users = await db.query("SELECT * FROM users");
perfLogger.end("database-query", { count: users.length });

// Automatic timing
const result = await perfLogger.measure(
  "complex-operation",
  async () => await processData(),
  { userId: "123" },
);
```
