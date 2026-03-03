---
name: static-code-analysis
description: >
  Implement static code analysis with linters, formatters, and security scanners
  to catch bugs early. Use when enforcing code standards, detecting security
  vulnerabilities, or automating code review.
---

# Static Code Analysis

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Use automated tools to analyze code without executing it, catching bugs, security issues, and style violations early.

## When to Use

- Enforcing coding standards
- Security vulnerability detection
- Bug prevention
- Code review automation
- CI/CD pipelines
- Pre-commit hooks
- Refactoring assistance

## Quick Start

Minimal working example:

```javascript
// .eslintrc.js
module.exports = {
  extends: [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:security/recommended",
  ],
  plugins: ["@typescript-eslint", "security", "import"],
  rules: {
    "no-console": ["warn", { allow: ["error", "warn"] }],
    "no-unused-vars": "error",
    "prefer-const": "error",
    eqeqeq: ["error", "always"],
    "no-eval": "error",
    "security/detect-object-injection": "warn",
    "security/detect-non-literal-regexp": "warn",
    "@typescript-eslint/no-explicit-any": "warn",
    "@typescript-eslint/explicit-function-return-type": "error",
    "import/order": [
      "error",
      {
        groups: [
          "builtin",
          "external",
          "internal",
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [ESLint Configuration](references/eslint-configuration.md) | ESLint Configuration |
| [Python Linting (pylint + mypy)](references/python-linting-pylint-mypy.md) | Python Linting (pylint + mypy) |
| [Pre-commit Hooks](references/pre-commit-hooks.md) | Pre-commit Hooks |
| [SonarQube Integration](references/sonarqube-integration.md) | SonarQube Integration |
| [Custom AST Analysis](references/custom-ast-analysis.md) | Custom AST Analysis |
| [Security Scanning](references/security-scanning.md) | Security Scanning |

## Best Practices

### ✅ DO

- Run linters in CI/CD
- Use pre-commit hooks
- Configure IDE integration
- Fix issues incrementally
- Document custom rules
- Share configuration across team
- Automate security scanning

### ❌ DON'T

- Ignore all warnings
- Skip linter setup
- Commit lint violations
- Use overly strict rules initially
- Skip security scans
- Disable rules without reason
