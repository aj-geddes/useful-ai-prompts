---
name: transaction-management
description: >
  Manage database transactions for data consistency. Use when implementing ACID
  compliance, handling concurrency, or managing transaction isolation levels.
---

# Transaction Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement robust transaction management with ACID compliance, concurrency control, and error handling. Covers isolation levels, locking strategies, and deadlock resolution.

## When to Use

- ACID transaction implementation
- Concurrent data modification handling
- Isolation level selection
- Deadlock prevention and resolution
- Transaction timeout configuration
- Distributed transaction coordination
- Financial transaction safety

## Quick Start

**Simple Transaction:**

```sql
-- Start transaction
BEGIN;

-- Multiple statements
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Commit changes
COMMIT;

-- Or rollback
ROLLBACK;
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [PostgreSQL Transactions](references/postgresql-transactions.md) | PostgreSQL Transactions |
| [MySQL Transactions](references/mysql-transactions.md) | MySQL Transactions |
| [PostgreSQL Isolation Levels](references/postgresql-isolation-levels.md) | PostgreSQL Isolation Levels |
| [MySQL Isolation Levels](references/mysql-isolation-levels.md) | MySQL Isolation Levels |
| [PostgreSQL Explicit Locking](references/postgresql-explicit-locking.md) | PostgreSQL Explicit Locking |
| [MySQL Locking](references/mysql-locking.md) | MySQL Locking |
| [Deadlock Prevention](references/deadlock-prevention.md) | **PostgreSQL - Deadlock Detection:** |

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
