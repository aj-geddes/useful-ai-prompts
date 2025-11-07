---
name: security-documentation
description: Create security policies, guidelines, compliance documentation, and security best practices. Use when documenting security policies, compliance requirements, or security guidelines.
---

# Security Documentation

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

## Security Policy Template

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

This security policy defines the security standards, practices, and procedures to protect [Company Name]'s information assets, customer data, and infrastructure.

### Objectives

- Protect confidentiality, integrity, and availability of data
- Comply with regulatory requirements (GDPR, SOC 2, etc.)
- Minimize security risks and vulnerabilities
- Establish clear security responsibilities
- Define incident response procedures

### Scope

This policy applies to:
- All employees, contractors, and third-party vendors
- All systems, applications, and infrastructure
- All customer and company data
- Both on-premise and cloud resources

---

## 2. Authentication & Access Control

### 2.1 Password Requirements

**Minimum Requirements:**
- Length: Minimum 12 characters
- Complexity: Mix of uppercase, lowercase, numbers, and symbols
- History: Cannot reuse last 5 passwords
- Expiration: 90 days (for privileged accounts)
- Lockout: 5 failed attempts triggers 30-minute lockout

**Example Strong Password:**
```
Good: MyC0mplex!Pass#2025
Bad: password123
```

**Implementation:**

```javascript
// Password validation
function validatePassword(password) {
  const minLength = 12;
  const requirements = {
    length: password.length >= minLength,
    uppercase: /[A-Z]/.test(password),
    lowercase: /[a-z]/.test(password),
    number: /[0-9]/.test(password),
    special: /[!@#$%^&*(),.?":{}|<>]/.test(password)
  };

  return Object.values(requirements).every(Boolean);
}
```

### 2.2 Multi-Factor Authentication (MFA)

**Requirements:**
- **Mandatory** for:
  - Production system access
  - Administrative accounts
  - Customer-facing applications
  - VPN access
  - Source code repositories

**Supported Methods:**
1. TOTP (Google Authenticator, Authy)
2. SMS (backup only, not primary)
3. Hardware tokens (YubiKey)
4. Biometric (fingerprint, Face ID)

**Implementation:**

```javascript
// MFA verification
async function verifyMFA(userId, token) {
  const user = await User.findById(userId);
  const secret = user.twoFactorSecret;

  // Verify TOTP token
  const isValid = speakeasy.totp.verify({
    secret,
    encoding: 'base32',
    token,
    window: 2 // Allow 1 minute time drift
  });

  if (isValid) {
    await logSecurityEvent('mfa_success', userId);
    return true;
  }

  await logSecurityEvent('mfa_failure', userId);
  return false;
}
```

### 2.3 Role-Based Access Control (RBAC)

**Principle of Least Privilege:** Users receive minimum access needed for their role.

**Roles:**

| Role | Permissions | Access Level |
|------|-------------|--------------|
| Admin | Full system access | Read/Write/Delete All |
| Developer | Code, staging env | Read/Write Dev/Staging |
| Support | Customer data (limited) | Read customer data |
| Auditor | Logs, audit trails | Read-only all |
| User | Own data only | Read/Write own data |

**Implementation:**

```javascript
// Permission middleware
const requirePermission = (permission) => {
  return async (req, res, next) => {
    const user = req.user;
    const userPermissions = await getUserPermissions(user.role);

    if (!userPermissions.includes(permission)) {
      await logSecurityEvent('unauthorized_access', user.id, {
        permission,
        endpoint: req.path
      });

      return res.status(403).json({
        error: 'Insufficient permissions',
        required: permission
      });
    }

    next();
  };
};

// Usage
app.delete('/api/users/:id', requirePermission('users:delete'), deleteUser);
```

---

## 3. Data Protection

### 3.1 Data Classification

| Classification | Description | Examples | Protection |
|----------------|-------------|----------|------------|
| **Public** | Non-sensitive, publicly available | Marketing materials | None required |
| **Internal** | Internal use only | Company policies | Access control |
| **Confidential** | Sensitive business data | Financial reports | Encryption + MFA |
| **Restricted** | Highly sensitive | PII, passwords, keys | Encryption + strict access |

### 3.2 Encryption Standards

**Data at Rest:**
- Algorithm: AES-256
- Key Management: AWS KMS / HashiCorp Vault
- Database: Transparent Data Encryption (TDE)

```javascript
// Encrypt sensitive data before storage
const crypto = require('crypto');

function encryptData(plaintext, key) {
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);

  let encrypted = cipher.update(plaintext, 'utf8', 'hex');
  encrypted += cipher.final('hex');

  const authTag = cipher.getAuthTag();

  return {
    encrypted,
    iv: iv.toString('hex'),
    authTag: authTag.toString('hex')
  };
}
```

**Data in Transit:**
- Protocol: TLS 1.3 (minimum TLS 1.2)
- Cipher Suites: Strong ciphers only
- Certificate: Valid SSL/TLS certificate

```nginx
# Nginx TLS configuration
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256';
ssl_prefer_server_ciphers on;
ssl_session_cache shared:SSL:10m;
ssl_session_timeout 10m;
```

### 3.3 Data Retention

| Data Type | Retention Period | Deletion Method |
|-----------|------------------|-----------------|
| Customer data | Until account deletion + 30 days | Secure wipe |
| Access logs | 90 days | Automated deletion |
| Audit logs | 7 years | Archived, then deleted |
| Backups | 30 days | Overwrite + shred |

---

## 4. Application Security

### 4.1 Secure Coding Practices

**Input Validation:**

