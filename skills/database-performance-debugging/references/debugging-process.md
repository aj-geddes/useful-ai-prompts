# Debugging Process

## Debugging Process

```yaml
Steps:

1. Identify Slow Query
  - Enable slow query logging
  - Run workload
  - Review slow log
  - Note execution time

2. Analyze with EXPLAIN
  - Run EXPLAIN ANALYZE
  - Look for Seq Scan
  - Check estimated vs actual rows
  - Review join methods

3. Find Root Cause
  - Missing index?
  - Inefficient join?
  - Missing WHERE clause?
  - Outdated statistics?

4. Try Fix
  - Add index
  - Rewrite query
  - Update statistics
  - Archive old data

5. Measure Improvement
  - Run query after fix
  - Compare execution time
  - Before: 5000ms
  - After: 100ms (50x faster!)

6. Monitor
  - Track slow queries
  - Set baseline
  - Alert on regression
  - Periodic review

---

Checklist:

[ ] Slow query identified and logged
[ ] EXPLAIN ANALYZE run
[ ] Estimated vs actual rows analyzed
[ ] Seq Scans identified
[ ] Indexes checked
[ ] Join strategy reviewed
[ ] Statistics updated
[ ] Query rewritten if needed
[ ] Index created if needed
[ ] Fix verified
[ ] Performance baseline established
[ ] Monitoring configured
[ ] Documented for team
```
