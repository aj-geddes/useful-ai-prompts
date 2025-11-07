---
name: correlation-tracing
description: Implement distributed tracing with correlation IDs, trace propagation, and span tracking across microservices. Use when debugging distributed systems, monitoring request flows, or implementing observability.
---

# Correlation & Distributed Tracing

## Overview

Implement correlation IDs and distributed tracing to track requests across multiple services and understand system behavior.

## When to Use

- Microservices architectures
- Debugging distributed systems
- Performance monitoring
- Request flow visualization
- Error tracking across services
- Dependency analysis
- Latency optimization

## Implementation Examples

### 1. **Correlation ID Middleware (Express)**

```typescript
import express from 'express';
import { v4 as uuidv4 } from 'uuid';

// Async local storage for context
import { AsyncLocalStorage } from 'async_hooks';

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
    next: express.NextFunction
  ) => {
    // Extract or generate trace ID
    const traceId = req.headers['x-trace-id'] as string || uuidv4();
    const parentSpanId = req.headers['x-span-id'] as string;
    const spanId = uuidv4();

    // Set context
    const context = new Map<string, any>();
    context.set('traceId', traceId);
    context.set('spanId', spanId);
    context.set('parentSpanId', parentSpanId);
    context.set('serviceName', serviceName);

    // Inject trace headers
    res.setHeader('X-Trace-Id', traceId);
    res.setHeader('X-Span-Id', spanId);

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
    traceId: context.get('traceId'),
    spanId: context.get('spanId'),
    parentSpanId: context.get('parentSpanId'),
    serviceName: context.get('serviceName')
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
      timestamp: new Date().toISOString()
    };

    console.log(JSON.stringify(logEntry));
  }

  info(message: string, data?: any): void {
    this.log('info', message, data);
  }

  error(message: string, data?: any): void {
    this.log('error', message, data);
  }

  warn(message: string, data?: any): void {
    this.log('warn', message, data);
  }
}

const logger = new TracedLogger();

// HTTP client with trace propagation
async function tracedFetch(
  url: string,
  options: RequestInit = {}
): Promise<Response> {
  const context = getTraceContext();

  const headers = new Headers(options.headers);

  if (context) {
    headers.set('X-Trace-Id', context.traceId);
    headers.set('X-Span-Id', context.spanId);
    headers.set('X-Parent-Span-Id', context.spanId);
  }

  const startTime = Date.now();

  try {
    const response = await fetch(url, {
      ...options,
      headers
    });

    const duration = Date.now() - startTime;

    logger.info('HTTP request completed', {
      method: options.method || 'GET',
      url,
      statusCode: response.status,
      duration
    });

    return response;
  } catch (error) {
    const duration = Date.now() - startTime;

    logger.error('HTTP request failed', {
      method: options.method || 'GET',
      url,
      error: (error as Error).message,
      duration
    });

    throw error;
  }
}

// Usage
const app = express();

app.use(correlationMiddleware('api-service'));

app.get('/api/users/:id', async (req, res) => {
  logger.info('Fetching user', { userId: req.params.id });

  // Call another service with trace propagation
  const response = await tracedFetch(
    `http://user-service/users/${req.params.id}`
  );

  const data = await response.json();

  logger.info('User fetched successfully');

  res.json(data);
});
```

### 2. **OpenTelemetry Integration**

```typescript
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { JaegerExporter } from '@opentelemetry/exporter-jaeger';
import { Resource } from '@opentelemetry/resources';
import { SemanticResourceAttributes } from '@opentelemetry/semantic-conventions';

// Configure OpenTelemetry
const sdk = new NodeSDK({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'my-service',
    [SemanticResourceAttributes.SERVICE_VERSION]: '1.0.0',
  }),
  traceExporter: new JaegerExporter({
    endpoint: 'http://localhost:14268/api/traces',
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      '@opentelemetry/instrumentation-http': {
        enabled: true,
      },
      '@opentelemetry/instrumentation-express': {
        enabled: true,
      },
      '@opentelemetry/instrumentation-pg': {
        enabled: true,
      },
    }),
  ],
});

sdk.start();

// Custom spans
import { trace, SpanStatusCode } from '@opentelemetry/api';

const tracer = trace.getTracer('my-service');

