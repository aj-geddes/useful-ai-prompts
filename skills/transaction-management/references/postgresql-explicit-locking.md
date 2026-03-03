# PostgreSQL Explicit Locking

## PostgreSQL Explicit Locking

**Row-Level Locks:**

```sql
-- FOR UPDATE: exclusive lock for update
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
-- Other transactions cannot UPDATE/DELETE/SELECT FOR UPDATE this row
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- FOR SHARE: shared lock
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR SHARE;
-- Other transactions can SELECT FOR SHARE but not FOR UPDATE
COMMIT;

-- FOR UPDATE NOWAIT: error if locked instead of waiting
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE NOWAIT;
EXCEPTION WHEN OTHERS THEN
  -- Row is locked
END;
COMMIT;
```

**Table-Level Locks:**

```sql
-- Exclusive table lock
LOCK TABLE accounts IN EXCLUSIVE MODE;
-- No other transactions can access table

-- Share lock
LOCK TABLE accounts IN SHARE MODE;
-- Other transactions can read but not write

-- Exclusive for user access
LOCK TABLE accounts IN ACCESS EXCLUSIVE MODE;
```
