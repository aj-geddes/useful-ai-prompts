---
name: data-encryption
description: >
  Implement strong encryption using AES, RSA, TLS, and proper key management.
  Use when securing data at rest, in transit, or implementing end-to-end
  encryption.
---

# Data Encryption

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement robust encryption strategies for protecting sensitive data at rest and in transit using industry-standard cryptographic algorithms and key management practices.

## When to Use

- Sensitive data storage
- Database encryption
- File encryption
- Communication security
- Compliance requirements (GDPR, HIPAA, PCI-DSS)
- Password storage
- End-to-end encryption

## Quick Start

Minimal working example:

```javascript
// encryption-service.js
const crypto = require("crypto");
const fs = require("fs").promises;

class EncryptionService {
  constructor() {
    // AES-256-GCM for symmetric encryption
    this.algorithm = "aes-256-gcm";
    this.keyLength = 32; // 256 bits
    this.ivLength = 16; // 128 bits
    this.saltLength = 64;
    this.tagLength = 16;
  }

  /**
   * Generate a cryptographically secure random key
   */
  generateKey() {
    return crypto.randomBytes(this.keyLength);
  }

  /**
   * Derive a key from a password using PBKDF2
   */
  async deriveKey(password, salt = null) {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Node.js Encryption Library](references/nodejs-encryption-library.md) | Node.js Encryption Library |
| [Python Cryptography Implementation](references/python-cryptography-implementation.md) | Python Cryptography Implementation |
| [Database Encryption (PostgreSQL)](references/database-encryption-postgresql.md) | Database Encryption (PostgreSQL) |
| [TLS/SSL Configuration](references/tlsssl-configuration.md) | TLS/SSL Configuration |

## Best Practices

### ✅ DO

- Use AES-256-GCM for symmetric encryption
- Use RSA-4096 or ECC for asymmetric encryption
- Implement proper key rotation
- Use secure key storage (HSM, KMS)
- Salt and hash passwords
- Use TLS 1.2+ for transit encryption
- Implement key derivation (PBKDF2, Argon2)
- Use authenticated encryption

### ❌ DON'T

- Roll your own crypto
- Store keys in code
- Use ECB mode
- Use MD5 or SHA1
- Reuse IVs/nonces
- Use weak key lengths
- Skip authentication tags
