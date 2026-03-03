---
name: github-actions-workflow
description: >
  Build comprehensive GitHub Actions workflows for CI/CD, testing, security, and
  deployment. Master workflows, jobs, steps, and conditional execution.
---

# GitHub Actions Workflow

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Create powerful GitHub Actions workflows to automate testing, building, security scanning, and deployment processes directly from your GitHub repository.

## When to Use

- Continuous integration and testing
- Build automation
- Security scanning and analysis
- Dependency updates
- Automated deployments
- Release management
- Code quality checks

## Quick Start

Minimal working example:

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [16.x, 18.x, 20.x]
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node ${{ matrix.node-version }}
        uses: actions/setup-node@v3
        with:
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Complete CI/CD Workflow](references/complete-cicd-workflow.md) | Complete CI/CD Workflow |
| [Automated Release Workflow](references/automated-release-workflow.md) | Automated Release Workflow |
| [Docker Build and Push](references/docker-build-and-push.md) | Docker Build and Push |

## Best Practices

### ✅ DO

- Use caching for dependencies (npm, pip, Maven)
- Run tests in parallel with matrix strategy
- Require status checks on protected branches
- Use environment secrets and variables
- Implement conditional jobs with `if:`
- Lint and format before testing
- Set explicit permissions with permissions
- Use runner labels for specific hardware
- Cache Docker layers for faster builds

### ❌ DON'T

- Store secrets in workflow files
- Run untrusted code in workflows
- Use `secrets.*` with pull requests from forks
- Hardcode credentials or tokens
- Miss error handling with `continue-on-error`
- Create overly complex workflows
- Skip testing on pull requests
