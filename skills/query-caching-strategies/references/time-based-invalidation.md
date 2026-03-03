# Time-Based Invalidation

## Time-Based Invalidation

**TTL-Based Cache Expiration:**

```javascript
// Variable TTL based on data type
const CACHE_TTLS = {
  user_profile: 3600, // 1 hour
  product_list: 1800, // 30 minutes
  order_summary: 300, // 5 minutes (frequently changes)
  category_list: 86400, // 1 day (rarely changes)
  user_settings: 7200, // 2 hours
};

async function getCachedData(key, type, queryFn) {
  const cached = await client.get(key);
  if (cached) return JSON.parse(cached);

  const result = await queryFn();
  const ttl = CACHE_TTLS[type] || 3600;

  await client.setex(key, ttl, JSON.stringify(result));
  return result;
}
```


## LRU Cache Eviction

**Redis LRU Policy:**

```conf
# redis.conf
maxmemory 1gb
maxmemory-policy allkeys-lru  # Evict least recently used key

# Or other policies:
# volatile-lru: evict any key with TTL (LRU)
# allkeys-lfu: evict least frequently used key
# volatile-ttl: evict key with shortest TTL
```
