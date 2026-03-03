---
name: penetration-testing
description: >
  Ethical hacking and security testing methodologies using penetration testing
  tools, exploit frameworks, and manual security validation. Use when assessing
  application security posture and identifying exploitable vulnerabilities.
---

# Penetration Testing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Systematic security testing to identify, exploit, and document vulnerabilities in applications, networks, and infrastructure through simulated attacks.

## When to Use

- Pre-production security validation
- Annual security assessments
- Compliance requirements (PCI-DSS, ISO 27001)
- Post-incident security review
- Third-party security audits
- Red team exercises

## Quick Start

Minimal working example:

```python
# pentest_framework.py
import requests
import socket
import subprocess
import json
from typing import List, Dict
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Finding:
    severity: str
    category: str
    target: str
    vulnerability: str
    evidence: str
    remediation: str
    cvss_score: float

class PenetrationTester:
    def __init__(self, target: str):
        self.target = target
        self.findings: List[Finding] = []

    def test_sql_injection(self, url: str) -> None:
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Automated Penetration Testing Framework](references/automated-penetration-testing-framework.md) | Automated Penetration Testing Framework |
| [Burp Suite Automation Script](references/burp-suite-automation-script.md) | Burp Suite Automation Script |

## Best Practices

### ✅ DO

- Get written authorization
- Define clear scope
- Use controlled environments
- Document all findings
- Follow responsible disclosure
- Provide remediation guidance
- Verify fixes after patching
- Maintain chain of custody

### ❌ DON'T

- Test production without approval
- Cause service disruption
- Exfiltrate sensitive data
- Share findings publicly
- Exceed authorized scope
- Use destructive payloads
