---
name: sql-query-optimization
description: Analyze and optimize SQL queries for performance. Use when improving slow queries, reducing execution time, or analyzing query performance in PostgreSQL and MySQL.
---

# SQL Query Optimization

## Overview

Analyze SQL queries to identify performance bottlenecks and implement optimization techniques. Includes query analysis, indexing strategies, and rewriting patterns for improved performance.

## When to Use

- Slow query analysis and tuning
- Query rewriting and refactoring
- Index utilization verification
- Join optimization
- Subquery optimization
- Query plan analysis (EXPLAIN)
- Performance baseline establishment

## Query Analysis Framework

### 1. Analyze Current Performance

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

### 2. Common Optimization Patterns

**PostgreSQL - Index Optimization:**

```sql
-- Create indexes for frequently filtered columns
CREATE INDEX idx_orders_user_created
ON orders(user_id, created_at DESC)
WHERE status != 'cancelled';

-- Partial indexes for filtered queries
CREATE INDEX idx_active_products
ON products(category_id)
WHERE active = true;

-- Multi-column covering indexes
CREATE INDEX idx_users_email_verified_covering
ON users(email, verified)
INCLUDE (id, name, created_at);
```

**MySQL - Index Optimization:**

```sql
-- Create composite index for multi-column filtering
CREATE INDEX idx_orders_user_created
ON orders(user_id, created_at DESC);

-- Use FULLTEXT index for text search
CREATE FULLTEXT INDEX idx_products_search
ON products(name, description);

-- Prefix indexes for large VARCHAR
CREATE INDEX idx_large_text
ON large_table(text_column(100));
```

### 3. Query Rewriting Techniques

**PostgreSQL - Window Functions:**

```sql
-- Inefficient: multiple passes
SELECT p.id, p.name,
  (SELECT COUNT(*) FROM orders o WHERE o.product_id = p.id) as order_count,
  (SELECT SUM(quantity) FROM order_items oi WHERE oi.product_id = p.id) as total_sold
FROM products p;

-- Optimized: single pass with window functions
SELECT DISTINCT p.id, p.name,
  COUNT(*) OVER (PARTITION BY p.id) as order_count,
  SUM(oi.quantity) OVER (PARTITION BY p.id) as total_sold
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id;
```

**MySQL - JOIN Optimization:**

```sql
-- Inefficient: JOIN after aggregation
SELECT user_id, name, total_orders
FROM (
  SELECT u.id as user_id, u.name, COUNT(o.id) as total_orders
  FROM users u
  LEFT JOIN orders o ON u.id = o.user_id
  GROUP BY u.id, u.name
) subquery
WHERE total_orders > 5;

-- Optimized: aggregate with HAVING clause
SELECT u.id, u.name, COUNT(o.id) as total_orders
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
HAVING COUNT(o.id) > 5;
```

### 4. Batch Operations

**PostgreSQL - Bulk Insert:**

```sql
-- Inefficient: multiple round trips
INSERT INTO users (email, name) VALUES ('user1@example.com', 'User One');
INSERT INTO users (email, name) VALUES ('user2@example.com', 'User Two');

-- Optimized: single batch
INSERT INTO users (email, name) VALUES
  ('user1@example.com', 'User One'),
  ('user2@example.com', 'User Two'),
  ('user3@example.com', 'User Three')
ON CONFLICT (email) DO UPDATE SET updated_at = NOW();
```

**MySQL - Bulk Update:**

```sql
-- Optimized: bulk update with VALUES clause
UPDATE products p
JOIN (
  SELECT id, price FROM product_updates
) AS updates ON p.id = updates.id
SET p.price = updates.price;
```

## Performance Monitoring

**PostgreSQL - Long Running Queries:**

```sql
-- Find slow queries
SELECT query, calls, mean_exec_time, total_exec_time
FROM pg_stat_statements
WHERE mean_exec_time > 1000
ORDER BY mean_exec_time DESC
LIMIT 10;

-- Reset statistics
SELECT pg_stat_statements_reset();
```

**MySQL - Slow Query Log:**

```sql
-- Enable slow query log
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 2;

-- View slow queries
SELECT * FROM mysql.slow_log
ORDER BY start_time DESC LIMIT 10;
```

## Key Optimization Checklist

- Use EXPLAIN/EXPLAIN ANALYZE before and after optimization
- Add indexes to columns in WHERE, JOIN, and ORDER BY clauses
- Use LIMIT when exploring large result sets
- Avoid SELECT * when only specific columns needed
- Use database functions instead of application-level processing
- Batch operations to reduce network round trips
- Partition large tables for improved query performance
- Update statistics regularly with ANALYZE

## Common Pitfalls

❌ Don't create indexes without testing impact
❌ Don't use LIKE with leading wildcard without full-text search
❌ Don't JOIN unnecessary tables
❌ Don't ignore ORDER BY performance impact
❌ Don't skip EXPLAIN analysis

✅ DO test query changes in development first
✅ DO monitor query performance after deployment
✅ DO update table statistics regularly
✅ DO use appropriate data types for columns
✅ DO consider materialized views for complex aggregations

## Resources

- [PostgreSQL EXPLAIN Documentation](https://www.postgresql.org/docs/current/sql-explain.html)
- [MySQL EXPLAIN Documentation](https://dev.mysql.com/doc/refman/8.0/en/explain.html)
- [pgBadger - PostgreSQL log analyzer](https://pgbadger.darold.net/)
- [MySQL Workbench Query Analyzer](https://www.mysql.com/products/workbench/)
