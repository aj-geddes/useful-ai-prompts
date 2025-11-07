---
name: api-versioning-strategy
description: Implement API versioning strategies including URL versioning, header versioning, backward compatibility, deprecation strategies, and migration guides. Use when dealing with API versions, deprecating endpoints, or managing breaking changes.
---

# API Versioning Strategy

## Overview

Comprehensive guide to API versioning approaches, deprecation strategies, backward compatibility techniques, and migration planning for REST APIs, GraphQL, and gRPC services.

## When to Use

- Designing new APIs with versioning from the start
- Adding breaking changes to existing APIs
- Deprecating old API versions
- Planning API migrations
- Ensuring backward compatibility
- Managing multiple API versions simultaneously
- Creating API documentation for different versions
- Implementing API version routing

## Instructions

### 1. **Versioning Approaches**

#### URL Path Versioning
```typescript
// express-router.ts
import express from 'express';

const app = express();

// Version 1
app.get('/api/v1/users', (req, res) => {
  res.json({
    users: [
      { id: 1, name: 'John Doe' }
    ]
  });
});

// Version 2 - Added email field
app.get('/api/v2/users', (req, res) => {
  res.json({
    users: [
      { id: 1, name: 'John Doe', email: 'john@example.com' }
    ]
  });
});

// Shared logic with version-specific transformations
app.get('/api/:version/users/:id', async (req, res) => {
  const user = await userService.findById(req.params.id);

  if (req.params.version === 'v1') {
    res.json({ id: user.id, name: user.name });
  } else if (req.params.version === 'v2') {
    res.json({ id: user.id, name: user.name, email: user.email });
  }
});
```

**Pros:** Simple, explicit, cache-friendly
**Cons:** URL pollution, harder to deprecate

#### Header Versioning (Content Negotiation)
```typescript
// header-versioning.ts
app.get('/api/users', (req, res) => {
  const version = req.headers['api-version'] || '1';

  switch (version) {
    case '1':
      return res.json(transformToV1(users));
    case '2':
      return res.json(transformToV2(users));
    default:
      return res.status(400).json({ error: 'Unsupported API version' });
  }
});

// Or using Accept header
app.get('/api/users', (req, res) => {
  const acceptHeader = req.headers['accept'];

  if (acceptHeader.includes('application/vnd.myapi.v2+json')) {
    return res.json(transformToV2(users));
  }

  // Default to v1
  return res.json(transformToV1(users));
});
```

**Pros:** Clean URLs, RESTful
**Cons:** Less visible, harder to test manually

#### Query Parameter Versioning
```typescript
// query-param-versioning.ts
app.get('/api/users', (req, res) => {
  const version = req.query.version || '1';

  if (version === '2') {
    return res.json(transformToV2(users));
  }

  return res.json(transformToV1(users));
});

// Usage: GET /api/users?version=2
```

**Pros:** Easy to implement, flexible
**Cons:** Not RESTful, can be overlooked

### 2. **Backward Compatibility Patterns**

#### Additive Changes (Non-Breaking)
```typescript
// ✅ Safe: Adding optional fields
interface UserV1 {
  id: string;
  name: string;
}

interface UserV2 extends UserV1 {
  email?: string;  // Optional field
  avatar?: string; // Optional field
}

// ✅ Safe: Adding new endpoints
app.post('/api/v1/users/:id/avatar', uploadAvatar);

// ✅ Safe: Accepting additional parameters
app.get('/api/v1/users', (req, res) => {
  const { page, limit, sortBy } = req.query; // New optional params
  const users = await userService.list({ page, limit, sortBy });
  res.json(users);
});
```

#### Breaking Changes (Require New Version)
```typescript
// ❌ Breaking: Removing fields
interface UserV1 {
  id: string;
  name: string;
  username: string;
}

interface UserV2 {
  id: string;
  name: string;
  // username removed - BREAKING!
}

// ❌ Breaking: Changing field types
interface UserV1 {
  id: string;
  created: string; // ISO string
}

interface UserV2 {
  id: string;
  created: number; // Unix timestamp - BREAKING!
}

// ❌ Breaking: Renaming fields
interface UserV1 {
  fullName: string;
}

interface UserV2 {
  name: string; // Renamed from fullName - BREAKING!
}

// ❌ Breaking: Changing response structure
// V1
{ users: [...], total: 10 }

// V2 - BREAKING!
{ data: [...], meta: { total: 10 } }
```

