# 🚨 Breaking Changes

## 🚨 Breaking Changes

### Authentication Method Changed

**Previous (v2):**

```http
GET /api/users
Authorization: Token abc123
```
````

**Current (v3):**

```http
GET /api/v3/users
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

**Impact:** All API consumers must switch from API tokens to JWT Bearer tokens

**Migration Steps:**

1. Obtain JWT token from `/api/v3/auth/login` endpoint
2. Replace `Authorization: Token` with `Authorization: Bearer`
3. Update token refresh logic (JWT tokens expire after 1 hour)

**Migration Deadline:** June 1, 2025 (v2 auth will be deprecated)

**Migration Guide:** [JWT Authentication Guide](docs/migration/v2-to-v3-auth.md)

---

### Response Format Changed

**Previous (v2):**

```json
{
  "id": "123",
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Current (v3):**

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

**Impact:** All API responses now follow JSON:API specification

**Migration:**

```javascript
// Before (v2)
const user = await response.json();
console.log(user.name);

// After (v3)
const { data } = await response.json();
console.log(data.attributes.name);

// Or use our SDK which handles this automatically
import { ApiClient } from "@company/api-sdk";
const user = await client.users.get("123");
console.log(user.name); // SDK unwraps the response
```

---

### Removed Endpoints

| Removed Endpoint         | Replacement          | Notes                         |
| ------------------------ | -------------------- | ----------------------------- |
| `GET /api/users/list`    | `GET /api/v3/users`  | Use pagination parameters     |
| `POST /api/users/create` | `POST /api/v3/users` | RESTful convention            |
| `GET /api/search`        | `GET /api/v3/search` | Now supports advanced filters |

---
