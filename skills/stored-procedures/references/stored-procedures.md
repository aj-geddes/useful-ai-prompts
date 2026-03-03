# Stored Procedures

## Stored Procedures

**PostgreSQL - Procedure with OUT Parameters:**

```sql
-- Stored procedure with output parameters
CREATE OR REPLACE PROCEDURE process_order(
  p_order_id UUID,
  OUT p_success BOOLEAN,
  OUT p_message VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
  BEGIN
    -- Start transaction
    UPDATE orders SET status = 'processing' WHERE id = p_order_id;

    UPDATE inventory
    SET quantity = quantity - 1
    WHERE product_id IN (
      SELECT product_id FROM order_items WHERE order_id = p_order_id
    );

    -- Check inventory
    IF EXISTS (SELECT 1 FROM inventory WHERE quantity < 0) THEN
      RAISE EXCEPTION 'Insufficient inventory';
    END IF;

    p_success := true;
    p_message := 'Order processed successfully';
  EXCEPTION WHEN OTHERS THEN
    p_success := false;
    p_message := SQLERRM;
    -- Transaction automatically rolled back
  END;
END;
$$;

-- Call procedure
CALL process_order('order-123', success, message);
SELECT success, message;
```

**Complex Procedure with Logic:**

```sql
CREATE OR REPLACE PROCEDURE transfer_funds(
  p_from_account_id INT,
  p_to_account_id INT,
  p_amount DECIMAL,
  OUT p_success BOOLEAN,
  OUT p_error_message VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
  v_from_balance DECIMAL;
BEGIN
  BEGIN
    -- Check balance
    SELECT balance INTO v_from_balance
    FROM accounts
    WHERE id = p_from_account_id
    FOR UPDATE;

    IF v_from_balance < p_amount THEN
      RAISE EXCEPTION 'Insufficient funds';
    END IF;

    -- Debit from account
    UPDATE accounts
    SET balance = balance - p_amount
    WHERE id = p_from_account_id;

    -- Credit to account
    UPDATE accounts
    SET balance = balance + p_amount
    WHERE id = p_to_account_id;

    -- Log transaction
    INSERT INTO transaction_log (from_id, to_id, amount, status)
    VALUES (p_from_account_id, p_to_account_id, p_amount, 'completed');

    p_success := true;
    p_error_message := NULL;
  EXCEPTION WHEN OTHERS THEN
    p_success := false;
    p_error_message := SQLERRM;
  END;
END;
$$;
```