async function processOrder(orderId: string) {
  const span = tracer.startSpan('process_order');

  span.setAttribute('order.id', orderId);

  try {
    // Validate order
    const validateSpan = tracer.startSpan('validate_order', {
      parent: span,
    });

    await validateOrder(orderId);
    validateSpan.setStatus({ code: SpanStatusCode.OK });
    validateSpan.end();

    // Process payment
    const paymentSpan = tracer.startSpan('process_payment', {
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

### 3. **Python Distributed Tracing**

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import Resource
from flask import Flask, request
import requests
import uuid

# Setup tracing
resource = Resource.create({"service.name": "python-service"})
trace.set_tracer_provider(TracerProvider(resource=resource))

jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

# Auto-instrument Flask and requests
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

tracer = trace.get_tracer(__name__)

@app.route('/api/orders/<order_id>')
def get_order(order_id):
    # Current span is automatically created by FlaskInstrumentor

    with tracer.start_as_current_span("fetch_order_details") as span:
        span.set_attribute("order.id", order_id)

        # Fetch from database
        with tracer.start_as_current_span("database_query"):
            order = fetch_order_from_db(order_id)

        # Call another service (automatically traced)
        with tracer.start_as_current_span("fetch_user_details"):
            user = requests.get(
                f"http://user-service/users/{order['user_id']}"
            ).json()

        return {
            "order": order,
            "user": user
        }

def fetch_order_from_db(order_id):
    # Database logic
    return {"id": order_id, "user_id": "user123"}

if __name__ == '__main__':
    app.run(port=5000)
```

### 4. **Manual Trace Propagation**

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
  status: 'ok' | 'error';
}

class DistributedTracer {
  private spans: Span[] = [];

  startSpan(
    name: string,
    parentSpanId?: string
  ): Span {
    const context = getTraceContext();

    const span: Span = {
      traceId: context?.traceId || uuidv4(),
      spanId: uuidv4(),
      parentSpanId: parentSpanId || context?.parentSpanId,
      name,
      serviceName: context?.serviceName || 'unknown',
      startTime: Date.now(),
      tags: {},
      logs: [],
      status: 'ok'
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
      fields
    });
  }

  setError(span: Span, error: Error): void {
    span.status = 'error';
    span.tags['error'] = true;
    span.tags['error.message'] = error.message;
    span.tags['error.stack'] = error.stack;
  }

  private async reportSpan(span: Span): Promise<void> {
    // Send to Jaeger, Zipkin, or other backend
    console.log('Reporting span:', JSON.stringify(span, null, 2));

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
    return this.spans.filter(s => s.traceId === traceId);
  }
}

const tracer = new DistributedTracer();

// Usage
async function handleRequest() {
  const span = tracer.startSpan('handle_request');

  tracer.setTag(span, 'http.method', 'GET');
  tracer.setTag(span, 'http.url', '/api/users/123');

  try {
    // Database operation
    const dbSpan = tracer.startSpan('database_query', span.spanId);
    tracer.setTag(dbSpan, 'db.type', 'postgresql');
    tracer.setTag(dbSpan, 'db.statement', 'SELECT * FROM users WHERE id = $1');

    await queryDatabase();

    tracer.endSpan(dbSpan);

    // External API call
    const apiSpan = tracer.startSpan('external_api_call', span.spanId);
    tracer.setTag(apiSpan, 'http.url', 'https://api.example.com/data');

    await callExternalAPI();

    tracer.endSpan(apiSpan);

    tracer.logEvent(span, 'Request completed successfully');
    tracer.endSpan(span);
  } catch (error) {
    tracer.setError(span, error as Error);
    tracer.logEvent(span, 'Request failed', { error: (error as Error).message });
    tracer.endSpan(span);
    throw error;
  }
}

async function queryDatabase() {
  await new Promise(resolve => setTimeout(resolve, 100));
}

async function callExternalAPI() {
  await new Promise(resolve => setTimeout(resolve, 200));
}
```

## Best Practices

### ✅ DO
- Generate trace IDs at entry points
- Propagate trace context across services
- Include correlation IDs in logs
- Use structured logging
- Set appropriate span attributes
- Sample traces in high-traffic systems
- Monitor trace collection overhead
- Implement context propagation

### ❌ DON'T
- Skip trace propagation
- Log without correlation context
- Create too many spans
- Store sensitive data in spans
- Block on trace reporting
- Forget error tracking

## Trace Headers

```
X-Trace-Id: trace identifier
X-Span-Id: current span
X-Parent-Span-Id: parent span
X-Sampled: sampling decision
```

## Resources

- [OpenTelemetry](https://opentelemetry.io/)
- [Jaeger Tracing](https://www.jaegertracing.io/)
- [Zipkin](https://zipkin.io/)
