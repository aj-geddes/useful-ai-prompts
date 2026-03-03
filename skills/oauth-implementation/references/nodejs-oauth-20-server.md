# Node.js OAuth 2.0 Server

## Node.js OAuth 2.0 Server

```javascript
// oauth-server.js - Complete OAuth 2.0 implementation
const express = require("express");
const jwt = require("jsonwebtoken");
const crypto = require("crypto");
const bcrypt = require("bcrypt");

class OAuthServer {
  constructor() {
    this.app = express();
    this.clients = new Map();
    this.authorizationCodes = new Map();
    this.refreshTokens = new Map();
    this.accessTokens = new Map();

    // JWT signing keys
    this.privateKey = process.env.JWT_PRIVATE_KEY;
    this.publicKey = process.env.JWT_PUBLIC_KEY;

    this.setupRoutes();
  }

  // Register OAuth client
  registerClient(clientId, clientSecret, redirectUris) {
    this.clients.set(clientId, {
      clientSecret: bcrypt.hashSync(clientSecret, 10),
      redirectUris,
      grants: ["authorization_code", "refresh_token"],
    });
  }

  setupRoutes() {
    this.app.use(express.json());
    this.app.use(express.urlencoded({ extended: true }));

    // Authorization endpoint
    this.app.get("/oauth/authorize", (req, res) => {
      const { client_id, redirect_uri, response_type, scope, state } =
        req.query;

      // Validate client
      if (!this.clients.has(client_id)) {
        return res.status(400).json({ error: "invalid_client" });
      }

      const client = this.clients.get(client_id);

      // Validate redirect URI
      if (!client.redirectUris.includes(redirect_uri)) {
        return res.status(400).json({ error: "invalid_redirect_uri" });
      }

      // Validate response type
      if (response_type !== "code") {
        return res.status(400).json({ error: "unsupported_response_type" });
      }

      // Generate authorization code
      const code = crypto.randomBytes(32).toString("hex");

      this.authorizationCodes.set(code, {
        clientId: client_id,
        redirectUri: redirect_uri,
        scope: scope || "read",
        userId: req.user?.id, // From session
        expiresAt: Date.now() + 600000, // 10 minutes
      });

      // Redirect with authorization code
      const redirectUrl = new URL(redirect_uri);
      redirectUrl.searchParams.set("code", code);
      if (state) redirectUrl.searchParams.set("state", state);

      res.redirect(redirectUrl.toString());
    });

    // Token endpoint
    this.app.post("/oauth/token", async (req, res) => {
      const {
        grant_type,
        code,
        refresh_token,
        client_id,
        client_secret,
        redirect_uri,
      } = req.body;

      // Validate client credentials
      const client = this.clients.get(client_id);
      if (!client || !bcrypt.compareSync(client_secret, client.clientSecret)) {
        return res.status(401).json({ error: "invalid_client" });
      }

      if (grant_type === "authorization_code") {
        return this.handleAuthorizationCodeGrant(
          req,
          res,
          code,
          client_id,
          redirect_uri,
        );
      } else if (grant_type === "refresh_token") {
        return this.handleRefreshTokenGrant(req, res, refresh_token, client_id);
      }

      res.status(400).json({ error: "unsupported_grant_type" });
    });

    // Token introspection endpoint
    this.app.post("/oauth/introspect", (req, res) => {
      const { token } = req.body;

      try {
        const decoded = jwt.verify(token, this.publicKey, {
          algorithms: ["RS256"],
        });

        res.json({
          active: true,
          scope: decoded.scope,
          client_id: decoded.client_id,
          user_id: decoded.sub,
          exp: decoded.exp,
        });
      } catch (error) {
        res.json({ active: false });
      }
    });

    // Token revocation endpoint
    this.app.post("/oauth/revoke", (req, res) => {
      const { token, token_type_hint } = req.body;

      if (token_type_hint === "refresh_token") {
        this.refreshTokens.delete(token);
      } else {
        this.accessTokens.delete(token);
      }

      res.status(200).json({ success: true });
    });
  }

  handleAuthorizationCodeGrant(req, res, code, clientId, redirectUri) {
    const authCode = this.authorizationCodes.get(code);

    if (!authCode) {
      return res.status(400).json({ error: "invalid_grant" });
    }

    // Validate authorization code
    if (
      authCode.clientId !== clientId ||
      authCode.redirectUri !== redirectUri
    ) {
      return res.status(400).json({ error: "invalid_grant" });
    }

    if (authCode.expiresAt < Date.now()) {
      this.authorizationCodes.delete(code);
      return res.status(400).json({ error: "expired_grant" });
    }

    // Delete used authorization code
    this.authorizationCodes.delete(code);

    // Generate tokens
    const tokens = this.generateTokens(
      clientId,
      authCode.userId,
      authCode.scope,
    );

    res.json(tokens);
  }

  handleRefreshTokenGrant(req, res, refreshToken, clientId) {
    const storedToken = this.refreshTokens.get(refreshToken);

    if (!storedToken || storedToken.clientId !== clientId) {
      return res.status(400).json({ error: "invalid_grant" });
    }

    if (storedToken.expiresAt < Date.now()) {
      this.refreshTokens.delete(refreshToken);
      return res.status(400).json({ error: "expired_refresh_token" });
    }

    // Generate new access token
    const tokens = this.generateTokens(
      clientId,
      storedToken.userId,
      storedToken.scope,
    );

    res.json(tokens);
  }

  generateTokens(clientId, userId, scope) {
    // Generate access token (JWT)
    const accessToken = jwt.sign(
      {
        sub: userId,
        client_id: clientId,
        scope: scope,
        type: "access_token",
      },
      this.privateKey,
      {
        algorithm: "RS256",
        expiresIn: "1h",
        issuer: "https://auth.example.com",
        audience: "https://api.example.com",
      },
    );

    // Generate refresh token
    const refreshToken = crypto.randomBytes(64).toString("hex");

    this.refreshTokens.set(refreshToken, {
      clientId,
      userId,
      scope,
      expiresAt: Date.now() + 2592000000, // 30 days
    });

    return {
      access_token: accessToken,
      token_type: "Bearer",
      expires_in: 3600,
      refresh_token: refreshToken,
      scope: scope,
    };
  }

  // Middleware to protect routes
  authenticate() {
    return (req, res, next) => {
      const authHeader = req.headers.authorization;

      if (!authHeader || !authHeader.startsWith("Bearer ")) {
        return res.status(401).json({ error: "missing_token" });
      }

      const token = authHeader.substring(7);

      try {
        const decoded = jwt.verify(token, this.publicKey, {
          algorithms: ["RS256"],
          issuer: "https://auth.example.com",
          audience: "https://api.example.com",
        });

        req.user = {
          id: decoded.sub,
          clientId: decoded.client_id,
          scope: decoded.scope,
        };

        next();
      } catch (error) {
        if (error.name === "TokenExpiredError") {
          return res.status(401).json({ error: "token_expired" });
        }
        return res.status(401).json({ error: "invalid_token" });
      }
    };
  }

  start(port = 3000) {
    this.app.listen(port, () => {
      console.log(`OAuth server running on port ${port}`);
    });
  }
}

// Usage
const oauthServer = new OAuthServer();

// Register OAuth client
oauthServer.registerClient("client-app-123", "super-secret-key", [
  "https://myapp.com/callback",
]);

// Protected API endpoint
oauthServer.app.get(
  "/api/user/profile",
  oauthServer.authenticate(),
  (req, res) => {
    res.json({
      userId: req.user.id,
      scope: req.user.scope,
    });
  },
);

oauthServer.start(3000);
```
