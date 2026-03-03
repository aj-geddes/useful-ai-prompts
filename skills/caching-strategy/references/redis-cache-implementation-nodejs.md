# Redis Cache Implementation (Node.js)

## Redis Cache Implementation (Node.js)

```typescript
import Redis from "ioredis";

interface CacheOptions {
  ttl?: number; // Time to live in seconds
  prefix?: string;
}

class CacheService {
  private redis: Redis;
  private defaultTTL = 3600; // 1 hour

  constructor(redisUrl: string) {
    this.redis = new Redis(redisUrl, {
      retryStrategy: (times) => {
        const delay = Math.min(times * 50, 2000);
        return delay;
      },
      maxRetriesPerRequest: 3,
    });

    this.redis.on("connect", () => {
      console.log("Redis connected");
    });

    this.redis.on("error", (error) => {
      console.error("Redis error:", error);
    });
  }

  /**
   * Get cached value
   */
  async get<T>(key: string): Promise<T | null> {
    try {
      const value = await this.redis.get(key);
      if (!value) return null;

      return JSON.parse(value) as T;
    } catch (error) {
      console.error(`Cache get error for key ${key}:`, error);
      return null;
    }
  }

  /**
   * Set cached value
   */
  async set(
    key: string,
    value: any,
    options: CacheOptions = {},
  ): Promise<boolean> {
    try {
      const ttl = options.ttl || this.defaultTTL;
      const serialized = JSON.stringify(value);

      if (ttl > 0) {
        await this.redis.setex(key, ttl, serialized);
      } else {
        await this.redis.set(key, serialized);
      }

      return true;
    } catch (error) {
      console.error(`Cache set error for key ${key}:`, error);
      return false;
    }
  }

  /**
   * Delete cached value
   */
  async delete(key: string): Promise<boolean> {
    try {
      await this.redis.del(key);
      return true;
    } catch (error) {
      console.error(`Cache delete error for key ${key}:`, error);
      return false;
    }
  }

  /**
   * Delete multiple keys by pattern
   */
  async deletePattern(pattern: string): Promise<number> {
    try {
      const keys = await this.redis.keys(pattern);
      if (keys.length === 0) return 0;

      await this.redis.del(...keys);
      return keys.length;
    } catch (error) {
      console.error(`Cache delete pattern error for ${pattern}:`, error);
      return 0;
    }
  }

  /**
   * Get or set pattern - fetch from cache or compute and cache
   */
  async getOrSet<T>(
    key: string,
    fetchFn: () => Promise<T>,
    options: CacheOptions = {},
  ): Promise<T> {
    // Try to get from cache
    const cached = await this.get<T>(key);
    if (cached !== null) {
      return cached;
    }

    // Fetch and cache
    const value = await fetchFn();
    await this.set(key, value, options);

    return value;
  }

  /**
   * Implement cache-aside pattern with stale-while-revalidate
   */
  async getStaleWhileRevalidate<T>(
    key: string,
    fetchFn: () => Promise<T>,
    options: {
      ttl: number;
      staleTime: number;
    },
  ): Promise<T> {
    const cacheKey = `cache:${key}`;
    const timestampKey = `cache:${key}:timestamp`;

    const [cached, timestamp] = await Promise.all([
      this.get<T>(cacheKey),
      this.redis.get(timestampKey),
    ]);

    const now = Date.now();
    const age = timestamp ? now - parseInt(timestamp) : Infinity;

    // Return cached if fresh
    if (cached !== null && age < options.ttl * 1000) {
      return cached;
    }

    // Return stale while revalidating in background
    if (cached !== null && age < options.staleTime * 1000) {
      // Background revalidation
      fetchFn()
        .then(async (fresh) => {
          await this.set(cacheKey, fresh, { ttl: options.ttl });
          await this.redis.set(timestampKey, now.toString());
        })
        .catch(console.error);

      return cached;
    }

    // Fetch fresh data
    const fresh = await fetchFn();
    await Promise.all([
      this.set(cacheKey, fresh, { ttl: options.ttl }),
      this.redis.set(timestampKey, now.toString()),
    ]);

    return fresh;
  }

  /**
   * Increment counter with TTL
   */
  async increment(key: string, ttl?: number): Promise<number> {
    const count = await this.redis.incr(key);

    if (count === 1 && ttl) {
      await this.redis.expire(key, ttl);
    }

    return count;
  }

  /**
   * Check if key exists
   */
  async exists(key: string): Promise<boolean> {
    const result = await this.redis.exists(key);
    return result === 1;
  }

  /**
   * Get remaining TTL
   */
  async ttl(key: string): Promise<number> {
    return await this.redis.ttl(key);
  }

  /**
   * Close connection
   */
  async disconnect(): Promise<void> {
    await this.redis.quit();
  }
}

// Usage
const cache = new CacheService("redis://localhost:6379");

// Simple get/set
await cache.set("user:123", { name: "John", age: 30 }, { ttl: 3600 });
const user = await cache.get("user:123");

// Get or set pattern
const posts = await cache.getOrSet(
  "posts:recent",
  async () => {
    return await database.query(
      "SELECT * FROM posts ORDER BY created_at DESC LIMIT 10",
    );
  },
  { ttl: 300 },
);

// Stale-while-revalidate
const data = await cache.getStaleWhileRevalidate(
  "expensive-query",
  async () => await runExpensiveQuery(),
  { ttl: 300, staleTime: 600 },
);
```
