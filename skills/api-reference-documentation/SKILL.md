---
name: api-reference-documentation
description: Create comprehensive API reference documentation with OpenAPI/Swagger specs, REST endpoints, authentication, examples, and SDKs. Use when documenting REST APIs, GraphQL APIs, endpoint documentation, or OpenAPI specifications.
---

# API Reference Documentation

## Overview

Generate professional API documentation that developers can use to integrate with your API, including endpoint specifications, authentication, request/response examples, and interactive documentation.

## When to Use

- Documenting REST APIs
- Creating OpenAPI/Swagger specifications
- GraphQL API documentation
- SDK and client library docs
- API authentication guides
- Rate limiting documentation
- Webhook documentation
- API versioning guides

## OpenAPI Specification Example

```yaml
openapi: 3.0.3
info:
  title: E-Commerce API
  description: |
    Complete API for managing e-commerce operations including products,
    orders, customers, and payments.

    ## Authentication
    All endpoints require Bearer token authentication. Include your API key
    in the Authorization header: `Authorization: Bearer YOUR_API_KEY`

    ## Rate Limiting
    - 1000 requests per hour for authenticated users
    - 100 requests per hour for unauthenticated requests

    ## Pagination
    List endpoints return paginated results with `page` and `limit` parameters.
  version: 2.0.0
  contact:
    name: API Support
    email: api@example.com
    url: https://example.com/support
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT

servers:
  - url: https://api.example.com/v2
    description: Production server
  - url: https://staging-api.example.com/v2
    description: Staging server
  - url: http://localhost:3000/v2
    description: Local development

tags:
  - name: Products
    description: Product management operations
  - name: Orders
    description: Order processing and tracking
  - name: Customers
    description: Customer management
  - name: Authentication
    description: Authentication endpoints

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: JWT token obtained from /auth/login endpoint

    apiKey:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key for server-to-server authentication

  schemas:
    Product:
      type: object
      required:
        - name
        - price
        - sku
      properties:
        id:
          type: string
          format: uuid
          readOnly: true
          example: "550e8400-e29b-41d4-a716-446655440000"
        name:
          type: string
          minLength: 1
          maxLength: 200
          example: "Wireless Headphones"
        description:
          type: string
          maxLength: 2000
          example: "Premium noise-cancelling wireless headphones"
        price:
          type: number
          format: float
          minimum: 0
          example: 299.99
        sku:
          type: string
          pattern: '^[A-Z0-9-]+$'
          example: "WH-1000XM5"
        category:
          type: string
          enum: [electronics, clothing, books, home, sports]
          example: "electronics"
        stock:
          type: integer
          minimum: 0
          example: 150
        images:
          type: array
          items:
            type: string
            format: uri
          example:
            - "https://cdn.example.com/products/wh-1000xm5-1.jpg"
            - "https://cdn.example.com/products/wh-1000xm5-2.jpg"
        tags:
          type: array
          items:
            type: string
          example: ["wireless", "bluetooth", "noise-cancelling"]
        createdAt:
          type: string
          format: date-time
          readOnly: true
        updatedAt:
          type: string
          format: date-time
          readOnly: true

    Order:
      type: object
      required:
        - customerId
        - items
      properties:
        id:
          type: string
          format: uuid
          readOnly: true
        customerId:
          type: string
          format: uuid
        items:
          type: array
          minItems: 1
          items:
            $ref: '#/components/schemas/OrderItem'
        status:
          type: string
          enum: [pending, processing, shipped, delivered, cancelled]
          default: pending
        totalAmount:
          type: number
          format: float
          readOnly: true
        shippingAddress:
          $ref: '#/components/schemas/Address'
        createdAt:
          type: string
          format: date-time
          readOnly: true

    OrderItem:
      type: object
      required:
        - productId
        - quantity
      properties:
        productId:
          type: string
          format: uuid
        quantity:
          type: integer
          minimum: 1
        price:
          type: number
          format: float
          readOnly: true

    Address:
      type: object
      required:
        - street
        - city
        - country
        - postalCode
      properties:
        street:
          type: string
        city:
          type: string
        state:
          type: string
        country:
          type: string
        postalCode:
          type: string

    Error:
      type: object
      properties:
        code:
          type: string
        message:
          type: string
        details:
          type: object

    PaginatedProducts:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/Product'
        pagination:
          type: object
          properties:
            page:
              type: integer
            limit:
              type: integer
            total:
              type: integer
            totalPages:
              type: integer

  responses:
    Unauthorized:
      description: Authentication required
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            code: "UNAUTHORIZED"
            message: "Authentication token is missing or invalid"

    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            code: "NOT_FOUND"
            message: "The requested resource was not found"

paths:
  /products:
    get:
      summary: List products
      description: Retrieve a paginated list of products with optional filtering
      tags:
        - Products
      security:
        - bearerAuth: []
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
            minimum: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
            minimum: 1
            maximum: 100
        - name: category
          in: query
          schema:
            type: string
        - name: search
          in: query
          schema:
            type: string
        - name: minPrice
          in: query
          schema:
            type: number
        - name: maxPrice
          in: query
          schema:
            type: number
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaginatedProducts'
        '401':
          $ref: '#/components/responses/Unauthorized'

    post:
      summary: Create product
      description: Create a new product
      tags:
        - Products
      security:
        - bearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Product'
            examples:
              headphones:
                summary: Wireless headphones
                value:
                  name: "Wireless Headphones"
                  description: "Premium noise-cancelling"
                  price: 299.99
                  sku: "WH-1000XM5"
                  category: "electronics"
                  stock: 150
      responses:
        '201':
          description: Product created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Product'
        '401':
          $ref: '#/components/responses/Unauthorized'

  /products/{productId}:
    get:
      summary: Get product
      description: Retrieve a specific product by ID
      tags:
        - Products
      security:
        - bearerAuth: []
      parameters:
        - name: productId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Product found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Product'
        '404':
          $ref: '#/components/responses/NotFound'
```

