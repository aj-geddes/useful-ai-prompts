# The 5 Whys Technique

## The 5 Whys Technique

```yaml
Example: Website Down

Symptom: Website returned 503 Service Unavailable

Why 1: Why was website down?
  Answer: Database connection pool exhausted

Why 2: Why was connection pool exhausted?
  Answer: Queries taking too long, connections not released

Why 3: Why were queries slow?
  Answer: Missing index on frequently queried column

Why 4: Why was index missing?
  Answer: Performance testing didn't use production-like data volume

Why 5: Why wasn't production-like data used?
  Answer: Load testing environment doesn't mirror production

Root Cause: Load testing environment under-provisioned

Solution: Update load testing environment with production-like data

Prevention: Establish environment parity requirements
```
