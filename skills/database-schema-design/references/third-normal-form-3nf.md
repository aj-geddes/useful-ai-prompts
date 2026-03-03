# Third Normal Form (3NF)

## Third Normal Form (3NF)

**PostgreSQL - Remove Transitive Dependencies:**

```sql
-- NOT 3NF: transitive dependency (customer_city depends on customer_state)
CREATE TABLE orders_bad (
  id UUID PRIMARY KEY,
  customer_city VARCHAR(100),
  customer_state VARCHAR(50),
  state_tax_rate DECIMAL(5,3)  -- depends on customer_state
);

-- 3NF: separate tables
CREATE TABLE states (
  id UUID PRIMARY KEY,
  code VARCHAR(2) UNIQUE,
  name VARCHAR(100),
  tax_rate DECIMAL(5,3)
);

CREATE TABLE orders (
  id UUID PRIMARY KEY,
  customer_city VARCHAR(100),
  state_id UUID NOT NULL,
  FOREIGN KEY (state_id) REFERENCES states(id)
);
```
