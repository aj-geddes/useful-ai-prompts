# Indexing Strategy

## Indexing Strategy

```yaml
Index Types:

Single Column:
  CREATE INDEX idx_users_email ON users(email);
  Use: WHERE email = ?
  Size: Small, quick to create

Composite Index:
  CREATE INDEX idx_orders_user_date
    ON orders(user_id, created_at);
  Use: WHERE user_id = ? AND created_at > ?
  Order: Most selective first

Covering Index:
  CREATE INDEX idx_orders_covering
    ON orders(user_id) INCLUDE (total_amount);
  Benefit: No table lookup needed

Partial Index:
  CREATE INDEX idx_active_users
    ON users(id) WHERE status = 'active';
  Benefit: Smaller, faster

Full Text:
  CREATE FULLTEXT INDEX idx_search
    ON articles(title, content);
  Use: Text search queries

---

Index Rules:

- Create indexes for WHERE conditions
- Create indexes for JOIN columns
- Create indexes for ORDER BY
- Don't over-index (slows writes)
- Monitor index usage
- Remove unused indexes
- Update statistics regularly
- Partial indexes for filtered queries

Missing Index Query:
SELECT object_name, equality_columns
FROM sys.dm_db_missing_index_details
ORDER BY equality_columns;
```
