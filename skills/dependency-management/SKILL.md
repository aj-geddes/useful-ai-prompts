---
name: dependency-management
description: >
  Manage project dependencies across languages including npm install, package
  versioning, dependency conflicts, security scanning, and lock files. Use when
  dealing with dependencies, version pinning, semantic versioning, or resolving
  conflicts.
---

# Dependency Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Comprehensive dependency management across JavaScript/Node.js, Python, Ruby, Java, and other ecosystems. Covers version control, conflict resolution, security auditing, and best practices for maintaining healthy dependencies.

## When to Use

- Installing or updating project dependencies
- Resolving version conflicts
- Auditing security vulnerabilities
- Managing lock files (package-lock.json, Gemfile.lock, etc.)
- Implementing semantic versioning
- Setting up monorepo dependencies
- Optimizing dependency trees
- Managing peer dependencies

## Quick Start

Minimal working example:

```bash
# Initialize project
npm init -y

# Install dependencies
npm install express
npm install --save-dev jest
npm install --save-exact lodash  # Exact version

# Update dependencies
npm update
npm outdated  # Check for outdated packages

# Audit security
npm audit
npm audit fix

# Clean install from lock file
npm ci  # Use in CI/CD

# View dependency tree
npm list
npm list --depth=0  # Top-level only
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Package Manager Basics](references/package-manager-basics.md) | Package Manager Basics |
| [Semantic Versioning (SemVer)](references/semantic-versioning-semver.md) | Semantic Versioning (SemVer) |
| [Dependency Lock Files](references/dependency-lock-files.md) | Dependency Lock Files |
| [Resolving Dependency Conflicts](references/resolving-dependency-conflicts.md) | Resolving Dependency Conflicts |
| [Security Vulnerability Management](references/security-vulnerability-management.md) | Security Vulnerability Management |
| [Monorepo Dependency Management](references/monorepo-dependency-management.md) | Monorepo Dependency Management |
| [Peer Dependencies](references/peer-dependencies.md) | Peer Dependencies |
| [Performance Optimization](references/performance-optimization.md) | Performance Optimization |
| [CI/CD Best Practices](references/cicd-best-practices.md) | CI/CD Best Practices |
| [Dependency Update Strategies](references/dependency-update-strategies.md) | Dependency Update Strategies |

## Best Practices

### ✅ DO

- Commit lock files to version control
- Use `npm ci` or equivalent in CI/CD pipelines
- Regular dependency audits (weekly/monthly)
- Keep dependencies up-to-date (automate with Dependabot)
- Use exact versions for critical dependencies
- Document why specific versions are pinned
- Test after updating dependencies
- Use semantic versioning correctly
- Minimize dependency count
- Review dependency licenses

### ❌ DON'T

- Manually edit lock files
- Mix package managers (npm + yarn in same project)
- Use `npm install` in CI/CD (use `npm ci`)
- Ignore security vulnerabilities
- Use wildcards (\*) for versions
- Install packages globally when local install is possible
- Commit node_modules to git
- Use `latest` tag in production
- Blindly run `npm audit fix`
- Install unnecessary dependencies
