# MySQL Triggers

## MySQL Triggers

**MySQL - Insert Trigger:**

```sql
DELIMITER //

CREATE TRIGGER create_order_trigger
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  -- Update user statistics
  UPDATE user_stats
  SET total_orders = total_orders + 1,
      total_spent = total_spent + NEW.total
  WHERE user_id = NEW.user_id;

  -- Create audit log
  INSERT INTO audit_log (table_name, operation, record_id, timestamp)
  VALUES ('orders', 'INSERT', NEW.id, NOW());
END //

DELIMITER ;
```

**MySQL - Update Prevention Trigger:**

```sql
DELIMITER //

CREATE TRIGGER prevent_old_order_update
BEFORE UPDATE ON orders
FOR EACH ROW
BEGIN
  IF OLD.status = 'completed' THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Cannot update completed orders';
  END IF;
END //

DELIMITER ;
```
