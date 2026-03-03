# PostgreSQL Isolation Levels

## PostgreSQL Isolation Levels

**Read Uncommitted (not fully implemented):**

```sql
-- PostgreSQL treats as READ COMMITTED
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

BEGIN;
-- Can read uncommitted changes from other transactions
SELECT COUNT(*) FROM orders WHERE user_id = 123;
COMMIT;
```

**Read Committed (Default):**

```sql
-- Default PostgreSQL isolation level
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

BEGIN;
-- Read committed data only
-- Allows phantom reads and non-repeatable reads
SELECT * FROM accounts WHERE id = 1;

-- May see different data if other transactions modify rows
SELECT * FROM accounts WHERE id = 1;
COMMIT;
```

**Repeatable Read:**

```sql
-- Higher isolation level
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

BEGIN;
-- Snapshot of data at transaction start
SELECT COUNT(*) as count_1 FROM orders;

-- Other transaction inserts order
-- Will still see same count
SELECT COUNT(*) as count_2 FROM orders;
COMMIT;
```

**Serializable:**

```sql
-- Highest isolation level
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

BEGIN;
-- Transactions execute as if serially
-- Prevents all anomalies (serialization failures may occur)
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;  -- May fail with serialization_failure error
```
