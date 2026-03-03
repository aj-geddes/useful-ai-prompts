# Redis Caching with PostgreSQL

## Redis Caching with PostgreSQL

**Setup Redis Cache Layer:**

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
async function warmCache() {
  const hotUsers = await db.query(
    "SELECT * FROM users WHERE active = true ORDER BY last_login DESC LIMIT 100",
  );

  for (const user of hotUsers) {
    await client.setex(`user:${user.id}`, 3600, JSON.stringify(user));
  }
}
```

**Query Result Caching Pattern:**

```javascript
// Generalized cache pattern
async function queryCached(
  key,
  queryFn,
  ttl = 3600, // Default 1 hour
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
  "user:123:posts",
  async () =>
    db.query(
      "SELECT * FROM posts WHERE user_id = $1 ORDER BY created_at DESC",
      [123],
    ),
  1800, // 30 minutes TTL
);
```
