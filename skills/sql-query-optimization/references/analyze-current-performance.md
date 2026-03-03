# Analyze Current Performance

## Analyze Current Performance

**PostgreSQL:**

```sql
-- Analyze query plan with execution time
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
SELECT u.id, u.email, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > NOW() - INTERVAL '1 year'
GROUP BY u.id, u.email;

-- Check table statistics
SELECT * FROM pg_stats
WHERE tablename = 'users' AND attname = 'created_at';
```

**MySQL:**

```sql
-- Analyze query plan
EXPLAIN FORMAT=JSON
SELECT u.id, u.email, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > DATE_SUB(NOW(), INTERVAL 1 YEAR)
GROUP BY u.id, u.email;

-- Check table size
SELECT table_name, ROUND(((data_length + index_length) / 1024 / 1024), 2) AS 'Size_MB'
FROM information_schema.tables WHERE table_schema = 'database_name';
```
