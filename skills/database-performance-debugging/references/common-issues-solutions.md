# Common Issues & Solutions

## Common Issues & Solutions

```yaml
Issue: N+1 Query Problem

Symptom: 1001 queries for 1000 records

Example (Python):
  for user in users:
    posts = db.query(Post).filter(Post.user_id == user.id)
    # 1 + 1000 queries

Solution:
  users = db.query(User).options(joinedload(User.posts))
  # Single query with JOIN

---

Issue: Missing Index

Symptom: Seq Scan instead of Index Scan

Solution:
  CREATE INDEX idx_orders_user_id ON orders(user_id);
  Verify: EXPLAIN ANALYZE shows Index Scan now

---

Issue: Inefficient JOIN

Before:
  SELECT * FROM orders o, users u
  WHERE o.user_id = u.id AND u.email LIKE '%@example.com'
  # Bad: Table scan on users for every order

After:
  SELECT o.* FROM orders o
  JOIN users u ON o.user_id = u.id
  WHERE u.email = 'exact@example.com'
  # Good: Single email lookup

---

Issue: Large Table Scan

Symptom: SELECT * FROM large_table (1M rows)

Solutions:
  1. Add LIMIT clause
  2. Add WHERE condition
  3. Select specific columns
  4. Use pagination
  5. Archive old data

---

Issue: Slow Aggregation

Before (1 minute):
  SELECT user_id, COUNT(*), SUM(amount)
  FROM transactions
  GROUP BY user_id

After (50ms):
  SELECT user_id, transaction_count, total_amount
  FROM user_transaction_stats
  WHERE updated_at > NOW() - INTERVAL 1 DAY
  # Materialized view or aggregation table
```
