---
name: database-query-optimization
description: >
  Improve database query performance through indexing, query optimization, and.
  Use when slow response times, high database cpu usage, performance regression, or new feature deployment.
  execution plan analysis. Reduce response times and database load.
---

# Database Query Optimization

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Slow database queries are a common performance bottleneck. Optimization through indexing, efficient queries, and caching dramatically improves application performance.

## When to Use

- Slow response times
- High database CPU usage
- Performance regression
- New feature deployment
- Regular maintenance

## Quick Start

Minimal working example:

```sql
-- Analyze query performance

EXPLAIN ANALYZE
SELECT users.id, users.name, COUNT(orders.id) as order_count
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE users.created_at > '2024-01-01'
GROUP BY users.id, users.name
ORDER BY order_count DESC;

-- Results show:
-- - Seq Scan (slow) vs Index Scan (fast)
-- - Rows: actual vs planned (high variance = bad)
-- - Execution time (milliseconds)

-- Key metrics:
-- - Sequential Scan: Full table read (slow)
-- - Index Scan: Uses index (fast)
-- - Nested Loop: Joins with loops
-- - Sort: In-memory or disk sort
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Query Analysis](references/query-analysis.md) | Query Analysis |
| [Indexing Strategy](references/indexing-strategy.md) | Indexing Strategy |
| [Query Optimization Techniques](references/query-optimization-techniques.md) | Query Optimization Techniques |
| [Optimization Checklist](references/optimization-checklist.md) | Optimization Checklist |

## Best Practices

### ✅ DO

- Rewrite SELECT * to select only the columns needed — reduces I/O and enables index-only scans
- Use EXPLAIN ANALYZE to verify index usage and check for unexpected seq scans or sort spills
- Push filtering into WHERE clauses and JOINs rather than filtering in application code
- Batch bulk operations (INSERT, UPDATE) to reduce round-trips and lock duration
- Use CTEs or subqueries strategically — in PostgreSQL 12+, CTEs are inlined unless marked MATERIALIZED
- Add covering indexes for frequently run queries to enable index-only scans

### ❌ DON'T

- Use OR across different columns in WHERE clauses without rewriting as UNION ALL
- Wrap indexed columns in functions (e.g., WHERE LOWER(email) = ...) without a matching expression index
- Use OFFSET for deep pagination — use keyset (cursor-based) pagination instead
- Rely on query plan caching without periodically re-checking plans after significant data changes
