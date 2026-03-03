# Contextual Logging

## Contextual Logging

### Request Context Middleware

```typescript
// request-logger.ts
import { v4 as uuidv4 } from "uuid";
import { AsyncLocalStorage } from "async_hooks";

const asyncLocalStorage = new AsyncLocalStorage();

// Middleware to add request context
export function requestLogger(req, res, next) {
  const requestId = req.headers["x-request-id"] || uuidv4();
  const context = {
    requestId,
    method: req.method,
    path: req.path,
    ip: req.ip,
    userAgent: req.headers["user-agent"],
    userId: req.user?.id,
  };

  asyncLocalStorage.run(context, () => {
    logger.info("Request started", context);

    // Log response when finished
    res.on("finish", () => {
      logger.info("Request completed", {
        ...context,
        statusCode: res.statusCode,
        duration: Date.now() - req.startTime,
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
      logger.debug(message, { ...context, ...meta }),
  };
}

// Usage in route handler
app.get("/api/users/:id", async (req, res) => {
  const log = getLogger();

  log.info("Fetching user", { userId: req.params.id });

  try {
    const user = await userService.findById(req.params.id);
    log.info("User found", { userId: user.id });
    res.json(user);
  } catch (error) {
    log.error("Failed to fetch user", error, { userId: req.params.id });
    res.status(500).json({ error: "Internal server error" });
  }
});
```

### Correlation IDs

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
  const correlationId = req.headers["x-correlation-id"] || uuidv4();
  res.setHeader("x-correlation-id", correlationId);

  CorrelationIdManager.run(correlationId, () => {
    next();
  });
});

// Enhanced logger
const enhancedLogger = {
  info: (message: string, meta?: object) =>
    logger.info(message, {
      correlationId: CorrelationIdManager.get(),
      ...meta,
    }),
};
```
