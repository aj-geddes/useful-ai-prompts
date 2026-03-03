# MySQL Query Cache

## MySQL Query Cache

**MySQL Query Cache Configuration:**

```sql
-- Check query cache status
SHOW VARIABLES LIKE 'query_cache%';

-- Enable query cache
SET GLOBAL query_cache_type = 1;
SET GLOBAL query_cache_size = 268435456;  -- 256MB

-- Monitor query cache
SHOW STATUS LIKE 'Qcache%';

-- View cached queries
SELECT * FROM performance_schema.table_io_waits_summary_by_table_io_type;

-- Invalidate specific queries
FLUSH QUERY CACHE;
FLUSH TABLES;
```
