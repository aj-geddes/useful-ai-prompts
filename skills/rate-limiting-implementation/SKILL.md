---
name: rate-limiting-implementation
description: Implement rate limiting, throttling, API quotas, and backpressure mechanisms to protect services from abuse and ensure fair resource usage. Use when building APIs, preventing DOS attacks, or managing system load.
---

# Rate Limiting Implementation

## Overview

Implement rate limiting and throttling mechanisms to protect your services from abuse, ensure fair resource allocation, and maintain system stability under load.

## When to Use

- Protecting public APIs from abuse
- Preventing DOS/DDOS attacks
- Ensuring fair resource usage across users
- Implementing API quotas and billing tiers
- Managing system load and backpressure
- Enforcing SLA limits
- Controlling third-party API usage
- Database connection management

## Rate Limiting Algorithms

| Algorithm | Description | Use Case | Pros | Cons |
|-----------|-------------|----------|------|------|
| **Token Bucket** | Tokens added at fixed rate, consumed per request | Bursty traffic allowed | Flexible, allows bursts | Complex implementation |
| **Leaky Bucket** | Requests processed at constant rate | Smooth output | Consistent throughput | No burst allowance |
| **Fixed Window** | Count requests in fixed time windows | Simple quotas | Easy to implement | Edge case issues |
| **Sliding Window** | Rolling time window | Precise limiting | More accurate | Higher memory usage |

## Implementation Examples

### 1. **Token Bucket Algorithm (TypeScript)**

```typescript
interface TokenBucketConfig {
  capacity: number;
  refillRate: number; // tokens per second
  refillInterval: number; // milliseconds
}

class TokenBucket {
  private tokens: number;
  private lastRefill: number;
  private readonly capacity: number;
  private readonly refillRate: number;
  private readonly refillInterval: number;
  private refillTimer?: NodeJS.Timeout;

  constructor(config: TokenBucketConfig) {
    this.capacity = config.capacity;
    this.tokens = config.capacity;
    this.refillRate = config.refillRate;
    this.refillInterval = config.refillInterval;
    this.lastRefill = Date.now();

    this.startRefill();
  }

  private startRefill(): void {
    this.refillTimer = setInterval(() => {
      this.refill();
    }, this.refillInterval);
  }

  private refill(): void {
    const now = Date.now();
    const timePassed = now - this.lastRefill;
    const tokensToAdd = (timePassed / 1000) * this.refillRate;

    this.tokens = Math.min(this.capacity, this.tokens + tokensToAdd);
    this.lastRefill = now;
  }

  tryConsume(tokens: number = 1): boolean {
    this.refill(); // Refill before checking

    if (this.tokens >= tokens) {
      this.tokens -= tokens;
      return true;
    }

    return false;
  }

  getAvailableTokens(): number {
    this.refill();
    return Math.floor(this.tokens);
  }

  getWaitTime(tokens: number = 1): number {
    this.refill();

    if (this.tokens >= tokens) {
      return 0;
    }

    const tokensNeeded = tokens - this.tokens;
    return (tokensNeeded / this.refillRate) * 1000;
  }

  reset(): void {
    this.tokens = this.capacity;
    this.lastRefill = Date.now();
  }

  destroy(): void {
    if (this.refillTimer) {
      clearInterval(this.refillTimer);
    }
  }
}

// Usage
const rateLimiter = new TokenBucket({
  capacity: 100,
  refillRate: 10, // 10 tokens per second
  refillInterval: 100 // Check every 100ms
});

if (rateLimiter.tryConsume(1)) {
  // Process request
  console.log('Request allowed');
} else {
  const waitTime = rateLimiter.getWaitTime(1);
  console.log(`Rate limited. Retry after ${waitTime}ms`);
}
```

### 2. **Redis-Based Distributed Rate Limiter**

