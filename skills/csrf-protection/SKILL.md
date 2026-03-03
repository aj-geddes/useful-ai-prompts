---
name: csrf-protection
description: >
  Implement Cross-Site Request Forgery (CSRF) protection using tokens, SameSite
  cookies, and origin validation. Use when building forms and state-changing
  operations.
---

# CSRF Protection

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive Cross-Site Request Forgery protection using synchronizer tokens, double-submit cookies, SameSite cookie attributes, and custom headers.

## When to Use

- Form submissions
- State-changing operations
- Authentication systems
- Payment processing
- Account management
- Any POST/PUT/DELETE requests

## Quick Start

Minimal working example:

```javascript
// csrf-protection.js
const crypto = require("crypto");
const csrf = require("csurf");

class CSRFProtection {
  constructor() {
    this.tokens = new Map();
    this.tokenExpiry = 3600000; // 1 hour
  }

  /**
   * Generate CSRF token
   */
  generateToken() {
    return crypto.randomBytes(32).toString("hex");
  }

  /**
   * Create token for session
   */
  createToken(sessionId) {
    const token = this.generateToken();
    const expiry = Date.now() + this.tokenExpiry;

    this.tokens.set(sessionId, {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Node.js/Express CSRF Protection](references/nodejsexpress-csrf-protection.md) | Node.js/Express CSRF Protection |
| [Double Submit Cookie Pattern](references/double-submit-cookie-pattern.md) | Double Submit Cookie Pattern |
| [Python Flask CSRF Protection](references/python-flask-csrf-protection.md) | Python Flask CSRF Protection |
| [Frontend CSRF Implementation](references/frontend-csrf-implementation.md) | Frontend CSRF Implementation |
| [Origin and Referer Validation](references/origin-and-referer-validation.md) | Origin and Referer Validation |

## Best Practices

### ✅ DO

- Use CSRF tokens for all state-changing operations
- Set SameSite=Strict on cookies
- Validate Origin/Referer headers
- Use secure, random tokens
- Implement token expiration
- Use HTTPS only
- Include tokens in AJAX requests
- Test CSRF protection

### ❌ DON'T

- Skip CSRF for authenticated requests
- Use GET for state changes
- Trust Origin header alone
- Reuse tokens
- Store tokens in localStorage
- Allow credentials in CORS without validation
