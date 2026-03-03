# Data Transformations

## Data Transformations

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
