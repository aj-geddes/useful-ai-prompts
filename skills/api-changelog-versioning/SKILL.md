---
name: api-changelog-versioning
description: Document API changes, breaking changes, migration guides, and version history for APIs. Use when documenting API versioning, breaking changes, or creating API migration guides.
---

# API Changelog & Versioning

## Overview

Create comprehensive API changelogs that document changes, deprecations, breaking changes, and provide migration guides for API consumers.

## When to Use

- API version changelogs
- Breaking changes documentation
- Migration guides between versions
- Deprecation notices
- API upgrade guides
- Backward compatibility notes
- Version comparison

## API Changelog Template

```markdown
# API Changelog

## Version 3.0.0 - 2025-01-15

### 🚨 Breaking Changes

#### Authentication Method Changed

**Previous (v2):**
```http
GET /api/users
Authorization: Token abc123
```

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

#### Response Format Changed

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
import { ApiClient } from '@company/api-sdk';
const user = await client.users.get('123');
console.log(user.name); // SDK unwraps the response
```

---

#### Removed Endpoints

| Removed Endpoint | Replacement | Notes |
|------------------|-------------|-------|
| `GET /api/users/list` | `GET /api/v3/users` | Use pagination parameters |
| `POST /api/users/create` | `POST /api/v3/users` | RESTful convention |
| `GET /api/search` | `GET /api/v3/search` | Now supports advanced filters |

---

### ✨ New Features

#### Webhook Support

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

#### Batch Operations

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

#### Field Filtering

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
      "preferences": { /* ... */ },
      "metadata": { /* ... */ }
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

### 🔧 Improvements

#### Performance Enhancements

- **50% faster response times** for list endpoints
- **Database query optimization** reducing average query time from 150ms to 50ms
- **Caching layer** added for frequently accessed resources
- **CDN integration** for static assets

**Benchmark Comparison:**

| Endpoint | v2 (avg) | v3 (avg) | Improvement |
|----------|----------|----------|-------------|
| GET /users | 320ms | 140ms | 56% faster |
| GET /users/{id} | 180ms | 60ms | 67% faster |
| POST /users | 250ms | 120ms | 52% faster |

---

#### Better Error Messages

**Before (v2):**
```json
{
  "error": "Validation failed"
}
```

**After (v3):**
```json
{
  "errors": [
    {
      "code": "VALIDATION_ERROR",
      "field": "email",
      "message": "Email format is invalid",
      "suggestion": "Use format: user@example.com"
    },
    {
      "code": "VALIDATION_ERROR",
      "field": "password",
      "message": "Password too weak",
      "suggestion": "Password must be at least 8 characters with uppercase, lowercase, and numbers"
    }
  ]
}
```

---

#### Enhanced Rate Limiting

New rate limit headers in every response:

```http
HTTP/1.1 200 OK
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 950
X-RateLimit-Reset: 1642694400
X-RateLimit-Window: 3600
Retry-After: 3600
```

**Rate Limits by Plan:**

| Plan | Requests/Hour | Burst | Reset |
|------|---------------|-------|-------|
| Free | 100 | 10/min | 1 hour |
| Pro | 1,000 | 50/min | 1 hour |
| Enterprise | 10,000 | 200/min | 1 hour |

---

### 🔒 Security

- **TLS 1.3 Required:** Dropped support for TLS 1.2
- **JWT Expiry:** Tokens now expire after 1 hour (was 24 hours)
- **Rate Limiting:** Stricter limits on authentication endpoints
- **CORS:** Updated allowed origins (see security policy)
- **Input Validation:** Enhanced validation on all endpoints

---

### 🗑️ Deprecated

#### Deprecation Schedule

| Feature | Deprecated | Removal Date | Replacement |
|---------|------------|--------------|-------------|
| API Token Auth | v3.0.0 | 2025-06-01 | JWT Bearer tokens |
| XML Response Format | v3.0.0 | 2025-04-01 | JSON only |
| `/api/v1/*` endpoints | v3.0.0 | 2025-03-01 | `/api/v3/*` |
| Query param `filter` | v3.0.0 | 2025-05-01 | Use `filters[field]=value` |

**Deprecation Warnings:**

All deprecated features return a warning header:

