# Performance Schema

## Performance Schema

**MySQL - Query Statistics:**

```sql
-- Enable performance schema
-- In my.cnf: performance_schema = ON

-- Slowest queries
SELECT
  object_schema,
  object_name,
  COUNT_STAR,
  SUM_TIMER_WAIT / 1000000000000 as total_time_sec,
  AVG_TIMER_WAIT / 1000000000 as avg_time_ms
FROM performance_schema.table_io_waits_summary_by_table_io_type
ORDER BY SUM_TIMER_WAIT DESC
LIMIT 10;

-- Query response time plugin
SELECT
  TIME,
  COUNT,
  TOTAL,
  ERRORS
FROM mysql.query_response_time
ORDER BY TIME DESC;
```

**MySQL - Connection Monitoring:**

```sql
-- Current connections
SHOW PROCESSLIST;

-- Enhanced processlist
SELECT
  ID,
  USER,
  HOST,
  DB,
  COMMAND,
  TIME,
  STATE,
  INFO
FROM INFORMATION_SCHEMA.PROCESSLIST
WHERE STATE != 'Sleep'
ORDER BY TIME DESC;

-- Kill long-running query
KILL QUERY process_id;
KILL CONNECTION process_id;

-- Max connections usage
SHOW STATUS LIKE 'Threads%';
SHOW STATUS LIKE 'Max_used_connections';
```
