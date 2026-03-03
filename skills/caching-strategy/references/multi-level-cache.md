# Multi-Level Cache

## Multi-Level Cache

```typescript
interface CacheLevel {
  get(key: string): Promise<any>;
  set(key: string, value: any, ttl?: number): Promise<void>;
  delete(key: string): Promise<void>;
}

class MemoryCache implements CacheLevel {
  private cache = new Map<string, { value: any; expiry: number }>();

  async get(key: string): Promise<any> {
    const item = this.cache.get(key);
    if (!item) return null;

    if (Date.now() > item.expiry) {
      this.cache.delete(key);
      return null;
    }

    return item.value;
  }

  async set(key: string, value: any, ttl: number = 60): Promise<void> {
    this.cache.set(key, {
      value,
      expiry: Date.now() + ttl * 1000,
    });
  }

  async delete(key: string): Promise<void> {
    this.cache.delete(key);
  }

  clear(): void {
    this.cache.clear();
  }
}

class RedisCache implements CacheLevel {
  constructor(private redis: Redis) {}

  async get(key: string): Promise<any> {
    const value = await this.redis.get(key);
    return value ? JSON.parse(value) : null;
  }

  async set(key: string, value: any, ttl: number = 3600): Promise<void> {
    await this.redis.setex(key, ttl, JSON.stringify(value));
  }

  async delete(key: string): Promise<void> {
    await this.redis.del(key);
  }
}

class MultiLevelCache {
  private levels: CacheLevel[];

  constructor(levels: CacheLevel[]) {
    this.levels = levels; // Ordered from fastest to slowest
  }

  async get<T>(key: string): Promise<T | null> {
    for (let i = 0; i < this.levels.length; i++) {
      const value = await this.levels[i].get(key);

      if (value !== null) {
        // Backfill faster caches
        for (let j = 0; j < i; j++) {
          await this.levels[j].set(key, value);
        }

        return value as T;
      }
    }

    return null;
  }

  async set(key: string, value: any, ttl?: number): Promise<void> {
    // Set in all cache levels
    await Promise.all(this.levels.map((level) => level.set(key, value, ttl)));
  }

  async delete(key: string): Promise<void> {
    await Promise.all(this.levels.map((level) => level.delete(key)));
  }
}

// Usage
const cache = new MultiLevelCache([new MemoryCache(), new RedisCache(redis)]);

// Get from fastest available cache
const data = await cache.get("user:123");

// Set in all caches
await cache.set("user:123", userData, 3600);
```
