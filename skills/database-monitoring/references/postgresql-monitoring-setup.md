# PostgreSQL Monitoring Setup

## PostgreSQL Monitoring Setup

**PostgreSQL with Prometheus:**

```yaml
# prometheus.yml configuration
scrape_configs:
  - job_name: "postgres"
    static_configs:
      - targets: ["localhost:9187"]
# Using postgres_exporter
# Download and run:
# ./postgres_exporter --web.listen-address=:9187
```

**Custom Monitoring Query:**

```sql
-- Create monitoring function
CREATE OR REPLACE FUNCTION get_database_metrics()
RETURNS TABLE (
  metric_name VARCHAR,
  metric_value NUMERIC,
  collected_at TIMESTAMP
) AS $$
BEGIN
  -- Return various metrics
  RETURN QUERY
  SELECT 'connections'::VARCHAR,
    (SELECT count(*) FROM pg_stat_activity)::NUMERIC,
    NOW();

  RETURN QUERY
  SELECT 'transactions_per_second',
    (SELECT sum(xact_commit + xact_rollback) / 60 FROM pg_stat_database)::NUMERIC,
    NOW();

  RETURN QUERY
  SELECT 'cache_hit_ratio',
    ROUND(100.0 * (1 - (
      (SELECT sum(heap_blks_read) FROM pg_statio_user_tables)::FLOAT /
      ((SELECT sum(heap_blks_read + heap_blks_hit) FROM pg_statio_user_tables)::FLOAT)
    )), 2)::NUMERIC,
    NOW();
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_database_metrics();
```
