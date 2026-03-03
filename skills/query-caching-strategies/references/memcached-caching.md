# Memcached Caching

## Memcached Caching

**PostgreSQL with Memcached:**

```javascript
// Node.js with Memcached
const Memcached = require("memcached");
const memcached = new Memcached(["localhost:11211"]);

async function getProductWithCache(productId) {
  const cacheKey = `product:${productId}`;

  try {
    // Try cache first
    const cached = await memcached.get(cacheKey);
    if (cached) return cached;
  } catch (err) {
    // Memcached down, continue to database
  }

  // Query database
  const product = await db.query("SELECT * FROM products WHERE id = $1", [
    productId,
  ]);

  // Set cache (TTL: 3600 seconds)
  try {
    await memcached.set(cacheKey, product, 3600);
  } catch (err) {
    // Fail silently, serve from database
  }

  return product;
}
```
