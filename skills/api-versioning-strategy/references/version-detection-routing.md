# Version Detection & Routing

## Version Detection & Routing

```typescript
// version-router.ts
import express from "express";

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
          error: "Invalid API version",
          supportedVersions: Array.from(this.versions.keys()),
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
    if (req.headers["api-version"]) {
      return req.headers["api-version"];
    }

    // 3. Check Accept header
    const acceptMatch = req.headers["accept"]?.match(
      /application\/vnd\.myapi\.v(\d+)\+json/,
    );
    if (acceptMatch) return acceptMatch[1];

    // 4. Check query parameter
    if (req.query.version) {
      return req.query.version;
    }

    // 5. Default version
    return "1";
  }
}

// Usage
const versionRouter = new VersionRouter();

versionRouter.registerVersion("1", v1Router);
versionRouter.registerVersion("2", v2Router);
versionRouter.registerVersion("3", v3Router);

app.use("/api", versionRouter.getMiddleware());
```
