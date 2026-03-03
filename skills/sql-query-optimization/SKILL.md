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

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
