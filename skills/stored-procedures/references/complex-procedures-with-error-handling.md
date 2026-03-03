# Complex Procedures with Error Handling

## Complex Procedures with Error Handling

**MySQL - Transaction Management:**

```sql
DELIMITER //

CREATE PROCEDURE create_order(
  IN p_user_id INT,
  IN p_items JSON,
  OUT p_order_id INT,
  OUT p_success BOOLEAN,
  OUT p_error VARCHAR(500)
)
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    SET p_success = FALSE;
    SET p_error = 'Transaction failed';
  END;

  START TRANSACTION;

  -- Create order
  INSERT INTO orders (user_id, status, created_at)
  VALUES (p_user_id, 'pending', NOW());

  SET p_order_id = LAST_INSERT_ID();

  -- Add items to order (assuming items is JSON array)
  -- Would require JSON parsing in MySQL 5.7+
  -- INSERT INTO order_items (order_id, product_id, quantity)
  -- SELECT p_order_id, JSON_EXTRACT(...), ...

  -- Update inventory
  UPDATE inventory
  SET quantity = quantity - 1
  WHERE product_id IN (
    SELECT product_id FROM order_items WHERE order_id = p_order_id
  );

  -- Check inventory
  IF EXISTS (SELECT 1 FROM inventory WHERE quantity < 0) THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Insufficient inventory';
  END IF;

  COMMIT;
  SET p_success = TRUE;
  SET p_error = NULL;
END //

DELIMITER ;
```
