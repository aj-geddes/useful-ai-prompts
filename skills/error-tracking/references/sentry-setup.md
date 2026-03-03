# Sentry Setup

## Sentry Setup

```bash
npm install -g @sentry/cli
npm install @sentry/node @sentry/tracing
sentry init -d
```


## Node.js Sentry Integration

```javascript
// sentry.js
const Sentry = require("@sentry/node");
const Tracing = require("@sentry/tracing");

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV || "development",
  tracesSampleRate: process.env.NODE_ENV === "production" ? 0.1 : 1.0,
  release: process.env.APP_VERSION || "1.0.0",
  integrations: [
    new Sentry.Integrations.Http({ tracing: true }),
    new Tracing.Integrations.Express({
      app: true,
      request: true,
      transaction: true,
    }),
  ],
  ignoreErrors: ["Network request failed", "TimeoutError"],
});

module.exports = Sentry;
```
