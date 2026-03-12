---
name: query-caching-strategies
description: >
  Implement query caching strategies to improve performance. Use when setting up
  caching layers, configuring Redis, or optimizing database query response
  times.
---

# Query Caching Strategies

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement multi-level caching strategies using Redis, Memcached, and database-level caching. Covers cache invalidation, TTL strategies, and cache warming patterns.

## When to Use

- Query result caching
- High-read workload optimization
- Reducing database load
- Improving response time
- Cache layer selection
- Cache invalidation patterns
- Distributed cache setup

## Quick Start

Minimal working example:

```javascript
// Node.js example with Redis
const redis = require("redis");
const client = redis.createClient({
  host: "localhost",
  port: 6379,
  db: 0,
});

// Get user with caching
async function getUser(userId) {
  const cacheKey = `user:${userId}`;

  // Check cache
  const cached = await client.get(cacheKey);
  if (cached) return JSON.parse(cached);

  // Query database
  const user = await db.query("SELECT * FROM users WHERE id = $1", [userId]);

  // Cache result (TTL: 1 hour)
  await client.setex(cacheKey, 3600, JSON.stringify(user));
  return user;
}

// Cache warming on startup
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Redis Caching with PostgreSQL](references/redis-caching-with-postgresql.md) | Redis Caching with PostgreSQL |
| [Memcached Caching](references/memcached-caching.md) | Memcached Caching |
| [PostgreSQL Query Cache](references/postgresql-query-cache.md) | PostgreSQL Query Cache |
| [MySQL Query Cache](references/mysql-query-cache.md) | MySQL Query Cache |
| [Event-Based Invalidation](references/event-based-invalidation.md) | Event-Based Invalidation |
| [Time-Based Invalidation](references/time-based-invalidation.md) | Time-Based Invalidation, LRU Cache Eviction |

## Best Practices

### ✅ DO

- Set explicit TTLs on every cached entry based on how frequently the underlying data changes
- Use consistent, predictable cache key naming conventions (e.g., `entity:id:field`) across the codebase
- Invalidate cache entries on write operations to prevent serving stale data
- Implement cache warming for high-traffic queries during deployment or startup
- Monitor cache hit ratios and eviction rates to tune TTLs and capacity
- Use multi-level caching (in-process -> distributed -> database) for latency-sensitive paths

### ❌ DON'T

- Cache user-specific or sensitive data in shared cache layers without proper scoping
- Let cache failures cascade into application errors — always fall through to the source of truth
- Use unbounded caches without an eviction policy (LRU, LFU, or TTL-based)
- Cache query results that include non-deterministic values (e.g., `NOW()`, `RANDOM()`)