```typescript
import Redis from 'ioredis';

interface RateLimitConfig {
  points: number; // Number of requests
  duration: number; // Time window in seconds
  blockDuration?: number; // Block duration after limit exceeded
}

class RedisRateLimiter {
  private redis: Redis;

  constructor(redis: Redis) {
    this.redis = redis;
  }

  async consume(
    key: string,
    config: RateLimitConfig,
    points: number = 1
  ): Promise<{
    allowed: boolean;
    remaining: number;
    resetTime: number;
    retryAfter?: number;
  }> {
    const now = Date.now();
    const windowKey = `ratelimit:${key}`;
    const blockKey = `ratelimit:block:${key}`;

    // Check if blocked
    const isBlocked = await this.redis.exists(blockKey);
    if (isBlocked) {
      const ttl = await this.redis.ttl(blockKey);
      return {
        allowed: false,
        remaining: 0,
        resetTime: now + ttl * 1000,
        retryAfter: ttl
      };
    }

    // Use Lua script for atomic operation
    const luaScript = `
      local key = KEYS[1]
      local limit = tonumber(ARGV[1])
      local window = tonumber(ARGV[2])
      local points = tonumber(ARGV[3])
      local now = tonumber(ARGV[4])

      local current = redis.call('GET', key)

      if current == false then
        redis.call('SET', key, points, 'EX', window)
        return {limit - points, now + (window * 1000)}
      end

      current = tonumber(current)

      if current + points <= limit then
        redis.call('INCRBY', key, points)
        return {limit - current - points, now + (window * 1000)}
      end

      return {0, now + (redis.call('TTL', key) * 1000)}
    `;

    const result = await this.redis.eval(
      luaScript,
      1,
      windowKey,
      config.points,
      config.duration,
      points,
      now
    ) as [number, number];

    const [remaining, resetTime] = result;
    const allowed = remaining >= 0;

    // Block if limit exceeded and blockDuration specified
    if (!allowed && config.blockDuration) {
      await this.redis.setex(blockKey, config.blockDuration, '1');
    }

    return {
      allowed,
      remaining: Math.max(0, remaining),
      resetTime,
      retryAfter: allowed ? undefined : Math.ceil((resetTime - now) / 1000)
    };
  }

  async reset(key: string): Promise<void> {
    await this.redis.del(`ratelimit:${key}`, `ratelimit:block:${key}`);
  }

  async getRemainingPoints(key: string, limit: number): Promise<number> {
    const current = await this.redis.get(`ratelimit:${key}`);
    if (!current) return limit;

    return Math.max(0, limit - parseInt(current));
  }
}

// Usage
const redis = new Redis();
const limiter = new RedisRateLimiter(redis);

const result = await limiter.consume(
  `user:${userId}`,
  {
    points: 100, // 100 requests
    duration: 60, // per minute
    blockDuration: 300 // block for 5 minutes if exceeded
  },
  1 // consume 1 point
);

if (!result.allowed) {
  throw new Error(`Rate limit exceeded. Retry after ${result.retryAfter}s`);
}
```

### 3. **Express Middleware**

```typescript
import express from 'express';
import { RedisRateLimiter } from './rate-limiter';

interface RateLimitMiddlewareOptions {
  points: number;
  duration: number;
  blockDuration?: number;
  keyGenerator?: (req: express.Request) => string;
  handler?: (req: express.Request, res: express.Response) => void;
  skipSuccessfulRequests?: boolean;
  skipFailedRequests?: boolean;
}

function createRateLimitMiddleware(
  limiter: RedisRateLimiter,
  options: RateLimitMiddlewareOptions
) {
  const keyGenerator = options.keyGenerator || ((req) => req.ip || 'unknown');

  return async (
    req: express.Request,
    res: express.Response,
    next: express.NextFunction
  ) => {
    const key = keyGenerator(req);

    try {
      const result = await limiter.consume(key, {
        points: options.points,
        duration: options.duration,
        blockDuration: options.blockDuration
      });

      // Set rate limit headers
      res.setHeader('X-RateLimit-Limit', options.points);
      res.setHeader('X-RateLimit-Remaining', result.remaining);
      res.setHeader('X-RateLimit-Reset', new Date(result.resetTime).toISOString());

      if (!result.allowed) {
        res.setHeader('Retry-After', result.retryAfter!);

        if (options.handler) {
          return options.handler(req, res);
        }

        return res.status(429).json({
          error: 'Too Many Requests',
          message: `Rate limit exceeded. Retry after ${result.retryAfter} seconds.`,
          retryAfter: result.retryAfter
        });
      }

      // Handle conditional consumption
      if (options.skipSuccessfulRequests || options.skipFailedRequests) {
        const originalSend = res.send;
        res.send = function(data: any) {
          const statusCode = res.statusCode;

          if (
            (options.skipSuccessfulRequests && statusCode < 400) ||
            (options.skipFailedRequests && statusCode >= 400)
          ) {
            // Refund the consumed point
            limiter.consume(key, {
              points: options.points,
              duration: options.duration
            }, -1);
          }

          return originalSend.call(this, data);
        };
      }

      next();
    } catch (error) {
      console.error('Rate limiting error:', error);
      // Fail open - allow request if rate limiter fails
      next();
    }
  };
}

// Usage
const app = express();
const redis = new Redis();
const limiter = new RedisRateLimiter(redis);

// Global rate limit
app.use(createRateLimitMiddleware(limiter, {
  points: 100,
  duration: 60,
  blockDuration: 300
}));

// API-specific rate limit
app.use('/api/search', createRateLimitMiddleware(limiter, {
  points: 10,
  duration: 60,
  keyGenerator: (req) => `search:${req.ip}`,
  skipSuccessfulRequests: true
}));

// User-specific rate limit
app.use('/api/user', createRateLimitMiddleware(limiter, {
  points: 1000,
  duration: 3600,
  keyGenerator: (req) => `user:${req.user?.id || req.ip}`
}));
```

