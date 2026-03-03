# Webhook Event Schema

## Webhook Event Schema

```json
{
  "id": "evt_1234567890",
  "timestamp": "2025-01-15T10:30:00Z",
  "event": "order.created",
  "version": "1.0",
  "data": {
    "orderId": "ORD-123456",
    "customerId": "CUST-789",
    "amount": 99.99,
    "currency": "USD",
    "items": [
      {
        "productId": "PROD-001",
        "quantity": 2,
        "price": 49.99
      }
    ],
    "status": "pending"
  },
  "attempt": 1,
  "retryable": true
}
```
