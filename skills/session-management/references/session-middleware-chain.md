# Session Middleware Chain

## Session Middleware Chain

```javascript
// Node.js middleware chain
const express = require("express");
const app = express();

// 1. Parse cookies
app.use(express.json());
app.use(cookieParser(process.env.COOKIE_SECRET));

// 2. Session middleware
app.use(
  session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: {
      httpOnly: true,
      secure: process.env.NODE_ENV === "production",
      sameSite: "strict",
      maxAge: 24 * 60 * 60 * 1000,
    },
    store: new RedisStore({ client: redisClient }),
  }),
);

// 3. CSRF protection
const csrfProtection = csrf({ cookie: false });

// 4. Rate limiting per session
const sessionRateLimit = rateLimit({
  store: new RedisStore({ client: redisClient }),
  keyGenerator: (req) => req.sessionID,
  windowMs: 15 * 60 * 1000,
  max: 100,
});

app.use(sessionRateLimit);

// 5. Authentication check
const requireAuth = (req, res, next) => {
  if (!req.session.user) {
    return res.status(401).json({ error: "Unauthorized" });
  }
  req.user = req.session.user;
  next();
};

app.post("/api/login", csrfProtection, async (req, res) => {
  // Verify credentials
  const user = await User.findOne({ email: req.body.email });
  if (user && (await user.verifyPassword(req.body.password))) {
    req.session.user = { id: user.id, email: user.email, role: user.role };
    req.session.regenerate((err) => {
      if (err) return res.status(500).json({ error: "Server error" });
      res.json({ success: true });
    });
  } else {
    res.status(401).json({ error: "Invalid credentials" });
  }
});

app.post("/api/logout", requireAuth, (req, res) => {
  req.session.destroy((err) => {
    if (err) return res.status(500).json({ error: "Logout failed" });
    res.clearCookie("connect.sid");
    res.json({ success: true });
  });
});
```
