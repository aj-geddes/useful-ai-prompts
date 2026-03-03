# Identify Slow Queries

## Identify Slow Queries

```sql
-- Enable slow query log (MySQL)
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 0.5;

-- View slow queries
SHOW GLOBAL STATUS LIKE 'Slow_queries';
SELECT * FROM mysql.slow_log;

-- PostgreSQL slow queries
CREATE EXTENSION pg_stat_statements;
SELECT mean_exec_time, calls, query
FROM pg_stat_statements
ORDER BY mean_exec_time DESC LIMIT 10;

-- SQL Server slow queries
SELECT TOP 10
  execution_count,
  total_elapsed_time,
  statement_text
FROM sys.dm_exec_query_stats
ORDER BY total_elapsed_time DESC;

-- Query profiling
EXPLAIN ANALYZE
SELECT * FROM orders WHERE user_id = 123;
-- Slow: Seq Scan (full table scan)
-- Fast: Index Scan
```
