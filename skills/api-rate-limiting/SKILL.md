---
name: api-rate-limiting
description: >
  Implement API rate limiting strategies using token bucket, sliding window, and
  fixed window algorithms. Use when protecting APIs from abuse, managing
  traffic, or implementing tiered rate limits.
---

# API Rate Limiting

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Protect APIs from abuse and manage traffic using various rate limiting algorithms with per-user, per-IP, and per-endpoint strategies.

## When to Use

- Protecting APIs from brute force attacks
- Managing traffic spikes
- Implementing tiered service plans
- Preventing DoS attacks
- Fairness in resource allocation
- Enforcing quotas and usage limits

## Quick Start

Minimal working example:

```javascript
// Token Bucket Rate Limiter
class TokenBucket {
  constructor(capacity, refillRate) {
    this.capacity = capacity;
    this.tokens = capacity;
    this.refillRate = refillRate; // tokens per second
    this.lastRefillTime = Date.now();
  }

  refill() {
    const now = Date.now();
    const timePassed = (now - this.lastRefillTime) / 1000;
    const tokensToAdd = timePassed * this.refillRate;

    this.tokens = Math.min(this.capacity, this.tokens + tokensToAdd);
    this.lastRefillTime = now;
  }

  consume(tokens = 1) {
    this.refill();

    if (this.tokens >= tokens) {
      this.tokens -= tokens;
      return true;
    }
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Token Bucket Algorithm](references/token-bucket-algorithm.md) | Token Bucket Algorithm |
| [Sliding Window Algorithm](references/sliding-window-algorithm.md) | Sliding Window Algorithm |
| [Redis-Based Rate Limiting](references/redis-based-rate-limiting.md) | Redis-Based Rate Limiting |
| [Tiered Rate Limiting](references/tiered-rate-limiting.md) | Tiered Rate Limiting |
| [Python Rate Limiting (Flask)](references/python-rate-limiting-flask.md) | Python Rate Limiting (Flask) |
| [Response Headers](references/response-headers.md) | Response Headers |

## Best Practices

### ✅ DO

- Include rate limit headers in responses
- Use Redis for distributed rate limiting
- Implement tiered limits for different user plans
- Set appropriate window sizes and limits
- Monitor rate limit metrics
- Provide clear retry guidance
- Document rate limits in API docs
- Test under high load

### ❌ DON'T

- Use in-memory storage in production
- Set limits too restrictively
- Forget to include Retry-After header
- Ignore distributed scenarios
- Make rate limits public (security)
- Use simple counters for distributed systems
- Forget cleanup of old data
