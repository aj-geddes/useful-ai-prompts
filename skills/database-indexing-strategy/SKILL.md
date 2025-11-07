---
name: database-indexing-strategy
description: Design and implement database indexing strategies. Use when creating indexes, choosing index types, or optimizing index performance in PostgreSQL and MySQL.
---

# Database Indexing Strategy

## Overview

Design comprehensive indexing strategies to improve query performance, reduce lock contention, and maintain data integrity. Covers index types, design patterns, and maintenance procedures.

## When to Use

- Index creation and planning
- Query performance optimization through indexing
- Index type selection (B-tree, Hash, GiST, BRIN)
- Composite and partial index design
- Index maintenance and monitoring
- Storage optimization with indexes
- Full-text search index design

## Index Types and Use Cases

### PostgreSQL Index Types

**B-tree Indexes (Default):**

```sql
-- Standard equality and range queries
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_created_at ON orders(created_at DESC);

-- Composite indexes for multi-column queries
CREATE INDEX idx_orders_user_status
ON orders(user_id, status)
WHERE cancelled_at IS NULL;
```

**Hash Indexes:**

```sql
-- Exact match queries only
CREATE INDEX idx_product_sku USING hash ON products(sku);

-- Good for equality lookups on large text fields
CREATE INDEX idx_uuid_hash USING hash ON sessions(session_id);
```

**BRIN Indexes (Block Range):**

```sql
-- For large tables with monotonically increasing columns
CREATE INDEX idx_events_timestamp USING brin ON events(created_at)
WITH (pages_per_range = 128);

-- Excellent for time-series data
CREATE INDEX idx_logs_timestamp USING brin
ON application_logs(log_timestamp);
```

**GiST & GIN Indexes:**

```sql
-- GiST for spatial data and complex types
CREATE INDEX idx_locations_geom USING gist ON locations(geom);

-- GIN for JSONB and array columns
CREATE INDEX idx_products_metadata USING gin ON products(metadata);
CREATE INDEX idx_user_tags USING gin ON users(tags);
```

### MySQL Index Types

**B-tree Indexes:**

```sql
-- Standard index for most queries
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_created
ON orders(user_id, created_at);

-- Prefix indexes for large columns
CREATE INDEX idx_description_prefix
ON products(description(100));
```

**FULLTEXT Indexes:**

```sql
-- Full-text search on text columns
CREATE FULLTEXT INDEX idx_products_search
ON products(name, description);

-- Query using MATCH...AGAINST
SELECT * FROM products
WHERE MATCH(name, description) AGAINST('laptop' IN BOOLEAN MODE);
```

**Spatial Indexes:**

```sql
-- For geographic data
CREATE SPATIAL INDEX idx_locations
ON locations(geom);
```

## Index Design Patterns

### Single Column Indexes

**PostgreSQL:**

```sql
-- Filtered index for active records only
CREATE INDEX idx_users_active
ON users(created_at)
WHERE deleted_at IS NULL;

-- Descending order for LIMIT queries
CREATE INDEX idx_posts_published DESC
ON posts(published_at DESC)
WHERE status = 'published';
```

**MySQL:**

```sql
-- Simple equality lookup
CREATE INDEX idx_users_verified ON users(email_verified);

-- Range queries on numeric columns
CREATE INDEX idx_products_price ON products(price);
```

### Composite Indexes

**PostgreSQL - Optimal Ordering:**

```sql
-- Order: equality columns, then range, then sort
-- Query: WHERE user_id = X AND created_at > Y ORDER BY id
CREATE INDEX idx_optimal_composite
ON orders(user_id, created_at, id);

-- Covering index to eliminate table access
CREATE INDEX idx_covering_orders
ON orders(user_id, status, created_at)
INCLUDE (total, currency);
```

**MySQL - Leftmost Prefix:**

```sql
-- MySQL uses leftmost prefix matching
-- Can be used by: (user_id), (user_id, status), (user_id, status, created_at)
CREATE INDEX idx_users_complex
ON users(user_id, status, created_at);

-- For queries: user_id + status + created_at
SELECT * FROM orders
WHERE user_id = 1 AND status = 'completed' AND created_at > '2024-01-01';
```

### Partial/Filtered Indexes

**PostgreSQL:**

```sql
-- Only index active products
CREATE INDEX idx_active_products
ON products(category_id)
WHERE active = true;

-- Reduce index size and improve performance
CREATE INDEX idx_not_cancelled_orders
ON orders(user_id, created_at)
WHERE status != 'cancelled';

-- Complex filter conditions
CREATE INDEX idx_vip_orders
ON orders(total DESC)
WHERE total > 10000 AND customer_type = 'vip';
```

