# Common Optimization Patterns

## Common Optimization Patterns

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
