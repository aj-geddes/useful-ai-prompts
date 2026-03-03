# Content Security Policy

## Content Security Policy

```javascript
// csp-config.js
const helmet = require("helmet");

function setupCSP(app) {
  app.use(
    helmet.contentSecurityPolicy({
      directives: {
        defaultSrc: ["'self'"],

        // Only allow scripts from trusted sources
        scriptSrc: [
          "'self'",
          "'nonce-RANDOM_NONCE'", // Use dynamic nonces
          "https://cdn.example.com",
        ],

        // Styles
        styleSrc: [
          "'self'",
          "'nonce-RANDOM_NONCE'",
          "https://fonts.googleapis.com",
        ],

        // No inline styles/scripts
        objectSrc: ["'none'"],
        baseUri: ["'self'"],

        // Report violations
        reportUri: ["/api/csp-violations"],
      },
    }),
  );

  // CSP violation reporter
  app.post("/api/csp-violations", (req, res) => {
    console.error("CSP Violation:", req.body);
    res.status(204).end();
  });
}

// Generate nonce for inline scripts
function generateNonce() {
  return require("crypto").randomBytes(16).toString("base64");
}

// Express middleware to add nonce
app.use((req, res, next) => {
  res.locals.nonce = generateNonce();
  next();
});

// In templates: <script nonce="<%= nonce %>">
```
