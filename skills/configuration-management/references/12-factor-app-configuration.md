# 12-Factor App Configuration

## 12-Factor App Configuration

```typescript
// config/twelve-factor.ts

/**
 * 12-Factor App Configuration Principles
 *
 * III. Config - Store config in the environment
 * - Strict separation of config from code
 * - Config varies between deploys, code does not
 * - Store in environment variables
 */

// ✅ Good: Configuration from environment
export const config = {
  database: {
    url: process.env.DATABASE_URL!,
    poolMin: parseInt(process.env.DB_POOL_MIN || "2", 10),
    poolMax: parseInt(process.env.DB_POOL_MAX || "10", 10),
  },
  redis: {
    url: process.env.REDIS_URL!,
  },
  s3: {
    bucket: process.env.S3_BUCKET!,
    region: process.env.AWS_REGION!,
  },
  sendgrid: {
    apiKey: process.env.SENDGRID_API_KEY!,
  },
};

// ❌ Bad: Hardcoded configuration
const badConfig = {
  database: {
    host: "prod-db.example.com", // Hardcoded!
    password: "secretpassword", // Secret in code!
  },
};

/**
 * Backing Services - Treat backing services as attached resources
 * - Database, cache, message queue, etc. are accessed via URLs
 * - Should be swappable without code changes
 */

// ✅ Good: Backing service as URL
const db = createConnection(process.env.DATABASE_URL);
const cache = createClient(process.env.REDIS_URL);

// Can swap services by changing environment variable
// DATABASE_URL=postgresql://localhost/dev  (local dev)
// DATABASE_URL=postgresql://prod-db/app     (production)

/**
 * Disposability - Fast startup and graceful shutdown
 */
function startServer() {
  const server = app.listen(config.port, () => {
    console.log(`Server started on port ${config.port}`);
  });

  // Graceful shutdown
  process.on("SIGTERM", async () => {
    console.log("SIGTERM received, shutting down gracefully");

    server.close(() => {
      console.log("HTTP server closed");
    });

    await db.close();
    await cache.quit();

    process.exit(0);
  });
}
```
