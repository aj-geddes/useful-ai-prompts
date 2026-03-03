# Node.js Metrics Implementation

## Node.js Metrics Implementation

```javascript
// metrics.js
const promClient = require("prom-client");
const register = new promClient.Registry();

promClient.collectDefaultMetrics({ register });

const httpRequestDuration = new promClient.Histogram({
  name: "http_request_duration_seconds",
  help: "HTTP request duration",
  labelNames: ["method", "route", "status_code"],
  buckets: [0.1, 0.5, 1, 2, 5],
  registers: [register],
});

const requestsTotal = new promClient.Counter({
  name: "requests_total",
  help: "Total requests",
  labelNames: ["method", "route", "status_code"],
  registers: [register],
});

// Express middleware
const express = require("express");
const app = express();

app.get("/metrics", (req, res) => {
  res.set("Content-Type", register.contentType);
  res.end(register.metrics());
});

app.use((req, res, next) => {
  const start = Date.now();
  res.on("finish", () => {
    const duration = (Date.now() - start) / 1000;
    httpRequestDuration
      .labels(req.method, req.path, res.statusCode)
      .observe(duration);
    requestsTotal.labels(req.method, req.path, res.statusCode).inc();
  });
  next();
});

module.exports = { register, httpRequestDuration, requestsTotal };
```
