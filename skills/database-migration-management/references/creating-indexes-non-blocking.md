# Creating Indexes Non-blocking

## Creating Indexes Non-blocking

**PostgreSQL - Concurrent Index Creation:**

```sql
-- Migration: 20240115_003_add_performance_indexes.sql

-- Create indexes without blocking writes
CREATE INDEX CONCURRENTLY idx_orders_user_created
ON orders(user_id, created_at DESC);

CREATE INDEX CONCURRENTLY idx_products_category_active
ON products(category_id)
WHERE active = true;

-- Verify index creation
SELECT schemaname, tablename, indexname, idx_scan
FROM pg_stat_user_indexes
WHERE indexname LIKE 'idx_%';

-- Rollback:
-- DROP INDEX CONCURRENTLY idx_orders_user_created;
-- DROP INDEX CONCURRENTLY idx_products_category_active;
```

**MySQL - Online Index Creation:**

```sql
-- Migration: 20240115_003_add_performance_indexes.sql

-- Create indexes with ALGORITHM=INPLACE and LOCK=NONE
ALTER TABLE orders
ADD INDEX idx_user_created (user_id, created_at),
ALGORITHM=INPLACE, LOCK=NONE;

-- Monitor progress
SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST
WHERE INFO LIKE 'ALTER TABLE%';
```
