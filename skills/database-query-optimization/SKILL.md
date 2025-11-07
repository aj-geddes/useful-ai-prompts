---
name: database-query-optimization
description: Improve database query performance through indexing, query optimization, and execution plan analysis. Reduce response times and database load.
---

# Database Query Optimization

## Overview

Slow database queries are a common performance bottleneck. Optimization through indexing, efficient queries, and caching dramatically improves application performance.

## When to Use

- Slow response times
- High database CPU usage
- Performance regression
- New feature deployment
- Regular maintenance

## Instructions

### 1. **Query Analysis**

```sql
-- Analyze query performance

EXPLAIN ANALYZE
SELECT users.id, users.name, COUNT(orders.id) as order_count
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE users.created_at > '2024-01-01'
GROUP BY users.id, users.name
ORDER BY order_count DESC;

-- Results show:
-- - Seq Scan (slow) vs Index Scan (fast)
-- - Rows: actual vs planned (high variance = bad)
-- - Execution time (milliseconds)

-- Key metrics:
-- - Sequential Scan: Full table read (slow)
-- - Index Scan: Uses index (fast)
-- - Nested Loop: Joins with loops
-- - Sort: In-memory or disk sort
```

### 2. **Indexing Strategy**

```yaml
Index Types:

Single Column:
  CREATE INDEX idx_users_email ON users(email);
  Use: WHERE email = ?
  Size: Small, quick to create

Composite Index:
  CREATE INDEX idx_orders_user_date
    ON orders(user_id, created_at);
  Use: WHERE user_id = ? AND created_at > ?
  Order: Most selective first

Covering Index:
  CREATE INDEX idx_orders_covering
    ON orders(user_id) INCLUDE (total_amount);
  Benefit: No table lookup needed

Partial Index:
  CREATE INDEX idx_active_users
    ON users(id) WHERE status = 'active';
  Benefit: Smaller, faster

Full Text:
  CREATE FULLTEXT INDEX idx_search
    ON articles(title, content);
  Use: Text search queries

---

Index Rules:

- Create indexes for WHERE conditions
- Create indexes for JOIN columns
- Create indexes for ORDER BY
- Don't over-index (slows writes)
- Monitor index usage
- Remove unused indexes
- Update statistics regularly
- Partial indexes for filtered queries

Missing Index Query:
SELECT object_name, equality_columns
FROM sys.dm_db_missing_index_details
ORDER BY equality_columns;
```

### 3. **Query Optimization Techniques**

```python
# Common optimization patterns

# BEFORE (N+1 queries)
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)
    # 1 + N queries

# AFTER (single query with JOIN)
orders = db.query("""
  SELECT u.*, o.* FROM users u
  LEFT JOIN orders o ON u.id = o.user_id
  WHERE u.created_at > ?
""", date_threshold)

# BEFORE (inefficient WHERE)
SELECT * FROM users
WHERE LOWER(email) = LOWER('Test@Example.com')
# Can't use index (function used)

# AFTER (index-friendly)
SELECT * FROM users
WHERE email = 'test@example.com'
# Case-insensitive constraint + index

# BEFORE (wildcard at start)
SELECT * FROM users WHERE email LIKE '%example.com'
# Can't use index (wildcard at start)

# AFTER (wildcard at end)
SELECT * FROM users WHERE email LIKE 'user%'
# Can use index

# BEFORE (slow aggregation)
SELECT user_id, COUNT(*) as cnt
FROM orders
GROUP BY user_id
ORDER BY cnt DESC
LIMIT 10

# AFTER (pre-aggregated)
SELECT user_id, order_count
FROM user_order_stats
WHERE order_count IS NOT NULL
ORDER BY order_count DESC
LIMIT 10
```

### 4. **Optimization Checklist**

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

## Key Points

- EXPLAIN ANALYZE shows query execution
- Indexes must match WHERE/JOIN/ORDER BY
- Avoid functions in WHERE clauses
- Fix N+1 queries (join instead of loop)
- Monitor slow query log regularly
- Stats updates needed for accuracy
- Pre-calculate aggregations
- Archive historical data
- Use explain plans before/after
- Measure and monitor continuously
