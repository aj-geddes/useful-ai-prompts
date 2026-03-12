---
name: database-performance-debugging
description: >
  Debug database performance issues through query analysis, index optimization,.
  Use when slow application response times, high database cpu, slow queries identified, or performance regression.
  and execution plan review. Identify and fix slow queries.
---

# Database Performance Debugging

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Database performance issues directly impact application responsiveness. Debugging focuses on identifying slow queries and optimizing execution plans.

## When to Use

- Slow application response times
- High database CPU
- Slow queries identified
- Performance regression
- Under load stress

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Identify Slow Queries](references/identify-slow-queries.md) | Identify Slow Queries |
| [Common Issues & Solutions](references/common-issues-solutions.md) | Common Issues & Solutions |
| [Execution Plan Analysis](references/execution-plan-analysis.md) | Execution Plan Analysis |
| [Debugging Process](references/debugging-process.md) | Debugging Process |

## Best Practices

### ✅ DO

- Start with EXPLAIN (ANALYZE, BUFFERS) to compare estimated vs actual rows and identify seq scans
- Check pg_stat_statements or slow query log for top offenders by total execution time, not just single-call latency
- Correlate query regressions with recent schema changes, data growth, or autovacuum activity
- Profile under realistic load — single-query EXPLAIN misses contention and lock-wait issues
- Look at actual buffer hits vs disk reads to distinguish CPU-bound from I/O-bound queries

### ❌ DON'T

- Optimize queries in isolation without considering how they behave under concurrent load
- Add indexes as a reflex without confirming the planner will use them (check with EXPLAIN)
- Ignore table bloat and dead tuples — they cause full-table scans even with valid indexes
- Tune database parameters (work_mem, shared_buffers) without measuring the effect with benchmarks