```http
HTTP/1.1 200 OK
Deprecation: true
Sunset: Sat, 01 Jun 2025 00:00:00 GMT
Link: <https://docs.example.com/migration/v2-to-v3>; rel="deprecation"
```

---

### 📊 Version Support Policy

| Version | Status | Release Date | End of Support |
|---------|--------|--------------|----------------|
| v3.x | Current | 2025-01-15 | TBD |
| v2.x | Maintenance | 2024-01-01 | 2025-07-01 |
| v1.x | End of Life | 2023-01-01 | 2024-12-31 |

**Support Levels:**
- **Current:** Full support, new features
- **Maintenance:** Bug fixes and security patches only
- **End of Life:** No support, upgrade required

---

## Migration Guide: v2 → v3

### Step 1: Update Base URL

```javascript
// Before
const API_BASE = 'https://api.example.com/api';

// After
const API_BASE = 'https://api.example.com/api/v3';
```

### Step 2: Migrate Authentication

```javascript
// Before (v2) - API Token
const response = await fetch(`${API_BASE}/users`, {
  headers: {
    'Authorization': `Token ${apiToken}`
  }
});

// After (v3) - JWT Bearer
const tokenResponse = await fetch(`${API_BASE}/auth/login`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email, password })
});
const { token } = await tokenResponse.json();

const response = await fetch(`${API_BASE}/users`, {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});
```

### Step 3: Update Response Parsing

```javascript
// Before (v2)
const user = await response.json();
console.log(user.name);

// After (v3) - Unwrap data object
const { data } = await response.json();
console.log(data.attributes.name);

// Or use SDK
import { ApiClient } from '@company/api-sdk';
const client = new ApiClient(token);
const user = await client.users.get('123');
console.log(user.name); // SDK handles unwrapping
```

### Step 4: Update Error Handling

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
    errors.forEach(err => {
      console.error(`${err.field}: ${err.message}`);
      console.log(`Suggestion: ${err.suggestion}`);
    });
  }
} catch (error) {
  console.error(error);
}
```

### Step 5: Update Pagination

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

### Step 6: Testing

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

## Version Comparison

### Feature Matrix

| Feature | v1 | v2 | v3 |
|---------|----|----|-----|
| REST API | ✅ | ✅ | ✅ |
| GraphQL | ❌ | ❌ | ✅ |
| Webhooks | ❌ | ❌ | ✅ |
| Batch Operations | ❌ | ❌ | ✅ |
| Field Filtering | ❌ | ✅ | ✅ |
| JSON:API Format | ❌ | ❌ | ✅ |
| JWT Auth | ❌ | ✅ | ✅ |
| API Token Auth | ✅ | ✅ | ⚠️ Deprecated |
| XML Responses | ✅ | ⚠️ Deprecated | ❌ |

Legend: ✅ Supported | ❌ Not Available | ⚠️ Deprecated

---

## SDK Updates

Update to the latest SDK version:

```bash
# JavaScript/TypeScript
npm install @company/api-sdk@^3.0.0

# Python
pip install company-api-sdk>=3.0.0

# Ruby
gem install company-api-sdk -v '~> 3.0'

# Go
go get github.com/company/api-sdk/v3
```

**SDK Changelog:** [SDK Releases](https://github.com/company/api-sdk/releases)

---

## Support & Resources

- **Migration Support:** migration@example.com
- **Documentation:** https://docs.example.com/v3
- **API Status:** https://status.example.com
- **Community Forum:** https://community.example.com
- **GitHub Issues:** https://github.com/company/api/issues
```

## Best Practices

### ✅ DO
- Clearly mark breaking changes
- Provide migration guides with code examples
- Include before/after comparisons
- Document deprecation timelines
- Show impact on existing implementations
- Provide SDKs for major versions
- Use semantic versioning
- Give advance notice (3-6 months)
- Maintain backward compatibility when possible
- Document version support policy

### ❌ DON'T
- Make breaking changes without notice
- Remove endpoints without deprecation period
- Skip migration examples
- Forget to version your API
- Change behavior without documentation
- Rush deprecations

## Resources

- [Stripe API Versioning](https://stripe.com/docs/api/versioning)
- [GitHub API Changes](https://docs.github.com/en/rest/overview/api-versions)
- [Semantic Versioning](https://semver.org/)
- [JSON:API Specification](https://jsonapi.org/)
