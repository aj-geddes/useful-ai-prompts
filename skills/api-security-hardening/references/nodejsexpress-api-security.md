# Node.js/Express API Security

## Node.js/Express API Security

```javascript
// secure-api.js - Comprehensive API security
const express = require("express");
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");
const mongoSanitize = require("express-mongo-sanitize");
const xss = require("xss-clean");
const hpp = require("hpp");
const cors = require("cors");
const jwt = require("jsonwebtoken");
const validator = require("validator");

class SecureAPIServer {
  constructor() {
    this.app = express();
    this.setupSecurityMiddleware();
    this.setupRoutes();
  }

  setupSecurityMiddleware() {
    // 1. Helmet - Set security headers
    this.app.use(
      helmet({
        contentSecurityPolicy: {
          directives: {
            defaultSrc: ["'self'"],
            styleSrc: ["'self'", "'unsafe-inline'"],
            scriptSrc: ["'self'"],
            imgSrc: ["'self'", "data:", "https:"],
          },
        },
        hsts: {
          maxAge: 31536000,
          includeSubDomains: true,
          preload: true,
        },
      }),
    );

    // 2. CORS configuration
    const corsOptions = {
      origin: (origin, callback) => {
        const whitelist = ["https://example.com", "https://app.example.com"];

        if (!origin || whitelist.includes(origin)) {
          callback(null, true);
        } else {
          callback(new Error("Not allowed by CORS"));
        }
      },
      credentials: true,
      optionsSuccessStatus: 200,
      methods: ["GET", "POST", "PUT", "DELETE"],
      allowedHeaders: ["Content-Type", "Authorization"],
    };

    this.app.use(cors(corsOptions));

    // 3. Rate limiting
    const generalLimiter = rateLimit({
      windowMs: 15 * 60 * 1000, // 15 minutes
      max: 100, // limit each IP to 100 requests per windowMs
      message: "Too many requests from this IP",
      standardHeaders: true,
      legacyHeaders: false,
      handler: (req, res) => {
        res.status(429).json({
          error: "rate_limit_exceeded",
          message: "Too many requests, please try again later",
          retryAfter: req.rateLimit.resetTime,
        });
      },
    });

    const authLimiter = rateLimit({
      windowMs: 15 * 60 * 1000,
      max: 5, // Stricter limit for auth endpoints
      skipSuccessfulRequests: true,
    });

    this.app.use("/api/", generalLimiter);
    this.app.use("/api/auth/", authLimiter);

    // 4. Body parsing with size limits
    this.app.use(express.json({ limit: "10kb" }));
    this.app.use(express.urlencoded({ extended: true, limit: "10kb" }));

    // 5. NoSQL injection prevention
    this.app.use(mongoSanitize());

    // 6. XSS protection
    this.app.use(xss());

    // 7. HTTP Parameter Pollution prevention
    this.app.use(hpp());

    // 8. Request ID for tracking
    this.app.use((req, res, next) => {
      req.id = require("crypto").randomUUID();
      res.setHeader("X-Request-ID", req.id);
      next();
    });

    // 9. Security logging
    this.app.use(this.securityLogger());
  }

  securityLogger() {
    return (req, res, next) => {
      const startTime = Date.now();

      res.on("finish", () => {
        const duration = Date.now() - startTime;

        const logEntry = {
          timestamp: new Date().toISOString(),
          requestId: req.id,
          method: req.method,
          path: req.path,
          statusCode: res.statusCode,
          duration,
          ip: req.ip,
          userAgent: req.get("user-agent"),
        };

        // Log suspicious activity
        if (res.statusCode === 401 || res.statusCode === 403) {
          console.warn("Security event:", logEntry);
        }

        if (res.statusCode >= 500) {
          console.error("Server error:", logEntry);
        }
      });

      next();
    };
  }

  // JWT authentication middleware
  authenticateJWT() {
    return (req, res, next) => {
      const authHeader = req.headers.authorization;

      if (!authHeader || !authHeader.startsWith("Bearer ")) {
        return res.status(401).json({
          error: "unauthorized",
          message: "Missing or invalid authorization header",
        });
      }

      const token = authHeader.substring(7);

      try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET, {
          algorithms: ["HS256"],
          issuer: "api.example.com",
          audience: "api.example.com",
        });

        req.user = decoded;
        next();
      } catch (error) {
        if (error.name === "TokenExpiredError") {
          return res.status(401).json({
            error: "token_expired",
            message: "Token has expired",
          });
        }

        return res.status(401).json({
          error: "invalid_token",
          message: "Invalid token",
        });
      }
    };
  }

  // Input validation middleware
  validateInput(schema) {
    return (req, res, next) => {
      const errors = [];

      // Validate request body
      if (schema.body) {
        for (const [field, rules] of Object.entries(schema.body)) {
          const value = req.body[field];

          if (rules.required && !value) {
            errors.push(`${field} is required`);
            continue;
          }

          if (value) {
            // Type validation
            if (rules.type === "email" && !validator.isEmail(value)) {
              errors.push(`${field} must be a valid email`);
            }

            if (rules.type === "uuid" && !validator.isUUID(value)) {
              errors.push(`${field} must be a valid UUID`);
            }

            if (rules.type === "url" && !validator.isURL(value)) {
              errors.push(`${field} must be a valid URL`);
            }

            // Length validation
            if (rules.minLength && value.length < rules.minLength) {
              errors.push(
                `${field} must be at least ${rules.minLength} characters`,
              );
            }

            if (rules.maxLength && value.length > rules.maxLength) {
              errors.push(
                `${field} must be at most ${rules.maxLength} characters`,
              );
            }

            // Pattern validation
            if (rules.pattern && !rules.pattern.test(value)) {
              errors.push(`${field} format is invalid`);
            }
          }
        }
      }

      if (errors.length > 0) {
        return res.status(400).json({
          error: "validation_error",
          message: "Input validation failed",
          details: errors,
        });
      }

      next();
    };
  }

  // Authorization middleware
  authorize(...roles) {
    return (req, res, next) => {
      if (!req.user) {
        return res.status(401).json({
          error: "unauthorized",
          message: "Authentication required",
        });
      }

      if (roles.length > 0 && !roles.includes(req.user.role)) {
        return res.status(403).json({
          error: "forbidden",
          message: "Insufficient permissions",
        });
      }

      next();
    };
  }

  setupRoutes() {
    // Public endpoint
    this.app.get("/api/health", (req, res) => {
      res.json({ status: "healthy" });
    });

    // Protected endpoint with validation
    this.app.post(
      "/api/users",
      this.authenticateJWT(),
      this.authorize("admin"),
      this.validateInput({
        body: {
          email: { required: true, type: "email" },
          name: { required: true, minLength: 2, maxLength: 100 },
          password: { required: true, minLength: 8 },
        },
      }),
      async (req, res) => {
        try {
          // Sanitized and validated input
          const { email, name, password } = req.body;

          // Process request
          res.status(201).json({
            message: "User created successfully",
            userId: "123",
          });
        } catch (error) {
          res.status(500).json({
            error: "internal_error",
            message: "An error occurred",
          });
        }
      },
    );

    // Error handling middleware
    this.app.use((err, req, res, next) => {
      console.error("Unhandled error:", err);

      res.status(500).json({
        error: "internal_error",
        message: "An unexpected error occurred",
        requestId: req.id,
      });
    });
  }

  start(port = 3000) {
    this.app.listen(port, () => {
      console.log(`Secure API server running on port ${port}`);
    });
  }
}

// Usage
const server = new SecureAPIServer();
server.start(3000);
```
