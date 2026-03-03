# Containerized Application (Node.js)

## Containerized Application (Node.js)

```dockerfile
# Dockerfile
FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application code
COPY . .

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node healthcheck.js

# Expose port (Cloud Run uses 8080 by default)
EXPOSE 8080

# Run application
CMD ["node", "server.js"]
```

```javascript
// server.js
const express = require("express");
const app = express();

const PORT = process.env.PORT || 8080;

app.use(express.json());

// Health check endpoint
app.get("/health", (req, res) => {
  res.json({ status: "ok", timestamp: new Date().toISOString() });
});

// Liveness probe
app.get("/live", (req, res) => {
  res.status(200).send("alive");
});

// Readiness probe
app.get("/ready", (req, res) => {
  res.status(200).send("ready");
});

// API endpoints
app.get("/api/data", async (req, res) => {
  try {
    const data = await fetchData();
    res.json(data);
  } catch (error) {
    console.error("Error fetching data:", error);
    res.status(500).json({ error: "Internal server error" });
  }
});

// Graceful shutdown
let isShuttingDown = false;

process.on("SIGTERM", () => {
  console.log("SIGTERM signal received: closing HTTP server");
  isShuttingDown = true;

  server.close(() => {
    console.log("HTTP server closed");
    process.exit(0);
  });

  // Force close after 30 seconds
  setTimeout(() => {
    console.error("Forced shutdown due to timeout");
    process.exit(1);
  }, 30000);
});

const server = app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

async function fetchData() {
  return { items: [] };
}
```
