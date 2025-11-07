---
name: oauth-implementation
description: Implement secure OAuth 2.0, OpenID Connect (OIDC), JWT authentication, and SSO integration. Use when building secure authentication systems for web and mobile applications.
---

# OAuth Implementation

## Overview

Implement industry-standard OAuth 2.0 and OpenID Connect authentication flows with JWT tokens, refresh tokens, and secure session management.

## When to Use

- User authentication systems
- Third-party API integration
- Single Sign-On (SSO) implementation
- Mobile app authentication
- Microservices security
- Social login integration

## Implementation Examples

### 1. **Node.js OAuth 2.0 Server**

```javascript
// oauth-server.js - Complete OAuth 2.0 implementation
const express = require('express');
const jwt = require('jsonwebtoken');
const crypto = require('crypto');
const bcrypt = require('bcrypt');

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
      grants: ['authorization_code', 'refresh_token']
    });
  }

  setupRoutes() {
    this.app.use(express.json());
    this.app.use(express.urlencoded({ extended: true }));

    // Authorization endpoint
    this.app.get('/oauth/authorize', (req, res) => {
      const { client_id, redirect_uri, response_type, scope, state } = req.query;

      // Validate client
      if (!this.clients.has(client_id)) {
        return res.status(400).json({ error: 'invalid_client' });
      }

      const client = this.clients.get(client_id);

      // Validate redirect URI
      if (!client.redirectUris.includes(redirect_uri)) {
        return res.status(400).json({ error: 'invalid_redirect_uri' });
      }

      // Validate response type
      if (response_type !== 'code') {
        return res.status(400).json({ error: 'unsupported_response_type' });
      }

      // Generate authorization code
      const code = crypto.randomBytes(32).toString('hex');

      this.authorizationCodes.set(code, {
        clientId: client_id,
        redirectUri: redirect_uri,
        scope: scope || 'read',
        userId: req.user?.id, // From session
        expiresAt: Date.now() + 600000 // 10 minutes
      });

      // Redirect with authorization code
      const redirectUrl = new URL(redirect_uri);
      redirectUrl.searchParams.set('code', code);
      if (state) redirectUrl.searchParams.set('state', state);

      res.redirect(redirectUrl.toString());
    });

    // Token endpoint
    this.app.post('/oauth/token', async (req, res) => {
      const { grant_type, code, refresh_token, client_id, client_secret, redirect_uri } = req.body;

      // Validate client credentials
      const client = this.clients.get(client_id);
      if (!client || !bcrypt.compareSync(client_secret, client.clientSecret)) {
        return res.status(401).json({ error: 'invalid_client' });
      }

      if (grant_type === 'authorization_code') {
        return this.handleAuthorizationCodeGrant(req, res, code, client_id, redirect_uri);
      } else if (grant_type === 'refresh_token') {
        return this.handleRefreshTokenGrant(req, res, refresh_token, client_id);
      }

      res.status(400).json({ error: 'unsupported_grant_type' });
    });

    // Token introspection endpoint
    this.app.post('/oauth/introspect', (req, res) => {
      const { token } = req.body;

      try {
        const decoded = jwt.verify(token, this.publicKey, { algorithms: ['RS256'] });

        res.json({
          active: true,
          scope: decoded.scope,
          client_id: decoded.client_id,
          user_id: decoded.sub,
          exp: decoded.exp
        });
      } catch (error) {
        res.json({ active: false });
      }
    });

    // Token revocation endpoint
    this.app.post('/oauth/revoke', (req, res) => {
      const { token, token_type_hint } = req.body;

      if (token_type_hint === 'refresh_token') {
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
      return res.status(400).json({ error: 'invalid_grant' });
    }

    // Validate authorization code
    if (authCode.clientId !== clientId || authCode.redirectUri !== redirectUri) {
      return res.status(400).json({ error: 'invalid_grant' });
    }

    if (authCode.expiresAt < Date.now()) {
      this.authorizationCodes.delete(code);
      return res.status(400).json({ error: 'expired_grant' });
    }

    // Delete used authorization code
    this.authorizationCodes.delete(code);

    // Generate tokens
    const tokens = this.generateTokens(clientId, authCode.userId, authCode.scope);

    res.json(tokens);
  }

  handleRefreshTokenGrant(req, res, refreshToken, clientId) {
    const storedToken = this.refreshTokens.get(refreshToken);

    if (!storedToken || storedToken.clientId !== clientId) {
      return res.status(400).json({ error: 'invalid_grant' });
    }

    if (storedToken.expiresAt < Date.now()) {
      this.refreshTokens.delete(refreshToken);
      return res.status(400).json({ error: 'expired_refresh_token' });
    }

    // Generate new access token
    const tokens = this.generateTokens(clientId, storedToken.userId, storedToken.scope);

    res.json(tokens);
  }

  generateTokens(clientId, userId, scope) {
    // Generate access token (JWT)
    const accessToken = jwt.sign(
      {
        sub: userId,
        client_id: clientId,
        scope: scope,
        type: 'access_token'
      },
      this.privateKey,
      {
        algorithm: 'RS256',
        expiresIn: '1h',
        issuer: 'https://auth.example.com',
        audience: 'https://api.example.com'
      }
    );

    // Generate refresh token
    const refreshToken = crypto.randomBytes(64).toString('hex');

    this.refreshTokens.set(refreshToken, {
      clientId,
      userId,
      scope,
      expiresAt: Date.now() + 2592000000 // 30 days
    });

    return {
      access_token: accessToken,
      token_type: 'Bearer',
      expires_in: 3600,
      refresh_token: refreshToken,
      scope: scope
    };
  }

  // Middleware to protect routes
  authenticate() {
    return (req, res, next) => {
      const authHeader = req.headers.authorization;

      if (!authHeader || !authHeader.startsWith('Bearer ')) {
        return res.status(401).json({ error: 'missing_token' });
      }

      const token = authHeader.substring(7);

      try {
        const decoded = jwt.verify(token, this.publicKey, {
          algorithms: ['RS256'],
          issuer: 'https://auth.example.com',
          audience: 'https://api.example.com'
        });

        req.user = {
          id: decoded.sub,
          clientId: decoded.client_id,
          scope: decoded.scope
        };

        next();
      } catch (error) {
        if (error.name === 'TokenExpiredError') {
          return res.status(401).json({ error: 'token_expired' });
        }
        return res.status(401).json({ error: 'invalid_token' });
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
oauthServer.registerClient(
  'client-app-123',
  'super-secret-key',
  ['https://myapp.com/callback']
);

// Protected API endpoint
oauthServer.app.get('/api/user/profile',
  oauthServer.authenticate(),
  (req, res) => {
    res.json({
      userId: req.user.id,
      scope: req.user.scope
    });
  }
);

oauthServer.start(3000);
```

