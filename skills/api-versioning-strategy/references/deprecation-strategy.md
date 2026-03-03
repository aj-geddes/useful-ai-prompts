# Deprecation Strategy

## Deprecation Strategy

### Deprecation Headers

```typescript
// deprecation-middleware.ts
export function deprecationWarning(version: string, sunsetDate: Date) {
  return (req, res, next) => {
    res.setHeader("Deprecation", "true");
    res.setHeader("Sunset", sunsetDate.toUTCString());
    res.setHeader("Link", '</api/v2/docs>; rel="successor-version"');
    res.setHeader(
      "X-API-Warn",
      `Version ${version} is deprecated. Please migrate to v2 by ${sunsetDate.toDateString()}`,
    );
    next();
  };
}

// Apply to deprecated routes
app.use("/api/v1/*", deprecationWarning("v1", new Date("2024-12-31")));

app.get("/api/v1/users", (req, res) => {
  // Return v1 response with deprecation headers
  res.json(users);
});
```

### Deprecation Response

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

### Gradual Deprecation Timeline

```typescript
// deprecation-stages.ts
enum DeprecationStage {
  SUPPORTED = "supported",
  DEPRECATED = "deprecated",
  SUNSET_ANNOUNCED = "sunset_announced",
  READONLY = "readonly",
  SHUTDOWN = "shutdown",
}

const versionStatus = {
  v1: {
    stage: DeprecationStage.READONLY,
    sunsetDate: new Date("2024-06-30"),
    message: "Read-only mode. New writes are disabled.",
  },
  v2: {
    stage: DeprecationStage.DEPRECATED,
    sunsetDate: new Date("2024-12-31"),
    message: "Deprecated. Please migrate to v3.",
  },
  v3: {
    stage: DeprecationStage.SUPPORTED,
    message: "Current stable version.",
  },
};

// Middleware to enforce deprecation
app.use("/api/:version/*", (req, res, next) => {
  const status = versionStatus[req.params.version];

  if (!status) {
    return res.status(404).json({ error: "API version not found" });
  }

  if (status.stage === DeprecationStage.SHUTDOWN) {
    return res.status(410).json({ error: "API version no longer available" });
  }

  if (
    status.stage === DeprecationStage.READONLY &&
    ["POST", "PUT", "PATCH", "DELETE"].includes(req.method)
  ) {
    return res.status(403).json({
      error: "API version is read-only",
      message: status.message,
    });
  }

  // Add deprecation headers
  if (status.stage !== DeprecationStage.SUPPORTED) {
    res.setHeader("X-API-Deprecated", "true");
    res.setHeader("X-API-Sunset", status.sunsetDate.toISOString());
  }

  next();
});
```
