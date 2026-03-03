---
name: e2e-testing-automation
description: >
  Build end-to-end automated tests that simulate real user interactions across
  the full application stack. Use for E2E test, Selenium, Cypress, Playwright,
  browser automation, and user journey testing.
---

# E2E Testing Automation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

End-to-end (E2E) testing validates complete user workflows from the UI through all backend systems, ensuring the entire application stack works together correctly from a user's perspective. E2E tests simulate real user interactions with browsers, handling authentication, navigation, form submissions, and validating results.

## When to Use

- Testing critical user journeys (signup, checkout, login)
- Validating multi-step workflows
- Testing across different browsers and devices
- Regression testing for UI changes
- Verifying frontend-backend integration
- Testing with real user interactions (clicks, typing, scrolling)
- Smoke testing deployments

## Quick Start

Minimal working example:

```typescript
// tests/e2e/checkout.spec.ts
import { test, expect, Page } from "@playwright/test";

test.describe("E-commerce Checkout Flow", () => {
  let page: Page;

  test.beforeEach(async ({ page: p }) => {
    page = p;
    await page.goto("/");
  });

  test("complete checkout flow as guest user", async () => {
    // 1. Browse and add product to cart
    await page.click("text=Shop Now");
    await page.click('[data-testid="product-1"]');
    await expect(page.locator("h1")).toContainText("Product Name");

    await page.click('button:has-text("Add to Cart")');
    await expect(page.locator(".cart-count")).toHaveText("1");

    // 2. Go to cart and proceed to checkout
    await page.click('[data-testid="cart-icon"]');
    await expect(page.locator(".cart-item")).toHaveCount(1);
    await page.click("text=Proceed to Checkout");

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Playwright E2E Tests](references/playwright-e2e-tests.md) | Playwright E2E Tests |
| [Cypress E2E Tests](references/cypress-e2e-tests.md) | Cypress E2E Tests |
| [Selenium with Python (pytest)](references/selenium-with-python-pytest.md) | Selenium with Python (pytest) |
| [Page Object Model Pattern](references/page-object-model-pattern.md) | Page Object Model Pattern |

## Best Practices

### ✅ DO

- Use data-testid attributes for stable selectors
- Implement Page Object Model for maintainability
- Test critical user journeys thoroughly
- Run tests in multiple browsers (cross-browser testing)
- Use explicit waits instead of sleep/timeouts
- Clean up test data after each test
- Take screenshots on failures
- Parallelize test execution where possible

### ❌ DON'T

- Use brittle CSS selectors (like nth-child)
- Test every possible UI combination (focus on critical paths)
- Share state between tests
- Use fixed delays (sleep/timeout)
- Ignore flaky tests
- Run E2E tests for unit-level testing
- Test third-party UI components in detail
- Skip mobile/responsive testing
