---
name: visual-regression-testing
description: >
  Detect unintended visual changes in UI by comparing screenshots across
  versions. Use for visual regression, screenshot diff, Percy, Chromatic, UI
  testing, and visual validation.
---

# Visual Regression Testing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Visual regression testing captures screenshots of UI components and pages, then compares them across versions to detect unintended visual changes. This automated approach catches CSS bugs, layout issues, and design regressions that traditional functional tests miss.

## When to Use

- Detecting CSS regression bugs
- Validating responsive design across viewports
- Testing across different browsers
- Verifying component visual consistency
- Catching layout shifts and overlaps
- Testing theme changes
- Validating design system components
- Reviewing visual changes in PRs

## Quick Start

Minimal working example:

```typescript
// tests/visual/homepage.spec.ts
import { test, expect } from "@playwright/test";

test.describe("Homepage Visual Tests", () => {
  test("homepage matches baseline", async ({ page }) => {
    await page.goto("/");

    // Wait for images to load
    await page.waitForLoadState("networkidle");

    // Full page screenshot
    await expect(page).toHaveScreenshot("homepage-full.png", {
      fullPage: true,
      maxDiffPixels: 100, // Allow small differences
    });
  });

  test("responsive design - mobile", async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 667 }); // iPhone SE
    await page.goto("/");

    await expect(page).toHaveScreenshot("homepage-mobile.png");
  });

  test("responsive design - tablet", async ({ page }) => {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Playwright Visual Testing](references/playwright-visual-testing.md) | Playwright Visual Testing |
| [Percy Visual Testing](references/percy-visual-testing.md) | Percy Visual Testing |
| [Chromatic for Storybook](references/chromatic-for-storybook.md) | Chromatic for Storybook |
| [Cypress Visual Testing](references/cypress-visual-testing.md) | Cypress Visual Testing |
| [BackstopJS Configuration](references/backstopjs-configuration.md) | BackstopJS Configuration |
| [Handling Dynamic Content](references/handling-dynamic-content.md) | Handling Dynamic Content |
| [Testing Responsive Components](references/testing-responsive-components.md) | Testing Responsive Components |

## Best Practices

### ✅ DO

- Hide or mock dynamic content (timestamps, ads)
- Test across multiple viewports
- Wait for animations and images to load
- Use consistent viewport sizes
- Disable animations during capture
- Test interactive states (hover, focus)
- Review diffs carefully before approving
- Store baselines in version control

### ❌ DON'T

- Test pages with constantly changing content
- Ignore small legitimate differences
- Skip responsive testing
- Forget to update baselines after design changes
- Test pages with random data
- Use overly strict thresholds (0% diff)
- Skip browser/device variations
- Commit unapproved diffs
