---
name: query-caching-strategies
description: Implement query caching strategies to improve performance. Use when setting up caching layers, configuring Redis, or optimizing database query response times.
---

# Query Caching Strategies

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

## Application-Level Caching

### Redis Caching with PostgreSQL

**Setup Redis Cache Layer:**

```javascript
// Node.js example with Redis
const redis = require('redis');
const client = redis.createClient({
  host: 'localhost',
  port: 6379,
  db: 0
});

// Get user with caching
async function getUser(userId) {
  const cacheKey = `user:${userId}`;

  // Check cache
  const cached = await client.get(cacheKey);
  if (cached) return JSON.parse(cached);

  // Query database
  const user = await db.query(
    'SELECT * FROM users WHERE id = $1',
    [userId]
  );

  // Cache result (TTL: 1 hour)
  await client.setex(cacheKey, 3600, JSON.stringify(user));
  return user;
}

// Cache warming on startup
async function warmCache() {
  const hotUsers = await db.query(
    'SELECT * FROM users WHERE active = true ORDER BY last_login DESC LIMIT 100'
  );

  for (const user of hotUsers) {
    await client.setex(
      `user:${user.id}`,
      3600,
      JSON.stringify(user)
    );
  }
}
```

**Query Result Caching Pattern:**

```javascript
// Generalized cache pattern
async function queryCached(
  key,
  queryFn,
  ttl = 3600  // Default 1 hour
) {
  // Check cache
  const cached = await client.get(key);
  if (cached) return JSON.parse(cached);

  // Execute query
  const result = await queryFn();

  // Cache result
  await client.setex(key, ttl, JSON.stringify(result));
  return result;
}

// Usage
const posts = await queryCached(
  'user:123:posts',
  async () => db.query(
    'SELECT * FROM posts WHERE user_id = $1 ORDER BY created_at DESC',
    [123]
  ),
  1800  // 30 minutes TTL
);
```

### Memcached Caching

**PostgreSQL with Memcached:**

```javascript
// Node.js with Memcached
const Memcached = require('memcached');
const memcached = new Memcached(['localhost:11211']);

async function getProductWithCache(productId) {
  const cacheKey = `product:${productId}`;

  try {
    // Try cache first
    const cached = await memcached.get(cacheKey);
    if (cached) return cached;
  } catch (err) {
    // Memcached down, continue to database
  }

  // Query database
  const product = await db.query(
    'SELECT * FROM products WHERE id = $1',
    [productId]
  );

  // Set cache (TTL: 3600 seconds)
  try {
    await memcached.set(cacheKey, product, 3600);
  } catch (err) {
    // Fail silently, serve from database
  }

  return product;
}
```

## Database-Level Caching

### PostgreSQL Query Cache

**Materialized Views for Caching:**

```sql
-- Create materialized view for expensive query
CREATE MATERIALIZED VIEW user_statistics AS
SELECT
  u.id,
  u.email,
  COUNT(o.id) as total_orders,
  SUM(o.total) as total_spent,
  AVG(o.total) as avg_order_value,
  MAX(o.created_at) as last_order_date
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.email;

-- Index materialized view for fast access
CREATE INDEX idx_user_stats_email ON user_statistics(email);

-- Refresh strategy (scheduled)
REFRESH MATERIALIZED VIEW CONCURRENTLY user_statistics;

-- Query view instead of base tables
SELECT * FROM user_statistics WHERE email = 'john@example.com';
```

**Partial Indexes for Query Optimization:**

```sql
-- Index only active users (reduce index size)
CREATE INDEX idx_active_users ON users(created_at DESC)
WHERE active = true AND deleted_at IS NULL;

-- Index recently created records
CREATE INDEX idx_recent_orders ON orders(user_id, total DESC)
WHERE created_at > NOW() - INTERVAL '30 days';
```

### MySQL Query Cache

**MySQL Query Cache Configuration:**

```sql
-- Check query cache status
SHOW VARIABLES LIKE 'query_cache%';

-- Enable query cache
SET GLOBAL query_cache_type = 1;
SET GLOBAL query_cache_size = 268435456;  -- 256MB

-- Monitor query cache
SHOW STATUS LIKE 'Qcache%';

-- View cached queries
SELECT * FROM performance_schema.table_io_waits_summary_by_table_io_type;

-- Invalidate specific queries
FLUSH QUERY CACHE;
FLUSH TABLES;
```

## Cache Invalidation Strategies

### Event-Based Invalidation

**PostgreSQL with Triggers:**

```sql
-- Create function to invalidate cache on write
CREATE OR REPLACE FUNCTION invalidate_user_cache()
RETURNS TRIGGER AS $$
BEGIN
  -- In production, this would publish to Redis/Memcached
  -- PERFORM redis_publish('cache_invalidation', json_build_object(
  --   'event', 'user_updated',
  --   'user_id', NEW.id
  -- ));
  RAISE LOG 'Invalidating cache for user %', NEW.id;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Attach to users table
CREATE TRIGGER invalidate_cache_on_user_update
AFTER UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION invalidate_user_cache();

-- When users are updated, trigger fires and invalidates cache
UPDATE users SET email = 'newemail@example.com' WHERE id = 123;
```