#### Handling Both Versions
```typescript
// version-adapter.ts
export class UserAdapter {
  toV1(user: User): UserV1Response {
    return {
      id: user.id,
      name: user.fullName,
      username: user.username,
      created: user.createdAt.toISOString()
    };
  }

  toV2(user: User): UserV2Response {
    return {
      id: user.id,
      name: user.fullName,
      email: user.email,
      profile: {
        avatar: user.avatarUrl,
        bio: user.bio
      },
      createdAt: user.createdAt.getTime()
    };
  }

  fromV1(data: UserV1Request): User {
    return {
      fullName: data.name,
      username: data.username,
      email: data.email || null
    };
  }

  fromV2(data: UserV2Request): User {
    return {
      fullName: data.name,
      username: data.username || generateUsername(data.email),
      email: data.email,
      avatarUrl: data.profile?.avatar,
      bio: data.profile?.bio
    };
  }
}

// Usage in controller
app.get('/api/:version/users/:id', async (req, res) => {
  const user = await userService.findById(req.params.id);
  const adapter = new UserAdapter();

  const response = req.params.version === 'v2'
    ? adapter.toV2(user)
    : adapter.toV1(user);

  res.json(response);
});
```

### 3. **Deprecation Strategy**

#### Deprecation Headers
```typescript
// deprecation-middleware.ts
export function deprecationWarning(version: string, sunsetDate: Date) {
  return (req, res, next) => {
    res.setHeader('Deprecation', 'true');
    res.setHeader('Sunset', sunsetDate.toUTCString());
    res.setHeader('Link', '</api/v2/docs>; rel="successor-version"');
    res.setHeader('X-API-Warn', `Version ${version} is deprecated. Please migrate to v2 by ${sunsetDate.toDateString()}`);
    next();
  };
}

// Apply to deprecated routes
app.use('/api/v1/*', deprecationWarning('v1', new Date('2024-12-31')));

app.get('/api/v1/users', (req, res) => {
  // Return v1 response with deprecation headers
  res.json(users);
});
```

#### Deprecation Response
```typescript
// Include deprecation info in response body
app.get('/api/v1/users', (req, res) => {
  res.json({
    _meta: {
      deprecated: true,
      sunsetDate: '2024-12-31',
      message: 'This API version is deprecated. Please migrate to v2.',
      migrationGuide: 'https://docs.example.com/migration-v1-to-v2'
    },
    users: [...]
  });
});
```

#### Gradual Deprecation Timeline
```typescript
// deprecation-stages.ts
enum DeprecationStage {
  SUPPORTED = 'supported',
  DEPRECATED = 'deprecated',
  SUNSET_ANNOUNCED = 'sunset_announced',
  READONLY = 'readonly',
  SHUTDOWN = 'shutdown'
}

const versionStatus = {
  'v1': {
    stage: DeprecationStage.READONLY,
    sunsetDate: new Date('2024-06-30'),
    message: 'Read-only mode. New writes are disabled.'
  },
  'v2': {
    stage: DeprecationStage.DEPRECATED,
    sunsetDate: new Date('2024-12-31'),
    message: 'Deprecated. Please migrate to v3.'
  },
  'v3': {
    stage: DeprecationStage.SUPPORTED,
    message: 'Current stable version.'
  }
};

// Middleware to enforce deprecation
app.use('/api/:version/*', (req, res, next) => {
  const status = versionStatus[req.params.version];

  if (!status) {
    return res.status(404).json({ error: 'API version not found' });
  }

  if (status.stage === DeprecationStage.SHUTDOWN) {
    return res.status(410).json({ error: 'API version no longer available' });
  }

  if (status.stage === DeprecationStage.READONLY &&
      ['POST', 'PUT', 'PATCH', 'DELETE'].includes(req.method)) {
    return res.status(403).json({
      error: 'API version is read-only',
      message: status.message
    });
  }

  // Add deprecation headers
  if (status.stage !== DeprecationStage.SUPPORTED) {
    res.setHeader('X-API-Deprecated', 'true');
    res.setHeader('X-API-Sunset', status.sunsetDate.toISOString());
  }

  next();
});
```

### 4. **Migration Guide Example**

