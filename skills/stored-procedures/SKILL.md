---
name: stored-procedures
description: >
  Implement stored procedures and functions for database logic. Use when
  creating reusable database routines, complex queries, or server-side
  calculations.
---

# Stored Procedures & Functions

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement stored procedures, functions, and triggers for business logic, data validation, and performance optimization. Covers procedure design, error handling, and performance considerations.

## When to Use

- Business logic encapsulation
- Complex multi-step operations
- Data validation and constraints
- Audit trail maintenance
- Performance optimization
- Code reusability across applications
- Trigger-based automation

## Quick Start

**PostgreSQL - Scalar Function:**

```sql
-- Create function returning single value
CREATE OR REPLACE FUNCTION calculate_order_total(
  p_subtotal DECIMAL,
  p_tax_rate DECIMAL,
  p_shipping DECIMAL
)
RETURNS DECIMAL AS $$
BEGIN
  RETURN ROUND((p_subtotal * (1 + p_tax_rate) + p_shipping)::NUMERIC, 2);
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- Use in queries
SELECT id, subtotal, calculate_order_total(subtotal, 0.08, 10) as total
FROM orders;

-- Or in application code
SELECT * FROM orders
WHERE calculate_order_total(subtotal, 0.08, 10) > 100;
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Simple Functions](references/simple-functions.md) | Simple Functions |
| [Stored Procedures](references/stored-procedures.md) | Stored Procedures |
| [Simple Procedures](references/simple-procedures.md) | Simple Procedures |
| [Complex Procedures with Error Handling](references/complex-procedures-with-error-handling.md) | Complex Procedures with Error Handling |
| [PostgreSQL Triggers](references/postgresql-triggers.md) | PostgreSQL Triggers |
| [MySQL Triggers](references/mysql-triggers.md) | MySQL Triggers |

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
