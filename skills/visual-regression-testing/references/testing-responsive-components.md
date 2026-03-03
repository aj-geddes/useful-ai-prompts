# Testing Responsive Components

## Testing Responsive Components

```typescript
const viewports = [
  { name: "mobile", width: 375, height: 667 },
  { name: "tablet", width: 768, height: 1024 },
  { name: "desktop", width: 1920, height: 1080 },
  { name: "4k", width: 3840, height: 2160 },
];

for (const viewport of viewports) {
  test(`navigation at ${viewport.name}`, async ({ page }) => {
    await page.setViewportSize({
      width: viewport.width,
      height: viewport.height,
    });

    await page.goto("/");

    await expect(page.locator("nav")).toHaveScreenshot(
      `nav-${viewport.name}.png`,
    );
  });
}
```
