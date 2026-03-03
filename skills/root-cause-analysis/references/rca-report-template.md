# RCA Report Template

## RCA Report Template

```yaml
RCA Report:

Incident: Database connection failure (2024-01-15, 14:30-15:15)

Impact:
  - Duration: 45 minutes
  - Users affected: 5,000 (10% of user base)
  - Revenue lost: ~$2,000
  - Severity: P1 (Critical)

Timeline:
  14:30: Automated monitoring alert: High error rate (20%)
  14:32: On-call engineer notified
  14:35: Identified database connection error in logs
  14:40: Restarted database connection pool
  14:42: Service recovered, error rate returned to 0.1%
  14:50: Incident declared resolved
  15:15: Full recovery verified

Root Cause:
  Poorly optimized query introduced in release 2.5.0 caused
  queries to take 10x longer. Connection pool exhausted as
  connections weren't released quickly.

Contributing Factors:
  1. No query performance testing pre-deployment
  2. Load testing environment doesn't match production volume
  3. No alerting on query duration
  4. Connection pool timeout set too high

Solutions:
  Immediate (Done):
    - Rolled back problematic query optimization

  Short-term (1 week):
    - Added query performance alerts (>1s)
    - Added index for slow query
    - Set query timeout to 5 seconds

  Long-term (1 month):
    - Updated load testing with production-like data
    - Implement performance benchmarks in CI/CD
    - Improve monitoring for connection pool health
    - Training on query optimization

Prevention:
  - Query performance regression tests
  - Load testing with production data
  - Connection pool metrics monitoring
  - Code review of database changes
```
