---
name: correlation-tracing
description: >
  Implement distributed tracing with correlation IDs, trace propagation, and
  span tracking across microservices. Use when debugging distributed systems,
  monitoring request flows, or implementing observability.
---

# Correlation & Distributed Tracing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

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

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Correlation ID Middleware (Express)](references/correlation-id-middleware-express.md) | Correlation ID Middleware (Express) |
| [OpenTelemetry Integration](references/opentelemetry-integration.md) | OpenTelemetry Integration |
| [Python Distributed Tracing](references/python-distributed-tracing.md) | Python Distributed Tracing |
| [Manual Trace Propagation](references/manual-trace-propagation.md) | Manual Trace Propagation |

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