### 2. **Python OpenID Connect Implementation**

```python
# oidc_provider.py
from flask import Flask, request, jsonify, redirect
from authlib.integrations.flask_oauth2 import AuthorizationServer
from authlib.integrations.flask_oauth2 import ResourceProtector
from authlib.oauth2.rfc6749 import grants
from authlib.jose import jwt
import secrets
import time
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)

class OIDCProvider:
    def __init__(self):
        self.clients = {}
        self.authorization_codes = {}
        self.access_tokens = {}
        self.id_tokens = {}

        # RSA keys for JWT signing
        self.private_key = self._load_private_key()
        self.public_key = self._load_public_key()

    def _load_private_key(self):
        # Load from environment or key management service
        return """-----BEGIN RSA PRIVATE KEY-----
        ... Your private key ...
        -----END RSA PRIVATE KEY-----"""

    def _load_public_key(self):
        return """-----BEGIN PUBLIC KEY-----
        ... Your public key ...
        -----END PUBLIC KEY-----"""

    def register_client(self, client_id, client_secret, redirect_uris, scopes):
        """Register OIDC client"""
        self.clients[client_id] = {
            'client_secret': client_secret,
            'redirect_uris': redirect_uris,
            'scopes': scopes,
            'response_types': ['code', 'id_token', 'token']
        }

    def generate_id_token(self, user_id, client_id, nonce=None):
        """Generate OpenID Connect ID Token"""
        now = int(time.time())

        payload = {
            'iss': 'https://auth.example.com',
            'sub': user_id,
            'aud': client_id,
            'exp': now + 3600,
            'iat': now,
            'auth_time': now,
            'nonce': nonce
        }

        # Add optional claims
        payload.update({
            'email': f'{user_id}@example.com',
            'email_verified': True,
            'name': 'John Doe',
            'given_name': 'John',
            'family_name': 'Doe',
            'picture': 'https://example.com/avatar.jpg'
        })

        header = {'alg': 'RS256', 'typ': 'JWT'}

        return jwt.encode(header, payload, self.private_key)

    def generate_access_token(self, user_id, client_id, scope):
        """Generate OAuth 2.0 access token"""
        token = secrets.token_urlsafe(32)

        self.access_tokens[token] = {
            'user_id': user_id,
            'client_id': client_id,
            'scope': scope,
            'expires_at': datetime.now() + timedelta(hours=1)
        }

        return token

    def verify_token(self, token):
        """Verify JWT token"""
        try:
            claims = jwt.decode(token, self.public_key)
            claims.validate()
            return claims
        except Exception as e:
            return None

# OIDC Endpoints
provider = OIDCProvider()

@app.route('/.well-known/openid-configuration')
def openid_configuration():
    """OpenID Connect Discovery endpoint"""
    return jsonify({
        'issuer': 'https://auth.example.com',
        'authorization_endpoint': 'https://auth.example.com/oauth/authorize',
        'token_endpoint': 'https://auth.example.com/oauth/token',
        'userinfo_endpoint': 'https://auth.example.com/oauth/userinfo',
        'jwks_uri': 'https://auth.example.com/.well-known/jwks.json',
        'response_types_supported': ['code', 'id_token', 'token id_token'],
        'subject_types_supported': ['public'],
        'id_token_signing_alg_values_supported': ['RS256'],
        'scopes_supported': ['openid', 'profile', 'email'],
        'token_endpoint_auth_methods_supported': ['client_secret_basic', 'client_secret_post'],
        'claims_supported': ['sub', 'iss', 'aud', 'exp', 'iat', 'name', 'email']
    })

@app.route('/.well-known/jwks.json')
def jwks():
    """JSON Web Key Set endpoint"""
    # Return public key in JWK format
    return jsonify({
        'keys': [
            {
                'kty': 'RSA',
                'use': 'sig',
                'kid': '1',
                'n': '...',  # Public key modulus
                'e': 'AQAB'
            }
        ]
    })

@app.route('/oauth/userinfo')
def userinfo():
    """UserInfo endpoint"""
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'invalid_token'}), 401

    token = auth_header[7:]
    claims = provider.verify_token(token)

    if not claims:
        return jsonify({'error': 'invalid_token'}), 401

    return jsonify({
        'sub': claims['sub'],
        'email': claims.get('email'),
        'name': claims.get('name'),
        'picture': claims.get('picture')
    })

# Register sample client
provider.register_client(
    'sample-app',
    'secret123',
    ['https://myapp.com/callback'],
    ['openid', 'profile', 'email']
)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
```

