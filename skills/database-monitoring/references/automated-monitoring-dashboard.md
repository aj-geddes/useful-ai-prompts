# Automated Monitoring Dashboard

## Automated Monitoring Dashboard

```sql
-- Create monitoring table
CREATE TABLE database_metrics_history (
  collected_at TIMESTAMP,
  metric_name VARCHAR(100),
  metric_value NUMERIC,
  PRIMARY KEY (collected_at, metric_name)
);

-- Function to collect metrics
CREATE OR REPLACE FUNCTION collect_metrics()
RETURNS void AS $$
BEGIN
  INSERT INTO database_metrics_history (collected_at, metric_name, metric_value)
  SELECT
    NOW(),
    'active_connections',
    (SELECT count(*) FROM pg_stat_activity WHERE state != 'idle')::NUMERIC
  UNION ALL
  SELECT
    NOW(),
    'cache_hit_ratio',
    ROUND(100.0 * sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)), 2)
  FROM pg_statio_user_tables
  UNION ALL
  SELECT
    NOW(),
    'database_size_mb',
    pg_database_size(current_database())::NUMERIC / 1024 / 1024
  UNION ALL
  SELECT
    NOW(),
    'table_bloat_percent',
    ROUND(100.0 * sum(n_dead_tup) / sum(n_live_tup + n_dead_tup), 2)
  FROM pg_stat_user_tables;
END;
$$ LANGUAGE plpgsql;

-- Schedule via cron
-- SELECT cron.schedule('collect_metrics', '* * * * *', 'SELECT collect_metrics()');
```
