# MySQL Transactions

## MySQL Transactions

**MySQL Transaction:**

```sql
-- Start transaction
START TRANSACTION;

-- Or
BEGIN;

-- Statements
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Commit
COMMIT;

-- Or rollback
ROLLBACK;
```

**MySQL Savepoints:**

```sql
START TRANSACTION;

INSERT INTO orders (user_id, total) VALUES (123, 99.99);
SAVEPOINT after_insert;

UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 456;

-- If inventory check fails
IF (SELECT quantity FROM inventory WHERE product_id = 456) < 0 THEN
  ROLLBACK TO after_insert;
END IF;

COMMIT;
```
