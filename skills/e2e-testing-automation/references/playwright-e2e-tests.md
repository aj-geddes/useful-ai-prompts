# Playwright E2E Tests

## Playwright E2E Tests

```typescript
// tests/e2e/checkout.spec.ts
import { test, expect, Page } from "@playwright/test";

test.describe("E-commerce Checkout Flow", () => {
  let page: Page;

  test.beforeEach(async ({ page: p }) => {
    page = p;
    await page.goto("/");
  });

  test("complete checkout flow as guest user", async () => {
    // 1. Browse and add product to cart
    await page.click("text=Shop Now");
    await page.click('[data-testid="product-1"]');
    await expect(page.locator("h1")).toContainText("Product Name");

    await page.click('button:has-text("Add to Cart")');
    await expect(page.locator(".cart-count")).toHaveText("1");

    // 2. Go to cart and proceed to checkout
    await page.click('[data-testid="cart-icon"]');
    await expect(page.locator(".cart-item")).toHaveCount(1);
    await page.click("text=Proceed to Checkout");

    // 3. Fill shipping information
    await page.fill('[name="email"]', "test@example.com");
    await page.fill('[name="firstName"]', "John");
    await page.fill('[name="lastName"]', "Doe");
    await page.fill('[name="address"]', "123 Main St");
    await page.fill('[name="city"]', "San Francisco");
    await page.selectOption('[name="state"]', "CA");
    await page.fill('[name="zip"]', "94105");

    // 4. Enter payment information
    await page.click("text=Continue to Payment");

    // Wait for payment iframe to load
    const paymentFrame = page.frameLocator('iframe[name="payment-frame"]');
    await paymentFrame.locator('[name="cardNumber"]').fill("4242424242424242");
    await paymentFrame.locator('[name="expiry"]').fill("12/25");
    await paymentFrame.locator('[name="cvc"]').fill("123");

    // 5. Complete order
    await page.click('button:has-text("Place Order")');

    // 6. Verify success
    await expect(page).toHaveURL(/\/order\/confirmation/);
    await expect(page.locator(".confirmation-message")).toContainText(
      "Order placed successfully",
    );

    const orderNumber = await page
      .locator('[data-testid="order-number"]')
      .textContent();
    expect(orderNumber).toMatch(/^ORD-\d+$/);
  });

  test("checkout with existing user account", async () => {
    // Login first
    await page.click("text=Sign In");
    await page.fill('[name="email"]', "existing@example.com");
    await page.fill('[name="password"]', "Password123!");
    await page.click('button[type="submit"]');

    await expect(page.locator(".user-menu")).toContainText(
      "existing@example.com",
    );

    // Add product and checkout with saved information
    await page.click('[data-testid="product-2"]');
    await page.click('button:has-text("Add to Cart")');
    await page.click('[data-testid="cart-icon"]');
    await page.click("text=Checkout");

    // Verify saved address is pre-filled
    await expect(page.locator('[name="address"]')).toHaveValue(/./);

    // Complete checkout
    await page.click('button:has-text("Use Saved Payment")');
    await page.click('button:has-text("Place Order")');

    await expect(page).toHaveURL(/\/order\/confirmation/);
  });

  test("handle out of stock product", async () => {
    await page.click('[data-testid="product-out-of-stock"]');

    const addToCartButton = page.locator('button:has-text("Add to Cart")');
    await expect(addToCartButton).toBeDisabled();
    await expect(page.locator(".stock-status")).toHaveText("Out of Stock");
  });
});
```
