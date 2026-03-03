---
name: circuit-breaker-pattern
description: >
  Implement circuit breaker patterns for fault tolerance, automatic failure
  detection, and fallback mechanisms. Use when calling external services,
  handling cascading failures, or implementing resilience patterns.
---

# Circuit Breaker Pattern

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement circuit breaker patterns to prevent cascading failures and provide graceful degradation when dependencies fail.

## When to Use

- External API calls
- Microservices communication
- Database connections
- Third-party service integrations
- Preventing cascading failures
- Implementing fallback mechanisms
- Rate limiting protection
- Timeout handling

## Quick Start

Minimal working example:

```typescript
enum CircuitState {
  CLOSED = "CLOSED",
  OPEN = "OPEN",
  HALF_OPEN = "HALF_OPEN",
}

interface CircuitBreakerConfig {
  failureThreshold: number;
  successThreshold: number;
  timeout: number;
  resetTimeout: number;
}

interface CircuitBreakerStats {
  failures: number;
  successes: number;
  consecutiveFailures: number;
  consecutiveSuccesses: number;
  lastFailureTime?: number;
}

class CircuitBreaker {
  private state: CircuitState = CircuitState.CLOSED;
  private stats: CircuitBreakerStats = {
    failures: 0,
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [TypeScript Circuit Breaker](references/typescript-circuit-breaker.md) | TypeScript Circuit Breaker |
| [Circuit Breaker with Monitoring](references/circuit-breaker-with-monitoring.md) | Circuit Breaker with Monitoring |
| [Opossum-Style Circuit Breaker (Node.js)](references/opossum-style-circuit-breaker-nodejs.md) | Opossum-Style Circuit Breaker (Node.js) |
| [Python Circuit Breaker](references/python-circuit-breaker.md) | Python Circuit Breaker |
| [Resilience4j-Style (Java)](references/resilience4j-style-java.md) | Resilience4j-Style (Java) |

## Best Practices

### ✅ DO

- Use appropriate thresholds for your use case
- Implement fallback mechanisms
- Monitor circuit breaker states
- Set reasonable timeouts
- Use exponential backoff
- Log state transitions
- Alert on frequent trips
- Test circuit breaker behavior
- Use per-dependency breakers
- Implement health checks

### ❌ DON'T

- Use same breaker for all dependencies
- Set unrealistic thresholds
- Skip fallback implementation
- Ignore open circuit breakers
- Use overly aggressive reset timeouts
- Forget to monitor
