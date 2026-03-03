# Handling Dynamic Content

## Handling Dynamic Content

```typescript
// Hide or mock dynamic content
test("page with dynamic content", async ({ page }) => {
  await page.goto("/dashboard");

  // Hide timestamps
  await page.addStyleTag({
    content: ".timestamp { visibility: hidden; }",
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
test("ignore dynamic regions", async ({ page }) => {
  await page.goto("/");

  await expect(page).toHaveScreenshot({
    mask: [
      page.locator(".ad-banner"),
      page.locator(".live-chat"),
      page.locator(".timestamp"),
    ],
  });
});
```
