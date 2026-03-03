# Express Middleware Integration

## Express Middleware Integration

```javascript
// app.js
const express = require("express");
const Sentry = require("./sentry");

const app = express();

app.use(Sentry.Handlers.requestHandler());
app.use(Sentry.Handlers.tracingHandler());

app.get("/api/users/:id", (req, res) => {
  const transaction = Sentry.startTransaction({
    name: "get_user",
    op: "http.server",
  });

  try {
    const userId = req.params.id;

    Sentry.captureMessage("Fetching user", {
      level: "info",
      tags: { userId: userId },
    });

    const user = db.query(`SELECT * FROM users WHERE id = ${userId}`);

    if (!user) {
      Sentry.captureException(new Error("User not found"), {
        level: "warning",
        contexts: { request: { userId } },
      });
      return res.status(404).json({ error: "User not found" });
    }

    transaction.setTag("user.id", user.id);
    res.json(user);
  } catch (error) {
    Sentry.captureException(error, {
      level: "error",
      tags: { endpoint: "get_user", userId: req.params.id },
    });
    res.status(500).json({ error: "Internal server error" });
  } finally {
    transaction.finish();
  }
});

app.use(Sentry.Handlers.errorHandler());

app.listen(3000);
```