```javascript
// ✅ Good - Validate and sanitize input
const validator = require('validator');

function createUser(req, res) {
  const { email, name } = req.body;

  // Validate email
  if (!validator.isEmail(email)) {
    return res.status(400).json({ error: 'Invalid email' });
  }

  // Sanitize name
  const sanitizedName = validator.escape(name);

  // Use parameterized queries
  db.query(
    'INSERT INTO users (email, name) VALUES ($1, $2)',
    [email, sanitizedName]
  );
}

// ❌ Bad - SQL injection vulnerability
function createUserBad(req, res) {
  const { email, name } = req.body;
  db.query(`INSERT INTO users VALUES ('${email}', '${name}')`);
}
```

**XSS Prevention:**

```javascript
// Content Security Policy headers
app.use((req, res, next) => {
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';"
  );
  next();
});

// Sanitize output
import DOMPurify from 'isomorphic-dompurify';

function renderComment(comment) {
  const clean = DOMPurify.sanitize(comment, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong'],
    ALLOWED_ATTR: []
  });
  return clean;
}
```

### 4.2 Security Headers

```javascript
// Security headers middleware
app.use((req, res, next) => {
  // Prevent clickjacking
  res.setHeader('X-Frame-Options', 'DENY');

  // XSS protection
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-XSS-Protection', '1; mode=block');

  // HTTPS enforcement
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');

  // Referrer policy
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');

  next();
});
```

### 4.3 API Security

**Rate Limiting:**

```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP',
  standardHeaders: true,
  legacyHeaders: false
});

app.use('/api/', limiter);
```

---

## 5. Infrastructure Security

### 5.1 Network Security

**Firewall Rules:**
- Default deny all
- Allow only required ports
- Whitelist trusted IPs for admin access

```bash
# Example iptables rules
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow SSH from specific IP
iptables -A INPUT -p tcp -s 203.0.113.0/24 --dport 22 -j ACCEPT

# Allow HTTP/HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

### 5.2 Server Hardening

**Checklist:**
- [ ] Disable root SSH login
- [ ] Use SSH keys, disable password auth
- [ ] Install security updates automatically
- [ ] Enable firewall (ufw/iptables)
- [ ] Configure fail2ban
- [ ] Disable unused services
- [ ] Enable audit logging
- [ ] Set up intrusion detection (AIDE, Tripwire)

---

## 6. Incident Response

### 6.1 Security Incident Severity

| Severity | Description | Response Time | Examples |
|----------|-------------|---------------|----------|
| **Critical** | Massive data breach, ransomware | Immediate | Database exposed, encryption compromised |
| **High** | Significant security compromise | < 1 hour | Admin account compromised, DDoS |
| **Medium** | Limited security issue | < 4 hours | XSS vulnerability, phishing attempt |
| **Low** | Minor security concern | < 24 hours | Weak password, outdated library |

### 6.2 Incident Response Plan

**Phase 1: Detection (0-15 minutes)**
1. Alert received via monitoring/user report
2. Triage severity level
3. Assemble incident response team
4. Create incident ticket

**Phase 2: Containment (15-60 minutes)**
1. Isolate affected systems
2. Block malicious IPs/domains
3. Revoke compromised credentials
4. Enable additional monitoring

**Phase 3: Investigation (1-4 hours)**
1. Analyze logs and forensics
2. Identify attack vector
3. Determine scope of breach
4. Document findings

**Phase 4: Eradication (4-24 hours)**
1. Remove malware/backdoors
2. Patch vulnerabilities
3. Update security controls
4. Verify systems are clean

**Phase 5: Recovery (24-48 hours)**
1. Restore from clean backups
2. Gradually restore services
3. Monitor for re-infection
4. Update documentation

**Phase 6: Post-Incident (1 week)**
1. Conduct post-mortem
2. Update security policies
3. Implement preventive measures
4. Train team on lessons learned

---

## 7. Compliance

### 7.1 GDPR Compliance

**Requirements:**
- [ ] Data processing records
- [ ] Privacy policy
- [ ] Cookie consent
- [ ] Data subject rights (access, deletion, portability)
- [ ] Data breach notification (72 hours)
- [ ] Data Protection Impact Assessment (DPIA)

### 7.2 SOC 2 Compliance

**Trust Services Criteria:**
- **Security:** Protect against unauthorized access
- **Availability:** System is available as committed
- **Processing Integrity:** Processing is complete and accurate
- **Confidentiality:** Confidential information is protected
- **Privacy:** Personal information is properly handled

---

## 8. Vulnerability Disclosure

### Reporting Security Issues

**Contact:** security@example.com
**PGP Key:** [Link to public key]

**Reward Program:**
- Critical: $5,000 - $10,000
- High: $1,000 - $5,000
- Medium: $500 - $1,000
- Low: $100 - $500

**Scope:**
- ✅ In scope: Production systems, APIs, mobile apps
- ❌ Out of scope: Test environments, third-party services

---

## 9. Security Audit Log

All security events must be logged:

```javascript
function logSecurityEvent(event, userId, metadata = {}) {
  logger.security({
    timestamp: new Date().toISOString(),
    event,
    userId,
    ip: metadata.ip,
    userAgent: metadata.userAgent,
    resource: metadata.resource,
    outcome: metadata.outcome
  });
}

// Events to log:
// - login_success, login_failure
// - password_change
// - mfa_enabled, mfa_disabled
// - permission_change
// - data_export
// - admin_action
```
```

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

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [CIS Controls](https://www.cisecurity.org/controls)
- [GDPR Compliance](https://gdpr.eu/)
- [SOC 2 Compliance](https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/aicpasoc2report)
