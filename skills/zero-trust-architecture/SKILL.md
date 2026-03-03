---
name: zero-trust-architecture
description: >
  Implement Zero Trust security model with identity verification,
  microsegmentation, least privilege access, and continuous monitoring. Use when
  building secure cloud-native applications.
---

# Zero Trust Architecture

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive Zero Trust security architecture based on "never trust, always verify" principle with identity-centric security, microsegmentation, and continuous verification.

## When to Use

- Cloud-native applications
- Microservices architecture
- Remote workforce security
- API security
- Multi-cloud deployments
- Legacy modernization
- Compliance requirements

## Quick Start

Minimal working example:

```javascript
// zero-trust-gateway.js
const jwt = require("jsonwebtoken");
const axios = require("axios");

class ZeroTrustGateway {
  constructor() {
    this.identityProvider = process.env.IDENTITY_PROVIDER_URL;
    this.deviceRegistry = new Map();
    this.sessionContext = new Map();
  }

  /**
   * Verify identity - Who are you?
   */
  async verifyIdentity(token) {
    try {
      // Verify JWT token
      const decoded = jwt.verify(token, process.env.JWT_PUBLIC_KEY, {
        algorithms: ["RS256"],
      });

      // Check token hasn't been revoked
      const revoked = await this.checkTokenRevocation(decoded.jti);
      if (revoked) {
        throw new Error("Token has been revoked");
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Zero Trust Gateway](references/zero-trust-gateway.md) | Zero Trust Gateway |
| [Service Mesh - Microsegmentation](references/service-mesh-microsegmentation.md) | Service Mesh - Microsegmentation |
| [Python Zero Trust Policy Engine](references/python-zero-trust-policy-engine.md) | Python Zero Trust Policy Engine |

## Best Practices

### ✅ DO

- Verify every request
- Implement MFA everywhere
- Use microsegmentation
- Monitor continuously
- Encrypt all communications
- Implement least privilege
- Log all access
- Regular audits

### ❌ DON'T

- Trust network location
- Use implicit trust
- Skip device verification
- Allow lateral movement
- Use static credentials
