---
name: distributed-tracing
description: >
  Implement distributed tracing with Jaeger and Zipkin for tracking requests
  across microservices. Use when debugging distributed systems, tracking request
  flows, or analyzing service performance.
---

# Distributed Tracing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Set up distributed tracing infrastructure with Jaeger or Zipkin to track requests across microservices and identify performance bottlenecks.

## When to Use

- Debugging microservice interactions
- Identifying performance bottlenecks
- Tracking request flows
- Analyzing service dependencies
- Root cause analysis

## Quick Start

Minimal working example:

```yaml
# docker-compose.yml
version: "3.8"
services:
  jaeger:
    image: jaegertracing/all-in-one:latest
    ports:
      - "5775:5775/udp"
      - "6831:6831/udp"
      - "16686:16686"
      - "14268:14268"
    networks:
      - tracing

networks:
  tracing:
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Jaeger Setup](references/jaeger-setup.md) | Jaeger Setup, Node.js Jaeger Instrumentation |
| [Express Tracing Middleware](references/express-tracing-middleware.md) | Express Tracing Middleware |
| [Python Jaeger Integration](references/python-jaeger-integration.md) | Python Jaeger Integration |
| [Distributed Context Propagation](references/distributed-context-propagation.md) | Distributed Context Propagation |
| [Zipkin Integration](references/zipkin-integration.md) | Zipkin Integration, Trace Analysis |

## Best Practices

### ✅ DO

- Sample appropriately for your traffic volume
- Propagate trace context across services
- Add meaningful span tags
- Log errors with spans
- Use consistent service naming
- Monitor trace latency
- Document trace format
- Keep instrumentation lightweight

### ❌ DON'T

- Sample 100% in production
- Skip trace context propagation
- Log sensitive data in spans
- Create excessive spans
- Ignore sampling configuration
- Use unbounded cardinality tags
- Deploy without testing collection
