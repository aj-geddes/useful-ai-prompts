# Keyboard Navigation Testing

## Keyboard Navigation Testing

```typescript
// tests/accessibility/keyboard-navigation.test.ts
import { test, expect } from "@playwright/test";

test.describe("Keyboard Navigation", () => {
  test("should navigate through focusable elements with Tab", async ({
    page,
  }) => {
    await page.goto("/");

    // Get all focusable elements
    const focusableSelectors =
      'a[href], button, input, select, textarea, [tabindex]:not([tabindex="-1"])';

    const focusableElements = await page.locator(focusableSelectors).all();

    // Tab through all elements
    for (let i = 0; i < focusableElements.length; i++) {
      await page.keyboard.press("Tab");

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

  test("should skip navigation with skip link", async ({ page }) => {
    await page.goto("/");

    // Tab to skip link (usually first focusable element)
    await page.keyboard.press("Tab");

    const skipLink = await page.locator(".skip-link");
    await expect(skipLink).toBeFocused();

    // Activate skip link
    await page.keyboard.press("Enter");

    // Focus should be on main content
    const focusedElement = await page.evaluate(() => {
      return document.activeElement?.id;
    });

    expect(focusedElement).toBe("main-content");
  });

  test("modal should trap focus", async ({ page }) => {
    await page.goto("/");

    // Open modal
    await page.click('[data-testid="open-modal"]');
    await page.waitForSelector('[role="dialog"]');

    const modal = page.locator('[role="dialog"]');
    const focusableInModal = modal.locator(
      "a[href], button, input, select, textarea",
    );

    const count = await focusableInModal.count();

    // Tab through all elements in modal
    for (let i = 0; i < count + 2; i++) {
      await page.keyboard.press("Tab");
    }

    // Focus should still be within modal
    const focusedElement = await page.evaluate(() => {
      const modal = document.querySelector('[role="dialog"]');
      return modal?.contains(document.activeElement);
    });

    expect(focusedElement).toBe(true);
  });

  test("dropdown menu should be keyboard accessible", async ({ page }) => {
    await page.goto("/");

    // Navigate to dropdown trigger
    await page.keyboard.press("Tab");
    const dropdown = page.locator('[data-testid="dropdown-menu"]');
    await dropdown.focus();

    // Open dropdown with Enter
    await page.keyboard.press("Enter");

    // Menu should be visible
    const menu = page.locator('[role="menu"]');
    await expect(menu).toBeVisible();

    // Navigate menu items with arrow keys
    await page.keyboard.press("ArrowDown");
    const firstItem = menu.locator('[role="menuitem"]').first();
    await expect(firstItem).toBeFocused();

    await page.keyboard.press("ArrowDown");
    const secondItem = menu.locator('[role="menuitem"]').nth(1);
    await expect(secondItem).toBeFocused();

    // Escape should close menu
    await page.keyboard.press("Escape");
    await expect(menu).not.toBeVisible();
    await expect(dropdown).toBeFocused();
  });

  test("form can be completed using keyboard only", async ({ page }) => {
    await page.goto("/contact");

    // Tab to first field
    await page.keyboard.press("Tab");
    await page.keyboard.type("John Doe");

    // Tab to email field
    await page.keyboard.press("Tab");
    await page.keyboard.type("john@example.com");

    // Tab to message
    await page.keyboard.press("Tab");
    await page.keyboard.type("Test message");

    // Tab to submit and activate
    await page.keyboard.press("Tab");
    await page.keyboard.press("Enter");

    // Check form was submitted
    await expect(page.locator(".success-message")).toBeVisible();
  });
});
```
