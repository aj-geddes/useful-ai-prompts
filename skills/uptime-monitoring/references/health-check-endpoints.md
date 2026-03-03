# Health Check Endpoints

## Health Check Endpoints

```javascript
// Node.js health check
const express = require("express");
const app = express();

app.get("/health", (req, res) => {
  res.json({
    status: "ok",
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
  });
});

app.get("/health/deep", async (req, res) => {
  const health = {
    status: "ok",
    checks: {
      database: "unknown",
      cache: "unknown",
      externalApi: "unknown",
    },
  };

  try {
    const dbResult = await db.query("SELECT 1");
    health.checks.database = dbResult ? "ok" : "error";
  } catch {
    health.checks.database = "error";
    health.status = "degraded";
  }

  try {
    const cacheResult = await redis.ping();
    health.checks.cache = cacheResult === "PONG" ? "ok" : "error";
  } catch {
    health.checks.cache = "error";
  }

  try {
    const response = await fetch("https://api.example.com/health");
    health.checks.externalApi = response.ok ? "ok" : "error";
  } catch {
    health.checks.externalApi = "error";
  }

  const statusCode = health.status === "ok" ? 200 : 503;
  res.status(statusCode).json(health);
});

app.get("/readiness", async (req, res) => {
  try {
    const dbCheck = await db.query("SELECT 1");
    const cacheCheck = await redis.ping();

    if (dbCheck && cacheCheck === "PONG") {
      res.json({ ready: true });
    } else {
      res.status(503).json({ ready: false });
    }
  } catch {
    res.status(503).json({ ready: false });
  }
});

app.get("/liveness", (req, res) => {
  res.json({ alive: true });
});
```
