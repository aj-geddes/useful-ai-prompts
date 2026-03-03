# PM2 Graceful Shutdown

## PM2 Graceful Shutdown

```typescript
// ecosystem.config.js
module.exports = {
  apps: [
    {
      name: "api-server",
      script: "./dist/server.js",
      instances: 4,
      exec_mode: "cluster",
      kill_timeout: 30000, // Wait 30s for graceful shutdown
      wait_ready: true,
      listen_timeout: 10000,
      shutdown_with_message: true,
    },
  ],
};

// server.ts
import express from "express";

const app = express();
const port = process.env.PORT || 3000;

// ... setup routes ...

const server = app.listen(port, () => {
  console.log(`Server started on port ${port}`);

  // Signal to PM2 that app is ready
  if (process.send) {
    process.send("ready");
  }
});

// Handle shutdown message from PM2
process.on("message", (msg) => {
  if (msg === "shutdown") {
    console.log("Received shutdown message from PM2");
    gracefulShutdown();
  }
});

async function gracefulShutdown() {
  console.log("Starting graceful shutdown...");

  // Stop accepting new connections
  server.close(() => {
    console.log("Server closed");
    process.exit(0);
  });

  // Force shutdown after timeout
  setTimeout(() => {
    console.error("Forced shutdown after timeout");
    process.exit(1);
  }, 28000); // Less than PM2's kill_timeout
}
```
