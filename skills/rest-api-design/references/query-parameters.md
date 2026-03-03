# Query Parameters

## Query Parameters

```http
# Filtering
GET /api/products?category=electronics&inStock=true

# Sorting
GET /api/users?sort=lastName,asc

# Pagination
GET /api/users?page=2&limit=20

# Field Selection
GET /api/users?fields=id,email,firstName

# Search
GET /api/products?q=laptop

# Multiple filters combined
GET /api/orders?status=pending&customer=123&sort=createdAt,desc&limit=50
```
