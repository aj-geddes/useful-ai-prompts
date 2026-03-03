---
name: secrets-rotation
description: >
  Implement automated secrets rotation for API keys, credentials, certificates,
  and encryption keys. Use when managing secrets lifecycle, compliance
  requirements, or security hardening.
---

# Secrets Rotation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement automated secrets rotation strategy for credentials, API keys, certificates, and encryption keys with zero-downtime deployment and comprehensive audit logging.

## When to Use

- API key management
- Database credentials
- TLS/SSL certificates
- Encryption key rotation
- Compliance requirements
- Security incident response
- Service account management

## Quick Start

Minimal working example:

```javascript
// secrets-manager.js
const AWS = require("aws-sdk");
const crypto = require("crypto");

class SecretsManager {
  constructor() {
    this.secretsManager = new AWS.SecretsManager({
      region: process.env.AWS_REGION,
    });

    this.rotationSchedule = new Map();
  }

  /**
   * Generate new secret value
   */
  generateSecret(type = "api_key", length = 32) {
    switch (type) {
      case "api_key":
        return crypto.randomBytes(length).toString("hex");

      case "password":
        // Generate strong password
        const chars =
          "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Node.js Secrets Manager with Rotation](references/nodejs-secrets-manager-with-rotation.md) | Node.js Secrets Manager with Rotation |
| [Python Secrets Rotation with Vault](references/python-secrets-rotation-with-vault.md) | Python Secrets Rotation with Vault |
| [Kubernetes Secrets Rotation](references/kubernetes-secrets-rotation.md) | Kubernetes Secrets Rotation |

## Best Practices

### ✅ DO

- Automate rotation
- Use grace periods
- Verify new secrets
- Maintain rotation audit trail
- Implement rollback procedures
- Monitor rotation failures
- Use managed services (AWS Secrets Manager)
- Test rotation procedures

### ❌ DON'T

- Hardcode secrets
- Share secrets
- Skip verification
- Rotate without grace period
- Ignore rotation failures
- Store secrets in version control
