---
name: api-security-hardening
description: >
  Secure REST APIs with authentication, rate limiting, CORS, input validation,
  and security middleware. Use when building or hardening API endpoints against
  common attacks.
---

# API Security Hardening

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive API security measures including authentication, authorization, rate limiting, input validation, and attack prevention to protect against common vulnerabilities.

## When to Use

- New API development
- Security audit remediation
- Production API hardening
- Compliance requirements
- High-traffic API protection
- Public API exposure

## Quick Start

Minimal working example:

```javascript
// secure-api.js - Comprehensive API security
const express = require("express");
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");
const mongoSanitize = require("express-mongo-sanitize");
const xss = require("xss-clean");
const hpp = require("hpp");
const cors = require("cors");
const jwt = require("jsonwebtoken");
const validator = require("validator");

class SecureAPIServer {
  constructor() {
    this.app = express();
    this.setupSecurityMiddleware();
    this.setupRoutes();
  }

  setupSecurityMiddleware() {
    // 1. Helmet - Set security headers
    this.app.use(
      helmet({
        contentSecurityPolicy: {
          directives: {
            defaultSrc: ["'self'"],
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Node.js/Express API Security](references/nodejsexpress-api-security.md) | Node.js/Express API Security |
| [Python FastAPI Security](references/python-fastapi-security.md) | Python FastAPI Security |
| [API Gateway Security Configuration](references/api-gateway-security-configuration.md) | API Gateway Security Configuration |

## Best Practices

### ✅ DO

- Use HTTPS everywhere
- Implement rate limiting
- Validate all inputs
- Use security headers
- Log security events
- Implement CORS properly
- Use strong authentication
- Version your APIs

### ❌ DON'T

- Expose stack traces
- Return detailed errors
- Trust user input
- Use HTTP for APIs
- Skip input validation
- Ignore rate limiting
