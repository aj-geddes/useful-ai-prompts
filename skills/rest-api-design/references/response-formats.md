# Response Formats

## Response Formats

### Success Response

```json
{
  "data": {
    "id": "123",
    "email": "user@example.com",
    "firstName": "John"
  },
  "meta": {
    "timestamp": "2025-01-15T10:30:00Z",
    "version": "1.0"
  }
}
```

### Collection Response with Pagination

```json
{
  "data": [
    { "id": "1", "name": "Product 1" },
    { "id": "2", "name": "Product 2" }
  ],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 145,
    "totalPages": 8,
    "hasNext": true,
    "hasPrev": true
  },
  "links": {
    "self": "/api/products?page=2&limit=20",
    "first": "/api/products?page=1&limit=20",
    "prev": "/api/products?page=1&limit=20",
    "next": "/api/products?page=3&limit=20",
    "last": "/api/products?page=8&limit=20"
  }
}
```

### Error Response

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "message": "Email format is invalid"
      },
      {
        "field": "age",
        "message": "Must be at least 18"
      }
    ]
  },
  "meta": {
    "timestamp": "2025-01-15T10:30:00Z",
    "requestId": "abc-123-def"
  }
}
```
