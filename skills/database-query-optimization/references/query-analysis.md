# Query Analysis

## Query Analysis

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
