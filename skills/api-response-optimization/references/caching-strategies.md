# Caching Strategies

## Caching Strategies

```yaml
HTTP Caching Headers:

Cache-Control:
  Immutable assets: Cache-Control: public, max-age=31536000
  API responses: Cache-Control: private, max-age=300
  No cache: Cache-Control: no-store
  Revalidate: Cache-Control: max-age=0, must-revalidate

ETag:
  - Unique identifier for response version
  - If-None-Match: return 304 if unchanged
  - Saves bandwidth on unchanged data

Last-Modified:
  - If-Modified-Since: return 304 if unchanged
  - Simple versioning mechanism

---

Application-Level Caching:

Database Query Caching:
  - Cache expensive queries
  - TTL: 5-30 minutes
  - Invalidate on write
  - Tools: Redis, Memcached

Response Caching:
  - Cache entire API responses
  - Use Cache-Control headers
  - Key: URL + query params
  - TTL: Based on data freshness

Fragment Caching:
  - Cache parts of response
  - Combine multiple fragments
  - Different TTL per fragment

---

Cache Invalidation:

Time-based (TTL):
  - Simple: expires after time
  - Risk: stale data
  - Best for: Non-critical data

Event-based:
  - Invalidate on write
  - Immediate freshness
  - Requires coordination

Hybrid:
  - TTL + event invalidation
  - Short TTL + invalidate on change
  - Good balance

---

Implementation Example:

GET /api/users/123/orders
Authorization: Bearer token
Cache-Control: public, max-age=300

Response:
HTTP/1.1 200 OK
Cache-Control: public, max-age=300
ETag: "123abc"
Last-Modified: 2024-01-01

{data: [...]}

-- Next request within 5 minutes from cache
-- After 5 minutes, revalidate with ETag
-- If unchanged: 304 Not Modified
```
