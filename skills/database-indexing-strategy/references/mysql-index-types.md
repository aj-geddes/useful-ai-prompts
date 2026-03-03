# MySQL Index Types

## MySQL Index Types

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
