# ARIA Testing

## ARIA Testing

```typescript
// tests/accessibility/aria.test.ts
import { test, expect } from "@playwright/test";

test.describe("ARIA Attributes", () => {
  test("buttons should have accessible names", async ({ page }) => {
    await page.goto("/");

    const buttons = await page.locator("button").all();

    for (const button of buttons) {
      const text = await button.textContent();
      const ariaLabel = await button.getAttribute("aria-label");
      const ariaLabelledBy = await button.getAttribute("aria-labelledby");

      expect(
        text?.trim() || ariaLabel || ariaLabelledBy,
        "Button has no accessible name",
      ).toBeTruthy();
    }
  });

  test("icons should have aria-hidden or labels", async ({ page }) => {
    await page.goto("/");

    const icons = await page
      .locator('[class*="icon"], svg[class*="icon"]')
      .all();

    for (const icon of icons) {
      const ariaHidden = await icon.getAttribute("aria-hidden");
      const ariaLabel = await icon.getAttribute("aria-label");
      const title = await icon.locator("title").count();

      // Icon should be hidden from screen readers OR have a label
      expect(
        ariaHidden === "true" || ariaLabel || title > 0,
        "Icon without aria-hidden or accessible name",
      ).toBeTruthy();
    }
  });

  test("custom widgets should have correct roles", async ({ page }) => {
    await page.goto("/components");

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
    const ariaControls = await firstTab.getAttribute("aria-controls");
    const associatedPanel = page.locator(`[id="${ariaControls}"]`);
    await expect(associatedPanel).toHaveCount(1);
  });

  test("live regions announce changes", async ({ page }) => {
    await page.goto("/");

    // Find live region
    const liveRegion = page.locator('[role="status"], [aria-live]');

    // Trigger update
    await page.click('[data-testid="load-data"]');

    // Wait for content
    await liveRegion.waitFor({ state: "visible" });

    const ariaLive = await liveRegion.getAttribute("aria-live");
    expect(["polite", "assertive"]).toContain(ariaLive);
  });
});
```
