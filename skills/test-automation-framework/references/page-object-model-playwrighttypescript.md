# Page Object Model (Playwright/TypeScript)

## Page Object Model (Playwright/TypeScript)

```typescript
// framework/pages/BasePage.ts
import { Page, Locator } from "@playwright/test";

export abstract class BasePage {
  constructor(protected page: Page) {}

  async goto(path: string) {
    await this.page.goto(path);
  }

  async waitForPageLoad() {
    await this.page.waitForLoadState("networkidle");
  }

  async takeScreenshot(name: string) {
    await this.page.screenshot({ path: `screenshots/${name}.png` });
  }

  protected async clickAndWait(locator: Locator) {
    await Promise.all([
      this.page.waitForResponse((resp) => resp.status() === 200),
      locator.click(),
    ]);
  }
}

// framework/pages/LoginPage.ts
export class LoginPage extends BasePage {
  // Locators
  private readonly emailInput = this.page.locator('[name="email"]');
  private readonly passwordInput = this.page.locator('[name="password"]');
  private readonly submitButton = this.page.locator('button[type="submit"]');
  private readonly errorMessage = this.page.locator(".error-message");

  async goto() {
    await super.goto("/login");
  }

  async login(email: string, password: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }

  async loginWithValidation(email: string, password: string) {
    await this.login(email, password);
    await this.page.waitForURL("/dashboard");
  }

  async getErrorMessage(): Promise<string> {
    return (await this.errorMessage.textContent()) || "";
  }

  async isLoggedIn(): Promise<boolean> {
    return this.page.url().includes("/dashboard");
  }
}

// framework/pages/ProductPage.ts
export class ProductPage extends BasePage {
  private readonly addToCartButton = this.page.locator(
    '[data-testid="add-to-cart"]',
  );
  private readonly quantityInput = this.page.locator('[name="quantity"]');
  private readonly priceLabel = this.page.locator(".price");

  async goto(productId: string) {
    await super.goto(`/products/${productId}`);
  }

  async addToCart(quantity: number = 1) {
    if (quantity > 1) {
      await this.quantityInput.fill(String(quantity));
    }
    await this.addToCartButton.click();
  }

  async getPrice(): Promise<number> {
    const priceText = await this.priceLabel.textContent();
    return parseFloat(priceText?.replace(/[^0-9.]/g, "") || "0");
  }
}

// tests/checkout.test.ts
import { test, expect } from "@playwright/test";
import { LoginPage } from "../framework/pages/LoginPage";
import { ProductPage } from "../framework/pages/ProductPage";
import { CartPage } from "../framework/pages/CartPage";
import { CheckoutPage } from "../framework/pages/CheckoutPage";

test.describe("Checkout Flow", () => {
  let loginPage: LoginPage;
  let productPage: ProductPage;
  let cartPage: CartPage;
  let checkoutPage: CheckoutPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    productPage = new ProductPage(page);
    cartPage = new CartPage(page);
    checkoutPage = new CheckoutPage(page);

    await loginPage.goto();
    await loginPage.loginWithValidation("user@test.com", "password123");
  });

  test("complete checkout process", async () => {
    // Add product to cart
    await productPage.goto("product-1");
    await productPage.addToCart(2);

    // Verify cart
    await cartPage.goto();
    expect(await cartPage.getItemCount()).toBe(2);

    // Checkout
    await checkoutPage.goto();
    await checkoutPage.fillShippingInfo({
      name: "John Doe",
      address: "123 Main St",
      city: "San Francisco",
      zip: "94105",
    });

    await checkoutPage.fillPaymentInfo({
      cardNumber: "4242424242424242",
      expiry: "12/25",
      cvc: "123",
    });

    await checkoutPage.placeOrder();

    expect(await checkoutPage.isOrderConfirmed()).toBe(true);
  });
});
```
