# List Products

## List Products

Retrieve a paginated list of products.

**Endpoint:** `GET /products`

**Query Parameters:**

| Parameter | Type   | Required | Description                  |
| --------- | ------ | -------- | ---------------------------- |
| page      | number | No       | Page number (default: 1)     |
| limit     | number | No       | Items per page (default: 20) |
| category  | string | No       | Filter by category           |
| search    | string | No       | Search in name/description   |

**Example Request:**

```bash
curl -X GET "https://api.example.com/v2/products?page=1&limit=20&category=electronics" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "Wireless Headphones",
      "description": "Premium noise-cancelling wireless headphones",
      "price": 299.99,
      "sku": "WH-1000XM5",
      "category": "electronics",
      "stock": 150,
      "createdAt": "2025-01-15T10:00:00Z",
      "updatedAt": "2025-01-15T10:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "totalPages": 8
  }
}
```

**Error Responses:**

| Status Code | Description           |
| ----------- | --------------------- |
| 400         | Invalid parameters    |
| 401         | Unauthorized          |
| 500         | Internal server error |

```
