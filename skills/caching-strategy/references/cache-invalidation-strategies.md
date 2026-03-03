# Cache Invalidation Strategies

## Cache Invalidation Strategies

```typescript
class CacheInvalidation {
  constructor(private cache: CacheService) {}

  /**
   * Time-based invalidation (TTL)
   */
  async setWithTTL(key: string, value: any, seconds: number): Promise<void> {
    await this.cache.set(key, value, { ttl: seconds });
  }

  /**
   * Tag-based invalidation
   */
  async setWithTags(key: string, value: any, tags: string[]): Promise<void> {
    // Store value
    await this.cache.set(key, value);

    // Store tag associations
    for (const tag of tags) {
      await this.cache.redis.sadd(`tag:${tag}`, key);
    }
  }

  async invalidateByTag(tag: string): Promise<number> {
    // Get all keys with this tag
    const keys = await this.cache.redis.smembers(`tag:${tag}`);

    if (keys.length === 0) return 0;

    // Delete all keys
    await Promise.all(keys.map((key) => this.cache.delete(key)));

    // Delete tag set
    await this.cache.redis.del(`tag:${tag}`);

    return keys.length;
  }

  /**
   * Event-based invalidation
   */
  async invalidateOnEvent(
    entity: string,
    id: string,
    event: "create" | "update" | "delete",
  ): Promise<void> {
    const patterns = [
      `${entity}:${id}`,
      `${entity}:${id}:*`,
      `${entity}:list:*`,
      `${entity}:count`,
    ];

    for (const pattern of patterns) {
      await this.cache.deletePattern(pattern);
    }
  }

  /**
   * Version-based invalidation
   */
  async setVersioned(key: string, value: any, version: number): Promise<void> {
    const versionedKey = `${key}:v${version}`;
    await this.cache.set(versionedKey, value);
    await this.cache.set(`${key}:version`, version);
  }

  async getVersioned(key: string): Promise<any> {
    const version = await this.cache.get<number>(`${key}:version`);
    if (!version) return null;

    return await this.cache.get(`${key}:v${version}`);
  }
}
```
