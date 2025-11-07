---
name: database-performance-debugging
description: Debug database performance issues through query analysis, index optimization, and execution plan review. Identify and fix slow queries.
---

# Database Performance Debugging

## Overview

Database performance issues directly impact application responsiveness. Debugging focuses on identifying slow queries and optimizing execution plans.

## When to Use

- Slow application response times
- High database CPU
- Slow queries identified
- Performance regression
- Under load stress

## Instructions

### 1. **Identify Slow Queries**

```sql
-- Enable slow query log (MySQL)
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 0.5;

-- View slow queries
SHOW GLOBAL STATUS LIKE 'Slow_queries';
SELECT * FROM mysql.slow_log;

-- PostgreSQL slow queries
CREATE EXTENSION pg_stat_statements;
SELECT mean_exec_time, calls, query
FROM pg_stat_statements
ORDER BY mean_exec_time DESC LIMIT 10;

-- SQL Server slow queries
SELECT TOP 10
  execution_count,
  total_elapsed_time,
  statement_text
FROM sys.dm_exec_query_stats
ORDER BY total_elapsed_time DESC;

-- Query profiling
EXPLAIN ANALYZE
SELECT * FROM orders WHERE user_id = 123;
-- Slow: Seq Scan (full table scan)
-- Fast: Index Scan
```

### 2. **Common Issues & Solutions**

```yaml
Issue: N+1 Query Problem

Symptom: 1001 queries for 1000 records

Example (Python):
  for user in users:
    posts = db.query(Post).filter(Post.user_id == user.id)
    # 1 + 1000 queries

Solution:
  users = db.query(User).options(joinedload(User.posts))
  # Single query with JOIN

---

Issue: Missing Index

Symptom: Seq Scan instead of Index Scan

Solution:
  CREATE INDEX idx_orders_user_id ON orders(user_id);
  Verify: EXPLAIN ANALYZE shows Index Scan now

---

Issue: Inefficient JOIN

Before:
  SELECT * FROM orders o, users u
  WHERE o.user_id = u.id AND u.email LIKE '%@example.com'
  # Bad: Table scan on users for every order

After:
  SELECT o.* FROM orders o
  JOIN users u ON o.user_id = u.id
  WHERE u.email = 'exact@example.com'
  # Good: Single email lookup

---

Issue: Large Table Scan

Symptom: SELECT * FROM large_table (1M rows)

Solutions:
  1. Add LIMIT clause
  2. Add WHERE condition
  3. Select specific columns
  4. Use pagination
  5. Archive old data

---

Issue: Slow Aggregation

Before (1 minute):
  SELECT user_id, COUNT(*), SUM(amount)
  FROM transactions
  GROUP BY user_id

After (50ms):
  SELECT user_id, transaction_count, total_amount
  FROM user_transaction_stats
  WHERE updated_at > NOW() - INTERVAL 1 DAY
  # Materialized view or aggregation table
```

### 3. **Execution Plan Analysis**

```yaml
EXPLAIN Output Understanding:

Seq Scan (Full Table Scan):
  - Reads entire table
  - Slowest method
  - Fix: Add index

Index Scan:
  - Uses index
  - Fast
  - Ideal

Bitmap Index Scan:
  - Partial index scan
  - Converts to heap scan
  - Moderate speed

Nested Loop:
  - For each row in left, scan right
  - O(n*m) complexity
  - Slow for large tables

Hash Join:
  - Build hash table of smaller table
  - Probe with larger table
  - Faster than nested loop

Merge Join:
  - Sort both tables, merge
  - Fastest for large sorted data
  - Requires sort operation

---

Reading EXPLAIN ANALYZE:

Node: Seq Scan on orders (actual 8023.456 ms)
  - Seq Scan = Full table scan
  - actual time = real execution time
  - 8023 ms = TOO SLOW

Rows: 1000000 (estimated) 1000000 (actual)
  - Match = planner accurate
  - Mismatch = update statistics

Node: Index Scan (actual 15.234 ms)
  - Index Scan = Fast
  - 15 ms = ACCEPTABLE
```

### 4. **Debugging Process**

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

## Key Points

- Enable slow query logging in production
- Use EXPLAIN ANALYZE to investigate
- Look for Seq Scan = missing index
- Add indexes to WHERE/JOIN columns
- Monitor query statistics
- Update table statistics regularly
- Rewrite queries to avoid inefficiencies
- Use pagination for large result sets
- Measure before and after optimization
- Track slow query trends
