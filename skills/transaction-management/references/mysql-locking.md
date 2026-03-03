# MySQL Locking

## MySQL Locking

**Row-Level Locking:**

```sql
-- Implicit locking on UPDATE/DELETE
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- Row is locked until transaction ends
COMMIT;

-- SELECT FOR UPDATE: explicit lock
START TRANSACTION;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
-- Exclusive lock acquired
UPDATE accounts SET balance = 100 WHERE id = 1;
COMMIT;

-- SELECT FOR SHARE: read lock
START TRANSACTION;
SELECT * FROM accounts WHERE id = 1 FOR SHARE;
-- Shared lock (blocks FOR UPDATE)
COMMIT;
```

**Gap Locking (InnoDB):**

```sql
-- InnoDB locks gaps between rows
START TRANSACTION;
-- Locks rows and gaps where id between 1 and 100
SELECT * FROM products WHERE id BETWEEN 1 AND 100 FOR UPDATE;
-- Prevents phantom rows in range
COMMIT;
```
