# Versioning Approaches

## Versioning Approaches

### URL Path Versioning

```typescript
// express-router.ts
import express from "express";

const app = express();

// Version 1
app.get("/api/v1/users", (req, res) => {
  res.json({
    users: [{ id: 1, name: "John Doe" }],
  });
});

// Version 2 - Added email field
app.get("/api/v2/users", (req, res) => {
  res.json({
    users: [{ id: 1, name: "John Doe", email: "john@example.com" }],
  });
});

// Shared logic with version-specific transformations
app.get("/api/:version/users/:id", async (req, res) => {
  const user = await userService.findById(req.params.id);

  if (req.params.version === "v1") {
    res.json({ id: user.id, name: user.name });
  } else if (req.params.version === "v2") {
    res.json({ id: user.id, name: user.name, email: user.email });
  }
});
```

**Pros:** Simple, explicit, cache-friendly
**Cons:** URL pollution, harder to deprecate

### Header Versioning (Content Negotiation)

```typescript
// header-versioning.ts
app.get("/api/users", (req, res) => {
  const version = req.headers["api-version"] || "1";

  switch (version) {
    case "1":
      return res.json(transformToV1(users));
    case "2":
      return res.json(transformToV2(users));
    default:
      return res.status(400).json({ error: "Unsupported API version" });
  }
});

// Or using Accept header
app.get("/api/users", (req, res) => {
  const acceptHeader = req.headers["accept"];

  if (acceptHeader.includes("application/vnd.myapi.v2+json")) {
    return res.json(transformToV2(users));
  }

  // Default to v1
  return res.json(transformToV1(users));
});
```

**Pros:** Clean URLs, RESTful
**Cons:** Less visible, harder to test manually

### Query Parameter Versioning

```typescript
// query-param-versioning.ts
app.get("/api/users", (req, res) => {
  const version = req.query.version || "1";

  if (version === "2") {
    return res.json(transformToV2(users));
  }

  return res.json(transformToV1(users));
});

// Usage: GET /api/users?version=2
```

**Pros:** Easy to implement, flexible
**Cons:** Not RESTful, can be overlooked
