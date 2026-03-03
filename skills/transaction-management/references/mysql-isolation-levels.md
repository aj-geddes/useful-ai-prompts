# MySQL Isolation Levels

## MySQL Isolation Levels

**MySQL Isolation Level Configuration:**

```sql
-- Check current isolation level
SHOW VARIABLES LIKE 'transaction_isolation';

-- Set for current session
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- Set for all new connections
SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- Set for specific transaction
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
START TRANSACTION;
-- Statements
COMMIT;
```

**Isolation Level Comparison:**

```sql
-- READ UNCOMMITTED (dirty reads possible)
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

-- READ COMMITTED (repeatable reads, phantom reads possible)
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- REPEATABLE READ (phantom reads possible, MySQL default)
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- SERIALIZABLE (no anomalies)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```
