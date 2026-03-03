# Percy Visual Testing

## Percy Visual Testing

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
