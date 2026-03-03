# Connection Monitoring

## Connection Monitoring

**PostgreSQL - Active Connections:**

```sql
-- View current connections
SELECT
  pid,
  usename,
  application_name,
  client_addr,
  state,
  query_start,
  state_change
FROM pg_stat_activity
WHERE state != 'idle'
ORDER BY query_start DESC;

-- Count connections per database
SELECT
  datname,
  COUNT(*) as connection_count,
  MAX(EXTRACT(EPOCH FROM (NOW() - query_start))) as max_query_duration_sec
FROM pg_stat_activity
GROUP BY datname;

-- Find idle transactions
SELECT
  pid,
  usename,
  state,
  query_start,
  xact_start,
  EXTRACT(EPOCH FROM (NOW() - xact_start)) as transaction_age_sec
FROM pg_stat_activity
WHERE state = 'idle in transaction'
ORDER BY xact_start;
```

**PostgreSQL - Max Connections Configuration:**

```sql
-- Check current max_connections
SHOW max_connections;

-- Set max_connections (requires restart)
-- In postgresql.conf:
-- max_connections = 200

-- Monitor connection pool usage
SELECT
  sum(numbackends) as total_backends,
  (SELECT setting::int FROM pg_settings WHERE name = 'max_connections') as max_connections,
  ROUND(100.0 * sum(numbackends) /
    (SELECT setting::int FROM pg_settings WHERE name = 'max_connections'), 2) as usage_percent
FROM pg_stat_database;
```
