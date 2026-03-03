# Optimization Checklist

## Optimization Checklist

```yaml
Analysis:
  [ ] Run EXPLAIN ANALYZE on slow queries
  [ ] Check actual vs estimated rows
  [ ] Look for sequential scans
  [ ] Identify expensive operations
  [ ] Compare execution plans

Indexing:
  [ ] Index WHERE columns
  [ ] Index JOIN columns
  [ ] Index ORDER BY columns
  [ ] Check unused indexes
  [ ] Remove duplicate indexes
  [ ] Create composite indexes strategically
  [ ] Analyze index statistics

Query Optimization:
  [ ] Remove unnecessary columns (SELECT *)
  [ ] Use JOINs instead of subqueries
  [ ] Avoid functions in WHERE
  [ ] Use wildcards carefully (avoid %)
  [ ] Batch operations
  [ ] Use LIMIT for result sets
  [ ] Archive old data

Caching:
  [ ] Implement query caching
  [ ] Cache aggregations
  [ ] Use Redis for hot data
  [ ] Invalidate strategically

Monitoring:
  [ ] Track slow queries
  [ ] Monitor index usage
  [ ] Set up alerts
  [ ] Regular statistics update
  [ ] Measure improvements

---

Expected Improvements:

With Proper Indexing:
  - Sequential Scan → Index Scan
  - Response time: 5 seconds → 50ms (100x faster)
  - CPU usage: 80% → 20%
  - Concurrent users: 100 → 1000

Quick Wins:
  - Add index to frequently filtered column
  - Fix N+1 queries
  - Use LIMIT for large results
  - Archive old data
  - Expected: 20-50% improvement
```
