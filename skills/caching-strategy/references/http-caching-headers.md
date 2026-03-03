# HTTP Caching Headers

## HTTP Caching Headers

```typescript
import express from "express";

const app = express();

// Cache-Control middleware
function cacheControl(
  maxAge: number,
  options: {
    private?: boolean;
    noStore?: boolean;
    noCache?: boolean;
    mustRevalidate?: boolean;
    staleWhileRevalidate?: number;
  } = {},
) {
  return (
    req: express.Request,
    res: express.Response,
    next: express.NextFunction,
  ) => {
    const directives: string[] = [];

    if (options.noStore) {
      directives.push("no-store");
    } else if (options.noCache) {
      directives.push("no-cache");
    } else {
      directives.push(options.private ? "private" : "public");
      directives.push(`max-age=${maxAge}`);

      if (options.staleWhileRevalidate) {
        directives.push(
          `stale-while-revalidate=${options.staleWhileRevalidate}`,
        );
      }
    }

    if (options.mustRevalidate) {
      directives.push("must-revalidate");
    }

    res.setHeader("Cache-Control", directives.join(", "));
    next();
  };
}

// Static assets - long cache
app.use("/static", cacheControl(31536000), express.static("public"));

// API - short cache with revalidation
app.get(
  "/api/data",
  cacheControl(60, { staleWhileRevalidate: 300 }),
  (req, res) => {
    res.json({ data: "cached for 60s" });
  },
);

// Dynamic content - no cache
app.get(
  "/api/user/profile",
  cacheControl(0, { private: true, noCache: true }),
  (req, res) => {
    res.json({ user: "always fresh" });
  },
);

// ETag support
app.get("/api/resource/:id", async (req, res) => {
  const resource = await getResource(req.params.id);
  const etag = generateETag(resource);

  res.setHeader("ETag", etag);

  // Check if client has current version
  if (req.headers["if-none-match"] === etag) {
    return res.status(304).end();
  }

  res.json(resource);
});

function generateETag(data: any): string {
  return require("crypto")
    .createHash("md5")
    .update(JSON.stringify(data))
    .digest("hex");
}
```