```markdown
# API Migration Guide: v1 to v2

## Overview
Version 2 introduces breaking changes to improve consistency and add new features.

**Timeline:**
- 2024-01-01: v2 released
- 2024-06-01: v1 deprecated
- 2024-09-01: v1 read-only
- 2024-12-31: v1 shutdown

## Breaking Changes

### 1. Response Structure
**v1:**
```json
{
  "users": [...],
  "total": 10,
  "page": 1
}
```

**v2:**
```json
{
  "data": [...],
  "meta": {
    "total": 10,
    "page": 1,
    "perPage": 20
  }
}
```

**Migration:**
```javascript
// Before
const users = response.users;
const total = response.total;

// After
const users = response.data;
const total = response.meta.total;
```

### 2. Date Format
**v1:** ISO 8601 strings
**v2:** Unix timestamps

**Migration:**
```javascript
// Before
const created = new Date(user.created);

// After
const created = new Date(user.created * 1000);
```

### 3. Error Format
**v1:**
```json
{ "error": "User not found" }
```

**v2:**
```json
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User not found",
    "details": {}
  }
}
```

## New Features in v2

### Pagination
```javascript
// v2 supports cursor-based pagination
GET /api/v2/users?cursor=eyJpZCI6MTIzfQ&limit=20
```

### Field Selection
```javascript
// v2 supports field filtering
GET /api/v2/users?fields=id,name,email
```

### Batch Operations
```javascript
// v2 supports batch requests
POST /api/v2/batch
{
  "requests": [
    { "method": "GET", "path": "/users/1" },
    { "method": "GET", "path": "/users/2" }
  ]
}
```

## Code Examples

### JavaScript/TypeScript
```typescript
// v1 Client
class ApiClientV1 {
  async getUsers() {
    const response = await fetch('/api/v1/users');
    const data = await response.json();
    return data.users;
  }
}

// v2 Client
class ApiClientV2 {
  async getUsers() {
    const response = await fetch('/api/v2/users');
    const data = await response.json();
    return data.data; // Changed from .users to .data
  }
}
```

### Python
```python
# v1
response = requests.get(f"{base_url}/api/v1/users")
users = response.json()["users"]

# v2
response = requests.get(f"{base_url}/api/v2/users")
users = response.json()["data"]
```
```

### 5. **GraphQL Versioning**

```typescript
// GraphQL handles versioning differently - through schema evolution
// schema-v1.graphql
type User {
  id: ID!
  name: String!
  username: String!
}

// schema-v2.graphql (deprecated fields)
type User {
  id: ID!
  name: String!
  username: String! @deprecated(reason: "Use email instead")
  email: String!
  profile: Profile
}

type Profile {
  avatar: String
  bio: String
}

// Field deprecation in resolver
const resolvers = {
  User: {
    username: (user) => {
      console.warn('username field is deprecated, use email instead');
      return user.email;
    }
  }
};
```

### 6. **gRPC Versioning**

```protobuf
// v1/user.proto
syntax = "proto3";
package user.v1;

message User {
  string id = 1;
  string name = 2;
}

// v2/user.proto
syntax = "proto3";
package user.v2;

message User {
  string id = 1;
  string name = 2;
  string email = 3;
  Profile profile = 4;
}

message Profile {
  string avatar = 1;
  string bio = 2;
}

// Both versions can coexist
service UserServiceV1 {
  rpc GetUser (GetUserRequest) returns (user.v1.User);
}

service UserServiceV2 {
  rpc GetUser (GetUserRequest) returns (user.v2.User);
}
```

### 7. **Version Detection & Routing**

```typescript
// version-router.ts
import express from 'express';

export class VersionRouter {
  private versions = new Map<string, express.Router>();

  registerVersion(version: string, router: express.Router) {
    this.versions.set(version, router);
  }

  getMiddleware() {
    return (req, res, next) => {
      // Detect version from multiple sources
      const version = this.detectVersion(req);

      const router = this.versions.get(version);
      if (!router) {
        return res.status(400).json({
          error: 'Invalid API version',
          supportedVersions: Array.from(this.versions.keys())
        });
      }

      // Set version in request for logging
      req.apiVersion = version;

      // Use versioned router
      router(req, res, next);
    };
  }

  private detectVersion(req): string {
    // 1. Check URL path
    const pathMatch = req.path.match(/^\/api\/v(\d+)\//);
    if (pathMatch) return pathMatch[1];

    // 2. Check header
    if (req.headers['api-version']) {
      return req.headers['api-version'];
    }

    // 3. Check Accept header
    const acceptMatch = req.headers['accept']?.match(/application\/vnd\.myapi\.v(\d+)\+json/);
    if (acceptMatch) return acceptMatch[1];

    // 4. Check query parameter
    if (req.query.version) {
      return req.query.version;
    }

    // 5. Default version
    return '1';
  }
}

// Usage
const versionRouter = new VersionRouter();

versionRouter.registerVersion('1', v1Router);
versionRouter.registerVersion('2', v2Router);
versionRouter.registerVersion('3', v3Router);

app.use('/api', versionRouter.getMiddleware());
```

