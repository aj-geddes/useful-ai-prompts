---
name: security-headers-configuration
description: >
  Configure HTTP security headers including CSP, HSTS, X-Frame-Options, and XSS
  protection. Use when hardening web applications against common attacks.
---

# Security Headers Configuration

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive HTTP security headers to protect web applications from XSS, clickjacking, MIME sniffing, and other browser-based attacks.

## When to Use

- New web application deployment
- Security audit remediation
- Compliance requirements
- Browser security hardening
- API security
- Static site protection

## Quick Start

Minimal working example:

```javascript
// security-headers.js
const helmet = require("helmet");

function configureSecurityHeaders(app) {
  // Comprehensive Helmet configuration
  app.use(
    helmet({
      // Content Security Policy
      contentSecurityPolicy: {
        directives: {
          defaultSrc: ["'self'"],
          scriptSrc: [
            "'self'",
            "'unsafe-inline'", // Remove in production
            "https://cdn.example.com",
            "https://www.google-analytics.com",
          ],
          styleSrc: [
            "'self'",
            "'unsafe-inline'",
            "https://fonts.googleapis.com",
          ],
          fontSrc: ["'self'", "https://fonts.gstatic.com"],
          imgSrc: ["'self'", "data:", "https:", "blob:"],
          connectSrc: ["'self'", "https://api.example.com"],
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Node.js/Express Security Headers](references/nodejsexpress-security-headers.md) | Node.js/Express Security Headers |
| [Nginx Security Headers Configuration](references/nginx-security-headers-configuration.md) | Nginx Security Headers Configuration |
| [Python Flask Security Headers](references/python-flask-security-headers.md) | Python Flask Security Headers |
| [Apache .htaccess Configuration](references/apache-htaccess-configuration.md) | Apache .htaccess Configuration |
| [Security Headers Testing Script](references/security-headers-testing-script.md) | Security Headers Testing Script |

## Best Practices

### ✅ DO

- Use HTTPS everywhere
- Implement strict CSP
- Enable HSTS with preload
- Block framing with X-Frame-Options
- Prevent MIME sniffing
- Report CSP violations
- Test headers regularly
- Use security scanners

### ❌ DON'T

- Allow unsafe-inline in CSP
- Skip HSTS on subdomains
- Ignore CSP violations
- Use overly permissive policies
- Forget to test changes
