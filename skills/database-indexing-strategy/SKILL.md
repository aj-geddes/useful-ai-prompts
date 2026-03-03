---
name: database-indexing-strategy
description: >
  Design and implement database indexing strategies. Use when creating indexes,
  choosing index types, or optimizing index performance in PostgreSQL and MySQL.
---

# Database Indexing Strategy

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Design comprehensive indexing strategies to improve query performance, reduce lock contention, and maintain data integrity. Covers index types, design patterns, and maintenance procedures.

## When to Use

- Index creation and planning
- Query performance optimization through indexing
- Index type selection (B-tree, Hash, GiST, BRIN)
- Composite and partial index design
- Index maintenance and monitoring
- Storage optimization with indexes
- Full-text search index design

## Quick Start

**B-tree Indexes (Default):**

```sql
-- Standard equality and range queries
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_created_at ON orders(created_at DESC);

-- Composite indexes for multi-column queries
CREATE INDEX idx_orders_user_status
ON orders(user_id, status)
WHERE cancelled_at IS NULL;
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [PostgreSQL Index Types](references/postgresql-index-types.md) | PostgreSQL Index Types |
| [MySQL Index Types](references/mysql-index-types.md) | MySQL Index Types |
| [Single Column Indexes](references/single-column-indexes.md) | Single Column Indexes, Composite Indexes, Partial/Filtered Indexes, Expression Indexes |

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
