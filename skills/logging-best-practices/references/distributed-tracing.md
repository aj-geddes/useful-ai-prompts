# Distributed Tracing

## Distributed Tracing

```typescript
// tracing.ts
import opentelemetry from "@opentelemetry/api";
import { NodeTracerProvider } from "@opentelemetry/node";
import { SimpleSpanProcessor } from "@opentelemetry/tracing";
import { JaegerExporter } from "@opentelemetry/exporter-jaeger";

// Setup tracer
const provider = new NodeTracerProvider();
provider.addSpanProcessor(
  new SimpleSpanProcessor(
    new JaegerExporter({
      serviceName: "user-service",
      endpoint: "http://jaeger:14268/api/traces",
    }),
  ),
);
provider.register();

const tracer = opentelemetry.trace.getTracer("user-service");

// Usage in application
app.get("/api/users/:id", async (req, res) => {
  const span = tracer.startSpan("get-user", {
    attributes: {
      "http.method": req.method,
      "http.url": req.url,
      "user.id": req.params.id,
    },
  });

  try {
    const user = await fetchUser(req.params.id, span);
    span.setStatus({ code: opentelemetry.SpanStatusCode.OK });
    res.json(user);
  } catch (error) {
    span.setStatus({
      code: opentelemetry.SpanStatusCode.ERROR,
      message: error.message,
    });
    res.status(500).json({ error: "Internal server error" });
  } finally {
    span.end();
  }
});

async function fetchUser(userId: string, parentSpan: Span) {
  const span = tracer.startSpan("database-query", {
    parent: parentSpan,
    attributes: { "db.statement": "SELECT * FROM users WHERE id = ?" },
  });

  try {
    const user = await db.query("SELECT * FROM users WHERE id = ?", [userId]);
    return user;
  } finally {
    span.end();
  }
}
```