**Application-Level Invalidation:**

```javascript
// Invalidate cache on data modification
async function updateUser(userId, userData) {
  // Update database
  const updatedUser = await db.query(
    'UPDATE users SET name = $1, email = $2 WHERE id = $3 RETURNING *',
    [userData.name, userData.email, userId]
  );

  // Invalidate related caches
  const cacheKeys = [
    `user:${userId}`,
    `user:${userId}:profile`,
    `user:${userId}:orders`,
    'active_users_list'
  ];

  for (const key of cacheKeys) {
    await client.del(key);
  }

  return updatedUser;
}
```

### Time-Based Invalidation

**TTL-Based Cache Expiration:**

```javascript
// Variable TTL based on data type
const CACHE_TTLS = {
  user_profile: 3600,        // 1 hour
  product_list: 1800,        // 30 minutes
  order_summary: 300,        // 5 minutes (frequently changes)
  category_list: 86400,      // 1 day (rarely changes)
  user_settings: 7200        // 2 hours
};

async function getCachedData(key, type, queryFn) {
  const cached = await client.get(key);
  if (cached) return JSON.parse(cached);

  const result = await queryFn();
  const ttl = CACHE_TTLS[type] || 3600;

  await client.setex(key, ttl, JSON.stringify(result));
  return result;
}
```

### LRU Cache Eviction

**Redis LRU Policy:**

```conf
# redis.conf
maxmemory 1gb
maxmemory-policy allkeys-lru  # Evict least recently used key

# Or other policies:
# volatile-lru: evict any key with TTL (LRU)
# allkeys-lfu: evict least frequently used key
# volatile-ttl: evict key with shortest TTL
```

## Cache Warming

**Pre-load Hot Data:**

```javascript
// Warm cache on application startup
async function warmApplicationCache() {
  // Warm popular users
  const popularUsers = await db.query(
    'SELECT * FROM users ORDER BY last_login DESC LIMIT 50'
  );

  for (const user of popularUsers) {
    await client.setex(
      `user:${user.id}`,
      3600,
      JSON.stringify(user)
    );
  }

  // Warm top products
  const topProducts = await db.query(
    'SELECT * FROM products ORDER BY sales DESC LIMIT 100'
  );

  for (const product of topProducts) {
    await client.setex(
      `product:${product.id}`,
      1800,
      JSON.stringify(product)
    );
  }

  console.log('Cache warming complete');
}

// Run on server startup
app.listen(3000, warmApplicationCache);
```

## Distributed Caching

**Redis Cluster Setup:**

```bash
# Multi-node Redis for distributed caching
redis-server --port 6379 --cluster-enabled yes
redis-server --port 6380 --cluster-enabled yes
redis-server --port 6381 --cluster-enabled yes

# Create cluster
redis-cli --cluster create localhost:6379 localhost:6380 localhost:6381
```

**Cross-Datacenter Cache:**

```javascript
// Replicate cache across regions
async function setCacheMultiRegion(key, value, ttl) {
  const regions = ['us-east', 'eu-west', 'ap-south'];

  await Promise.all(
    regions.map(region =>
      redisClients[region].setex(key, ttl, JSON.stringify(value))
    )
  );
}

// Read from nearest cache
async function getCacheNearest(key, region) {
  const value = await redisClients[region].get(key);
  if (value) return JSON.parse(value);

  // Fallback to other regions
  for (const fallbackRegion of ['us-east', 'eu-west', 'ap-south']) {
    const fallbackValue = await redisClients[fallbackRegion].get(key);
    if (fallbackValue) return JSON.parse(fallbackValue);
  }

  return null;
}
```

## Cache Monitoring

**Redis Cache Statistics:**

```javascript
async function getCacheStats() {
  const info = await client.info('stats');
  return {
    hits: info.keyspace_hits,
    misses: info.keyspace_misses,
    hitRate: info.keyspace_hits / (info.keyspace_hits + info.keyspace_misses)
  };
}

// Monitor hit ratio
setInterval(async () => {
  const stats = await getCacheStats();
  console.log(`Cache hit rate: ${(stats.hitRate * 100).toFixed(2)}%`);
}, 60000);
```

## Cache Strategy Selection

| Strategy | Best For | Drawbacks |
|----------|----------|-----------|
| Application-level | Flexible, fine-grained control | More code, consistency challenges |
| Database-level | Transparent, automatic | Less flexibility |
| Distributed cache | High throughput, scale | Extra complexity, network latency |
| Materialized views | Complex queries, aggregations | Manual refresh needed |

## Best Practices

✅ DO implement cache warming
✅ DO monitor cache hit rates
✅ DO use appropriate TTLs
✅ DO implement cache invalidation
✅ DO plan for cache failures
✅ DO test cache scenarios

❌ DON'T cache sensitive data
❌ DON'T cache without invalidation strategy
❌ DON'T ignore cache inconsistency risks
❌ DON'T use same TTL for all data

## Resources

- [Redis Documentation](https://redis.io/documentation)
- [Memcached Documentation](https://memcached.org/)
- [PostgreSQL Materialized Views](https://www.postgresql.org/docs/current/rules-materializedviews.html)
- [Redis Cache Patterns](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Best-Practices.html)
