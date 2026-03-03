# Sliding Window Algorithm

## Sliding Window Algorithm

```javascript
class SlidingWindowLimiter {
  constructor(maxRequests, windowSizeSeconds) {
    this.maxRequests = maxRequests;
    this.windowSize = windowSizeSeconds * 1000; // Convert to ms
    this.requests = [];
  }

  isAllowed() {
    const now = Date.now();
    const windowStart = now - this.windowSize;

    // Remove old requests outside window
    this.requests = this.requests.filter((time) => time > windowStart);

    if (this.requests.length < this.maxRequests) {
      this.requests.push(now);
      return true;
    }
    return false;
  }

  remaining() {
    const now = Date.now();
    const windowStart = now - this.windowSize;
    this.requests = this.requests.filter((time) => time > windowStart);
    return Math.max(0, this.maxRequests - this.requests.length);
  }
}

const slidingWindowRateLimit = (maxRequests, windowSeconds) => {
  const limiters = new Map();

  return (req, res, next) => {
    const key = req.user?.id || req.ip;

    if (!limiters.has(key)) {
      limiters.set(key, new SlidingWindowLimiter(maxRequests, windowSeconds));
    }

    const limiter = limiters.get(key);

    if (limiter.isAllowed()) {
      res.setHeader("X-RateLimit-Limit", maxRequests);
      res.setHeader("X-RateLimit-Remaining", limiter.remaining());
      next();
    } else {
      res.status(429).json({ error: "Rate limit exceeded" });
    }
  };
};

app.get("/api/search", slidingWindowRateLimit(30, 60), (req, res) => {
  res.json({ results: [] });
});
```
