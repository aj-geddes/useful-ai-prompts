---
name: test-automation-framework
description: >
  Design and implement scalable test automation frameworks with Page Object
  Model, fixtures, and reporting. Use for test framework, page object pattern,
  test architecture, test organization, and automation infrastructure.
---

# Test Automation Framework

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

A test automation framework provides structure, reusability, and maintainability for automated tests. It defines patterns for organizing tests, managing test data, handling dependencies, and generating reports. A well-designed framework reduces duplication, improves reliability, and accelerates test development.

## When to Use

- Setting up new test automation
- Scaling existing test suites
- Standardizing test practices across teams
- Reducing test maintenance burden
- Improving test reliability and speed
- Organizing large test codebases
- Implementing reusable test utilities
- Creating consistent reporting

## Quick Start

Minimal working example:

```typescript
// framework/pages/BasePage.ts
import { Page, Locator } from "@playwright/test";

export abstract class BasePage {
  constructor(protected page: Page) {}

  async goto(path: string) {
    await this.page.goto(path);
  }

  async waitForPageLoad() {
    await this.page.waitForLoadState("networkidle");
  }

  async takeScreenshot(name: string) {
    await this.page.screenshot({ path: `screenshots/${name}.png` });
  }

  protected async clickAndWait(locator: Locator) {
    await Promise.all([
      this.page.waitForResponse((resp) => resp.status() === 200),
      locator.click(),
    ]);
  }
}
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Page Object Model (Playwright/TypeScript)](references/page-object-model-playwrighttypescript.md) | Page Object Model (Playwright/TypeScript) |
| [Test Fixtures and Factories](references/test-fixtures-and-factories.md) | Test Fixtures and Factories |
| [Custom Test Utilities](references/custom-test-utilities.md) | Custom Test Utilities |
| [Configuration Management](references/configuration-management.md) | Configuration Management |
| [Custom Reporter](references/custom-reporter.md) | Custom Reporter |
| [pytest Framework (Python)](references/pytest-framework-python.md) | pytest Framework (Python) |
| [Test Organization](references/test-organization.md) | Test Organization |

## Best Practices

### ✅ DO

- Use Page Object Model for UI tests
- Create reusable test utilities
- Implement proper wait strategies
- Use fixtures for test data
- Configure for multiple environments
- Generate readable test reports
- Organize tests by feature/type
- Version control test framework

### ❌ DON'T

- Put test logic in page objects
- Use hard-coded waits (sleep)
- Duplicate test setup code
- Mix test data with test logic
- Skip error handling
- Ignore test flakiness
- Create overly complex abstractions
- Hardcode environment URLs
