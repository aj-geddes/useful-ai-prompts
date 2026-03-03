# Single Column Indexes

## Single Column Indexes

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


## Composite Indexes

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


## Partial/Filtered Indexes

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


## Expression Indexes

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
