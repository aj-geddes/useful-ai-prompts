# Origin and Referer Validation

## Origin and Referer Validation

```javascript
// origin-validation.js
function validateOrigin(req, res, next) {
  const allowedOrigins = ["https://example.com", "https://app.example.com"];

  const origin = req.headers.origin;
  const referer = req.headers.referer;

  // Check Origin header
  if (origin && !allowedOrigins.includes(origin)) {
    return res.status(403).json({
      error: "invalid_origin",
    });
  }

  // Check Referer header as fallback
  if (!origin && referer) {
    const refererUrl = new URL(referer);
    if (!allowedOrigins.includes(refererUrl.origin)) {
      return res.status(403).json({
        error: "invalid_referer",
      });
    }
  }

  next();
}

// Apply to state-changing routes
app.use("/api/*", validateOrigin);
```
