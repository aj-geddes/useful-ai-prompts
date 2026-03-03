# Node.js/Express JWT Implementation

## Node.js/Express JWT Implementation

```javascript
// Node.js/Express Example
const jwt = require("jsonwebtoken");
const crypto = require("crypto");
const redis = require("redis");

class SessionManager {
  constructor() {
    this.secretKey = process.env.JWT_SECRET || "dev-secret";
    this.algorithm = "HS256";
    this.accessTokenExpiry = "1h";
    this.refreshTokenExpiry = "7d";
    this.redisClient = redis.createClient();
  }

  generateTokens(userId, email, role = "user") {
    const now = new Date();
    const jti = crypto.randomBytes(16).toString("hex");

    const accessToken = jwt.sign(
      {
        userId,
        email,
        role,
        type: "access",
        jti,
        iat: Math.floor(now.getTime() / 1000),
      },
      this.secretKey,
      { algorithm: this.algorithm, expiresIn: this.accessTokenExpiry },
    );

    const refreshToken = jwt.sign(
      {
        userId,
        type: "refresh",
        jti,
        iat: Math.floor(now.getTime() / 1000),
      },
      this.secretKey,
      { algorithm: this.algorithm, expiresIn: this.refreshTokenExpiry },
    );

    return {
      accessToken,
      refreshToken,
      expiresIn: 3600,
      tokenType: "Bearer",
    };
  }

  verifyToken(token, tokenType = "access") {
    try {
      const decoded = jwt.verify(token, this.secretKey, {
        algorithms: [this.algorithm],
      });

      if (decoded.type !== tokenType) {
        return { payload: null, error: "Invalid token type" };
      }

      return { payload: decoded, error: null };
    } catch (err) {
      if (err.name === "TokenExpiredError") {
        return { payload: null, error: "Token expired" };
      }
      return { payload: null, error: "Invalid token" };
    }
  }

  async isTokenBlacklisted(jti) {
    const result = await this.redisClient.get(`blacklist:${jti}`);
    return result !== null;
  }

  async blacklistToken(jti, expiresIn) {
    await this.redisClient.setex(`blacklist:${jti}`, expiresIn, "1");
  }

  async logout(token) {
    const decoded = jwt.decode(token);
    if (decoded && decoded.jti) {
      const expiresIn = decoded.exp - Math.floor(Date.now() / 1000);
      await this.blacklistToken(decoded.jti, expiresIn);
    }
  }

  refreshAccessToken(refreshToken) {
    const { payload, error } = this.verifyToken(refreshToken, "refresh");
    if (error) {
      return { tokens: null, error };
    }

    return {
      tokens: this.generateTokens(payload.userId, payload.email, payload.role),
      error: null,
    };
  }
}

// Middleware
const authMiddleware = (req, res, next) => {
  const authHeader = req.headers["authorization"];
  const token = authHeader && authHeader.split(" ")[1];

  if (!token) {
    return res.status(401).json({ error: "No token provided" });
  }

  const sessionManager = new SessionManager();
  const { payload, error } = sessionManager.verifyToken(token);

  if (error) {
    return res.status(401).json({ error });
  }

  req.user = payload;
  next();
};
```
