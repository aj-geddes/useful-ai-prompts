---
name: access-control-rbac
description: >
  Implement Role-Based Access Control (RBAC), permissions management, and
  authorization policies. Use when building secure access control systems with
  fine-grained permissions.
---

# Access Control & RBAC

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive Role-Based Access Control systems with permissions management, attribute-based policies, and least privilege principles.

## When to Use

- Multi-tenant applications
- Enterprise access management
- API authorization
- Admin dashboards
- Data access controls
- Compliance requirements

## Quick Start

Minimal working example:

```javascript
// rbac-system.js
class Permission {
  constructor(resource, action) {
    this.resource = resource;
    this.action = action;
  }

  toString() {
    return `${this.resource}:${this.action}`;
  }
}

class Role {
  constructor(name, description) {
    this.name = name;
    this.description = description;
    this.permissions = new Set();
    this.inherits = new Set();
  }

  addPermission(permission) {
    this.permissions.add(permission.toString());
  }

  removePermission(permission) {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Node.js RBAC System](references/nodejs-rbac-system.md) | Node.js RBAC System |
| [Python ABAC (Attribute-Based Access Control)](references/python-abac-attribute-based-access-control.md) | Python ABAC (Attribute-Based Access Control) |
| [Java Spring Security RBAC](references/java-spring-security-rbac.md) | Java Spring Security RBAC |

## Best Practices

### ✅ DO

- Implement least privilege
- Use role hierarchies
- Audit access changes
- Regular access reviews
- Separate duties
- Document permissions
- Test access controls
- Use attribute-based policies

### ❌ DON'T

- Grant excessive permissions
- Share accounts
- Skip access reviews
- Hardcode permissions
- Ignore audit logs
- Use role explosion
