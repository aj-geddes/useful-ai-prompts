---
name: accessibility-testing
description: Test web applications for WCAG compliance and ensure usability for users with disabilities. Use for accessibility test, a11y, axe, ARIA, keyboard navigation, screen reader compatibility, and WCAG validation.
---

# Accessibility Testing

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

## WCAG Levels

- **Level A**: Basic accessibility (must have)
- **Level AA**: Intermediate accessibility (should have, legal requirement in many jurisdictions)
- **Level AAA**: Advanced accessibility (nice to have)

## Instructions

### 1. **axe-core with Playwright**

```typescript
// tests/accessibility/homepage.a11y.test.ts
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Homepage Accessibility', () => {
  test('should not have any automatically detectable WCAG A or AA violations', async ({
    page,
  }) => {
    await page.goto('/');

    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('navigation should be accessible', async ({ page }) => {
    await page.goto('/');

    const results = await new AxeBuilder({ page })
      .include('nav')
      .analyze();

    expect(results.violations).toEqual([]);
  });

  test('form should be accessible', async ({ page }) => {
    await page.goto('/contact');

    const results = await new AxeBuilder({ page })
      .include('form')
      .withTags(['wcag2a', 'wcag2aa'])
      .analyze();

    expect(results.violations).toEqual([]);

    // Additional form checks
    const inputs = await page.locator('input, select, textarea').all();
    for (const input of inputs) {
      const id = await input.getAttribute('id');
      const ariaLabel = await input.getAttribute('aria-label');
      const ariaLabelledBy = await input.getAttribute('aria-labelledby');

      // Every input should have an associated label
      if (id) {
        const label = await page.locator(`label[for="${id}"]`).count();
        expect(
          label > 0 || ariaLabel || ariaLabelledBy,
          `Input with id="${id}" has no associated label`
        ).toBeTruthy();
      }
    }
  });

  test('images should have alt text', async ({ page }) => {
    await page.goto('/');

    const images = await page.locator('img').all();

    for (const img of images) {
      const alt = await img.getAttribute('alt');
      const role = await img.getAttribute('role');
      const ariaLabel = await img.getAttribute('aria-label');

      // Decorative images should have empty alt or role="presentation"
      // Content images must have descriptive alt text
      expect(
        alt !== null || role === 'presentation' || ariaLabel,
        'Image missing alt text'
      ).toBeTruthy();
    }
  });

  test('color contrast should meet AA standards', async ({ page }) => {
    await page.goto('/');

    const results = await new AxeBuilder({ page })
      .withTags(['cat.color'])
      .analyze();

    expect(results.violations).toEqual([]);
  });
});
```

### 2. **Keyboard Navigation Testing**

```typescript
// tests/accessibility/keyboard-navigation.test.ts
import { test, expect } from '@playwright/test';

test.describe('Keyboard Navigation', () => {
  test('should navigate through focusable elements with Tab', async ({
    page,
  }) => {
    await page.goto('/');

    // Get all focusable elements
    const focusableSelectors =
      'a[href], button, input, select, textarea, [tabindex]:not([tabindex="-1"])';

    const focusableElements = await page.locator(focusableSelectors).all();

    // Tab through all elements
    for (let i = 0; i < focusableElements.length; i++) {
      await page.keyboard.press('Tab');

      const focusedElement = await page.evaluate(() => {
        return {
          tagName: document.activeElement?.tagName,
          id: document.activeElement?.id,
          className: document.activeElement?.className,
        };
      });

      expect(focusedElement.tagName).toBeTruthy();
    }
  });

  test('should skip navigation with skip link', async ({ page }) => {
    await page.goto('/');

    // Tab to skip link (usually first focusable element)
    await page.keyboard.press('Tab');

    const skipLink = await page.locator('.skip-link');
    await expect(skipLink).toBeFocused();

    // Activate skip link
    await page.keyboard.press('Enter');

    // Focus should be on main content
    const focusedElement = await page.evaluate(() => {
      return document.activeElement?.id;
    });

    expect(focusedElement).toBe('main-content');
  });

  test('modal should trap focus', async ({ page }) => {
    await page.goto('/');

    // Open modal
    await page.click('[data-testid="open-modal"]');
    await page.waitForSelector('[role="dialog"]');

    const modal = page.locator('[role="dialog"]');
    const focusableInModal = modal.locator(
      'a[href], button, input, select, textarea'
    );

    const count = await focusableInModal.count();

    // Tab through all elements in modal
    for (let i = 0; i < count + 2; i++) {
      await page.keyboard.press('Tab');
    }

    // Focus should still be within modal
    const focusedElement = await page.evaluate(() => {
      const modal = document.querySelector('[role="dialog"]');
      return modal?.contains(document.activeElement);
    });

    expect(focusedElement).toBe(true);
  });

  test('dropdown menu should be keyboard accessible', async ({ page }) => {
    await page.goto('/');

    // Navigate to dropdown trigger
    await page.keyboard.press('Tab');
    const dropdown = page.locator('[data-testid="dropdown-menu"]');
    await dropdown.focus();

    // Open dropdown with Enter
    await page.keyboard.press('Enter');

    // Menu should be visible
    const menu = page.locator('[role="menu"]');
    await expect(menu).toBeVisible();

    // Navigate menu items with arrow keys
    await page.keyboard.press('ArrowDown');
    const firstItem = menu.locator('[role="menuitem"]').first();
    await expect(firstItem).toBeFocused();

    await page.keyboard.press('ArrowDown');
    const secondItem = menu.locator('[role="menuitem"]').nth(1);
    await expect(secondItem).toBeFocused();

    // Escape should close menu
    await page.keyboard.press('Escape');
    await expect(menu).not.toBeVisible();
    await expect(dropdown).toBeFocused();
  });

  test('form can be completed using keyboard only', async ({ page }) => {
    await page.goto('/contact');

    // Tab to first field
    await page.keyboard.press('Tab');
    await page.keyboard.type('John Doe');

    // Tab to email field
    await page.keyboard.press('Tab');
    await page.keyboard.type('john@example.com');

    // Tab to message
    await page.keyboard.press('Tab');
    await page.keyboard.type('Test message');

    // Tab to submit and activate
    await page.keyboard.press('Tab');
    await page.keyboard.press('Enter');

    // Check form was submitted
    await expect(page.locator('.success-message')).toBeVisible();
  });
});
```

