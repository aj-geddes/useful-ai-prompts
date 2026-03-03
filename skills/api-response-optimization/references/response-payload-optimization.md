# Response Payload Optimization

## Response Payload Optimization

```javascript
// Inefficient response (unnecessary data)
GET /api/users/123
{
  "id": 123,
  "name": "John",
  "email": "john@example.com",
  "password_hash": "...", // ❌ Should never send
  "ssn": "123-45-6789", // ❌ Sensitive data
  "internal_id": "xyz",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-02T00:00:00Z",
  "meta_data": {...}, // ❌ Unused fields
  "address": {
    "street": "123 Main",
    "city": "City",
    "state": "ST",
    "zip": "12345",
    "geo": {...} // ❌ Not needed
  }
}

// Optimized response (only needed fields)
GET /api/users/123
{
  "id": 123,
  "name": "John",
  "email": "john@example.com"
}

// Results: 2KB → 100 bytes (20x smaller)

// Sparse fieldsets pattern
GET /api/users/123?fields=name,email
{
  "id": 123,
  "name": "John",
  "email": "john@example.com"
}
```
