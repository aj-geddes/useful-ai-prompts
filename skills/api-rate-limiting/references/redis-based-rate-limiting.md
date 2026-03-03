# Redis-Based Rate Limiting

## Redis-Based Rate Limiting

```javascript
const redis = require("redis");
const client = redis.createClient();

// Sliding window with Redis
const redisRateLimit = (maxRequests, windowSeconds) => {
  return async (req, res, next) => {
    const key = `ratelimit:${req.user?.id || req.ip}`;
    const now = Date.now();
    const windowStart = now - windowSeconds * 1000;

    try {
      // Remove old requests
      await client.zremrangebyscore(key, 0, windowStart);

      // Count requests in window
      const count = await client.zcard(key);

      if (count < maxRequests) {
        // Add current request
        await client.zadd(key, now, `${now}-${Math.random()}`);
        // Set expiration
        await client.expire(key, windowSeconds);

        res.setHeader("X-RateLimit-Limit", maxRequests);
        res.setHeader("X-RateLimit-Remaining", maxRequests - count - 1);
        next();
      } else {
        const oldestRequest = await client.zrange(key, 0, 0);
        const resetTime = parseInt(oldestRequest[0]) + windowSeconds * 1000;
        const retryAfter = Math.ceil((resetTime - now) / 1000);

        res.set("Retry-After", retryAfter);
        res.status(429).json({
          error: "Rate limit exceeded",
          retryAfter,
        });
      }
    } catch (error) {
      console.error("Rate limit error:", error);
      next(); // Allow request if Redis fails
    }
  };
};

app.get("/api/expensive", redisRateLimit(10, 60), (req, res) => {
  res.json({ result: "expensive operation" });
});
```