### 8. **Testing Multiple Versions**

```typescript
// api-version.test.ts
describe('API Versioning', () => {
  describe('v1', () => {
    it('should return user with v1 format', async () => {
      const response = await request(app)
        .get('/api/v1/users/1')
        .expect(200);

      expect(response.body).toHaveProperty('id');
      expect(response.body).toHaveProperty('name');
      expect(response.body).not.toHaveProperty('email');
    });
  });

  describe('v2', () => {
    it('should return user with v2 format', async () => {
      const response = await request(app)
        .get('/api/v2/users/1')
        .expect(200);

      expect(response.body).toHaveProperty('id');
      expect(response.body).toHaveProperty('name');
      expect(response.body).toHaveProperty('email');
      expect(response.body).toHaveProperty('profile');
    });

    it('should include deprecation headers for v1', async () => {
      const response = await request(app)
        .get('/api/v1/users/1');

      expect(response.headers['deprecation']).toBe('true');
      expect(response.headers['sunset']).toBeDefined();
    });
  });

  describe('version negotiation', () => {
    it('should use version from header', async () => {
      const response = await request(app)
        .get('/api/users/1')
        .set('API-Version', '2')
        .expect(200);

      expect(response.body).toHaveProperty('email');
    });

    it('should default to v1 if no version specified', async () => {
      const response = await request(app)
        .get('/api/users/1')
        .expect(200);

      expect(response.body).not.toHaveProperty('email');
    });
  });
});
```

## Best Practices

### ✅ DO
- Version from day one (even if v1)
- Document breaking vs non-breaking changes
- Provide clear migration guides with code examples
- Use semantic versioning principles
- Give 6-12 months deprecation notice
- Monitor usage of deprecated APIs
- Send deprecation warnings to API consumers
- Support at least 2 versions simultaneously
- Use adapters/transformers for version logic
- Test all supported versions
- Log which API version is being used
- Provide migration tooling when possible
- Be consistent with versioning approach

### ❌ DON'T
- Change API behavior without versioning
- Remove versions without notice
- Support too many versions (>3)
- Use different versioning strategies in same API
- Break APIs without incrementing version
- Forget to update documentation
- Deprecate too quickly (<6 months)
- Ignore feedback from API consumers
- Make every change a new version
- Use version numbers inconsistently

## Common Patterns

### Pattern 1: Version-Agnostic Core
```typescript
// Core logic remains version-agnostic
class UserService {
  async getUser(id: string): Promise<User> {
    return this.repository.findById(id);
  }
}

// Version-specific adapters
class UserV1Adapter {
  transform(user: User): UserV1 { /* ... */ }
}

class UserV2Adapter {
  transform(user: User): UserV2 { /* ... */ }
}
```

### Pattern 2: Feature Flags for Gradual Rollout
```typescript
app.get('/api/v2/users', async (req, res) => {
  const user = await userService.getUser(req.params.id);

  // Gradual rollout of new feature
  if (featureFlags.isEnabled('enhanced-profile', req.user.id)) {
    return res.json(transformWithEnhancedProfile(user));
  }

  return res.json(transformV2(user));
});
```

### Pattern 3: API Version Metrics
```typescript
// Track usage by version
app.use((req, res, next) => {
  const version = detectVersion(req);
  metrics.increment('api.requests', { version });
  next();
});
```

## Tools & Resources

- **OpenAPI/Swagger**: API documentation with version support
- **Postman**: API testing with version management
- **API Blueprint**: API design with versioning
- **Stoplight**: API design and documentation
- **Kong**: API gateway with version routing
