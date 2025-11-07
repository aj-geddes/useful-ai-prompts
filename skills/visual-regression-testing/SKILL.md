---
name: visual-regression-testing
description: Detect unintended visual changes in UI by comparing screenshots across versions. Use for visual regression, screenshot diff, Percy, Chromatic, UI testing, and visual validation.
---

# Visual Regression Testing

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

## Key Concepts

- **Baseline**: Reference screenshot (approved version)
- **Comparison**: New screenshot to compare against baseline
- **Diff**: Visual difference between baseline and comparison
- **Threshold**: Acceptable difference percentage
- **Snapshot**: Captured UI state at specific viewport
- **Approval**: Accepting new baseline after intentional changes

## Instructions

### 1. **Playwright Visual Testing**

```typescript
// tests/visual/homepage.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Homepage Visual Tests', () => {
  test('homepage matches baseline', async ({ page }) => {
    await page.goto('/');

    // Wait for images to load
    await page.waitForLoadState('networkidle');

    // Full page screenshot
    await expect(page).toHaveScreenshot('homepage-full.png', {
      fullPage: true,
      maxDiffPixels: 100,  // Allow small differences
    });
  });

  test('responsive design - mobile', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 667 }); // iPhone SE
    await page.goto('/');

    await expect(page).toHaveScreenshot('homepage-mobile.png');
  });

  test('responsive design - tablet', async ({ page }) => {
    await page.setViewportSize({ width: 768, height: 1024 }); // iPad
    await page.goto('/');

    await expect(page).toHaveScreenshot('homepage-tablet.png');
  });

  test('responsive design - desktop', async ({ page }) => {
    await page.setViewportSize({ width: 1920, height: 1080 });
    await page.goto('/');

    await expect(page).toHaveScreenshot('homepage-desktop.png');
  });

  test('dark mode visual', async ({ page }) => {
    await page.goto('/');
    await page.emulateMedia({ colorScheme: 'dark' });
    await page.waitForTimeout(500); // Allow theme transition

    await expect(page).toHaveScreenshot('homepage-dark.png');
  });

  test('component visual - hero section', async ({ page }) => {
    await page.goto('/');

    const hero = page.locator('[data-testid="hero-section"]');
    await expect(hero).toHaveScreenshot('hero-section.png');
  });

  test('interactive state - button hover', async ({ page }) => {
    await page.goto('/');

    const button = page.locator('button.primary');
    await button.hover();
    await page.waitForTimeout(200); // Allow hover animation

    await expect(button).toHaveScreenshot('button-hover.png');
  });
});

// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  expect: {
    toHaveScreenshot: {
      maxDiffPixels: 50,           // Maximum different pixels
      threshold: 0.2,              // 20% threshold
      animations: 'disabled',       // Disable animations for consistency
    },
  },
  use: {
    screenshot: 'only-on-failure',
  },
});
```

### 2. **Percy Visual Testing**

```typescript
// tests/visual-percy.spec.ts
import { test } from '@playwright/test';
import percySnapshot from '@percy/playwright';

test.describe('Percy Visual Tests', () => {
  test('homepage across viewports', async ({ page }) => {
    await page.goto('/');

    // Percy automatically tests across configured viewports
    await percySnapshot(page, 'Homepage');
  });

  test('product page variations', async ({ page }) => {
    await page.goto('/products/123');

    // Test different states
    await percySnapshot(page, 'Product Page - Default');

    // Open modal
    await page.click('[data-testid="size-guide"]');
    await percySnapshot(page, 'Product Page - Size Guide Modal');

    // Add to cart
    await page.click('[data-testid="add-to-cart"]');
    await percySnapshot(page, 'Product Page - Added to Cart');
  });

  test('component library', async ({ page }) => {
    await page.goto('/styleguide');

    // Test individual components
    const components = ['buttons', 'forms', 'cards', 'modals'];

    for (const component of components) {
      await page.click(`[data-component="${component}"]`);
      await percySnapshot(page, `Component - ${component}`);
    }
  });
});

// percy.config.yml
version: 2
snapshot:
  widths: [375, 768, 1280, 1920]
  min-height: 1024
  percy-css: |
    /* Hide dynamic content */
    .timestamp { visibility: hidden; }
    .ad-banner { display: none; }
```

