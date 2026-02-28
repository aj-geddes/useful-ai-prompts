# Monitoring & Tracking Patterns

## Sentry Integration (Node.js)

```javascript
import * as Sentry from "@sentry/node";

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 0.1,  // 10% of requests for performance tracking
});

// Capture structured error context
function trackError(error, context = {}) {
  Sentry.withScope((scope) => {
    scope.setTag("error.code", error.code);
    scope.setTag("error.status", error.statusCode);
    scope.setContext("request", {
      requestId: context.requestId,
      method: context.method,
      path: context.path,
      userId: context.userId,
    });
    Sentry.captureException(error);
  });
}

// Usage in global error middleware
if (error.statusCode >= 500) {
  trackError(error, { requestId, method: req.method, path: req.path, userId: req.user?.id });
}
```

## Error Rate Metrics

Track error rates by code and status to detect spikes:

```javascript
// In-memory error counter (production: use Redis or StatsD)
const errorMetrics = new Map();

function recordErrorMetric(code, statusCode) {
  const key = `${code}:${statusCode}`;
  const current = errorMetrics.get(key) || { count: 0, lastSeen: null };
  errorMetrics.set(key, {
    count: current.count + 1,
    lastSeen: new Date().toISOString(),
  });
}

// Call from global error handler
recordErrorMetric(err.code, err.statusCode);

// Expose /metrics/errors endpoint for dashboards
app.get("/metrics/errors", (req, res) => {
  const metrics = {};
  for (const [key, value] of errorMetrics.entries()) {
    metrics[key] = value;
  }
  res.json({
    timestamp: new Date().toISOString(),
    errors: metrics,
  });
});
```

## StatsD / Datadog Integration

```javascript
const StatsD = require("hot-shots");
const statsd = new StatsD({ host: "localhost", port: 8125 });

function recordErrorMetric(code, statusCode) {
  // Increment counter with tags for filtering
  statsd.increment("api.errors", 1, [`code:${code}`, `status:${statusCode}`]);

  // Track error rate by status family (4xx vs 5xx)
  const family = statusCode >= 500 ? "5xx" : "4xx";
  statsd.increment("api.errors.family", 1, [`family:${family}`]);
}
```

## Alerting Strategy

Alert on **rates**, not raw counts, to avoid false positives from traffic spikes:

| Metric | Warning | Critical |
|--------|---------|----------|
| 5xx error rate | > 1% of requests | > 5% of requests |
| 429 rate-limit rate | > 10% of requests | > 30% of requests |
| Circuit breaker OPEN | Any | Sustained > 2 min |
| p99 response time | > 2s | > 5s |

```javascript
// Example: alert on 5xx rate over a rolling window
function checkErrorRateAlert(windowMs = 60_000) {
  const now = Date.now();
  const recent = recentErrors.filter((ts) => now - ts < windowMs);
  const recentTotal = recentRequests.filter((ts) => now - ts < windowMs).length;

  const rate = recentTotal > 0 ? recent.length / recentTotal : 0;

  if (rate > 0.05) {
    console.error(`[ALERT] 5xx error rate ${(rate * 100).toFixed(1)}% exceeds 5% threshold`);
    // notify PagerDuty / Slack / etc.
  }
}
```
