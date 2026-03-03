# Batch Operations

## Batch Operations

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
