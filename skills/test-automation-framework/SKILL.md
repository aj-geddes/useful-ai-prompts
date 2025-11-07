---
name: test-automation-framework
description: Design and implement scalable test automation frameworks with Page Object Model, fixtures, and reporting. Use for test framework, page object pattern, test architecture, test organization, and automation infrastructure.
---

# Test Automation Framework

## Overview

A test automation framework provides structure, reusability, and maintainability for automated tests. It defines patterns for organizing tests, managing test data, handling dependencies, and generating reports. A well-designed framework reduces duplication, improves reliability, and accelerates test development.

## When to Use

- Setting up new test automation
- Scaling existing test suites
- Standardizing test practices across teams
- Reducing test maintenance burden
- Improving test reliability and speed
- Organizing large test codebases
- Implementing reusable test utilities
- Creating consistent reporting

## Framework Components

- **Test Organization**: Structure and hierarchy
- **Page Objects**: UI element abstraction
- **Test Data Management**: Fixtures and factories
- **Configuration**: Environment-specific settings
- **Utilities**: Shared helpers and functions
- **Reporting**: Test results and metrics
- **CI/CD Integration**: Automated execution

## Instructions

### 1. **Page Object Model (Playwright/TypeScript)**

```typescript
// framework/pages/BasePage.ts
import { Page, Locator } from '@playwright/test';

export abstract class BasePage {
  constructor(protected page: Page) {}

  async goto(path: string) {
    await this.page.goto(path);
  }

  async waitForPageLoad() {
    await this.page.waitForLoadState('networkidle');
  }

  async takeScreenshot(name: string) {
    await this.page.screenshot({ path: `screenshots/${name}.png` });
  }

  protected async clickAndWait(locator: Locator) {
    await Promise.all([
      this.page.waitForResponse(resp => resp.status() === 200),
      locator.click()
    ]);
  }
}

// framework/pages/LoginPage.ts
export class LoginPage extends BasePage {
  // Locators
  private readonly emailInput = this.page.locator('[name="email"]');
  private readonly passwordInput = this.page.locator('[name="password"]');
  private readonly submitButton = this.page.locator('button[type="submit"]');
  private readonly errorMessage = this.page.locator('.error-message');

  async goto() {
    await super.goto('/login');
  }

  async login(email: string, password: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }

  async loginWithValidation(email: string, password: string) {
    await this.login(email, password);
    await this.page.waitForURL('/dashboard');
  }

  async getErrorMessage(): Promise<string> {
    return await this.errorMessage.textContent() || '';
  }

  async isLoggedIn(): Promise<boolean> {
    return this.page.url().includes('/dashboard');
  }
}

// framework/pages/ProductPage.ts
export class ProductPage extends BasePage {
  private readonly addToCartButton = this.page.locator('[data-testid="add-to-cart"]');
  private readonly quantityInput = this.page.locator('[name="quantity"]');
  private readonly priceLabel = this.page.locator('.price');

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
    return parseFloat(priceText?.replace(/[^0-9.]/g, '') || '0');
  }
}

// tests/checkout.test.ts
import { test, expect } from '@playwright/test';
import { LoginPage } from '../framework/pages/LoginPage';
import { ProductPage } from '../framework/pages/ProductPage';
import { CartPage } from '../framework/pages/CartPage';
import { CheckoutPage } from '../framework/pages/CheckoutPage';

test.describe('Checkout Flow', () => {
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
    await loginPage.loginWithValidation('user@test.com', 'password123');
  });

  test('complete checkout process', async () => {
    // Add product to cart
    await productPage.goto('product-1');
    await productPage.addToCart(2);

    // Verify cart
    await cartPage.goto();
    expect(await cartPage.getItemCount()).toBe(2);

    // Checkout
    await checkoutPage.goto();
    await checkoutPage.fillShippingInfo({
      name: 'John Doe',
      address: '123 Main St',
      city: 'San Francisco',
      zip: '94105'
    });

    await checkoutPage.fillPaymentInfo({
      cardNumber: '4242424242424242',
      expiry: '12/25',
      cvc: '123'
    });

    await checkoutPage.placeOrder();

    expect(await checkoutPage.isOrderConfirmed()).toBe(true);
  });
});
```

### 2. **Test Fixtures and Factories**

