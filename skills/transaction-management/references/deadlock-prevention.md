# Deadlock Prevention

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
      await db.query("BEGIN");
      await db.query(
        "UPDATE accounts SET balance = balance - $1 WHERE id = $2 FOR UPDATE",
        [amount, fromId],
      );
      await db.query(
        "UPDATE accounts SET balance = balance + $1 WHERE id = $2 FOR UPDATE",
        [amount, toId],
      );
      await db.query("COMMIT");
      return { success: true };
    } catch (error) {
      if (error.code === "40P01") {
        // Deadlock detected
        await db.query("ROLLBACK");
        if (i === retries - 1) throw error;
        // Exponential backoff
        await new Promise((r) => setTimeout(r, 100 * Math.pow(2, i)));
      } else {
        throw error;
      }
    }
  }
}
```
