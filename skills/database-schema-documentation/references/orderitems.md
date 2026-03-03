# order_items

## order_items

Line items for each order.

**Columns:**

| Column           | Type          | Null | Default           | Description                |
| ---------------- | ------------- | ---- | ----------------- | -------------------------- |
| id               | uuid          | NO   | gen_random_uuid() | Primary key                |
| order_id         | uuid          | NO   | -                 | Foreign key to orders      |
| product_id       | uuid          | NO   | -                 | Foreign key to products    |
| product_snapshot | jsonb         | NO   | -                 | Product data at order time |
| quantity         | int           | NO   | -                 | Quantity ordered           |
| unit_price       | decimal(10,2) | NO   | -                 | Price per unit             |
| subtotal         | decimal(10,2) | NO   | -                 | Line item total            |
| created_at       | timestamp     | NO   | now()             | Record creation time       |

**Indexes:**

```sql
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);
```

**Foreign Keys:**

```sql
ALTER TABLE order_items
  ADD CONSTRAINT fk_order_items_order
  FOREIGN KEY (order_id)
  REFERENCES orders(id)
  ON DELETE CASCADE;

ALTER TABLE order_items
  ADD CONSTRAINT fk_order_items_product
  FOREIGN KEY (product_id)
  REFERENCES products(id)
  ON DELETE RESTRICT;
```

**Constraints:**

```sql
ALTER TABLE order_items
  ADD CONSTRAINT order_items_quantity_positive
  CHECK (quantity > 0);

ALTER TABLE order_items
  ADD CONSTRAINT order_items_subtotal_computation
  CHECK (subtotal = quantity * unit_price);
```

---