```typescript
// framework/fixtures/database.ts
import { test as base } from '@playwright/test';
import { PrismaClient } from '@prisma/client';

export const test = base.extend<{
  db: PrismaClient;
  testUser: User;
  cleanupData: () => Promise<void>;
}>({
  db: async ({}, use) => {
    const db = new PrismaClient();
    await use(db);
    await db.$disconnect();
  },

  testUser: async ({ db }, use) => {
    const user = await db.user.create({
      data: {
        email: `test-${Date.now()}@example.com`,
        name: 'Test User',
        password: await hashPassword('password123'),
      },
    });
    await use(user);
    await db.user.delete({ where: { id: user.id } });
  },

  cleanupData: async ({ db }, use) => {
    const cleanup = async () => {
      await db.order.deleteMany({});
      await db.product.deleteMany({});
    };
    await use(cleanup);
  },
});

export { expect } from '@playwright/test';

// Usage in tests
import { test, expect } from '../framework/fixtures/database';

test('user can create order', async ({ db, testUser }) => {
  const product = await db.product.create({
    data: { name: 'Test Product', price: 99.99 }
  });

  const order = await db.order.create({
    data: {
      userId: testUser.id,
      items: {
        create: [{ productId: product.id, quantity: 1 }]
      }
    }
  });

  expect(order.userId).toBe(testUser.id);
});
```

### 3. **Custom Test Utilities**

```typescript
// framework/utils/helpers.ts
import { Page, expect } from '@playwright/test';

export class TestHelpers {
  static async waitForAPIResponse(
    page: Page,
    urlPattern: string | RegExp,
    action: () => Promise<void>
  ) {
    const responsePromise = page.waitForResponse(urlPattern);
    await action();
    return await responsePromise;
  }

  static async mockAPIResponse(
    page: Page,
    url: string | RegExp,
    response: any,
    status: number = 200
  ) {
    await page.route(url, route => {
      route.fulfill({
        status,
        contentType: 'application/json',
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
    const toast = page.locator('.toast-message');
    await expect(toast).toContainText(message);
    await expect(toast).toBeVisible();
  }
}

// Usage
import { TestHelpers } from '../framework/utils/helpers';

test('form submission', async ({ page }) => {
  await page.goto('/contact');

  await TestHelpers.fillForm(page, {
    name: 'John Doe',
    email: TestHelpers.generateTestEmail(),
    message: 'Test message'
  });

  await page.click('button[type="submit"]');

  await TestHelpers.verifyToastMessage(page, 'Message sent successfully');
});
```

### 4. **Configuration Management**

```typescript
// framework/config/config.ts
import * as dotenv from 'dotenv';

dotenv.config();

export interface TestConfig {
  baseUrl: string;
  apiUrl: string;
  timeout: number;
  headless: boolean;
  slowMo: number;
  screenshots: boolean;
  video: boolean;
  testUser: {
    email: string;
    password: string;
  };
}

const environments: Record<string, TestConfig> = {
  development: {
    baseUrl: 'http://localhost:3000',
    apiUrl: 'http://localhost:3001',
    timeout: 30000,
    headless: false,
    slowMo: 0,
    screenshots: true,
    video: false,
    testUser: {
      email: 'dev@test.com',
      password: 'devpass123',
    },
  },
  staging: {
    baseUrl: 'https://staging.example.com',
    apiUrl: 'https://api-staging.example.com',
    timeout: 60000,
    headless: true,
    slowMo: 0,
    screenshots: true,
    video: true,
    testUser: {
      email: process.env.STAGING_USER_EMAIL!,
      password: process.env.STAGING_USER_PASSWORD!,
    },
  },
  production: {
    baseUrl: 'https://example.com',
    apiUrl: 'https://api.example.com',
    timeout: 60000,
    headless: true,
    slowMo: 100,
    screenshots: true,
    video: true,
    testUser: {
      email: process.env.PROD_USER_EMAIL!,
      password: process.env.PROD_USER_PASSWORD!,
    },
  },
};

export const config: TestConfig =
  environments[process.env.TEST_ENV || 'development'];
```

### 5. **Custom Reporter**