### 4. **Sliding Window Algorithm (Python)**

```python
import time
from collections import deque
from typing import Deque, Optional
import threading

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_size: int):
        """
        Initialize sliding window rate limiter.

        Args:
            max_requests: Maximum number of requests allowed
            window_size: Time window in seconds
        """
        self.max_requests = max_requests
        self.window_size = window_size
        self.requests: dict[str, Deque[float]] = {}
        self.lock = threading.Lock()

    def is_allowed(self, key: str) -> tuple[bool, Optional[float]]:
        """
        Check if request is allowed.

        Returns:
            Tuple of (is_allowed, retry_after_seconds)
        """
        with self.lock:
            now = time.time()

            # Initialize or get request queue for this key
            if key not in self.requests:
                self.requests[key] = deque()

            request_queue = self.requests[key]

            # Remove expired requests
            cutoff_time = now - self.window_size
            while request_queue and request_queue[0] < cutoff_time:
                request_queue.popleft()

            # Check if limit exceeded
            if len(request_queue) >= self.max_requests:
                # Calculate retry after time
                oldest_request = request_queue[0]
                retry_after = self.window_size - (now - oldest_request)
                return False, retry_after

            # Add current request
            request_queue.append(now)
            return True, None

    def get_remaining(self, key: str) -> int:
        """Get remaining requests for key."""
        with self.lock:
            if key not in self.requests:
                return self.max_requests

            now = time.time()
            cutoff_time = now - self.window_size
            request_queue = self.requests[key]

            # Remove expired
            while request_queue and request_queue[0] < cutoff_time:
                request_queue.popleft()

            return max(0, self.max_requests - len(request_queue))

    def reset(self, key: str):
        """Reset rate limit for key."""
        with self.lock:
            if key in self.requests:
                del self.requests[key]

    def cleanup(self):
        """Remove all expired entries."""
        with self.lock:
            now = time.time()
            cutoff_time = now - self.window_size

            keys_to_delete = []
            for key, request_queue in self.requests.items():
                # Remove expired requests
                while request_queue and request_queue[0] < cutoff_time:
                    request_queue.popleft()

                # Delete empty queues
                if not request_queue:
                    keys_to_delete.append(key)

            for key in keys_to_delete:
                del self.requests[key]


# Usage
limiter = SlidingWindowRateLimiter(max_requests=100, window_size=60)

# Check if request is allowed
allowed, retry_after = limiter.is_allowed("user:123")

if not allowed:
    print(f"Rate limited. Retry after {retry_after:.2f} seconds")
else:
    # Process request
    remaining = limiter.get_remaining("user:123")
    print(f"Request allowed. {remaining} remaining")
```

### 5. **Tiered Rate Limiting**

