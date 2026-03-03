---
name: monorepo-management
description: >
  Manage monorepo architectures using Lerna, Turborepo, and Nx. Configure
  workspaces, dependency versioning, and cross-package testing.
---

# Monorepo Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Establish scalable monorepo structures that support multiple interdependent packages while maintaining build efficiency, dependency management, and deployment coordination.

## When to Use

- Multi-package projects
- Shared libraries across services
- Microservices architecture
- Plugin-based systems
- Multi-app platforms (web + mobile)
- Workspace dependency management
- Scaled team development

## Quick Start

Minimal working example:

```json
{
  "name": "monorepo-root",
  "version": "1.0.0",
  "private": true,
  "workspaces": ["packages/*", "apps/*"],
  "devDependencies": {
    "lerna": "^7.0.0",
    "turbo": "^1.10.0"
  },
  "scripts": {
    "lint": "npm run lint -r",
    "test": "npm run test -r",
    "build": "npm run build -r",
    "clean": "npm run clean -r"
  }
}
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Npm Workspaces Configuration](references/npm-workspaces-configuration.md) | Npm Workspaces Configuration, Lerna Configuration, Turborepo Configuration, Nx Workspace Configuration |
| [Monorepo Directory Structure](references/monorepo-directory-structure.md) | Monorepo Directory Structure |
| [Workspace Dependencies](references/workspace-dependencies.md) | Workspace Dependencies |
| [Lerna Commands](references/lerna-commands.md) | Lerna Commands |
| [Turborepo Commands](references/turborepo-commands.md) | Turborepo Commands |
| [CI/CD for Monorepo](references/cicd-for-monorepo.md) | CI/CD for Monorepo |
| [Version Management Across Packages](references/version-management-across-packages.md) | Version Management Across Packages |

## Best Practices

### ✅ DO

- Use workspace protocols for dependencies
- Implement shared tsconfig for consistency
- Cache build outputs in CI/CD
- Filter packages in CI to avoid unnecessary builds
- Hoist common dependencies
- Document workspace structure
- Use consistent versioning strategy
- Implement pre-commit hooks across workspace
- Test cross-package dependencies
- Version packages independently when appropriate

### ❌ DON'T

- Create circular dependencies
- Use hardcoded versions for workspace packages
- Build all packages when only one changed
- Forget to update lock files
- Ignore workspace boundaries
- Create tightly coupled packages
- Skip dependency management
- Use different tooling per package
