# Node.js/Express Security Headers

## Node.js/Express Security Headers

```javascript
// security-headers.js
const helmet = require("helmet");

function configureSecurityHeaders(app) {
  // Comprehensive Helmet configuration
  app.use(
    helmet({
      // Content Security Policy
      contentSecurityPolicy: {
        directives: {
          defaultSrc: ["'self'"],
          scriptSrc: [
            "'self'",
            "'unsafe-inline'", // Remove in production
            "https://cdn.example.com",
            "https://www.google-analytics.com",
          ],
          styleSrc: [
            "'self'",
            "'unsafe-inline'",
            "https://fonts.googleapis.com",
          ],
          fontSrc: ["'self'", "https://fonts.gstatic.com"],
          imgSrc: ["'self'", "data:", "https:", "blob:"],
          connectSrc: ["'self'", "https://api.example.com"],
          frameSrc: ["'none'"],
          objectSrc: ["'none'"],
          upgradeInsecureRequests: [],
        },
      },

      // Strict Transport Security
      hsts: {
        maxAge: 31536000, // 1 year
        includeSubDomains: true,
        preload: true,
      },

      // X-Frame-Options
      frameguard: {
        action: "deny",
      },

      // X-Content-Type-Options
      noSniff: true,

      // X-XSS-Protection
      xssFilter: true,

      // Referrer-Policy
      referrerPolicy: {
        policy: "strict-origin-when-cross-origin",
      },

      // Permissions-Policy (formerly Feature-Policy)
      permittedCrossDomainPolicies: {
        permittedPolicies: "none",
      },
    }),
  );

  // Additional custom headers
  app.use((req, res, next) => {
    // Permissions Policy
    res.setHeader(
      "Permissions-Policy",
      "geolocation=(), microphone=(), camera=(), payment=(), usb=()",
    );

    // Expect-CT
    res.setHeader("Expect-CT", "max-age=86400, enforce");

    // Cross-Origin policies
    res.setHeader("Cross-Origin-Embedder-Policy", "require-corp");
    res.setHeader("Cross-Origin-Opener-Policy", "same-origin");
    res.setHeader("Cross-Origin-Resource-Policy", "same-origin");

    // Remove powered-by header
    res.removeHeader("X-Powered-By");

    next();
  });
}

// CSP Violation Reporter
app.post(
  "/api/csp-report",
  express.json({ type: "application/csp-report" }),
  (req, res) => {
    const report = req.body["csp-report"];

    console.error("CSP Violation:", {
      documentUri: report["document-uri"],
      violatedDirective: report["violated-directive"],
      blockedUri: report["blocked-uri"],
      sourceFile: report["source-file"],
      lineNumber: report["line-number"],
    });

    // Store in database or send to monitoring service
    // monitoringService.logCSPViolation(report);

    res.status(204).end();
  },
);

module.exports = { configureSecurityHeaders };
```