```typescript
enum PricingTier {
  FREE = 'free',
  BASIC = 'basic',
  PRO = 'pro',
  ENTERPRISE = 'enterprise'
}

interface TierLimits {
  requestsPerMinute: number;
  requestsPerHour: number;
  requestsPerDay: number;
  burstLimit: number;
}

const TIER_LIMITS: Record<PricingTier, TierLimits> = {
  [PricingTier.FREE]: {
    requestsPerMinute: 10,
    requestsPerHour: 100,
    requestsPerDay: 1000,
    burstLimit: 20
  },
  [PricingTier.BASIC]: {
    requestsPerMinute: 60,
    requestsPerHour: 1000,
    requestsPerDay: 10000,
    burstLimit: 100
  },
  [PricingTier.PRO]: {
    requestsPerMinute: 300,
    requestsPerHour: 10000,
    requestsPerDay: 100000,
    burstLimit: 500
  },
  [PricingTier.ENTERPRISE]: {
    requestsPerMinute: 1000,
    requestsPerHour: 50000,
    requestsPerDay: 1000000,
    burstLimit: 2000
  }
};

class TieredRateLimiter {
  constructor(private limiter: RedisRateLimiter) {}

  async checkLimits(
    userId: string,
    tier: PricingTier
  ): Promise<{
    allowed: boolean;
    limitType?: string;
    retryAfter?: number;
    limits: {
      minuteRemaining: number;
      hourRemaining: number;
      dayRemaining: number;
    };
  }> {
    const limits = TIER_LIMITS[tier];

    // Check minute limit
    const minuteResult = await this.limiter.consume(
      `${userId}:minute`,
      { points: limits.requestsPerMinute, duration: 60 }
    );

    // Check hour limit
    const hourResult = await this.limiter.consume(
      `${userId}:hour`,
      { points: limits.requestsPerHour, duration: 3600 }
    );

    // Check day limit
    const dayResult = await this.limiter.consume(
      `${userId}:day`,
      { points: limits.requestsPerDay, duration: 86400 }
    );

    // Determine if any limit exceeded
    if (!minuteResult.allowed) {
      return {
        allowed: false,
        limitType: 'minute',
        retryAfter: minuteResult.retryAfter,
        limits: {
          minuteRemaining: 0,
          hourRemaining: hourResult.remaining,
          dayRemaining: dayResult.remaining
        }
      };
    }

    if (!hourResult.allowed) {
      return {
        allowed: false,
        limitType: 'hour',
        retryAfter: hourResult.retryAfter,
        limits: {
          minuteRemaining: minuteResult.remaining,
          hourRemaining: 0,
          dayRemaining: dayResult.remaining
        }
      };
    }

    if (!dayResult.allowed) {
      return {
        allowed: false,
        limitType: 'day',
        retryAfter: dayResult.retryAfter,
        limits: {
          minuteRemaining: minuteResult.remaining,
          hourRemaining: hourResult.remaining,
          dayRemaining: 0
        }
      };
    }

    return {
      allowed: true,
      limits: {
        minuteRemaining: minuteResult.remaining,
        hourRemaining: hourResult.remaining,
        dayRemaining: dayResult.remaining
      }
    };
  }
}
```

### 6. **Adaptive Rate Limiting**

```typescript
class AdaptiveRateLimiter {
  private successRate: number = 1.0;
  private errorRate: number = 0.0;
  private currentLimit: number;

  constructor(
    private baseLimit: number,
    private minLimit: number,
    private maxLimit: number
  ) {
    this.currentLimit = baseLimit;
  }

  recordSuccess(): void {
    this.successRate = this.successRate * 0.95 + 0.05;
    this.errorRate = this.errorRate * 0.95;
    this.adjustLimit();
  }

  recordError(): void {
    this.successRate = this.successRate * 0.95;
    this.errorRate = this.errorRate * 0.95 + 0.05;
    this.adjustLimit();
  }

  private adjustLimit(): void {
    // Increase limit if success rate is high
    if (this.successRate > 0.95 && this.errorRate < 0.01) {
      this.currentLimit = Math.min(
        this.currentLimit * 1.1,
        this.maxLimit
      );
    }

    // Decrease limit if error rate is high
    if (this.errorRate > 0.1 || this.successRate < 0.8) {
      this.currentLimit = Math.max(
        this.currentLimit * 0.9,
        this.minLimit
      );
    }
  }

  getCurrentLimit(): number {
    return Math.floor(this.currentLimit);
  }
}
```

## Best Practices

### ✅ DO
- Use distributed rate limiting for multi-server deployments
- Implement multiple rate limit tiers (per second, minute, hour, day)
- Return proper HTTP status codes (429 Too Many Requests)
- Include Retry-After header in responses
- Log rate limit violations for monitoring
- Implement graceful degradation
- Use Redis or similar for persistence
- Consider cost-based rate limiting (expensive operations cost more)
- Implement burst allowances for legitimate traffic spikes
- Provide clear API documentation about limits

### ❌ DON'T
- Store rate limit data in application memory for distributed systems
- Use fixed window counters without considering edge cases
- Forget to clean up expired data
- Block all requests from an IP due to one bad actor
- Set limits too restrictive for legitimate use
- Ignore the impact of rate limiting on user experience
- Fail closed (deny all) when rate limiter fails

## Resources

- [IETF Rate Limit Headers](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/)
- [Redis Rate Limiting Patterns](https://redis.io/docs/manual/patterns/rate-limiter/)
- [Token Bucket Algorithm](https://en.wikipedia.org/wiki/Token_bucket)
