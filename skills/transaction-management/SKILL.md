---
name: transaction-management
description: Manage database transactions for data consistency. Use when implementing ACID compliance, handling concurrency, or managing transaction isolation levels.
---

# Transaction Management

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

## Transaction Basics

### PostgreSQL Transactions

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

### MySQL Transactions

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

## Isolation Levels

### PostgreSQL Isolation Levels

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

### MySQL Isolation Levels

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

## Locking Strategies

### PostgreSQL Explicit Locking

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

### MySQL Locking

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

## Concurrency Control

### Optimistic Concurrency

**PostgreSQL with Version Numbers:**

```sql
-- Add version column
ALTER TABLE accounts ADD COLUMN version INT DEFAULT 1;

-- Update with version check
UPDATE accounts
SET balance = balance - 100, version = version + 1
WHERE id = 1 AND version = 5;

-- Application checks affected rows
-- If 0 rows updated, version mismatch (try again)
```

**PostgreSQL with Timestamps:**

```sql
-- Add last modified timestamp
ALTER TABLE accounts ADD COLUMN updated_at TIMESTAMP DEFAULT NOW();

-- Update with timestamp validation
UPDATE accounts
SET balance = balance - 100, updated_at = NOW()
WHERE id = 1 AND updated_at = '2024-01-15 10:00:00';

-- If no rows updated, data was modified by another transaction
```

### Pessimistic Concurrency

**PostgreSQL - Lock and Modify:**

```sql
BEGIN;
-- Lock row before modification
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;

-- Safe to modify (no other transactions can update)
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

## Deadlock Prevention

**PostgreSQL - Deadlock Detection:**

```sql
-- PostgreSQL automatically detects deadlocks
-- Kills one transaction and raises error

-- Example deadlock scenario
-- Transaction 1: Lock A, then try Lock B
-- Transaction 2: Lock B, then try Lock A
-- Result: One transaction rolled back with deadlock error

-- Retry logic
DO $$
DECLARE
  retry_count INT := 0;
BEGIN
  LOOP
    BEGIN
      BEGIN;
      UPDATE accounts SET balance = balance - 100 WHERE id = 1;
      UPDATE accounts SET balance = balance + 100 WHERE id = 2;
      COMMIT;
      EXIT;
    EXCEPTION WHEN deadlocked_table THEN
      ROLLBACK;
      retry_count := retry_count + 1;
      IF retry_count > 3 THEN
        RAISE;
      END IF;
      -- Wait before retry
      PERFORM pg_sleep(0.1);
    END;
  END LOOP;
END $$;
```

**MySQL - Deadlock Prevention:**

```sql
-- Prevent deadlock by consistent lock ordering
-- Always lock in same order: table1 id=1, then table2 id=2

START TRANSACTION;
-- Always lock account 1 first, then account 2
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
SELECT * FROM accounts WHERE id = 2 FOR UPDATE;
-- Safe order prevents deadlock
COMMIT;
```

**Deadlock Recovery Handling:**

```javascript
// Application-level deadlock retry (Node.js)
async function transferMoney(fromId, toId, amount, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      await db.query('BEGIN');
      await db.query(
        'UPDATE accounts SET balance = balance - $1 WHERE id = $2 FOR UPDATE',
        [amount, fromId]
      );
      await db.query(
        'UPDATE accounts SET balance = balance + $1 WHERE id = $2 FOR UPDATE',
        [amount, toId]
      );
      await db.query('COMMIT');
      return { success: true };
    } catch (error) {
      if (error.code === '40P01') { // Deadlock detected
        await db.query('ROLLBACK');
        if (i === retries - 1) throw error;
        // Exponential backoff
        await new Promise(r => setTimeout(r, 100 * Math.pow(2, i)));
      } else {
        throw error;
      }
    }
  }
}
```

## Distributed Transactions

**Two-Phase Commit Pattern:**

```sql
-- Prepare phase: acquire locks, validate
BEGIN;
SAVEPOINT prepare_phase;

-- Prepare writes on both databases
INSERT INTO account_shadow SELECT * FROM accounts WHERE id = 1;

-- Check if both databases are ready
-- If any fails, ROLLBACK TO prepare_phase

-- Commit phase: finalize
RELEASE SAVEPOINT prepare_phase;
COMMIT;
```

**Eventual Consistency Pattern:**

```javascript
// Asynchronous transaction across services
async function transferAcrossServices(fromId, toId, amount) {
  // 1. Debit from first service (transactional)
  await service1.debit(fromId, amount);

  // 2. Queue credit for second service (reliable queue)
  await queue.publish({
    type: 'credit',
    toId,
    amount,
    requestId: uuid()
  });

  // 3. Service 2 processes asynchronously
  queue.subscribe('credit', async (msg) => {
    try {
      await service2.credit(msg.toId, msg.amount);
      await queue.ack(msg.requestId);
    } catch (error) {
      // Retry mechanism
      await queue.retry(msg.requestId);
    }
  });
}
```

## Transaction Monitoring

**PostgreSQL - Active Transactions:**

```sql
-- View active transactions
SELECT
  pid,
  usename,
  application_name,
  state,
  query,
  query_start,
  xact_start
FROM pg_stat_activity
WHERE state != 'idle'
ORDER BY query_start DESC;

-- View transaction locks
SELECT
  l.locktype,
  l.relation::regclass,
  l.mode,
  l.granted,
  a.usename,
  a.query
FROM pg_locks l
JOIN pg_stat_activity a ON l.pid = a.pid
WHERE NOT l.granted;
```

**MySQL - Active Transactions:**

```sql
-- View active transactions
SELECT *
FROM INFORMATION_SCHEMA.INNODB_TRX
ORDER BY trx_started DESC;

-- View locks
SELECT *
FROM INFORMATION_SCHEMA.INNODB_LOCKS;

-- Kill long-running transaction
KILL QUERY process_id;
KILL CONNECTION process_id;
```

## Best Practices

✅ DO use appropriate isolation levels for use case
✅ DO keep transactions short
✅ DO commit frequently
✅ DO handle transaction errors
✅ DO use consistent lock ordering
✅ DO monitor transaction performance
✅ DO document transaction requirements

❌ DON'T hold transactions during user input
❌ DON'T use SERIALIZABLE for high-concurrency systems
❌ DON'T ignore deadlock errors
❌ DON'T lock too many rows
❌ DON'T use READ UNCOMMITTED for critical data

## Resources

- [PostgreSQL Transaction Documentation](https://www.postgresql.org/docs/current/sql-begin.html)
- [MySQL Transaction Documentation](https://dev.mysql.com/doc/refman/8.0/en/commit.html)
- [ACID Properties](https://en.wikipedia.org/wiki/ACID)
- [Isolation Levels Explained](https://www.postgresql.org/docs/current/transaction-iso.html)
