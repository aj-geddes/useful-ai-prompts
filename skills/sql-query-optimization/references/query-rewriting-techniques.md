# Query Rewriting Techniques

## Query Rewriting Techniques

**PostgreSQL - Window Functions:**

```sql
-- Inefficient: multiple passes
SELECT p.id, p.name,
  (SELECT COUNT(*) FROM orders o WHERE o.product_id = p.id) as order_count,
  (SELECT SUM(quantity) FROM order_items oi WHERE oi.product_id = p.id) as total_sold
FROM products p;

-- Optimized: single pass with window functions
SELECT DISTINCT p.id, p.name,
  COUNT(*) OVER (PARTITION BY p.id) as order_count,
  SUM(oi.quantity) OVER (PARTITION BY p.id) as total_sold
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id;
```

**MySQL - JOIN Optimization:**

```sql
-- Inefficient: JOIN after aggregation
SELECT user_id, name, total_orders
FROM (
  SELECT u.id as user_id, u.name, COUNT(o.id) as total_orders
  FROM users u
  LEFT JOIN orders o ON u.id = o.user_id
  GROUP BY u.id, u.name
) subquery
WHERE total_orders > 5;

-- Optimized: aggregate with HAVING clause
SELECT u.id, u.name, COUNT(o.id) as total_orders
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
HAVING COUNT(o.id) > 5;
```