### 3. **Chromatic for Storybook**

```typescript
// .storybook/main.ts
export default {
  addons: ['@storybook/addon-essentials'],
  framework: '@storybook/react',
};

// Button.stories.tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta: Meta<typeof Button> = {
  title: 'Components/Button',
  component: Button,
  parameters: {
    chromatic: {
      viewports: [320, 768, 1200],  // Test responsive
      delay: 300,                    // Wait for animations
    },
  },
};

export default meta;
type Story = StoryObj<typeof Button>;

export const Primary: Story = {
  args: {
    variant: 'primary',
    children: 'Primary Button',
  },
};

export const Secondary: Story = {
  args: {
    variant: 'secondary',
    children: 'Secondary Button',
  },
};

export const Disabled: Story = {
  args: {
    variant: 'primary',
    disabled: true,
    children: 'Disabled Button',
  },
};

export const WithIcon: Story = {
  args: {
    children: (
      <>
        <Icon name="arrow-right" /> Continue
      </>
    ),
  },
};

// Test hover states
export const HoverState: Story = {
  args: {
    variant: 'primary',
    children: 'Hover Me',
  },
  parameters: {
    pseudo: { hover: true },
  },
};

// Test focus states
export const FocusState: Story = {
  args: {
    variant: 'primary',
    children: 'Focus Me',
  },
  parameters: {
    pseudo: { focus: true },
  },
};
```

```bash
# Install Chromatic
npm install --save-dev chromatic

# Run visual tests
npx chromatic --project-token=<TOKEN>

# In CI
npx chromatic --exit-zero-on-changes
```

### 4. **Cypress Visual Testing**

```javascript
// cypress/e2e/visual.cy.js
describe('Visual Regression Tests', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('homepage visual snapshot', () => {
    cy.viewport(1280, 720);
    cy.matchImageSnapshot('homepage-desktop');
  });

  it('mobile navigation menu', () => {
    cy.viewport('iphone-x');
    cy.get('[data-cy="menu-toggle"]').click();
    cy.get('.mobile-menu').should('be.visible');
    cy.matchImageSnapshot('mobile-menu-open');
  });

  it('form validation errors', () => {
    cy.get('form').within(() => {
      cy.get('[type="email"]').type('invalid-email');
      cy.get('[type="submit"]').click();
    });

    cy.get('.error-message').should('be.visible');
    cy.matchImageSnapshot('form-validation-errors');
  });

  it('loading state', () => {
    cy.intercept('GET', '/api/products', (req) => {
      req.reply((res) => {
        res.delay(1000); // Simulate slow response
        res.send();
      });
    });

    cy.visit('/products');
    cy.matchImageSnapshot('loading-skeleton');
  });

  it('empty state', () => {
    cy.intercept('GET', '/api/cart', { items: [] });
    cy.visit('/cart');
    cy.matchImageSnapshot('cart-empty-state');
  });
});

// cypress.config.js
const { defineConfig } = require('cypress');
const {
  addMatchImageSnapshotPlugin,
} = require('cypress-image-snapshot/plugin');

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      addMatchImageSnapshotPlugin(on, config);
    },
  },
});

// cypress/support/commands.js
import { addMatchImageSnapshotCommand } from 'cypress-image-snapshot/command';

addMatchImageSnapshotCommand({
  failureThreshold: 0.03,        // Allow 3% difference
  failureThresholdType: 'percent',
  customDiffConfig: { threshold: 0.1 },
  capture: 'viewport',
});
```

### 5. **BackstopJS Configuration**

