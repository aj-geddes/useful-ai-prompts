# Simple Functions

## Simple Functions

**PostgreSQL - Scalar Function:**

```sql
-- Create function returning single value
CREATE OR REPLACE FUNCTION calculate_order_total(
  p_subtotal DECIMAL,
  p_tax_rate DECIMAL,
  p_shipping DECIMAL
)
RETURNS DECIMAL AS $$
BEGIN
  RETURN ROUND((p_subtotal * (1 + p_tax_rate) + p_shipping)::NUMERIC, 2);
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- Use in queries
SELECT id, subtotal, calculate_order_total(subtotal, 0.08, 10) as total
FROM orders;

-- Or in application code
SELECT * FROM orders
WHERE calculate_order_total(subtotal, 0.08, 10) > 100;
```

**PostgreSQL - Table Returning Function:**

```sql
-- Return set of rows
CREATE OR REPLACE FUNCTION get_user_orders(p_user_id UUID)
RETURNS TABLE (
  order_id UUID,
  order_date TIMESTAMP,
  total DECIMAL,
  status VARCHAR
) AS $$
BEGIN
  RETURN QUERY
  SELECT o.id, o.created_at, o.total, o.status
  FROM orders o
  WHERE o.user_id = p_user_id
  ORDER BY o.created_at DESC;
END;
$$ LANGUAGE plpgsql STABLE;

-- Use function
SELECT * FROM get_user_orders('user-123');
```
