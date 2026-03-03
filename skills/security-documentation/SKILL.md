---
name: security-documentation
description: >
  Create security policies, guidelines, compliance documentation, and security
  best practices. Use when documenting security policies, compliance
  requirements, or security guidelines.
---

# Security Documentation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Create comprehensive security documentation including policies, guidelines, compliance requirements, and best practices for secure application development and operations.

## When to Use

- Security policies
- Compliance documentation (SOC 2, GDPR, HIPAA)
- Security guidelines and best practices
- Incident response plans
- Access control policies
- Data protection policies
- Vulnerability disclosure policies
- Security audit reports

## Quick Start

Minimal working example:

```markdown
# Security Policy

**Version:** 2.0
**Last Updated:** 2025-01-15
**Review Schedule:** Quarterly
**Owner:** Security Team
**Contact:** security@example.com

## Table of Contents

1. [Overview](#overview)
2. [Scope](#scope)
3. [Authentication & Access Control](#authentication--access-control)
4. [Data Protection](#data-protection)
5. [Application Security](#application-security)
6. [Infrastructure Security](#infrastructure-security)
7. [Incident Response](#incident-response)
8. [Compliance](#compliance)
9. [Security Training](#security-training)

---

## 1. Overview

### Purpose
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [1 Password Requirements](references/1-password-requirements.md) | 1 Password Requirements |
| [2 Multi-Factor Authentication (MFA)](references/2-multi-factor-authentication-mfa.md) | 2 Multi-Factor Authentication (MFA) |
| [3 Role-Based Access Control (RBAC)](references/3-role-based-access-control-rbac.md) | 3 Role-Based Access Control (RBAC) |
| [1 Secure Coding Practices](references/1-secure-coding-practices.md) | 1 Secure Coding Practices |
| [2 Security Headers](references/2-security-headers.md) | 2 Security Headers, 3 API Security |

## Best Practices

### ✅ DO

- Follow principle of least privilege
- Encrypt sensitive data
- Implement MFA everywhere
- Log security events
- Regular security audits
- Keep systems updated
- Document security policies
- Train employees regularly
- Have incident response plan
- Test backups regularly

### ❌ DON'T

- Store passwords in plaintext
- Skip input validation
- Ignore security headers
- Share credentials
- Hardcode secrets in code
- Skip security testing
- Ignore vulnerability reports
