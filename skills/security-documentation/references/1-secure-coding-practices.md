# 1 Secure Coding Practices

## 1 Secure Coding Practices

**Input Validation:**

```javascript
// ✅ Good - Validate and sanitize input
const validator = require("validator");

function createUser(req, res) {
  const { email, name } = req.body;

  // Validate email
  if (!validator.isEmail(email)) {
    return res.status(400).json({ error: "Invalid email" });
  }

  // Sanitize name
  const sanitizedName = validator.escape(name);

  // Use parameterized queries
  db.query("INSERT INTO users (email, name) VALUES ($1, $2)", [
    email,
    sanitizedName,
  ]);
}

// ❌ Bad - SQL injection vulnerability
function createUserBad(req, res) {
  const { email, name } = req.body;
  db.query(`INSERT INTO users VALUES ('${email}', '${name}')`);
}
```

**XSS Prevention:**

```javascript
// Content Security Policy headers
app.use((req, res, next) => {
  res.setHeader(
    "Content-Security-Policy",
    "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';",
  );
  next();
});

// Sanitize output
import DOMPurify from "isomorphic-dompurify";

function renderComment(comment) {
  const clean = DOMPurify.sanitize(comment, {
    ALLOWED_TAGS: ["b", "i", "em", "strong"],
    ALLOWED_ATTR: [],
  });
  return clean;
}
```
