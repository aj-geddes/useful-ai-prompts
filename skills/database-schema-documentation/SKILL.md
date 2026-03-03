---
name: database-schema-documentation
description: >
  Document database schemas, ERD diagrams, table relationships, indexes, and
  constraints. Use when documenting database schema, creating ERD diagrams, or
  writing table documentation.
---

# Database Schema Documentation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Create comprehensive database schema documentation including entity relationship diagrams (ERD), table definitions, indexes, constraints, and data dictionaries.

## When to Use

- Database schema documentation
- ERD (Entity Relationship Diagrams)
- Data dictionary creation
- Table relationship documentation
- Index and constraint documentation
- Migration documentation
- Database design specs

## Quick Start

Minimal working example:

````markdown
# Database Schema Documentation

**Database:** PostgreSQL 14.x
**Version:** 2.0
**Last Updated:** 2025-01-15
**Schema Version:** 20250115120000

## Overview

This database supports an e-commerce application with user management, product catalog, orders, and payment processing.

## Entity Relationship Diagram

```mermaid
erDiagram
    users ||--o{ orders : places
    users ||--o{ addresses : has
    users ||--o{ payment_methods : has
    orders ||--|{ order_items : contains
    orders ||--|| payments : has
    products ||--o{ order_items : includes
    products }o--|| categories : belongs_to
    products ||--o{ product_images : has
    products ||--o{ inventory : tracks

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [users](references/users.md) | users |
| [products](references/products.md) | products |
| [orders](references/orders.md) | orders |
| [order_items](references/orderitems.md) | order_items |
| [Enum Types](references/enum-types.md) | Enum Types, JSONB Structures |

## Best Practices

### ✅ DO

- Document all tables and columns
- Create ERD diagrams
- Document indexes and constraints
- Include sample data
- Document foreign key relationships
- Show JSONB field structures
- Document triggers and functions
- Include migration scripts
- Specify data types precisely
- Document performance considerations

### ❌ DON'T

- Skip constraint documentation
- Forget to version schema changes
- Ignore performance implications
- Skip index documentation
- Forget to document enum values
