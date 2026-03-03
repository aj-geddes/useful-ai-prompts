# API Gateway Pattern

## API Gateway Pattern

```typescript
// api-gateway/src/gateway.ts
import express from "express";
import httpProxy from "http-proxy-middleware";
import jwt from "jsonwebtoken";
import rateLimit from "express-rate-limit";

const app = express();

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100,
});

app.use(limiter);

// Authentication middleware
const authenticateToken = (req, res, next) => {
  const token = req.headers["authorization"]?.split(" ")[1];
  if (!token) return res.sendStatus(401);

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};

// Route to services
app.use(
  "/api/users",
  authenticateToken,
  httpProxy.createProxyMiddleware({
    target: "http://user-service:3000",
    changeOrigin: true,
    pathRewrite: { "^/api/users": "/users" },
  }),
);

app.use(
  "/api/orders",
  authenticateToken,
  httpProxy.createProxyMiddleware({
    target: "http://order-service:3000",
    changeOrigin: true,
    pathRewrite: { "^/api/orders": "/orders" },
  }),
);

app.use(
  "/api/products",
  httpProxy.createProxyMiddleware({
    target: "http://product-service:3000",
    changeOrigin: true,
    pathRewrite: { "^/api/products": "/products" },
  }),
);

// Aggregation endpoint
app.get("/api/order-details/:orderId", authenticateToken, async (req, res) => {
  const orderId = req.params.orderId;

  // Parallel requests to multiple services
  const [order, user, products] = await Promise.all([
    fetch(`http://order-service:3000/orders/${orderId}`).then((r) => r.json()),
    fetch(`http://user-service:3000/users/${req.user.id}`).then((r) =>
      r.json(),
    ),
    fetch(`http://product-service:3000/products?ids=${order.itemIds}`).then(
      (r) => r.json(),
    ),
  ]);

  res.json({ order, user, products });
});
```
