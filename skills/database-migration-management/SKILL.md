---
name: database-migration-management
description: Manage database migrations and schema versioning. Use when planning migrations, version control, rollback strategies, or data transformations in PostgreSQL and MySQL.
---

# Database Migration Management

## Overview

Implement robust database migration systems with version control, rollback capabilities, and data transformation strategies. Includes migration frameworks and production deployment patterns.

## When to Use

- Schema versioning and evolution
- Data transformations and cleanup
- Adding/removing tables and columns
- Index creation and optimization
- Migration testing and validation
- Rollback planning and execution
- Multi-environment deployments

## Migration Framework Setup

### PostgreSQL - Schema Versioning

```sql
-- Create migrations tracking table
CREATE TABLE schema_migrations (
  version BIGINT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  duration_ms INTEGER,
  checksum VARCHAR(64)
);

-- Create migration log table
CREATE TABLE migration_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  version BIGINT NOT NULL,
  status VARCHAR(20) NOT NULL,
  error_message TEXT,
  rolled_back_at TIMESTAMP,
  executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Function to record migration
CREATE OR REPLACE FUNCTION record_migration(
  p_version BIGINT,
  p_name VARCHAR,
  p_duration_ms INTEGER
) RETURNS void AS $$
BEGIN
  INSERT INTO schema_migrations (version, name, duration_ms)
  VALUES (p_version, p_name, p_duration_ms)
  ON CONFLICT (version) DO UPDATE
  SET executed_at = CURRENT_TIMESTAMP;
END;
$$ LANGUAGE plpgsql;
```

### MySQL - Migration Tracking

```sql
-- Create migrations table for MySQL
CREATE TABLE schema_migrations (
  version BIGINT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  duration_ms INT,
  checksum VARCHAR(64)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Migration status table
CREATE TABLE migration_status (
  id INT AUTO_INCREMENT PRIMARY KEY,
  version BIGINT NOT NULL,
  status ENUM('pending', 'completed', 'failed', 'rolled_back'),
  error_message TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## Common Migration Patterns

### Adding Columns

**PostgreSQL - Safe Column Addition:**

```sql
-- Migration: 20240115_001_add_phone_to_users.sql

-- Add column with default (non-blocking)
ALTER TABLE users
ADD COLUMN phone VARCHAR(20) DEFAULT '';

-- Add constraint after population
ALTER TABLE users
ADD CONSTRAINT phone_format
CHECK (phone = '' OR phone ~ '^\+?[0-9\-\(\)]{10,}$');

-- Create index
CREATE INDEX CONCURRENTLY idx_users_phone ON users(phone);

-- Rollback:
-- DROP INDEX CONCURRENTLY idx_users_phone;
-- ALTER TABLE users DROP COLUMN phone;
```

**MySQL - Column Addition:**

```sql
-- Migration: 20240115_001_add_phone_to_users.sql

-- Add column with ALTER
ALTER TABLE users
ADD COLUMN phone VARCHAR(20) DEFAULT '',
ADD INDEX idx_phone (phone);

-- Rollback:
-- ALTER TABLE users DROP COLUMN phone;
```

### Renaming Columns

**PostgreSQL - Column Rename:**

```sql
-- Migration: 20240115_002_rename_user_name_columns.sql

-- Rename columns
ALTER TABLE users RENAME COLUMN user_name TO full_name;
ALTER TABLE users RENAME COLUMN user_email TO email_address;

-- Update indexes
REINDEX TABLE users;

-- Rollback:
-- ALTER TABLE users RENAME COLUMN email_address TO user_email;
-- ALTER TABLE users RENAME COLUMN full_name TO user_name;
```

### Creating Indexes Non-blocking

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

### Data Transformations

**PostgreSQL - Data Cleanup Migration:**

```sql
-- Migration: 20240115_004_normalize_email_addresses.sql

-- Normalize existing email addresses
UPDATE users
SET email = LOWER(TRIM(email))
WHERE email != LOWER(TRIM(email));

