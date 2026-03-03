# orders

## orders

Stores customer orders.

**Columns:**

| Column           | Type          | Null | Default           | Description                      |
| ---------------- | ------------- | ---- | ----------------- | -------------------------------- |
| id               | uuid          | NO   | gen_random_uuid() | Primary key                      |
| order_number     | varchar(20)   | NO   | -                 | Human-readable order ID (unique) |
| user_id          | uuid          | NO   | -                 | Foreign key to users             |
| status           | varchar(20)   | NO   | 'pending'         | Order status                     |
| subtotal         | decimal(10,2) | NO   | -                 | Items subtotal                   |
| tax              | decimal(10,2) | NO   | 0                 | Tax amount                       |
| shipping         | decimal(10,2) | NO   | 0                 | Shipping cost                    |
| total            | decimal(10,2) | NO   | -                 | Total amount                     |
| currency         | char(3)       | NO   | 'USD'             | Currency code                    |
| notes            | text          | YES  | -                 | Order notes                      |
| shipping_address | jsonb         | NO   | -                 | Shipping address                 |
| billing_address  | jsonb         | NO   | -                 | Billing address                  |
| created_at       | timestamp     | NO   | now()             | Order creation time              |
| updated_at       | timestamp     | NO   | now()             | Last update time                 |
| confirmed_at     | timestamp     | YES  | -                 | Order confirmation time          |
| shipped_at       | timestamp     | YES  | -                 | Shipping time                    |
| delivered_at     | timestamp     | YES  | -                 | Delivery time                    |
| cancelled_at     | timestamp     | YES  | -                 | Cancellation time                |

**Indexes:**

```sql
CREATE UNIQUE INDEX idx_orders_order_number ON orders(order_number);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_created_at ON orders(created_at);
```

**Constraints:**

```sql
ALTER TABLE orders
  ADD CONSTRAINT orders_status_check
  CHECK (status IN ('pending', 'confirmed', 'processing', 'shipped', 'delivered', 'cancelled', 'refunded'));

ALTER TABLE orders
  ADD CONSTRAINT orders_total_positive
  CHECK (total >= 0);
```

**Computed Columns:**

```sql
-- Total is computed from subtotal + tax + shipping
ALTER TABLE orders
  ADD CONSTRAINT orders_total_computation
  CHECK (total = subtotal + tax + shipping);
```

---
