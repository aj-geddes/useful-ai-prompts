# Adding Columns

## Adding Columns

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
