---
name: accessibility-testing
description: >
  Test web applications for WCAG compliance and ensure usability for users with
  disabilities. Use for accessibility test, a11y, axe, ARIA, keyboard
  navigation, screen reader compatibility, and WCAG validation.
---

# Accessibility Testing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Accessibility testing ensures web applications are usable by people with disabilities, including those using screen readers, keyboard navigation, or other assistive technologies. It validates compliance with WCAG (Web Content Accessibility Guidelines) and identifies barriers to accessibility.

## When to Use

- Validating WCAG 2.1/2.2 compliance
- Testing keyboard navigation
- Verifying screen reader compatibility
- Testing color contrast ratios
- Validating ARIA attributes
- Testing form accessibility
- Ensuring focus management
- Testing with assistive technologies

## Quick Start

Minimal working example:

```typescript
// tests/accessibility/homepage.a11y.test.ts
import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test.describe("Homepage Accessibility", () => {
  test("should not have any automatically detectable WCAG A or AA violations", async ({
    page,
  }) => {
    await page.goto("/");

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test("navigation should be accessible", async ({ page }) => {
    await page.goto("/");

    const results = await new AxeBuilder({ page }).include("nav").analyze();

    expect(results.violations).toEqual([]);
  });

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [axe-core with Playwright](references/axe-core-with-playwright.md) | axe-core with Playwright |
| [Keyboard Navigation Testing](references/keyboard-navigation-testing.md) | Keyboard Navigation Testing |
| [ARIA Testing](references/aria-testing.md) | ARIA Testing |
| [Jest with jest-axe](references/jest-with-jest-axe.md) | Jest with jest-axe |
| [Cypress Accessibility Testing](references/cypress-accessibility-testing.md) | Cypress Accessibility Testing |
| [Python with Selenium and axe](references/python-with-selenium-and-axe.md) | Python with Selenium and axe |

## Best Practices

### ✅ DO

- Test with real assistive technologies
- Include keyboard-only users
- Test color contrast
- Use semantic HTML
- Provide text alternatives
- Test with screen readers
- Run automated tests in CI
- Follow WCAG 2.1 AA standards

### ❌ DON'T

- Rely only on automated tests (they catch ~30-40% of issues)
- Use color alone to convey information
- Skip keyboard navigation testing
- Forget focus management in dynamic content
- Use div/span for interactive elements
- Hide focusable content with display:none
- Ignore ARIA best practices
- Skip manual testing
