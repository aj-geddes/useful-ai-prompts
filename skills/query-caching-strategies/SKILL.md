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

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
