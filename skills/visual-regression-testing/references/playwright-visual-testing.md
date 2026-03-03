# Playwright Visual Testing

## Playwright Visual Testing

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
    await page.setViewportSize({ width: 768, height: 1024 }); // iPad
    await page.goto("/");

    await expect(page).toHaveScreenshot("homepage-tablet.png");
  });

  test("responsive design - desktop", async ({ page }) => {
    await page.setViewportSize({ width: 1920, height: 1080 });
    await page.goto("/");

    await expect(page).toHaveScreenshot("homepage-desktop.png");
  });

  test("dark mode visual", async ({ page }) => {
    await page.goto("/");
    await page.emulateMedia({ colorScheme: "dark" });
    await page.waitForTimeout(500); // Allow theme transition

    await expect(page).toHaveScreenshot("homepage-dark.png");
  });

  test("component visual - hero section", async ({ page }) => {
    await page.goto("/");

    const hero = page.locator('[data-testid="hero-section"]');
    await expect(hero).toHaveScreenshot("hero-section.png");
  });

  test("interactive state - button hover", async ({ page }) => {
    await page.goto("/");

    const button = page.locator("button.primary");
    await button.hover();
    await page.waitForTimeout(200); // Allow hover animation

    await expect(button).toHaveScreenshot("button-hover.png");
  });
});

// playwright.config.ts
import { defineConfig } from "@playwright/test";

export default defineConfig({
  expect: {
    toHaveScreenshot: {
      maxDiffPixels: 50, // Maximum different pixels
      threshold: 0.2, // 20% threshold
      animations: "disabled", // Disable animations for consistency
    },
  },
  use: {
    screenshot: "only-on-failure",
  },
});
```
