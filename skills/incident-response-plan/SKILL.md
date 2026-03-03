---
name: incident-response-plan
description: >
  Create and execute incident response procedures for security breaches, data
  leaks, and cyber attacks. Use when handling security incidents, creating
  response playbooks, or conducting forensic analysis.
---

# Incident Response Plan

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Structured approach to detecting, responding to, containing, and recovering from security incidents with comprehensive playbooks and automation.

## When to Use

- Security breach detection
- Data breach response
- Malware infection
- DDoS attacks
- Insider threats
- Compliance violations
- Post-incident analysis

## Quick Start

Minimal working example:

```python
# incident_response.py
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime
import json

class IncidentSeverity(Enum):
    CRITICAL = "critical"  # P1 - Business critical
    HIGH = "high"          # P2 - Major impact
    MEDIUM = "medium"      # P3 - Moderate impact
    LOW = "low"            # P4 - Minor impact

class IncidentStatus(Enum):
    DETECTED = "detected"
    INVESTIGATING = "investigating"
    CONTAINED = "contained"
    ERADICATED = "eradicated"
    RECOVERED = "recovered"
    CLOSED = "closed"

class IncidentType(Enum):
    DATA_BREACH = "data_breach"
    MALWARE = "malware"
    UNAUTHORIZED_ACCESS = "unauthorized_access"
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Incident Response Framework](references/incident-response-framework.md) | Incident Response Framework |
| [Node.js Incident Detection & Response](references/nodejs-incident-detection-response.md) | Node.js Incident Detection & Response |

## Best Practices

### ✅ DO

- Maintain incident response plan
- Define clear escalation paths
- Practice incident drills
- Document all actions
- Preserve evidence
- Communicate transparently
- Conduct post-incident reviews
- Update playbooks regularly

### ❌ DON'T

- Panic or rush
- Delete evidence
- Skip documentation
- Work in isolation
- Ignore lessons learned
- Delay notifications
