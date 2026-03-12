---
name: database-monitoring
description: >
  Monitor database performance and health. Use when setting up monitoring,
  analyzing metrics, or troubleshooting database issues.
---

# Database Monitoring

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive database monitoring for performance analysis, health checks, and proactive alerting. Covers metrics collection, analysis, and troubleshooting strategies.

## When to Use

- Performance baseline establishment
- Real-time health monitoring
- Capacity planning
- Query performance analysis
- Resource utilization tracking
- Alerting rule configuration
- Incident response and troubleshooting

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Connection Monitoring](references/connection-monitoring.md) | Connection Monitoring |
| [Query Performance Monitoring](references/query-performance-monitoring.md) | Query Performance Monitoring |
| [Table & Index Monitoring](references/table-index-monitoring.md) | Table & Index Monitoring |
| [Performance Schema](references/performance-schema.md) | Performance Schema |
| [InnoDB Monitoring](references/innodb-monitoring.md) | InnoDB Monitoring |
| [PostgreSQL Monitoring Setup](references/postgresql-monitoring-setup.md) | PostgreSQL Monitoring Setup |
| [Automated Monitoring Dashboard](references/automated-monitoring-dashboard.md) | Automated Monitoring Dashboard |

## Best Practices

### ✅ DO

- Establish performance baselines during normal traffic before setting alert thresholds
- Monitor connection pool utilization and idle-in-transaction sessions continuously
- Track replication lag, WAL growth, and disk I/O alongside query-level metrics
- Set up alerts for table bloat, long-running transactions, and lock wait times
- Use pg_stat_statements or Performance Schema to identify top queries by total time
- Retain historical metrics for capacity planning and trend analysis

### ❌ DON'T

- Set alert thresholds so low they cause alert fatigue — tune for actionable signals only
- Monitor only CPU and memory while ignoring disk IOPS and query plan regressions
- Query system catalogs (pg_stat_activity, information_schema) at high frequency on production without rate-limiting
- Rely solely on application-level latency without correlating to database-level wait events
