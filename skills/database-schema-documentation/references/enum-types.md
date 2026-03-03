# Enum Types

## Enum Types

```sql
-- Order status values
CREATE TYPE order_status AS ENUM (
  'pending',
  'confirmed',
  'processing',
  'shipped',
  'delivered',
  'cancelled',
  'refunded'
);

-- Payment status values
CREATE TYPE payment_status AS ENUM (
  'pending',
  'processing',
  'succeeded',
  'failed',
  'refunded'
);
```


## JSONB Structures

### shipping_address format

```json
{
  "street": "123 Main St",
  "street2": "Apt 4B",
  "city": "New York",
  "state": "NY",
  "postalCode": "10001",
  "country": "US"
}
```

### product_snapshot format

```json
{
  "name": "Product Name",
  "sku": "PROD-123",
  "price": 99.99,
  "image": "https://cdn.example.com/product.jpg"
}
```

---
