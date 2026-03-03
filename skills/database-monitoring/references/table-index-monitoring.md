# Table & Index Monitoring

## Table & Index Monitoring

**PostgreSQL - Table Statistics:**

```sql
-- Table size analysis
SELECT
  schemaname,
  tablename,
  pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size,
  ROUND(100.0 * pg_total_relation_size(schemaname||'.'||tablename) /
    (SELECT pg_database_size(current_database()))::NUMERIC, 2) as percent_of_db
FROM pg_tables
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Table row counts and dead tuples
SELECT
  schemaname,
  tablename,
  n_live_tup,
  n_dead_tup,
  ROUND(100.0 * n_dead_tup / (n_live_tup + n_dead_tup), 2) as dead_percent
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;

-- Trigger VACUUM when dead tuples exceed threshold
-- Tables with > 20% dead tuples need VACUUM
SELECT
  schemaname,
  tablename,
  ROUND(100.0 * n_dead_tup / (n_live_tup + n_dead_tup), 2) as dead_percent
FROM pg_stat_user_tables
WHERE n_dead_tup > n_live_tup * 0.2;
```

**PostgreSQL - Index Monitoring:**

```sql
-- Unused indexes (never scanned)
SELECT
  schemaname,
  tablename,
  indexname,
  idx_scan,
  pg_size_pretty(pg_relation_size(indexrelid)) as size
FROM pg_stat_user_indexes
WHERE idx_scan = 0
ORDER BY pg_relation_size(indexrelid) DESC;

-- Index fragmentation
SELECT
  schemaname,
  tablename,
  indexname,
  ROUND(100.0 * (pg_relation_size(indexrelid) -
    pg_relation_size(indexrelid, 'main')) /
    pg_relation_size(indexrelid), 2) as fragmentation_percent
FROM pg_stat_user_indexes
WHERE pg_relation_size(indexrelid) > 1000000
ORDER BY fragmentation_percent DESC;

-- Rebuild fragmented indexes
REINDEX INDEX CONCURRENTLY idx_name;
```
