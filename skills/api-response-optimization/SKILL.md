---
name: api-response-optimization
description: Optimize API response times through caching, compression, and efficient payloads. Improve backend performance and reduce network traffic.
---

# API Response Optimization

## Overview

Fast API responses improve overall application performance and user experience. Optimization focuses on payload size, caching, and query efficiency.

## When to Use

- Slow API response times
- High server CPU/memory usage
- Large response payloads
- Performance degradation
- Scaling bottlenecks

## Instructions

### 1. **Response Payload Optimization**

```javascript
// Inefficient response (unnecessary data)
GET /api/users/123
{
  "id": 123,
  "name": "John",
  "email": "john@example.com",
  "password_hash": "...", // ❌ Should never send
  "ssn": "123-45-6789", // ❌ Sensitive data
  "internal_id": "xyz",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-02T00:00:00Z",
  "meta_data": {...}, // ❌ Unused fields
  "address": {
    "street": "123 Main",
    "city": "City",
    "state": "ST",
    "zip": "12345",
    "geo": {...} // ❌ Not needed
  }
}

// Optimized response (only needed fields)
GET /api/users/123
{
  "id": 123,
  "name": "John",
  "email": "john@example.com"
}

// Results: 2KB → 100 bytes (20x smaller)

// Sparse fieldsets pattern
GET /api/users/123?fields=name,email
{
  "id": 123,
  "name": "John",
  "email": "john@example.com"
}
```

### 2. **Caching Strategies**

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

### 3. **Compression & Performance**

```yaml
Compression:

gzip:
  Ratio: 60-80% reduction
  Format: text/html, application/json
  Overhead: CPU (minor)

brotli:
  Ratio: 20% better than gzip
  Support: Modern browsers (95%)
  Overhead: Higher CPU

Implementation:
  - Enable in server
  - Set Accept-Encoding headers
  - Measure: Before/after sizes
  - Monitor: CPU impact

---

Performance Optimization:

Pagination:
  - Limit: 20-100 items per request
  - Offset pagination: Simple, slow for large offsets
  - Cursor pagination: Efficient, stable
  - Implementation: Always use limit

Filtering:
  - Server-side filtering
  - Reduce response size
  - Example: ?status=active

Sorting:
  - Server-side only
  - Index frequently sorted fields
  - Limit sort keys to 1-2 fields

Eager Loading:
  - Fetch related data in one query
  - Avoid N+1 problem
  - Example: /users?include=posts

---

Metrics & Monitoring:

Track:
  - API response time (target: <200ms)
  - Payload size (target: <100KB)
  - Cache hit rate (target: >80%)
  - Server CPU/memory

Tools:
  - New Relic APM
  - DataDog
  - Prometheus
  - Custom logging

Setup alerts:
  - Response time >500ms
  - Payload >500KB
  - Cache miss spike
  - Error rates
```

### 4. **Optimization Checklist**

```yaml
Payload:
  [ ] Remove sensitive data
  [ ] Remove unused fields
  [ ] Implement sparse fieldsets
  [ ] Compress payload
  [ ] Use appropriate status codes

Caching:
  [ ] HTTP caching headers set
  [ ] ETags implemented
  [ ] Application cache configured
  [ ] Cache invalidation strategy
  [ ] Cache monitoring

Query Efficiency:
  [ ] Database queries optimized
  [ ] N+1 queries fixed
  [ ] Joins optimized
  [ ] Indexes in place

Compression:
  [ ] gzip enabled
  [ ] brotli enabled (modern)
  [ ] Accept-Encoding headers
  [ ] Content-Encoding responses

Monitoring:
  [ ] Response time tracked
  [ ] Payload size tracked
  [ ] Cache metrics
  [ ] Error rates
  [ ] Alerts configured

Expected Improvements:
  - Response time: 500ms → 100ms
  - Payload size: 500KB → 50KB
  - Server load: 80% CPU → 30%
  - Concurrent users: 100 → 1000
```

## Key Points

- Remove unnecessary data from responses
- Implement HTTP caching headers
- Use ETag for revalidation
- Paginate large result sets
- Enable gzip/brotli compression
- Monitor response times
- Cache expensive queries
- Implement sparse fieldsets
- Measure before and after
- Set up continuous monitoring