```javascript
// backstop.config.js
module.exports = {
  id: 'visual_regression',
  viewports: [
    {
      label: 'phone',
      width: 375,
      height: 667,
    },
    {
      label: 'tablet',
      width: 768,
      height: 1024,
    },
    {
      label: 'desktop',
      width: 1920,
      height: 1080,
    },
  ],
  scenarios: [
    {
      label: 'Homepage',
      url: 'http://localhost:3000',
      delay: 500,
      misMatchThreshold: 0.1,
      requireSameDimensions: true,
    },
    {
      label: 'Product List',
      url: 'http://localhost:3000/products',
      delay: 1000,
      removeSelectors: ['.timestamp', '.ad-banner'],
    },
    {
      label: 'Product Detail',
      url: 'http://localhost:3000/products/123',
      clickSelector: '.size-guide-link',
      postInteractionWait: 500,
    },
    {
      label: 'Hover State',
      url: 'http://localhost:3000',
      hoverSelector: '.primary-button',
      postInteractionWait: 200,
    },
  ],
  paths: {
    bitmaps_reference: 'backstop_data/bitmaps_reference',
    bitmaps_test: 'backstop_data/bitmaps_test',
    html_report: 'backstop_data/html_report',
  },
  engine: 'puppeteer',
  engineOptions: {
    args: ['--no-sandbox'],
  },
  asyncCaptureLimit: 5,
  asyncCompareLimit: 50,
  debug: false,
  debugWindow: false,
};
```

```bash
# Create reference images
backstop reference

# Run test
backstop test

# Approve changes
backstop approve
```

### 6. **Handling Dynamic Content**

```typescript
// Hide or mock dynamic content
test('page with dynamic content', async ({ page }) => {
  await page.goto('/dashboard');

  // Hide timestamps
  await page.addStyleTag({
    content: '.timestamp { visibility: hidden; }'
  });

  // Mock random content
  await page.evaluate(() => {
    Math.random = () => 0.5;
    Date.now = () => 1234567890;
  });

  // Wait for animations
  await page.waitForTimeout(500);

  await expect(page).toHaveScreenshot();
});

// Ignore regions
test('ignore dynamic regions', async ({ page }) => {
  await page.goto('/');

  await expect(page).toHaveScreenshot({
    mask: [
      page.locator('.ad-banner'),
      page.locator('.live-chat'),
      page.locator('.timestamp'),
    ],
  });
});
```

### 7. **Testing Responsive Components**

```typescript
const viewports = [
  { name: 'mobile', width: 375, height: 667 },
  { name: 'tablet', width: 768, height: 1024 },
  { name: 'desktop', width: 1920, height: 1080 },
  { name: '4k', width: 3840, height: 2160 },
];

for (const viewport of viewports) {
  test(`navigation at ${viewport.name}`, async ({ page }) => {
    await page.setViewportSize({
      width: viewport.width,
      height: viewport.height,
    });

    await page.goto('/');

    await expect(page.locator('nav')).toHaveScreenshot(
      `nav-${viewport.name}.png`
    );
  });
}
```

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

## Tools

- **Playwright**: Built-in screenshot comparison
- **Percy**: Cloud-based visual testing
- **Chromatic**: Storybook visual testing
- **BackstopJS**: Open-source visual regression
- **cypress-image-snapshot**: Cypress plugin
- **Applitools**: AI-powered visual testing
- **Sauce Labs Visual**: Cross-browser visual testing

## CI Integration

```yaml
# .github/workflows/visual-tests.yml
name: Visual Regression Tests

on: [pull_request]

jobs:
  visual-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0  # Needed for Percy

      - uses: actions/setup-node@v3

      - run: npm ci

      - run: npm run build

      - name: Run Playwright visual tests
        run: npx playwright test --grep @visual

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: visual-test-results
          path: test-results/

      - name: Percy snapshots
        run: npx percy exec -- npm run test:visual
        env:
          PERCY_TOKEN: ${{ secrets.PERCY_TOKEN }}
```

## Troubleshooting

### Flaky Tests
- Ensure consistent timing (wait for network idle)
- Disable animations
- Mock randomness
- Use fixed dates/times

### Large Diffs
- Check for font rendering differences
- Verify image loading
- Check for animation timing
- Review anti-aliasing differences

### False Positives
- Adjust threshold tolerance
- Mask dynamic regions
- Use relative comparison
- Review diff images carefully

## Examples

See also: e2e-testing-automation, accessibility-testing, test-automation-framework for comprehensive UI testing.