-- Remove duplicates by keeping latest
DELETE FROM users
WHERE id NOT IN (
  SELECT DISTINCT ON (LOWER(email)) id
  FROM users
  ORDER BY LOWER(email), created_at DESC
);

-- Rollback: Restore from backup (no safe rollback for data changes)
```

**MySQL - Bulk Data Update:**

```sql
-- Migration: 20240115_004_update_product_categories.sql

-- Update multiple rows with JOIN
UPDATE products p
JOIN category_mapping cm ON p.old_category = cm.old_name
SET p.category_id = cm.new_category_id
WHERE p.old_category IS NOT NULL;

-- Verify update
SELECT COUNT(*) as updated_count
FROM products
WHERE category_id IS NOT NULL;
```

### Table Structure Changes

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

## Testing Migrations

**PostgreSQL - Test in Transaction:**

```sql
-- Test migration in transaction (will be rolled back)
BEGIN;

-- Run migration statements
ALTER TABLE users ADD COLUMN test_column VARCHAR(255);

-- Validate data
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT email) FROM users;

-- Rollback if issues found
ROLLBACK;

-- Or commit if all good
COMMIT;
```

**Validate Migration:**

```sql
-- Check migration was applied
SELECT version, name, executed_at FROM schema_migrations
WHERE version = 20240115005;

-- Verify table structure
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'users'
ORDER BY ordinal_position;
```

## Rollback Strategies

**PostgreSQL - Bidirectional Migrations:**

```sql
-- Migration file: 20240115_006_add_user_status.sql

-- ===== UP =====
CREATE TYPE user_status AS ENUM ('active', 'suspended', 'deleted');
ALTER TABLE users ADD COLUMN status user_status DEFAULT 'active';

-- ===== DOWN =====
-- ALTER TABLE users DROP COLUMN status;
-- DROP TYPE user_status;
```

**Rollback Execution:**

```sql
-- Function to rollback to specific version
CREATE OR REPLACE FUNCTION rollback_to_version(p_target_version BIGINT)
RETURNS TABLE (version BIGINT, name VARCHAR, status VARCHAR) AS $$
BEGIN
  -- Execute down migrations in reverse order
  RETURN QUERY
  SELECT m.version, m.name, 'rolled_back'::VARCHAR
  FROM schema_migrations m
  WHERE m.version > p_target_version
  ORDER BY m.version DESC;
END;
$$ LANGUAGE plpgsql;
```

## Production Deployment

**Safe Migration Checklist:**

- Test migration on production-like database
- Verify backup exists before migration
- Schedule during low-traffic window
- Monitor table locks and long-running queries
- Have rollback plan ready
- Test rollback procedure
- Document all changes
- Run in transaction when possible
- Verify data integrity after migration
- Update application code coordinated with migration

**PostgreSQL - Long Transaction Safety:**

```sql
-- Use statement timeout to prevent hanging migrations
SET statement_timeout = '30min';

-- Use lock timeout to prevent deadlocks
SET lock_timeout = '5min';

-- Run migration with timeouts
ALTER TABLE large_table
ADD COLUMN new_column VARCHAR(255),
ALGORITHM='INPLACE';
```

## Migration Examples

**Combined Migration - Multiple Changes:**

```sql
-- Migration: 20240115_007_refactor_user_tables.sql

BEGIN;

-- 1. Create new column with data from old column
ALTER TABLE users ADD COLUMN full_name VARCHAR(255);
UPDATE users SET full_name = first_name || ' ' || last_name;

-- 2. Add indexes
CREATE INDEX idx_users_full_name ON users(full_name);

-- 3. Add new constraint
ALTER TABLE users
ADD CONSTRAINT email_unique UNIQUE(email);

-- 4. Drop old columns (after verification)
-- ALTER TABLE users DROP COLUMN first_name;
-- ALTER TABLE users DROP COLUMN last_name;

COMMIT;
```

## Resources

- [Flyway - Java Migration Tool](https://flywaydb.org/)
- [Liquibase - Database Changelog](https://www.liquibase.org/)
- [Alembic - Python Migration](https://alembic.sqlalchemy.org/)
- [PostgreSQL ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html)
- [MySQL ALTER TABLE](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html)
