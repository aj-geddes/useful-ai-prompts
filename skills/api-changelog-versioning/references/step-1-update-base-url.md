# Step 1: Update Base URL

## Step 1: Update Base URL

```javascript
// Before
const API_BASE = "https://api.example.com/api";

// After
const API_BASE = "https://api.example.com/api/v3";
```


## Step 2: Migrate Authentication

```javascript
// Before (v2) - API Token
const response = await fetch(`${API_BASE}/users`, {
  headers: {
    Authorization: `Token ${apiToken}`,
  },
});

// After (v3) - JWT Bearer
const tokenResponse = await fetch(`${API_BASE}/auth/login`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ email, password }),
});
const { token } = await tokenResponse.json();

const response = await fetch(`${API_BASE}/users`, {
  headers: {
    Authorization: `Bearer ${token}`,
  },
});
```


## Step 3: Update Response Parsing

```javascript
// Before (v2)
const user = await response.json();
console.log(user.name);

// After (v3) - Unwrap data object
const { data } = await response.json();
console.log(data.attributes.name);

// Or use SDK
import { ApiClient } from "@company/api-sdk";
const client = new ApiClient(token);
const user = await client.users.get("123");
console.log(user.name); // SDK handles unwrapping
```


## Step 4: Update Error Handling

```javascript
// Before (v2)
try {
  const response = await fetch(`${API_BASE}/users`);
  if (!response.ok) {
    const error = await response.json();
    console.error(error.error);
  }
} catch (error) {
  console.error(error);
}

// After (v3) - Handle multiple errors
try {
  const response = await fetch(`${API_BASE}/users`);
  if (!response.ok) {
    const { errors } = await response.json();
    errors.forEach((err) => {
      console.error(`${err.field}: ${err.message}`);
      console.log(`Suggestion: ${err.suggestion}`);
    });
  }
} catch (error) {
  console.error(error);
}
```


## Step 5: Update Pagination

```javascript
// Before (v2)
const response = await fetch(`${API_BASE}/users?page=1&per_page=20`);

// After (v3)
const response = await fetch(`${API_BASE}/users?page[number]=1&page[size]=20`);

// Response structure
{
  "data": [...],
  "meta": {
    "page": {
      "current": 1,
      "size": 20,
      "total": 150,
      "totalPages": 8
    }
  },
  "links": {
    "first": "/api/v3/users?page[number]=1",
    "last": "/api/v3/users?page[number]=8",
    "next": "/api/v3/users?page[number]=2",
    "prev": null
  }
}
```


## Step 6: Testing

```javascript
// Run tests against v3 API
npm run test:api -- --api-version=v3

// Test migration gradually
const USE_V3 = process.env.USE_API_V3 === 'true';
const API_BASE = USE_V3
  ? 'https://api.example.com/api/v3'
  : 'https://api.example.com/api/v2';
```

---
