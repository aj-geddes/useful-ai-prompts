# OpenTelemetry Integration

## OpenTelemetry Integration

```typescript
import { NodeSDK } from "@opentelemetry/sdk-node";
import { getNodeAutoInstrumentations } from "@opentelemetry/auto-instrumentations-node";
import { JaegerExporter } from "@opentelemetry/exporter-jaeger";
import { Resource } from "@opentelemetry/resources";
import { SemanticResourceAttributes } from "@opentelemetry/semantic-conventions";

// Configure OpenTelemetry
const sdk = new NodeSDK({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: "my-service",
    [SemanticResourceAttributes.SERVICE_VERSION]: "1.0.0",
  }),
  traceExporter: new JaegerExporter({
    endpoint: "http://localhost:14268/api/traces",
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      "@opentelemetry/instrumentation-http": {
        enabled: true,
      },
      "@opentelemetry/instrumentation-express": {
        enabled: true,
      },
      "@opentelemetry/instrumentation-pg": {
        enabled: true,
      },
    }),
  ],
});

sdk.start();

// Custom spans
import { trace, SpanStatusCode } from "@opentelemetry/api";

const tracer = trace.getTracer("my-service");

async function processOrder(orderId: string) {
  const span = tracer.startSpan("process_order");

  span.setAttribute("order.id", orderId);

  try {
    // Validate order
    const validateSpan = tracer.startSpan("validate_order", {
      parent: span,
    });

    await validateOrder(orderId);
    validateSpan.setStatus({ code: SpanStatusCode.OK });
    validateSpan.end();

    // Process payment
    const paymentSpan = tracer.startSpan("process_payment", {
      parent: span,
    });

    await processPayment(orderId);
    paymentSpan.setStatus({ code: SpanStatusCode.OK });
    paymentSpan.end();

    span.setStatus({ code: SpanStatusCode.OK });
  } catch (error) {
    span.setStatus({
      code: SpanStatusCode.ERROR,
      message: (error as Error).message,
    });
    span.recordException(error as Error);
    throw error;
  } finally {
    span.end();
  }
}

async function validateOrder(orderId: string) {
  // Validation logic
}

async function processPayment(orderId: string) {
  // Payment logic
}
```
