# Manual Trace Propagation

## Manual Trace Propagation

```typescript
interface Span {
  traceId: string;
  spanId: string;
  parentSpanId?: string;
  name: string;
  serviceName: string;
  startTime: number;
  endTime?: number;
  duration?: number;
  tags: Record<string, any>;
  logs: Array<{ timestamp: number; message: string; fields?: any }>;
  status: "ok" | "error";
}

class DistributedTracer {
  private spans: Span[] = [];

  startSpan(name: string, parentSpanId?: string): Span {
    const context = getTraceContext();

    const span: Span = {
      traceId: context?.traceId || uuidv4(),
      spanId: uuidv4(),
      parentSpanId: parentSpanId || context?.parentSpanId,
      name,
      serviceName: context?.serviceName || "unknown",
      startTime: Date.now(),
      tags: {},
      logs: [],
      status: "ok",
    };

    this.spans.push(span);
    return span;
  }

  endSpan(span: Span): void {
    span.endTime = Date.now();
    span.duration = span.endTime - span.startTime;

    // Send to tracing backend
    this.reportSpan(span);
  }

  setTag(span: Span, key: string, value: any): void {
    span.tags[key] = value;
  }

  logEvent(span: Span, message: string, fields?: any): void {
    span.logs.push({
      timestamp: Date.now(),
      message,
      fields,
    });
  }

  setError(span: Span, error: Error): void {
    span.status = "error";
    span.tags["error"] = true;
    span.tags["error.message"] = error.message;
    span.tags["error.stack"] = error.stack;
  }

  private async reportSpan(span: Span): Promise<void> {
    // Send to Jaeger, Zipkin, or other backend
    console.log("Reporting span:", JSON.stringify(span, null, 2));

    // In production:
    // await fetch('http://tracing-collector/api/spans', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify(span)
    // });
  }

  getAllSpans(): Span[] {
    return this.spans;
  }

  getTrace(traceId: string): Span[] {
    return this.spans.filter((s) => s.traceId === traceId);
  }
}

const tracer = new DistributedTracer();

// Usage
async function handleRequest() {
  const span = tracer.startSpan("handle_request");

  tracer.setTag(span, "http.method", "GET");
  tracer.setTag(span, "http.url", "/api/users/123");

  try {
    // Database operation
    const dbSpan = tracer.startSpan("database_query", span.spanId);
    tracer.setTag(dbSpan, "db.type", "postgresql");
    tracer.setTag(dbSpan, "db.statement", "SELECT * FROM users WHERE id = $1");

    await queryDatabase();

    tracer.endSpan(dbSpan);

    // External API call
    const apiSpan = tracer.startSpan("external_api_call", span.spanId);
    tracer.setTag(apiSpan, "http.url", "https://api.example.com/data");

    await callExternalAPI();

    tracer.endSpan(apiSpan);

    tracer.logEvent(span, "Request completed successfully");
    tracer.endSpan(span);
  } catch (error) {
    tracer.setError(span, error as Error);
    tracer.logEvent(span, "Request failed", {
      error: (error as Error).message,
    });
    tracer.endSpan(span);
    throw error;
  }
}

async function queryDatabase() {
  await new Promise((resolve) => setTimeout(resolve, 100));
}

async function callExternalAPI() {
  await new Promise((resolve) => setTimeout(resolve, 200));
}
```
