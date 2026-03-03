# Redis-Based Distributed Rate Limiter

## Redis-Based Distributed Rate Limiter

```typescript
import Redis from "ioredis";

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
    points: number = 1,
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
        retryAfter: ttl,
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

    const result = (await this.redis.eval(
      luaScript,
      1,
      windowKey,
      config.points,
      config.duration,
      points,
      now,
    )) as [number, number];

    const [remaining, resetTime] = result;
    const allowed = remaining >= 0;

    // Block if limit exceeded and blockDuration specified
    if (!allowed && config.blockDuration) {
      await this.redis.setex(blockKey, config.blockDuration, "1");
    }

    return {
      allowed,
      remaining: Math.max(0, remaining),
      resetTime,
      retryAfter: allowed ? undefined : Math.ceil((resetTime - now) / 1000),
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
    blockDuration: 300, // block for 5 minutes if exceeded
  },
  1, // consume 1 point
);

if (!result.allowed) {
  throw new Error(`Rate limit exceeded. Retry after ${result.retryAfter}s`);
}
```
