---
name: api-response-optimization
description: >
  Optimize API response times through caching, compression, and efficient.
  Use when slow api response times, high server cpu/memory usage, large response payloads, or performance degradation.
  payloads. Improve backend performance and reduce network traffic.
---

# API Response Optimization

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Fast API responses improve overall application performance and user experience. Optimization focuses on payload size, caching, and query efficiency.

## When to Use

- Slow API response times
- High server CPU/memory usage
- Large response payloads
- Performance degradation
- Scaling bottlenecks

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Response Payload Optimization](references/response-payload-optimization.md) | Response Payload Optimization |
| [Caching Strategies](references/caching-strategies.md) | Caching Strategies |
| [Compression & Performance](references/compression-performance.md) | Compression & Performance |
| [Optimization Checklist](references/optimization-checklist.md) | Optimization Checklist |

## Best Practices

### ✅ DO

- Return only the fields the client needs — use sparse fieldsets or a projection layer
- Enable gzip/brotli compression for all JSON responses over 1 KB
- Set appropriate `Cache-Control` and `ETag` headers for cacheable endpoints
- Paginate list endpoints and include `total`, `limit`, and `offset` in the response
- Use HTTP 304 (Not Modified) to avoid re-sending unchanged resources
- Profile slow queries with `EXPLAIN ANALYZE` and add indexes before caching around them

### ❌ DON'T

- Expose internal or sensitive fields (`password_hash`, `ssn`, internal IDs) in API responses
- Nest related resources deeply — prefer flat payloads or links for associations
- Cache authenticated or user-specific responses in shared/public caches
- Rely solely on application-level caching without setting HTTP cache headers
