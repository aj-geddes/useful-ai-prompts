---
name: git-hooks-setup
description: >
  Implement Git hooks using Husky, pre-commit, and custom scripts. Enforce code
  quality, linting, and testing before commits and pushes.
---

# Git Hooks Setup

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Configure Git hooks to enforce code quality standards, run automated checks, and prevent problematic commits from being pushed to shared repositories.

## When to Use

- Pre-commit code quality checks
- Commit message validation
- Preventing secrets in commits
- Running tests before push
- Code formatting enforcement
- Linting configuration
- Team-wide standards enforcement

## Quick Start

Minimal working example:

```bash
#!/bin/bash
# setup-husky.sh

# Install Husky
npm install husky --save-dev

# Initialize Husky
npx husky install

# Create pre-commit hook
npx husky add .husky/pre-commit "npm run lint"

# Create commit-msg hook
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"'

# Create pre-push hook
npx husky add .husky/pre-push "npm run test"

# Create post-merge hook
npx husky add .husky/post-merge "npm install"
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Husky Installation and Configuration](references/husky-installation-and-configuration.md) | Husky Installation and Configuration |
| [Pre-commit Hook (Node.js)](references/pre-commit-hook-nodejs.md) | Pre-commit Hook (Node.js) |
| [Commit Message Validation](references/commit-message-validation.md) | Commit Message Validation |
| [Commitlint Configuration](references/commitlint-configuration.md) | Commitlint Configuration, Pre-push Hook (Comprehensive) |
| [Pre-commit Framework (Python)](references/pre-commit-framework-python.md) | Pre-commit Framework (Python) |
| [Secret Detection Hook](references/secret-detection-hook.md) | Secret Detection Hook, Husky in package.json |

## Best Practices

### ✅ DO

- Enforce pre-commit linting and formatting
- Validate commit message format
- Scan for secrets before commit
- Run tests on pre-push
- Skip hooks only with `--no-verify` (rarely)
- Document hook requirements in README
- Use consistent hook configuration
- Make hooks fast (< 5 seconds)
- Provide helpful error messages
- Allow developers to bypass with clear warnings

### ❌ DON'T

- Skip checks with `--no-verify`
- Store secrets in committed files
- Use inconsistent implementations
- Ignore hook errors
- Run full test suite on pre-commit
