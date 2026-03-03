# Token Bucket Algorithm

## Token Bucket Algorithm

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
    return false;
  }

  available() {
    this.refill();
    return Math.floor(this.tokens);
  }
}

// Express middleware
const express = require("express");
const app = express();

const rateLimiters = new Map();

const tokenBucketRateLimit = (capacity, refillRate) => {
  return (req, res, next) => {
    const key = req.user?.id || req.ip;

    if (!rateLimiters.has(key)) {
      rateLimiters.set(key, new TokenBucket(capacity, refillRate));
    }

    const limiter = rateLimiters.get(key);

    if (limiter.consume(1)) {
      res.setHeader("X-RateLimit-Limit", capacity);
      res.setHeader("X-RateLimit-Remaining", limiter.available());
      next();
    } else {
      res.status(429).json({
        error: "Rate limit exceeded",
        retryAfter: Math.ceil(1 / limiter.refillRate),
      });
    }
  };
};

app.get("/api/data", tokenBucketRateLimit(100, 10), (req, res) => {
  res.json({ data: "api response" });
});
```
