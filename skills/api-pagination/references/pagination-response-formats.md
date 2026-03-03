# Pagination Response Formats

## Pagination Response Formats

```json
// Offset/Limit Response
{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 145,
    "totalPages": 8,
    "hasNext": true,
    "hasPrev": true
  },
  "links": {
    "self": "/api/users?page=2&limit=20",
    "first": "/api/users?page=1&limit=20",
    "prev": "/api/users?page=1&limit=20",
    "next": "/api/users?page=3&limit=20",
    "last": "/api/users?page=8&limit=20"
  }
}

// Cursor-Based Response
{
  "data": [...],
  "pageInfo": {
    "hasNextPage": true,
    "endCursor": "Y3JlYXRlZEF0OjE2NzA4ODA2MzU3NQ==",
    "totalCount": 1250
  },
  "links": {
    "next": "/api/users?limit=20&after=Y3JlYXRlZEF0OjE2NzA4ODA2MzU3NQ=="
  }
}

// Keyset Response
{
  "data": [...],
  "pageInfo": {
    "hasMore": true,
    "lastId": "507f1f77bcf86cd799439011"
  },
  "links": {
    "next": "/api/products?lastId=507f1f77bcf86cd799439011&sort=price"
  }
}
```
