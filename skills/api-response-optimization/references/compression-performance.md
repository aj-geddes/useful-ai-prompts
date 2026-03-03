# Compression & Performance

## Compression & Performance

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
