# Express HTTP Request Logging

## Express HTTP Request Logging

```javascript
// Express middleware
const express = require("express");
const expressWinston = require("express-winston");
const logger = require("./logger");

const app = express();

app.use(
  expressWinston.logger({
    transports: [
      new winston.transports.Console(),
      new winston.transports.File({ filename: "logs/http.log" }),
    ],
    format: winston.format.combine(
      winston.format.timestamp(),
      winston.format.json(),
    ),
    meta: true,
    msg: "HTTP {{req.method}} {{req.url}}",
    expressFormat: true,
  }),
);

app.get("/api/users/:id", (req, res) => {
  const requestId = req.headers["x-request-id"] || Math.random().toString();

  logger.info("User request started", { requestId, userId: req.params.id });

  try {
    const user = { id: req.params.id, name: "John Doe" };
    logger.debug("User data retrieved", { requestId, user });
    res.json(user);
  } catch (error) {
    logger.error("User retrieval failed", {
      requestId,
      error: error.message,
      stack: error.stack,
    });
    res.status(500).json({ error: "Internal server error" });
  }
});
```
