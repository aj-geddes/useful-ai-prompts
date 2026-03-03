# Simple Procedures

## Simple Procedures

**MySQL - Basic Procedure:**

```sql
-- Simple procedure
DELIMITER //

CREATE PROCEDURE get_user_by_email(IN p_email VARCHAR(255))
BEGIN
  SELECT id, email, name, created_at
  FROM users
  WHERE email = p_email;
END //

DELIMITER ;

-- Call procedure
CALL get_user_by_email('john@example.com');
```

**MySQL - Procedure with OUT Parameters:**

```sql
DELIMITER //

CREATE PROCEDURE calculate_user_stats(
  IN p_user_id INT,
  OUT p_total_orders INT,
  OUT p_total_spent DECIMAL
)
BEGIN
  SELECT
    COUNT(*),
    SUM(total)
  INTO p_total_orders, p_total_spent
  FROM orders
  WHERE user_id = p_user_id AND status != 'cancelled';

  IF p_total_orders IS NULL THEN
    SET p_total_orders = 0;
    SET p_total_spent = 0;
  END IF;
END //

DELIMITER ;

-- Call procedure
CALL calculate_user_stats(123, @orders, @spent);
SELECT @orders as total_orders, @spent as total_spent;
```
