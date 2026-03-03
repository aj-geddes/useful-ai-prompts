# ✨ New Features

## ✨ New Features

### Webhook Support

Subscribe to real-time events:

```http
POST /api/v3/webhooks
Content-Type: application/json

{
  "url": "https://your-app.com/webhook",
  "events": ["user.created", "user.updated", "user.deleted"],
  "secret": "your-webhook-secret"
}
```

**Webhook Payload:**

```json
{
  "event": "user.created",
  "timestamp": "2025-01-15T14:30:00Z",
  "data": {
    "id": "123",
    "type": "user",
    "attributes": {
      "name": "John Doe",
      "email": "john@example.com"
    }
  }
}
```

**Documentation:** [Webhook Guide](docs/webhooks.md)

---

### Batch Operations

Process multiple records in a single request:

```http
POST /api/v3/users/batch
Content-Type: application/json

{
  "operations": [
    {
      "method": "POST",
      "path": "/users",
      "body": { "name": "User 1", "email": "user1@example.com" }
    },
    {
      "method": "PATCH",
      "path": "/users/123",
      "body": { "name": "Updated Name" }
    },
    {
      "method": "DELETE",
      "path": "/users/456"
    }
  ]
}
```

**Response:**

```json
{
  "results": [
    { "status": 201, "data": { "id": "789", ... } },
    { "status": 200, "data": { "id": "123", ... } },
    { "status": 204 }
  ]
}
```

**Limits:** Maximum 100 operations per batch request

---

### Field Filtering

Request only the fields you need:

```http
GET /api/v3/users/123?fields=id,name,email
```

**Before (full response):**

```json
{
  "data": {
    "id": "123",
    "type": "user",
    "attributes": {
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "+1234567890",
      "address": { "street": "123 Main St", "city": "NYC" },
      "preferences": {
        /* ... */
      },
      "metadata": {
        /* ... */
      }
      // ... many more fields
    }
  }
}
```

**After (filtered response):**

```json
{
  "data": {
    "id": "123",
    "type": "user",
    "attributes": {
      "name": "John Doe",
      "email": "john@example.com"
    }
  }
}
```

**Benefits:**

- Reduced response size (up to 80% smaller)
- Faster response times
- Lower bandwidth usage

---
