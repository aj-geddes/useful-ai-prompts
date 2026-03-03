# Backward Compatibility Patterns

## Backward Compatibility Patterns

### Additive Changes (Non-Breaking)

```typescript
// ✅ Safe: Adding optional fields
interface UserV1 {
  id: string;
  name: string;
}

interface UserV2 extends UserV1 {
  email?: string; // Optional field
  avatar?: string; // Optional field
}

// ✅ Safe: Adding new endpoints
app.post("/api/v1/users/:id/avatar", uploadAvatar);

// ✅ Safe: Accepting additional parameters
app.get("/api/v1/users", (req, res) => {
  const { page, limit, sortBy } = req.query; // New optional params
  const users = await userService.list({ page, limit, sortBy });
  res.json(users);
});
```

### Breaking Changes (Require New Version)

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

### Handling Both Versions

```typescript
// version-adapter.ts
export class UserAdapter {
  toV1(user: User): UserV1Response {
    return {
      id: user.id,
      name: user.fullName,
      username: user.username,
      created: user.createdAt.toISOString(),
    };
  }

  toV2(user: User): UserV2Response {
    return {
      id: user.id,
      name: user.fullName,
      email: user.email,
      profile: {
        avatar: user.avatarUrl,
        bio: user.bio,
      },
      createdAt: user.createdAt.getTime(),
    };
  }

  fromV1(data: UserV1Request): User {
    return {
      fullName: data.name,
      username: data.username,
      email: data.email || null,
    };
  }

  fromV2(data: UserV2Request): User {
    return {
      fullName: data.name,
      username: data.username || generateUsername(data.email),
      email: data.email,
      avatarUrl: data.profile?.avatar,
      bio: data.profile?.bio,
    };
  }
}

// Usage in controller
app.get("/api/:version/users/:id", async (req, res) => {
  const user = await userService.findById(req.params.id);
  const adapter = new UserAdapter();

  const response =
    req.params.version === "v2" ? adapter.toV2(user) : adapter.toV1(user);

  res.json(response);
});
```
