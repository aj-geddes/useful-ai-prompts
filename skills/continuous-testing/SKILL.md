---
name: continuous-testing
description: >
  Integrate automated testing into CI/CD pipelines for continuous quality
  feedback. Use for continuous testing, CI testing, automated testing pipelines,
  test orchestration, and DevOps quality practices.
---

# Continuous Testing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Continuous testing integrates automated testing throughout the software development lifecycle, providing rapid feedback on quality at every stage. It shifts testing left in the development process and ensures that code changes are validated automatically before reaching production.

## When to Use

- Setting up CI/CD pipelines
- Automating test execution on commits
- Implementing shift-left testing
- Running tests in parallel
- Creating test gates for deployments
- Monitoring test health
- Optimizing test execution time
- Establishing quality gates

## Quick Start

Minimal working example:

```yaml
# .github/workflows/ci.yml
name: Continuous Testing

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

env:
  NODE_VERSION: "18"

jobs:
  # Unit tests - Fast feedback
  unit-tests:
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: ${{ env.NODE_VERSION }}
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [GitHub Actions CI Pipeline](references/github-actions-ci-pipeline.md) | GitHub Actions CI Pipeline |
| [GitLab CI Pipeline](references/gitlab-ci-pipeline.md) | GitLab CI Pipeline |
| [Jenkins Pipeline](references/jenkins-pipeline.md) | Jenkins Pipeline |
| [Test Selection Strategy](references/test-selection-strategy.md) | Test Selection Strategy |
| [Flaky Test Detection](references/flaky-test-detection.md) | Flaky Test Detection |
| [Test Metrics Dashboard](references/test-metrics-dashboard.md) | Test Metrics Dashboard |

## Best Practices

### ✅ DO

- Run fast tests first (unit → integration → E2E)
- Parallelize test execution
- Cache dependencies
- Set appropriate timeouts
- Monitor test health and flakiness
- Implement quality gates
- Use test selection strategies
- Generate comprehensive reports

### ❌ DON'T

- Run all tests sequentially
- Ignore flaky tests
- Skip test maintenance
- Allow tests to depend on each other
- Run slow tests on every commit
- Deploy with failing tests
- Ignore test execution time
- Skip security scanning
