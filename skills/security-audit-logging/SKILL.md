---
name: security-audit-logging
description: >
  Implement comprehensive security audit logging for compliance, forensics, and
  SIEM integration. Use when building audit trails, compliance logging, or
  security monitoring systems.
---

# Security Audit Logging

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive audit logging for security events, user actions, and system changes with structured logging, retention policies, and SIEM integration.

## When to Use

- Compliance requirements (SOC 2, HIPAA, PCI-DSS)
- Security monitoring
- Forensic investigations
- User activity tracking
- System change auditing
- Breach detection

## Quick Start

Minimal working example:

```javascript
// audit-logger.js
const winston = require("winston");
const { ElasticsearchTransport } = require("winston-elasticsearch");

class AuditLogger {
  constructor() {
    this.logger = winston.createLogger({
      level: "info",
      format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.json(),
      ),
      transports: [
        // File transport
        new winston.transports.File({
          filename: "logs/audit.log",
          maxsize: 10485760, // 10MB
          maxFiles: 30,
          tailable: true,
        }),

        // Elasticsearch transport for SIEM
        new ElasticsearchTransport({
          level: "info",
          clientOpts: {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Node.js Audit Logger](references/nodejs-audit-logger.md) | Node.js Audit Logger |
| [Python Audit Logging System](references/python-audit-logging-system.md) | Python Audit Logging System |
| [Java Audit Logging](references/java-audit-logging.md) | Java Audit Logging |

## Best Practices

### ✅ DO

- Log all security events
- Use structured logging
- Include timestamps (UTC)
- Log user context
- Implement log retention
- Encrypt sensitive logs
- Monitor log integrity
- Send to SIEM
- Include request IDs

### ❌ DON'T

- Log passwords/secrets
- Log sensitive PII unnecessarily
- Skip failed attempts
- Allow log tampering
- Store logs insecurely
- Ignore log analysis