### 3. **ARIA Testing**

```typescript
// tests/accessibility/aria.test.ts
import { test, expect } from '@playwright/test';

test.describe('ARIA Attributes', () => {
  test('buttons should have accessible names', async ({ page }) => {
    await page.goto('/');

    const buttons = await page.locator('button').all();

    for (const button of buttons) {
      const text = await button.textContent();
      const ariaLabel = await button.getAttribute('aria-label');
      const ariaLabelledBy = await button.getAttribute('aria-labelledby');

      expect(
        text?.trim() || ariaLabel || ariaLabelledBy,
        'Button has no accessible name'
      ).toBeTruthy();
    }
  });

  test('icons should have aria-hidden or labels', async ({ page }) => {
    await page.goto('/');

    const icons = await page
      .locator('[class*="icon"], svg[class*="icon"]')
      .all();

    for (const icon of icons) {
      const ariaHidden = await icon.getAttribute('aria-hidden');
      const ariaLabel = await icon.getAttribute('aria-label');
      const title = await icon.locator('title').count();

      // Icon should be hidden from screen readers OR have a label
      expect(
        ariaHidden === 'true' || ariaLabel || title > 0,
        'Icon without aria-hidden or accessible name'
      ).toBeTruthy();
    }
  });

  test('custom widgets should have correct roles', async ({ page }) => {
    await page.goto('/components');

    // Tab widget
    const tablist = page.locator('[role="tablist"]');
    await expect(tablist).toHaveCount(1);

    const tabs = tablist.locator('[role="tab"]');
    const tabpanels = page.locator('[role="tabpanel"]');

    expect(await tabs.count()).toBeGreaterThan(0);
    expect(await tabs.count()).toBe(await tabpanels.count());

    // Check aria-selected
    const selectedTab = tabs.locator('[aria-selected="true"]');
    await expect(selectedTab).toHaveCount(1);

    // Check tab associations
    const firstTab = tabs.first();
    const ariaControls = await firstTab.getAttribute('aria-controls');
    const associatedPanel = page.locator(`[id="${ariaControls}"]`);
    await expect(associatedPanel).toHaveCount(1);
  });

  test('live regions announce changes', async ({ page }) => {
    await page.goto('/');

    // Find live region
    const liveRegion = page.locator('[role="status"], [aria-live]');

    // Trigger update
    await page.click('[data-testid="load-data"]');

    // Wait for content
    await liveRegion.waitFor({ state: 'visible' });

    const ariaLive = await liveRegion.getAttribute('aria-live');
    expect(['polite', 'assertive']).toContain(ariaLive);
  });
});
```

### 4. **Jest with jest-axe**

```typescript
// tests/components/Button.a11y.test.tsx
import React from 'react';
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
import { Button } from '../Button';

expect.extend(toHaveNoViolations);

describe('Button Accessibility', () => {
  test('should not have accessibility violations', async () => {
    const { container } = render(<Button>Click me</Button>);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  test('icon button should have aria-label', async () => {
    const { container } = render(
      <Button aria-label="Close">
        <CloseIcon />
      </Button>
    );
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  test('disabled button should be accessible', async () => {
    const { container } = render(<Button disabled>Disabled</Button>);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });
});
```

