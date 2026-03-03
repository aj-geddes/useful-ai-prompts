# Correlation ID Middleware (Express)

## Correlation ID Middleware (Express)

```typescript
import express from "express";
import { v4 as uuidv4 } from "uuid";

// Async local storage for context
import { AsyncLocalStorage } from "async_hooks";

const traceContext = new AsyncLocalStorage<Map<string, any>>();

interface TraceContext {
  traceId: string;
  spanId: string;
  parentSpanId?: string;
  serviceName: string;
}

function correlationMiddleware(serviceName: string) {
  return (
    req: express.Request,
    res: express.Response,
    next: express.NextFunction,
  ) => {
    // Extract or generate trace ID
    const traceId = (req.headers["x-trace-id"] as string) || uuidv4();
    const parentSpanId = req.headers["x-span-id"] as string;
    const spanId = uuidv4();

    // Set context
    const context = new Map<string, any>();
    context.set("traceId", traceId);
    context.set("spanId", spanId);
    context.set("parentSpanId", parentSpanId);
    context.set("serviceName", serviceName);

    // Inject trace headers
    res.setHeader("X-Trace-Id", traceId);
    res.setHeader("X-Span-Id", spanId);

    // Run in context
    traceContext.run(context, () => {
      next();
    });
  };
}

// Helper to get current context
function getTraceContext(): TraceContext | null {
  const context = traceContext.getStore();
  if (!context) return null;

  return {
    traceId: context.get("traceId"),
    spanId: context.get("spanId"),
    parentSpanId: context.get("parentSpanId"),
    serviceName: context.get("serviceName"),
  };
}

// Enhanced logger with trace context
class TracedLogger {
  log(level: string, message: string, data?: any): void {
    const context = getTraceContext();

    const logEntry = {
      level,
      message,
      ...data,
      ...context,
      timestamp: new Date().toISOString(),
    };

    console.log(JSON.stringify(logEntry));
  }

  info(message: string, data?: any): void {
    this.log("info", message, data);
  }

  error(message: string, data?: any): void {
    this.log("error", message, data);
  }

  warn(message: string, data?: any): void {
    this.log("warn", message, data);
  }
}

const logger = new TracedLogger();

// HTTP client with trace propagation
async function tracedFetch(
  url: string,
  options: RequestInit = {},
): Promise<Response> {
  const context = getTraceContext();

  const headers = new Headers(options.headers);

  if (context) {
    headers.set("X-Trace-Id", context.traceId);
    headers.set("X-Span-Id", context.spanId);
    headers.set("X-Parent-Span-Id", context.spanId);
  }

  const startTime = Date.now();

  try {
    const response = await fetch(url, {
      ...options,
      headers,
    });

    const duration = Date.now() - startTime;

    logger.info("HTTP request completed", {
      method: options.method || "GET",
      url,
      statusCode: response.status,
      duration,
    });

    return response;
  } catch (error) {
    const duration = Date.now() - startTime;

    logger.error("HTTP request failed", {
      method: options.method || "GET",
      url,
      error: (error as Error).message,
      duration,
    });

    throw error;
  }
}

// Usage
const app = express();

app.use(correlationMiddleware("api-service"));

app.get("/api/users/:id", async (req, res) => {
  logger.info("Fetching user", { userId: req.params.id });

  // Call another service with trace propagation
  const response = await tracedFetch(
    `http://user-service/users/${req.params.id}`,
  );

  const data = await response.json();

  logger.info("User fetched successfully");

  res.json(data);
});
```
