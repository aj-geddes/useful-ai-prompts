# Renaming Columns

## Renaming Columns

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
