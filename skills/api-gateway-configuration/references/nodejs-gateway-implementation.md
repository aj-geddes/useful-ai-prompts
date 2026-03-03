# Node.js Gateway Implementation

## Node.js Gateway Implementation

```javascript
const express = require("express");
const httpProxy = require("express-http-proxy");
const rateLimit = require("express-rate-limit");
const jwt = require("jsonwebtoken");

const app = express();

// Rate limiting
const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: 100,
});

// JWT verification
const verifyJwt = (req, res, next) => {
  const token = req.headers["authorization"]?.split(" ")[1];
  if (!token) return res.status(401).json({ error: "No token" });

  try {
    jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch (err) {
    res.status(403).json({ error: "Invalid token" });
  }
};

// Request logging
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} ${req.method} ${req.path}`);
  next();
});

app.use(limiter);

// User service proxy
app.use(
  "/api/users",
  verifyJwt,
  httpProxy("http://user-service:3000", {
    proxyReqPathResolver: (req) => `/api/users${req.url}`,
    userResDecorator: (proxyRes, proxyResData, userReq, userRes) => {
      proxyRes.headers["X-Gateway"] = "true";
      return proxyResData;
    },
  }),
);

// Product service proxy
app.use(
  "/api/products",
  httpProxy("http://product-service:3001", {
    proxyReqPathResolver: (req) => `/api/products${req.url}`,
  }),
);

// Health check
app.get("/health", (req, res) => res.json({ status: "ok" }));

app.listen(8080, () => console.log("Gateway on port 8080"));
```
