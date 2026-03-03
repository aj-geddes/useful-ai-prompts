---
name: caching-strategy
description: >
  Implement efficient caching strategies using Redis, Memcached, CDN, and cache
  invalidation patterns. Use when optimizing application performance, reducing
  database load, or improving response times.
---

# Caching Strategy

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement effective caching strategies to improve application performance, reduce latency, and decrease load on backend systems.

## When to Use

- Reducing database query load
- Improving API response times
- Handling high traffic loads
- Caching expensive computations
- Storing session data
- CDN integration for static assets
- Implementing distributed caching
- Rate limiting and throttling

## Quick Start

Minimal working example:

```typescript
import Redis from "ioredis";

interface CacheOptions {
  ttl?: number; // Time to live in seconds
  prefix?: string;
}

class CacheService {
  private redis: Redis;
  private defaultTTL = 3600; // 1 hour

  constructor(redisUrl: string) {
    this.redis = new Redis(redisUrl, {
      retryStrategy: (times) => {
        const delay = Math.min(times * 50, 2000);
        return delay;
      },
      maxRetriesPerRequest: 3,
    });

    this.redis.on("connect", () => {
      console.log("Redis connected");
    });

    this.redis.on("error", (error) => {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Redis Cache Implementation (Node.js)](references/redis-cache-implementation-nodejs.md) | Redis Cache Implementation (Node.js) |
| [Cache Decorator (Python)](references/cache-decorator-python.md) | Cache Decorator (Python) |
| [Multi-Level Cache](references/multi-level-cache.md) | Multi-Level Cache |
| [Cache Invalidation Strategies](references/cache-invalidation-strategies.md) | Cache Invalidation Strategies |
| [HTTP Caching Headers](references/http-caching-headers.md) | HTTP Caching Headers |

## Best Practices

### ✅ DO

- Set appropriate TTL values
- Implement cache warming for critical data
- Use cache-aside pattern for reads
- Monitor cache hit rates
- Implement graceful degradation on cache failure
- Use compression for large cached values
- Namespace cache keys properly
- Implement cache stampede prevention
- Use consistent hashing for distributed caching
- Monitor cache memory usage

### ❌ DON'T

- Cache everything indiscriminately
- Use caching as a fix for poor database design
- Store sensitive data without encryption
- Forget to handle cache misses
- Set TTL too long for frequently changing data
- Ignore cache invalidation strategies
- Cache without monitoring
- Store large objects without consideration
