# Custom Error Context

## Custom Error Context

```javascript
// custom-error-context.js
const Sentry = require("@sentry/node");

Sentry.configureScope((scope) => {
  scope.setUser({
    id: userId,
    email: userEmail,
    subscription: "pro",
  });

  scope.setTag("feature_flag", "new-ui");
  scope.setTag("database", "postgres-v12");

  scope.setContext("character", {
    name: "Mighty Fighter",
    level: 19,
  });

  scope.addBreadcrumb({
    category: "ui.click",
    message: "User clicked signup button",
    level: "info",
  });

  scope.addBreadcrumb({
    category: "database",
    message: "Query executed",
    level: "debug",
    data: {
      query: "SELECT * FROM users",
      duration: 125,
    },
  });
});

// Before sending
Sentry.init({
  dsn: process.env.SENTRY_DSN,
  beforeSend(event, hint) {
    if (event.request) {
      delete event.request.cookies;
      delete event.request.headers["authorization"];
    }
    return event;
  },
});
```
