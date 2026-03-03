# Tiered Rate Limiting

## Tiered Rate Limiting

```javascript
const RATE_LIMITS = {
  free: { requests: 100, window: 3600 }, // 100 per hour
  pro: { requests: 10000, window: 3600 }, // 10,000 per hour
  enterprise: { requests: null, window: null }, // Unlimited
};

const tieredRateLimit = async (req, res, next) => {
  const user = req.user;
  const plan = user?.plan || "free";
  const limits = RATE_LIMITS[plan];

  if (!limits.requests) {
    return next(); // Unlimited plan
  }

  const key = `ratelimit:${user.id}`;
  const now = Date.now();
  const windowStart = now - limits.window * 1000;

  try {
    await client.zremrangebyscore(key, 0, windowStart);
    const count = await client.zcard(key);

    if (count < limits.requests) {
      await client.zadd(key, now, `${now}-${Math.random()}`);
      await client.expire(key, limits.window);

      res.setHeader("X-RateLimit-Limit", limits.requests);
      res.setHeader("X-RateLimit-Remaining", limits.requests - count - 1);
      res.setHeader("X-Plan", plan);
      next();
    } else {
      res.status(429).json({
        error: "Rate limit exceeded",
        plan,
        upgradeUrl: "/plans",
      });
    }
  } catch (error) {
    next();
  }
};

app.use(tieredRateLimit);
```
