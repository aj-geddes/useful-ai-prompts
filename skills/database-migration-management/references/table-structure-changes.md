# Table Structure Changes

## Table Structure Changes

**PostgreSQL - Alter Table Migration:**

```sql
-- Migration: 20240115_005_modify_order_columns.sql

-- Add new column
ALTER TABLE orders
ADD COLUMN status_updated_at TIMESTAMP;

-- Add constraint
ALTER TABLE orders
ADD CONSTRAINT valid_status
CHECK (status IN ('pending', 'processing', 'completed', 'cancelled'));

-- Set default for existing records
UPDATE orders
SET status_updated_at = updated_at
WHERE status_updated_at IS NULL;

-- Make column NOT NULL
ALTER TABLE orders
ALTER COLUMN status_updated_at SET NOT NULL;

-- Rollback:
-- ALTER TABLE orders DROP COLUMN status_updated_at;
-- ALTER TABLE orders DROP CONSTRAINT valid_status;
```
