# Query Optimization Techniques

## Query Optimization Techniques

```python
# Common optimization patterns

# BEFORE (N+1 queries)
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)
    # 1 + N queries

# AFTER (single query with JOIN)
orders = db.query("""
  SELECT u.*, o.* FROM users u
  LEFT JOIN orders o ON u.id = o.user_id
  WHERE u.created_at > ?
""", date_threshold)

# BEFORE (inefficient WHERE)
SELECT * FROM users
WHERE LOWER(email) = LOWER('Test@Example.com')
# Can't use index (function used)

# AFTER (index-friendly)
SELECT * FROM users
WHERE email = 'test@example.com'
# Case-insensitive constraint + index

# BEFORE (wildcard at start)
SELECT * FROM users WHERE email LIKE '%example.com'
# Can't use index (wildcard at start)

# AFTER (wildcard at end)
SELECT * FROM users WHERE email LIKE 'user%'
# Can use index

# BEFORE (slow aggregation)
SELECT user_id, COUNT(*) as cnt
FROM orders
GROUP BY user_id
ORDER BY cnt DESC
LIMIT 10

# AFTER (pre-aggregated)
SELECT user_id, order_count
FROM user_order_stats
WHERE order_count IS NOT NULL
ORDER BY order_count DESC
LIMIT 10
```
