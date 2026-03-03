---
name: security-testing
description: >
  Identify security vulnerabilities through SAST, DAST, penetration testing, and
  dependency scanning. Use for security test, vulnerability scanning, OWASP, SQL
  injection, XSS, CSRF, and penetration testing.
---

# Security Testing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Security testing identifies vulnerabilities, weaknesses, and threats in applications to ensure data protection, prevent unauthorized access, and maintain system integrity. It combines automated scanning (SAST, DAST) with manual penetration testing and code review.

## When to Use

- Testing for OWASP Top 10 vulnerabilities
- Scanning dependencies for known vulnerabilities
- Testing authentication and authorization
- Validating input sanitization
- Testing API security
- Checking for sensitive data exposure
- Validating security headers
- Testing session management

## Quick Start

Minimal working example:

```python
# security_scan.py
from zapv2 import ZAPv2
import time

class SecurityScanner:
    def __init__(self, target_url, api_key=None):
        self.zap = ZAPv2(apikey=api_key, proxies={
            'http': 'http://localhost:8080',
            'https': 'http://localhost:8080'
        })
        self.target = target_url

    def scan(self):
        """Run full security scan."""
        print(f"Scanning {self.target}...")

        # Spider the application
        print("Spidering...")
        scan_id = self.zap.spider.scan(self.target)
        while int(self.zap.spider.status(scan_id)) < 100:
            time.sleep(2)
            print(f"Spider progress: {self.zap.spider.status(scan_id)}%")

        # Active scan
        print("Running active scan...")
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [OWASP ZAP (DAST)](references/owasp-zap-dast.md) | OWASP ZAP (DAST) |
| [SQL Injection Testing](references/sql-injection-testing.md) | SQL Injection Testing |
| [XSS Testing](references/xss-testing.md) | XSS Testing |
| [Authentication & Authorization Testing](references/authentication-authorization-testing.md) | Authentication & Authorization Testing |
| [CSRF Protection Testing](references/csrf-protection-testing.md) | CSRF Protection Testing |
| [Dependency Vulnerability Scanning](references/dependency-vulnerability-scanning.md) | Dependency Vulnerability Scanning |
| [Security Headers Testing](references/security-headers-testing.md) | Security Headers Testing |
| [Secrets Detection](references/secrets-detection.md) | Secrets Detection |

## Best Practices

### ✅ DO

- Run security scans in CI/CD
- Test with real attack vectors
- Scan dependencies regularly
- Use security headers
- Implement rate limiting
- Validate and sanitize all input
- Use parameterized queries
- Test authentication/authorization thoroughly

### ❌ DON'T

- Store secrets in code
- Trust user input
- Expose detailed error messages
- Skip dependency updates
- Use default credentials
- Ignore security warnings
- Test only happy paths
- Commit sensitive data
