---
name: database-schema-design
description: >
  Design database schemas with normalization, relationships, and constraints.
  Use when creating new database schemas, designing tables, or planning data
  models for PostgreSQL and MySQL.
---

# Database Schema Design

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Design scalable, normalized database schemas with proper relationships, constraints, and data types. Includes normalization techniques, relationship patterns, and constraint strategies.

## When to Use

- New database schema design
- Data model planning
- Table structure definition
- Relationship design (1:1, 1:N, N:N)
- Normalization analysis
- Constraint and trigger planning
- Performance optimization at schema level

## Quick Start

**PostgreSQL - Eliminate Repeating Groups:**

```sql
-- NOT 1NF: repeating group in single column
CREATE TABLE orders_bad (
  id UUID PRIMARY KEY,
  customer_name VARCHAR(255),
  product_ids VARCHAR(255)  -- "1,2,3" - repeating group
);

-- 1NF: separate table for repeating data
CREATE TABLE orders (
  id UUID PRIMARY KEY,
  customer_name VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE order_items (
  id UUID PRIMARY KEY,
  order_id UUID NOT NULL,
  product_id UUID NOT NULL,
  quantity INTEGER NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
);
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [First Normal Form (1NF)](references/first-normal-form-1nf.md) | First Normal Form (1NF) |
| [Second Normal Form (2NF)](references/second-normal-form-2nf.md) | Second Normal Form (2NF) |
| [Third Normal Form (3NF)](references/third-normal-form-3nf.md) | Third Normal Form (3NF) |
| [Entity-Relationship Patterns](references/entity-relationship-patterns.md) | Entity-Relationship Patterns |

## Best Practices

### ✅ DO

- Normalize to 3NF by default, then selectively denormalize with clear justification for read performance
- Define explicit foreign keys with appropriate ON DELETE/ON UPDATE actions for every relationship
- Use the narrowest appropriate data type (e.g., INTEGER vs BIGINT, VARCHAR(n) vs TEXT where limits are known)
- Add NOT NULL constraints by default and only allow NULL when the business domain requires it
- Include created_at and updated_at timestamps on all mutable tables for auditability
- Use UUID or BIGSERIAL primary keys consistently — avoid natural keys that may change

### ❌ DON'T

- Store comma-separated values or JSON arrays when a proper join table should be used
- Create tables without primary keys or with composite natural keys that complicate joins
- Skip CHECK constraints for domain-specific validation (e.g., positive prices, valid status enums)
- Design schemas without considering the query patterns — schema and index strategy go together
