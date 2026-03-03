# axe-core with Playwright

## axe-core with Playwright

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

  test("form should be accessible", async ({ page }) => {
    await page.goto("/contact");

    const results = await new AxeBuilder({ page })
      .include("form")
      .withTags(["wcag2a", "wcag2aa"])
      .analyze();

    expect(results.violations).toEqual([]);

    // Additional form checks
    const inputs = await page.locator("input, select, textarea").all();
    for (const input of inputs) {
      const id = await input.getAttribute("id");
      const ariaLabel = await input.getAttribute("aria-label");
      const ariaLabelledBy = await input.getAttribute("aria-labelledby");

      // Every input should have an associated label
      if (id) {
        const label = await page.locator(`label[for="${id}"]`).count();
        expect(
          label > 0 || ariaLabel || ariaLabelledBy,
          `Input with id="${id}" has no associated label`,
        ).toBeTruthy();
      }
    }
  });

  test("images should have alt text", async ({ page }) => {
    await page.goto("/");

    const images = await page.locator("img").all();

    for (const img of images) {
      const alt = await img.getAttribute("alt");
      const role = await img.getAttribute("role");
      const ariaLabel = await img.getAttribute("aria-label");

      // Decorative images should have empty alt or role="presentation"
      // Content images must have descriptive alt text
      expect(
        alt !== null || role === "presentation" || ariaLabel,
        "Image missing alt text",
      ).toBeTruthy();
    }
  });

  test("color contrast should meet AA standards", async ({ page }) => {
    await page.goto("/");

    const results = await new AxeBuilder({ page })
      .withTags(["cat.color"])
      .analyze();

    expect(results.violations).toEqual([]);
  });
});
```
