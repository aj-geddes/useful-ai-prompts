---
name: session-management
description: >
  Implement secure session management systems with JWT tokens, session storage,
  token refresh, logout handling, and CSRF protection. Use when managing user
  authentication state, handling token lifecycle, and securing sessions.
---

# Session Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive session management systems with secure token handling, session persistence, token refresh mechanisms, proper logout procedures, and CSRF protection across different backend frameworks.

## When to Use

- Implementing user authentication systems
- Managing session state and user context
- Handling JWT token refresh cycles
- Implementing logout functionality
- Protecting against CSRF attacks
- Managing session expiration and cleanup

## Quick Start

Minimal working example:

```python
# Python/Flask Example
from flask import current_app
from datetime import datetime, timedelta
import jwt
import os

class TokenManager:
    def __init__(self, secret_key=None):
        self.secret_key = secret_key or os.getenv('JWT_SECRET')
        self.algorithm = 'HS256'
        self.access_token_expires_hours = 1
        self.refresh_token_expires_days = 7

    def generate_tokens(self, user_id, email, role='user'):
        """Generate both access and refresh tokens"""
        now = datetime.utcnow()

        # Access token
        access_payload = {
            'user_id': user_id,
            'email': email,
            'role': role,
            'type': 'access',
            'iat': now,
            'exp': now + timedelta(hours=self.access_token_expires_hours)
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [JWT Token Generation and Validation](references/jwt-token-generation-and-validation.md) | JWT Token Generation and Validation |
| [Node.js/Express JWT Implementation](references/nodejsexpress-jwt-implementation.md) | Node.js/Express JWT Implementation |
| [Session Storage with Redis](references/session-storage-with-redis.md) | Session Storage with Redis |
| [CSRF Protection](references/csrf-protection.md) | CSRF Protection |
| [Session Middleware Chain](references/session-middleware-chain.md) | Session Middleware Chain |
| [Token Refresh Endpoint](references/token-refresh-endpoint.md) | Token Refresh Endpoint |
| [Session Cleanup and Maintenance](references/session-cleanup-and-maintenance.md) | Session Cleanup and Maintenance |

## Best Practices

### ✅ DO

- Use HTTPS for all session transmission
- Implement secure cookies (httpOnly, sameSite, secure flags)
- Use JWT with proper expiration times
- Implement token refresh mechanism
- Store refresh tokens securely
- Validate tokens on every request
- Use strong secret keys
- Implement session timeout
- Log authentication events
- Clear session data on logout
- Use CSRF tokens for state-changing requests

### ❌ DON'T

- Store sensitive data in tokens
- Use short secret keys
- Transmit tokens in URLs
- Ignore token expiration
- Reuse token secrets across environments
- Store tokens in localStorage (use httpOnly cookies)
- Implement session without HTTPS
- Forget to validate token signatures
- Expose session IDs in logs
- Use predictable session IDs