### 5. **Cypress Accessibility Testing**

```javascript
// cypress/e2e/accessibility.cy.js
describe('Accessibility Tests', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.injectAxe();
  });

  it('has no detectable a11y violations on load', () => {
    cy.checkA11y();
  });

  it('navigation is accessible', () => {
    cy.checkA11y('nav');
  });

  it('focuses on first error when form submission fails', () => {
    cy.get('form').within(() => {
      cy.get('[type="submit"]').click();
    });

    cy.focused().should('have.attr', 'aria-invalid', 'true');
  });

  it('modal has correct focus management', () => {
    cy.get('[data-cy="open-modal"]').click();

    // Focus should be in modal
    cy.get('[role="dialog"]').should('exist');
    cy.focused().parents('[role="dialog"]').should('exist');

    // Close modal with Escape
    cy.get('body').type('{esc}');
    cy.get('[role="dialog"]').should('not.exist');

    // Focus returns to trigger
    cy.get('[data-cy="open-modal"]').should('have.focus');
  });
});
```

### 6. **Python with Selenium and axe**

```python
# tests/test_accessibility.py
import pytest
from selenium import webdriver
from axe_selenium_python import Axe

class TestAccessibility:
    @pytest.fixture
    def driver(self):
        """Setup Chrome driver."""
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()

    def test_homepage_accessibility(self, driver):
        """Test homepage for WCAG violations."""
        driver.get('http://localhost:3000')

        axe = Axe(driver)
        axe.inject()

        # Run axe accessibility tests
        results = axe.run()

        # Assert no violations
        assert len(results['violations']) == 0, \
            axe.report(results['violations'])

    def test_form_accessibility(self, driver):
        """Test form accessibility."""
        driver.get('http://localhost:3000/contact')

        axe = Axe(driver)
        axe.inject()

        # Run with specific tags
        results = axe.run(options={
            'runOnly': {
                'type': 'tag',
                'values': ['wcag2a', 'wcag2aa', 'wcag21aa']
            }
        })

        violations = results['violations']
        assert len(violations) == 0, \
            f"Found {len(violations)} accessibility violations"

    def test_keyboard_navigation(self, driver):
        """Test keyboard navigation."""
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By

        driver.get('http://localhost:3000')

        body = driver.find_element(By.TAG_NAME, 'body')

        # Tab through focusable elements
        for _ in range(10):
            body.send_keys(Keys.TAB)

            active = driver.switch_to.active_element
            tag_name = active.tag_name

            # Focused element should be interactive
            assert tag_name in ['a', 'button', 'input', 'select', 'textarea'], \
                f"Unexpected focused element: {tag_name}"
```

## Manual Testing Checklist

### Keyboard Navigation
- [ ] All interactive elements accessible via Tab
- [ ] Shift+Tab navigates backwards
- [ ] Enter/Space activates buttons/links
- [ ] Arrow keys work in custom widgets
- [ ] Escape closes modals/dropdowns
- [ ] Skip links present and functional
- [ ] Focus visible on all elements
- [ ] No keyboard traps

### Screen Readers
- [ ] Page has descriptive title
- [ ] Headings form logical hierarchy
- [ ] Images have alt text
- [ ] Form inputs have labels
- [ ] Error messages announced
- [ ] Dynamic content changes announced
- [ ] Links have descriptive text
- [ ] Custom widgets have ARIA roles

### Visual
- [ ] Color contrast meets AA (4.5:1 normal, 3:1 large text)
- [ ] Information not conveyed by color alone
- [ ] Text can be resized 200% without breaking
- [ ] Focus indicators visible
- [ ] Content readable in dark/light modes

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

## Tools

- **Automated Testing**: axe-core, Pa11y, Lighthouse, WAVE
- **Browser Extensions**: axe DevTools, WAVE, Accessibility Insights
- **Screen Readers**: NVDA, JAWS, VoiceOver, TalkBack
- **Color Contrast**: WebAIM Contrast Checker, Stark
- **Frameworks**: jest-axe, cypress-axe, axe-playwright

## Standards

- **WCAG 2.1**: Web Content Accessibility Guidelines
- **WCAG 2.2**: Latest version (2023)
- **Section 508**: US federal accessibility standard
- **EN 301 549**: European accessibility standard
- **ADA**: Americans with Disabilities Act

## Examples

See also: e2e-testing-automation, visual-regression-testing, accessibility-compliance for comprehensive accessibility implementation.
