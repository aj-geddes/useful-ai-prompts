---
name: sql-query-optimization
description: >
  Analyze and optimize SQL queries for performance. Use when improving slow
  queries, reducing execution time, or analyzing query performance in PostgreSQL
  and MySQL.
---

# SQL Query Optimization

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Analyze SQL queries to identify performance bottlenecks and implement optimization techniques. Includes query analysis, indexing strategies, and rewriting patterns for improved performance.

## When to Use

- Slow query analysis and tuning
- Query rewriting and refactoring
- Index utilization verification
- Join optimization
- Subquery optimization
- Query plan analysis (EXPLAIN)
- Performance baseline establishment

## Quick Start

**PostgreSQL:**

```sql
-- Analyze query plan with execution time
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
SELECT u.id, u.email, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > NOW() - INTERVAL '1 year'
GROUP BY u.id, u.email;

-- Check table statistics
SELECT * FROM pg_stats
WHERE tablename = 'users' AND attname = 'created_at';
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Analyze Current Performance](references/analyze-current-performance.md) | Analyze Current Performance |
| [Common Optimization Patterns](references/common-optimization-patterns.md) | Common Optimization Patterns |
| [Query Rewriting Techniques](references/query-rewriting-techniques.md) | Query Rewriting Techniques |
| [Batch Operations](references/batch-operations.md) | Batch Operations |

## Best Practices

### ✅ DO

- Run `EXPLAIN ANALYZE` before and after changes to measure actual improvement, not just estimated cost
- Add indexes on columns used in `WHERE`, `JOIN`, and `ORDER BY` clauses for high-traffic queries
- Use `EXISTS` instead of `IN` for correlated subqueries against large tables
- Prefer batch operations (`INSERT ... SELECT`, bulk updates) over row-by-row processing
- Keep statistics up to date with `ANALYZE` (PostgreSQL) or `ANALYZE TABLE` (MySQL) after large data changes
- Limit result sets with pagination or `LIMIT` to avoid fetching unnecessary rows

### ❌ DON'T

- Use `SELECT *` in production queries — fetch only the columns you need
- Wrap indexed columns in functions (e.g., `WHERE UPPER(name) = ...`) which prevents index usage
- Add indexes blindly — each index slows writes and consumes storage; profile first
- Optimize queries against development data and assume they will perform the same on production volumes
