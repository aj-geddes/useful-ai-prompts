# PostgreSQL Query Cache

## PostgreSQL Query Cache

**Materialized Views for Caching:**

```sql
-- Create materialized view for expensive query
CREATE MATERIALIZED VIEW user_statistics AS
SELECT
  u.id,
  u.email,
  COUNT(o.id) as total_orders,
  SUM(o.total) as total_spent,
  AVG(o.total) as avg_order_value,
  MAX(o.created_at) as last_order_date
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.email;

-- Index materialized view for fast access
CREATE INDEX idx_user_stats_email ON user_statistics(email);

-- Refresh strategy (scheduled)
REFRESH MATERIALIZED VIEW CONCURRENTLY user_statistics;

-- Query view instead of base tables
SELECT * FROM user_statistics WHERE email = 'john@example.com';
```

**Partial Indexes for Query Optimization:**

```sql
-- Index only active users (reduce index size)
CREATE INDEX idx_active_users ON users(created_at DESC)
WHERE active = true AND deleted_at IS NULL;

-- Index recently created records
CREATE INDEX idx_recent_orders ON orders(user_id, total DESC)
WHERE created_at > NOW() - INTERVAL '30 days';
```