## Markdown Documentation Template

```markdown
# Products API

## Overview

The Products API allows you to manage your product catalog, including creating,
updating, retrieving, and deleting products.

## Base URL

```
https://api.example.com/v2
```

## Authentication

All API requests require authentication using a Bearer token:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.example.com/v2/products
```

## Endpoints

### List Products

Retrieve a paginated list of products.

**Endpoint:** `GET /products`

**Query Parameters:**

| Parameter | Type   | Required | Description                |
|-----------|--------|----------|----------------------------|
| page      | number | No       | Page number (default: 1)   |
| limit     | number | No       | Items per page (default: 20) |
| category  | string | No       | Filter by category         |
| search    | string | No       | Search in name/description |

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

| Status Code | Description          |
|-------------|----------------------|
| 400         | Invalid parameters   |
| 401         | Unauthorized         |
| 500         | Internal server error |
```

## Best Practices

### ✅ DO
- Use OpenAPI 3.0+ specification
- Include request/response examples for every endpoint
- Document all query parameters and headers
- Provide authentication examples
- Include error response formats
- Document rate limits and pagination
- Use consistent naming conventions
- Include SDK examples in multiple languages
- Document webhook payloads
- Provide interactive API explorer (Swagger UI)
- Version your API documentation
- Include migration guides for breaking changes

### ❌ DON'T
- Skip error response documentation
- Forget to document authentication
- Use inconsistent terminology
- Leave endpoints undocumented
- Ignore deprecation notices
- Skip versioning information

## Resources

- [OpenAPI Specification](https://swagger.io/specification/)
- [Swagger Editor](https://editor.swagger.io/)
- [Redoc](https://github.com/Redocly/redoc)
- [Postman Documentation](https://www.postman.com/api-documentation-tool/)