```typescript
// framework/reporters/CustomReporter.ts
import { Reporter, TestCase, TestResult } from '@playwright/test/reporter';

class CustomReporter implements Reporter {
  private stats = {
    passed: 0,
    failed: 0,
    skipped: 0,
    total: 0,
  };

  onBegin() {
    console.log('Starting test run...');
  }

  onTestEnd(test: TestCase, result: TestResult) {
    this.stats.total++;

    if (result.status === 'passed') {
      this.stats.passed++;
      console.log(`✓ ${test.title}`);
    } else if (result.status === 'failed') {
      this.stats.failed++;
      console.log(`✗ ${test.title}`);
      console.log(`  Error: ${result.error?.message}`);
    } else if (result.status === 'skipped') {
      this.stats.skipped++;
      console.log(`⊘ ${test.title}`);
    }
  }

  onEnd() {
    console.log('\nTest Summary:');
    console.log(`  Total: ${this.stats.total}`);
    console.log(`  Passed: ${this.stats.passed}`);
    console.log(`  Failed: ${this.stats.failed}`);
    console.log(`  Skipped: ${this.stats.skipped}`);
  }
}

export default CustomReporter;
```

### 6. **pytest Framework (Python)**

```python
# framework/pages/base_page.py
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def goto(self, path: str):
        self.driver.get(f"{self.base_url}{path}")

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

# framework/conftest.py
import pytest
from selenium import webdriver
from framework.config import config

@pytest.fixture(scope='session')
def browser():
    """Setup browser for test session."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def page(browser):
    """Provide clean page for each test."""
    browser.delete_all_cookies()
    return browser

@pytest.fixture
def test_user(db_session):
    """Create test user."""
    from framework.factories import UserFactory
    user = UserFactory.create()
    db_session.add(user)
    db_session.commit()
    yield user
    db_session.delete(user)
    db_session.commit()

# tests/test_login.py
from framework.pages.login_page import LoginPage

def test_login_success(page, test_user):
    """Test successful login."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(test_user.email, 'password123')

    assert login_page.is_logged_in()
```

### 7. **Test Organization**

```
test-automation/
├── framework/
│   ├── pages/
│   │   ├── BasePage.ts
│   │   ├── LoginPage.ts
│   │   ├── ProductPage.ts
│   │   └── CheckoutPage.ts
│   ├── fixtures/
│   │   ├── database.ts
│   │   └── api.ts
│   ├── utils/
│   │   ├── helpers.ts
│   │   ├── validators.ts
│   │   └── waiters.ts
│   ├── config/
│   │   └── config.ts
│   └── reporters/
│       └── CustomReporter.ts
├── tests/
│   ├── e2e/
│   │   ├── checkout.test.ts
│   │   └── search.test.ts
│   ├── integration/
│   │   └── api.test.ts
│   ├── visual/
│   │   └── components.test.ts
│   └── accessibility/
│       └── a11y.test.ts
├── data/
│   ├── fixtures/
│   └── test-data.json
├── playwright.config.ts
└── package.json
```

## Framework Patterns

### Singleton Pattern
```typescript
class TestContext {
  private static instance: TestContext;
  private data: Map<string, any> = new Map();

  private constructor() {}

  static getInstance(): TestContext {
    if (!TestContext.instance) {
      TestContext.instance = new TestContext();
    }
    return TestContext.instance;
  }

  set(key: string, value: any): void {
    this.data.set(key, value);
  }

  get(key: string): any {
    return this.data.get(key);
  }
}
```

### Builder Pattern
```typescript
class TestDataBuilder {
  private data: Partial<User> = {};

  withEmail(email: string): this {
    this.data.email = email;
    return this;
  }

  withName(name: string): this {
    this.data.name = name;
    return this;
  }

  withRole(role: string): this {
    this.data.role = role;
    return this;
  }

  build(): User {
    return {
      email: this.data.email || 'test@example.com',
      name: this.data.name || 'Test User',
      role: this.data.role || 'user',
      ...this.data,
    } as User;
  }
}
```

## Best Practices

### ✅ DO
- Use Page Object Model for UI tests
- Create reusable test utilities
- Implement proper wait strategies
- Use fixtures for test data
- Configure for multiple environments
- Generate readable test reports
- Organize tests by feature/type
- Version control test framework

### ❌ DON'T
- Put test logic in page objects
- Use hard-coded waits (sleep)
- Duplicate test setup code
- Mix test data with test logic
- Skip error handling
- Ignore test flakiness
- Create overly complex abstractions
- Hardcode environment URLs

## Tools & Libraries

- **Playwright**: Modern browser automation
- **Selenium**: Cross-browser testing
- **Cypress**: JavaScript E2E framework
- **pytest**: Python testing framework
- **JUnit**: Java testing framework
- **TestNG**: Advanced Java framework
- **Robot Framework**: Keyword-driven testing

## Examples

See also: e2e-testing-automation, integration-testing, continuous-testing for implementing comprehensive test automation.