### Expression Indexes

**PostgreSQL:**

```sql
-- Index on computed values
CREATE INDEX idx_users_email_lower
ON users(LOWER(email));

-- Enable case-insensitive searches
SELECT * FROM users WHERE LOWER(email) = 'john@example.com';

-- Date extraction indexes
CREATE INDEX idx_orders_year
ON orders(EXTRACT(YEAR FROM created_at));
```

## Index Maintenance

**PostgreSQL Index Analysis:**

```sql
-- Check index size and usage
SELECT schemaname, tablename, indexname,
  pg_size_pretty(pg_relation_size(indexrelid)) as size,
  idx_scan as scans,
  idx_tup_read as tuples_read
FROM pg_stat_user_indexes
ORDER BY pg_relation_size(indexrelid) DESC;

-- Find unused indexes
SELECT schemaname, tablename, indexname
FROM pg_stat_user_indexes
WHERE idx_scan = 0 AND indexrelname NOT LIKE 'pg_toast%';

-- Rebuild fragmented indexes
REINDEX INDEX idx_users_email;
```

**MySQL Index Statistics:**

```sql
-- Check index cardinality
SELECT object_schema, object_name, count_star
FROM performance_schema.table_io_waits_summary_by_index_usage
WHERE object_schema != 'mysql'
ORDER BY count_star DESC;

-- Update table statistics
ANALYZE TABLE users;
ANALYZE TABLE orders;
```

## Concurrent Index Creation

**PostgreSQL - Non-blocking Index Creation:**

```sql
-- Create index without locking table (PostgreSQL 9.2+)
CREATE INDEX CONCURRENTLY idx_new_column
ON large_table(new_column);

-- Safe for production
REINDEX INDEX CONCURRENTLY idx_products_price;
```

**MySQL - Concurrent Index Creation:**

```sql
-- MySQL 8.0 supports ALGORITHM=INPLACE with LOCK=NONE
ALTER TABLE users ADD INDEX idx_created (created_at),
ALGORITHM=INPLACE, LOCK=NONE;

-- Check online DDL progress
SELECT * FROM INFORMATION_SCHEMA.INNODB_TRX;
```

## Performance Monitoring

**PostgreSQL - Index Performance:**

```sql
-- Top 10 most scanned indexes
SELECT schemaname, tablename, indexname, idx_scan
FROM pg_stat_user_indexes
ORDER BY idx_scan DESC LIMIT 10;

-- Indexes with high read/scan ratio
SELECT indexname, idx_scan, idx_tup_read,
  CASE WHEN idx_scan = 0 THEN 0
    ELSE ROUND(idx_tup_read::numeric / idx_scan, 2) END as efficiency
FROM pg_stat_user_indexes
WHERE idx_scan > 0
ORDER BY efficiency DESC;
```

**MySQL - Index Statistics:**

```sql
-- Show table index information
SHOW INDEX FROM products;

-- Check cardinality (distribution)
SELECT * FROM information_schema.STATISTICS
WHERE TABLE_SCHEMA = 'your_database'
  AND TABLE_NAME = 'products'
ORDER BY SEQ_IN_INDEX;
```

## Index Creation Checklist

- Identify slow queries with EXPLAIN/EXPLAIN ANALYZE
- Check filter columns, JOIN conditions, ORDER BY clauses
- Consider index order (equality → range → sort)
- Use partial indexes to reduce size on large tables
- Include columns for covering indexes
- Monitor index usage after creation
- Drop unused indexes to save space
- Rebuild fragmented indexes periodically

## Common Mistakes

❌ Don't create too many indexes (write performance impact)
❌ Don't create indexes without testing first
❌ Don't ignore index size and storage impact
❌ Don't forget to update table statistics after bulk operations
❌ Don't create duplicate indexes

✅ DO create indexes on foreign keys
✅ DO test index impact on INSERT/UPDATE performance
✅ DO use covering indexes for common queries
✅ DO drop unused indexes regularly
✅ DO monitor index fragmentation

## Resources

- [PostgreSQL Indexes Documentation](https://www.postgresql.org/docs/current/indexes.html)
- [MySQL Indexes Documentation](https://dev.mysql.com/doc/refman/8.0/en/optimization-indexes.html)
- [PostgreSQL Index Types](https://www.postgresql.org/docs/current/indexes-types.html)
