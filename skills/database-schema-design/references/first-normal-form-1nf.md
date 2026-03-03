# First Normal Form (1NF)

## First Normal Form (1NF)

**PostgreSQL - Eliminate Repeating Groups:**

```sql
-- NOT 1NF: repeating group in single column
CREATE TABLE orders_bad (
  id UUID PRIMARY KEY,
  customer_name VARCHAR(255),
  product_ids VARCHAR(255)  -- "1,2,3" - repeating group
);

-- 1NF: separate table for repeating data
CREATE TABLE orders (
  id UUID PRIMARY KEY,
  customer_name VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE order_items (
  id UUID PRIMARY KEY,
  order_id UUID NOT NULL,
  product_id UUID NOT NULL,
  quantity INTEGER NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
);
```
