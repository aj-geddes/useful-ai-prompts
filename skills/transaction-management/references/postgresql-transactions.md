# PostgreSQL Transactions

## PostgreSQL Transactions

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

**Transaction with Error Handling:**

```sql
BEGIN;

-- Savepoint for partial rollback
SAVEPOINT sp1;

UPDATE accounts SET balance = balance - 50 WHERE id = 1;

-- If error detected
IF (SELECT balance FROM accounts WHERE id = 1) < 0 THEN
  ROLLBACK TO sp1;
  -- Handle negative balance
END IF;

COMMIT;
```
