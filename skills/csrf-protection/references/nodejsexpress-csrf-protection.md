# Node.js/Express CSRF Protection

## Node.js/Express CSRF Protection

```javascript
// csrf-protection.js
const crypto = require("crypto");
const csrf = require("csurf");

class CSRFProtection {
  constructor() {
    this.tokens = new Map();
    this.tokenExpiry = 3600000; // 1 hour
  }

  /**
   * Generate CSRF token
   */
  generateToken() {
    return crypto.randomBytes(32).toString("hex");
  }

  /**
   * Create token for session
   */
  createToken(sessionId) {
    const token = this.generateToken();
    const expiry = Date.now() + this.tokenExpiry;

    this.tokens.set(sessionId, {
      token,
      expiry,
    });

    return token;
  }

  /**
   * Validate CSRF token
   */
  validateToken(sessionId, token) {
    const stored = this.tokens.get(sessionId);

    if (!stored) {
      return false;
    }

    if (Date.now() > stored.expiry) {
      this.tokens.delete(sessionId);
      return false;
    }

    return crypto.timingSafeEqual(
      Buffer.from(stored.token),
      Buffer.from(token),
    );
  }

  /**
   * Express middleware
   */
  middleware() {
    return (req, res, next) => {
      // Skip GET, HEAD, OPTIONS
      if (["GET", "HEAD", "OPTIONS"].includes(req.method)) {
        return next();
      }

      const token = req.headers["x-csrf-token"] || req.body._csrf;
      const sessionId = req.session?.id;

      if (!token) {
        return res.status(403).json({
          error: "csrf_token_missing",
          message: "CSRF token is required",
        });
      }

      if (!this.validateToken(sessionId, token)) {
        return res.status(403).json({
          error: "csrf_token_invalid",
          message: "Invalid or expired CSRF token",
        });
      }

      next();
    };
  }
}

// Express setup with csurf package
const express = require("express");
const session = require("express-session");
const cookieParser = require("cookie-parser");

const app = express();

// Session configuration
app.use(cookieParser());
app.use(
  session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: {
      httpOnly: true,
      secure: true,
      sameSite: "strict",
      maxAge: 3600000,
    },
  }),
);

// CSRF protection middleware
const csrfProtection = csrf({
  cookie: {
    httpOnly: true,
    secure: true,
    sameSite: "strict",
  },
});

app.use(csrfProtection);

// Provide token to templates
app.use((req, res, next) => {
  res.locals.csrfToken = req.csrfToken();
  next();
});

// API endpoint to get CSRF token
app.get("/api/csrf-token", (req, res) => {
  res.json({
    csrfToken: req.csrfToken(),
  });
});

// Protected route
app.post("/api/transfer", csrfProtection, (req, res) => {
  const { amount, toAccount } = req.body;

  // Process transfer
  res.json({
    message: "Transfer successful",
    amount,
    toAccount,
  });
});

// Error handler for CSRF errors
app.use((err, req, res, next) => {
  if (err.code === "EBADCSRFTOKEN") {
    return res.status(403).json({
      error: "csrf_error",
      message: "Invalid CSRF token",
    });
  }

  next(err);
});

module.exports = { CSRFProtection, csrfProtection };
```
