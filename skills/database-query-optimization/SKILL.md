---
name: database-query-optimization
description: >
  Improve database query performance through indexing, query optimization, and
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

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
