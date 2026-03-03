# Custom Test Utilities

## Custom Test Utilities

```typescript
// framework/utils/helpers.ts
import { Page, expect } from "@playwright/test";

export class TestHelpers {
  static async waitForAPIResponse(
    page: Page,
    urlPattern: string | RegExp,
    action: () => Promise<void>,
  ) {
    const responsePromise = page.waitForResponse(urlPattern);
    await action();
    return await responsePromise;
  }

  static async mockAPIResponse(
    page: Page,
    url: string | RegExp,
    response: any,
    status: number = 200,
  ) {
    await page.route(url, (route) => {
      route.fulfill({
        status,
        contentType: "application/json",
        body: JSON.stringify(response),
      });
    });
  }

  static async fillForm(page: Page, formData: Record<string, string>) {
    for (const [name, value] of Object.entries(formData)) {
      await page.fill(`[name="${name}"]`, value);
    }
  }

  static generateTestEmail(): string {
    return `test-${Date.now()}-${Math.random().toString(36)}@example.com`;
  }

  static async verifyToastMessage(page: Page, message: string) {
    const toast = page.locator(".toast-message");
    await expect(toast).toContainText(message);
    await expect(toast).toBeVisible();
  }
}

// Usage
import { TestHelpers } from "../framework/utils/helpers";

test("form submission", async ({ page }) => {
  await page.goto("/contact");

  await TestHelpers.fillForm(page, {
    name: "John Doe",
    email: TestHelpers.generateTestEmail(),
    message: "Test message",
  });

  await page.click('button[type="submit"]');

  await TestHelpers.verifyToastMessage(page, "Message sent successfully");
});
```
