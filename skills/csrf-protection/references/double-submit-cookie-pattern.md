# Double Submit Cookie Pattern

## Double Submit Cookie Pattern

```javascript
// double-submit-csrf.js
const crypto = require("crypto");

class DoubleSubmitCSRF {
  /**
   * Generate CSRF token and set cookie
   */
  static generateAndSetToken(res) {
    const token = crypto.randomBytes(32).toString("hex");

    // Set CSRF cookie
    res.cookie("XSRF-TOKEN", token, {
      httpOnly: false, // Allow JS to read for double submit
      secure: true,
      sameSite: "strict",
      maxAge: 3600000,
    });

    return token;
  }

  /**
   * Middleware to validate double submit
   */
  static middleware() {
    return (req, res, next) => {
      // Skip GET, HEAD, OPTIONS
      if (["GET", "HEAD", "OPTIONS"].includes(req.method)) {
        return next();
      }

      const cookieToken = req.cookies["XSRF-TOKEN"];
      const headerToken = req.headers["x-xsrf-token"];

      if (!cookieToken || !headerToken) {
        return res.status(403).json({
          error: "csrf_token_missing",
        });
      }

      // Compare tokens (timing-safe)
      if (
        !crypto.timingSafeEqual(
          Buffer.from(cookieToken),
          Buffer.from(headerToken),
        )
      ) {
        return res.status(403).json({
          error: "csrf_token_mismatch",
        });
      }

      next();
    };
  }
}

// Express setup
const app = express();
const cookieParser = require("cookie-parser");

app.use(cookieParser());
app.use(express.json());

// Generate token on login
app.post("/api/login", async (req, res) => {
  // Authenticate user
  const token = DoubleSubmitCSRF.generateAndSetToken(res);

  res.json({
    message: "Login successful",
    csrfToken: token,
  });
});

// Protected routes
app.use("/api/*", DoubleSubmitCSRF.middleware());

app.post("/api/update-profile", (req, res) => {
  // Update profile
  res.json({ message: "Profile updated" });
});
```
