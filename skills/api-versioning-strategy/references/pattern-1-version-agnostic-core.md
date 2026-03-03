# Pattern 1: Version-Agnostic Core

## Pattern 1: Version-Agnostic Core

```typescript
// Core logic remains version-agnostic
class UserService {
  async getUser(id: string): Promise<User> {
    return this.repository.findById(id);
  }
}

// Version-specific adapters
class UserV1Adapter {
  transform(user: User): UserV1 {
    /* ... */
  }
}

class UserV2Adapter {
  transform(user: User): UserV2 {
    /* ... */
  }
}
```


## Pattern 2: Feature Flags for Gradual Rollout

```typescript
app.get("/api/v2/users", async (req, res) => {
  const user = await userService.getUser(req.params.id);

  // Gradual rollout of new feature
  if (featureFlags.isEnabled("enhanced-profile", req.user.id)) {
    return res.json(transformWithEnhancedProfile(user));
  }

  return res.json(transformV2(user));
});
```


## Pattern 3: API Version Metrics

```typescript
// Track usage by version
app.use((req, res, next) => {
  const version = detectVersion(req);
  metrics.increment("api.requests", { version });
  next();
});
```
