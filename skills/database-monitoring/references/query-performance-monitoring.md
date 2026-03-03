# Query Performance Monitoring

## Query Performance Monitoring

**PostgreSQL - Query Statistics:**

```sql
-- Enable query statistics (pg_stat_statements extension)
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- View slowest queries
SELECT
  query,
  calls,
  mean_exec_time,
  max_exec_time,
  total_exec_time
FROM pg_stat_statements
WHERE query NOT LIKE '%pg_stat%'
ORDER BY mean_exec_time DESC
LIMIT 10;

-- Top queries by total execution time
SELECT
  SUBSTRING(query, 1, 50) as query_snippet,
  calls,
  ROUND(total_exec_time::NUMERIC, 2) as total_time_ms,
  ROUND(mean_exec_time::NUMERIC, 2) as avg_time_ms,
  ROUND(stddev_exec_time::NUMERIC, 2) as stddev_ms
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;

-- Reset statistics
SELECT pg_stat_statements_reset();
```

**PostgreSQL - Long Running Queries:**

```sql
-- Find queries running longer than 1 minute
SELECT
  pid,
  usename,
  application_name,
  state,
  query,
  EXTRACT(EPOCH FROM (NOW() - query_start)) as duration_seconds
FROM pg_stat_activity
WHERE (NOW() - query_start) > INTERVAL '1 minute'
ORDER BY query_start;

-- Cancel long-running query
SELECT pg_cancel_backend(pid);

-- Terminate stuck query
SELECT pg_terminate_backend(pid);
```
