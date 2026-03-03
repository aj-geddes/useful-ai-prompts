---
name: health-check-endpoints
description: >
  Implement comprehensive health check endpoints for liveness, readiness, and
  dependency monitoring. Use when deploying to Kubernetes, implementing load
  balancer health checks, or monitoring service availability.
---

# Health Check Endpoints

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement health check endpoints to monitor service health, dependencies, and readiness for traffic.

## When to Use

- Kubernetes liveness and readiness probes
- Load balancer health checks
- Service discovery and registration
- Monitoring and alerting systems
- Circuit breaker decisions
- Auto-scaling triggers
- Deployment verification

## Quick Start

Minimal working example:

```typescript
import express from "express";
import { Pool } from "pg";
import Redis from "ioredis";

interface HealthStatus {
  status: "healthy" | "degraded" | "unhealthy";
  timestamp: string;
  uptime: number;
  checks: Record<string, CheckResult>;
  version?: string;
  environment?: string;
}

interface CheckResult {
  status: "pass" | "fail" | "warn";
  time: number;
  output?: string;
  error?: string;
}

class HealthCheckService {
  private startTime = Date.now();
  private version = process.env.APP_VERSION || "1.0.0";
  private environment = process.env.NODE_ENV || "development";

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Express.js Health Checks](references/expressjs-health-checks.md) | Express.js Health Checks |
| [Spring Boot Actuator-Style (Java)](references/spring-boot-actuator-style-java.md) | Spring Boot Actuator-Style (Java) |
| [Python Flask Health Checks](references/python-flask-health-checks.md) | Python Flask Health Checks |

## Best Practices

### ✅ DO

- Implement separate liveness and readiness probes
- Keep liveness probes lightweight
- Check critical dependencies in readiness
- Return appropriate HTTP status codes
- Include response time metrics
- Set reasonable timeouts
- Cache health check results briefly
- Include version and environment info
- Monitor health check failures

### ❌ DON'T

- Make liveness probes check dependencies
- Return 200 for failed health checks
- Take too long to respond
- Skip important dependency checks
- Expose sensitive information
- Ignore health check failures
