# Resource Naming

## Resource Naming

```
✅ Good Resource Names (Nouns, Plural)
GET    /api/users
GET    /api/users/123
GET    /api/users/123/orders
POST   /api/products
DELETE /api/products/456

❌ Bad Resource Names (Verbs, Inconsistent)
GET    /api/getUsers
POST   /api/createProduct
GET    /api/user/123  (inconsistent singular/plural)
```


## HTTP Methods & Operations

```http
# CRUD Operations
GET    /api/users          # List all users (Read collection)
GET    /api/users/123      # Get specific user (Read single)
POST   /api/users          # Create new user (Create)
PUT    /api/users/123      # Replace user completely (Update)
PATCH  /api/users/123      # Partial update user (Partial update)
DELETE /api/users/123      # Delete user (Delete)

# Nested Resources
GET    /api/users/123/orders       # Get user's orders
POST   /api/users/123/orders       # Create order for user
GET    /api/users/123/orders/456   # Get specific order
```