### 3. **Java Spring Security OAuth**

```java
// OAuth2AuthorizationServerConfig.java
package com.example.oauth;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.oauth2.config.annotation.configurers.ClientDetailsServiceConfigurer;
import org.springframework.security.oauth2.config.annotation.web.configuration.AuthorizationServerConfigurerAdapter;
import org.springframework.security.oauth2.config.annotation.web.configuration.EnableAuthorizationServer;
import org.springframework.security.oauth2.config.annotation.web.configurers.AuthorizationServerEndpointsConfigurer;
import org.springframework.security.oauth2.provider.token.TokenStore;
import org.springframework.security.oauth2.provider.token.store.JwtAccessTokenConverter;
import org.springframework.security.oauth2.provider.token.store.JwtTokenStore;

@Configuration
@EnableAuthorizationServer
public class OAuth2AuthorizationServerConfig extends AuthorizationServerConfigurerAdapter {

    @Override
    public void configure(ClientDetailsServiceConfigurer clients) throws Exception {
        clients.inMemory()
            .withClient("client-app")
                .secret("{bcrypt}$2a$10$...")
                .authorizedGrantTypes("authorization_code", "refresh_token")
                .scopes("read", "write")
                .redirectUris("https://myapp.com/callback")
                .accessTokenValiditySeconds(3600)
                .refreshTokenValiditySeconds(86400)
            .and()
            .withClient("mobile-app")
                .secret("{bcrypt}$2a$10$...")
                .authorizedGrantTypes("password", "refresh_token")
                .scopes("read")
                .accessTokenValiditySeconds(7200);
    }

    @Override
    public void configure(AuthorizationServerEndpointsConfigurer endpoints) {
        endpoints
            .tokenStore(tokenStore())
            .accessTokenConverter(accessTokenConverter());
    }

    @Bean
    public TokenStore tokenStore() {
        return new JwtTokenStore(accessTokenConverter());
    }

    @Bean
    public JwtAccessTokenConverter accessTokenConverter() {
        JwtAccessTokenConverter converter = new JwtAccessTokenConverter();
        converter.setSigningKey("secret-key"); // Use proper key management
        return converter;
    }
}
```

## Best Practices

### ✅ DO
- Use PKCE for public clients
- Implement token rotation
- Store tokens securely
- Use HTTPS everywhere
- Validate redirect URIs
- Implement rate limiting
- Use short-lived access tokens
- Log authentication events

### ❌ DON'T
- Store tokens in localStorage
- Use implicit flow
- Skip state parameter
- Expose client secrets
- Allow open redirects
- Use weak signing keys

## OAuth 2.0 Flows

- **Authorization Code**: Web applications
- **PKCE**: Mobile and SPA apps
- **Client Credentials**: Service-to-service
- **Refresh Token**: Token renewal

## Resources

- [OAuth 2.0 RFC 6749](https://tools.ietf.org/html/rfc6749)
- [OpenID Connect Spec](https://openid.net/specs/openid-connect-core-1_0.html)
- [JWT.io](https://jwt.io/)
- [OAuth 2.0 Security Best Practices](https://tools.ietf.org/html/draft-ietf-oauth-security-topics)
