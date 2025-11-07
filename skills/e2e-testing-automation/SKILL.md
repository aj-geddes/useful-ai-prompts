---
name: e2e-testing-automation
description: Build end-to-end automated tests that simulate real user interactions across the full application stack. Use for E2E test, Selenium, Cypress, Playwright, browser automation, and user journey testing.
---

# E2E Testing Automation

## Overview

End-to-end (E2E) testing validates complete user workflows from the UI through all backend systems, ensuring the entire application stack works together correctly from a user's perspective. E2E tests simulate real user interactions with browsers, handling authentication, navigation, form submissions, and validating results.

## When to Use

- Testing critical user journeys (signup, checkout, login)
- Validating multi-step workflows
- Testing across different browsers and devices
- Regression testing for UI changes
- Verifying frontend-backend integration
- Testing with real user interactions (clicks, typing, scrolling)
- Smoke testing deployments

## Instructions

### 1. **Playwright E2E Tests**

```typescript
// tests/e2e/checkout.spec.ts
import { test, expect, Page } from '@playwright/test';

test.describe('E-commerce Checkout Flow', () => {
  let page: Page;

  test.beforeEach(async ({ page: p }) => {
    page = p;
    await page.goto('/');
  });

  test('complete checkout flow as guest user', async () => {
    // 1. Browse and add product to cart
    await page.click('text=Shop Now');
    await page.click('[data-testid="product-1"]');
    await expect(page.locator('h1')).toContainText('Product Name');

    await page.click('button:has-text("Add to Cart")');
    await expect(page.locator('.cart-count')).toHaveText('1');

    // 2. Go to cart and proceed to checkout
    await page.click('[data-testid="cart-icon"]');
    await expect(page.locator('.cart-item')).toHaveCount(1);
    await page.click('text=Proceed to Checkout');

    // 3. Fill shipping information
    await page.fill('[name="email"]', 'test@example.com');
    await page.fill('[name="firstName"]', 'John');
    await page.fill('[name="lastName"]', 'Doe');
    await page.fill('[name="address"]', '123 Main St');
    await page.fill('[name="city"]', 'San Francisco');
    await page.selectOption('[name="state"]', 'CA');
    await page.fill('[name="zip"]', '94105');

    // 4. Enter payment information
    await page.click('text=Continue to Payment');

    // Wait for payment iframe to load
    const paymentFrame = page.frameLocator('iframe[name="payment-frame"]');
    await paymentFrame.locator('[name="cardNumber"]').fill('4242424242424242');
    await paymentFrame.locator('[name="expiry"]').fill('12/25');
    await paymentFrame.locator('[name="cvc"]').fill('123');

    // 5. Complete order
    await page.click('button:has-text("Place Order")');

    // 6. Verify success
    await expect(page).toHaveURL(/\/order\/confirmation/);
    await expect(page.locator('.confirmation-message')).toContainText('Order placed successfully');

    const orderNumber = await page.locator('[data-testid="order-number"]').textContent();
    expect(orderNumber).toMatch(/^ORD-\d+$/);
  });

  test('checkout with existing user account', async () => {
    // Login first
    await page.click('text=Sign In');
    await page.fill('[name="email"]', 'existing@example.com');
    await page.fill('[name="password"]', 'Password123!');
    await page.click('button[type="submit"]');

    await expect(page.locator('.user-menu')).toContainText('existing@example.com');

    // Add product and checkout with saved information
    await page.click('[data-testid="product-2"]');
    await page.click('button:has-text("Add to Cart")');
    await page.click('[data-testid="cart-icon"]');
    await page.click('text=Checkout');

    // Verify saved address is pre-filled
    await expect(page.locator('[name="address"]')).toHaveValue(/./);

    // Complete checkout
    await page.click('button:has-text("Use Saved Payment")');
    await page.click('button:has-text("Place Order")');

    await expect(page).toHaveURL(/\/order\/confirmation/);
  });

  test('handle out of stock product', async () => {
    await page.click('[data-testid="product-out-of-stock"]');

    const addToCartButton = page.locator('button:has-text("Add to Cart")');
    await expect(addToCartButton).toBeDisabled();
    await expect(page.locator('.stock-status')).toHaveText('Out of Stock');
  });
});
```

### 2. **Cypress E2E Tests**

```javascript
// cypress/e2e/authentication.cy.js
describe('User Authentication Flow', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  it('should register a new user account', () => {
    cy.get('[data-cy="signup-button"]').click();
    cy.url().should('include', '/signup');

    // Fill registration form
    const timestamp = Date.now();
    cy.get('[name="email"]').type(`user${timestamp}@example.com`);
    cy.get('[name="password"]').type('SecurePass123!');
    cy.get('[name="confirmPassword"]').type('SecurePass123!');
    cy.get('[name="firstName"]').type('Test');
    cy.get('[name="lastName"]').type('User');

    // Accept terms
    cy.get('[name="acceptTerms"]').check();

    // Submit form
    cy.get('button[type="submit"]').click();

    // Verify success
    cy.url().should('include', '/dashboard');
    cy.get('.welcome-message').should('contain', 'Welcome, Test!');

    // Verify email sent (check via API)
    cy.request(`/api/test/emails/${timestamp}@example.com`)
      .its('body')
      .should('have.property', 'subject', 'Welcome to Our App');
  });

  it('should handle validation errors', () => {
    cy.get('[data-cy="signup-button"]').click();

    // Submit empty form
    cy.get('button[type="submit"]').click();

    // Check for validation errors
    cy.get('.error-message').should('have.length.greaterThan', 0);
    cy.get('[name="email"]')
      .parent()
      .should('contain', 'Email is required');

    // Fill invalid email
    cy.get('[name="email"]').type('invalid-email');
    cy.get('[name="password"]').type('weak');
    cy.get('button[type="submit"]').click();

    cy.get('[name="email"]')
      .parent()
      .should('contain', 'Invalid email format');
    cy.get('[name="password"]')
      .parent()
      .should('contain', 'Password must be at least 8 characters');
  });

  it('should login with valid credentials', () => {
    // Create test user first
    cy.request('POST', '/api/test/users', {
      email: 'test@example.com',
      password: 'Password123!',
      name: 'Test User'
    });

    // Login
    cy.get('[data-cy="login-button"]').click();
    cy.get('[name="email"]').type('test@example.com');
    cy.get('[name="password"]').type('Password123!');
    cy.get('button[type="submit"]').click();

    // Verify login successful
    cy.url().should('include', '/dashboard');
    cy.getCookie('auth_token').should('exist');

    // Verify user menu
    cy.get('[data-cy="user-menu"]').click();
    cy.get('.user-email').should('contain', 'test@example.com');
  });

  it('should maintain session across page reloads', () => {
    // Login
    cy.loginViaAPI('test@example.com', 'Password123!');
    cy.visit('/dashboard');

    // Verify logged in
    cy.get('.user-menu').should('exist');

    // Reload page
    cy.reload();

    // Still logged in
    cy.get('.user-menu').should('exist');
    cy.getCookie('auth_token').should('exist');
  });

  it('should logout successfully', () => {
    cy.loginViaAPI('test@example.com', 'Password123!');
    cy.visit('/dashboard');

    cy.get('[data-cy="user-menu"]').click();
    cy.get('[data-cy="logout-button"]').click();

    cy.url().should('equal', Cypress.config().baseUrl + '/');
    cy.getCookie('auth_token').should('not.exist');
  });
});

// Custom command for login
Cypress.Commands.add('loginViaAPI', (email, password) => {
  cy.request('POST', '/api/auth/login', { email, password })
    .then((response) => {
      window.localStorage.setItem('auth_token', response.body.token);
    });
});
```

### 3. **Selenium with Python (pytest)**

```python
# tests/e2e/test_search_functionality.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestSearchFunctionality:
    @pytest.fixture
    def driver(self):
        """Setup and teardown browser."""
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    def test_search_with_results(self, driver):
        """Test search functionality returns relevant results."""
        driver.get('http://localhost:3000')

        # Find search box and enter query
        search_box = driver.find_element(By.NAME, 'search')
        search_box.send_keys('laptop')
        search_box.send_keys(Keys.RETURN)

        # Wait for results
        wait = WebDriverWait(driver, 10)
        results = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'search-result'))
        )

        # Verify results
        assert len(results) > 0
        assert 'laptop' in driver.page_source.lower()

        # Check first result has required elements
        first_result = results[0]
        assert first_result.find_element(By.CLASS_NAME, 'product-title')
        assert first_result.find_element(By.CLASS_NAME, 'product-price')
        assert first_result.find_element(By.CLASS_NAME, 'product-image')

    def test_search_filters(self, driver):
        """Test applying filters to search results."""
        driver.get('http://localhost:3000/search?q=laptop')

        wait = WebDriverWait(driver, 10)

        # Wait for results to load
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-result'))
        )

        initial_count = len(driver.find_elements(By.CLASS_NAME, 'search-result'))

        # Apply price filter
        price_filter = driver.find_element(By.ID, 'price-filter-500-1000')
        price_filter.click()

        # Wait for filtered results
        wait.until(
            EC.staleness_of(driver.find_element(By.CLASS_NAME, 'search-result'))
        )
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-result'))
        )

        filtered_count = len(driver.find_elements(By.CLASS_NAME, 'search-result'))

        # Verify filter was applied
        assert filtered_count <= initial_count

        # Verify all prices are in range
        prices = driver.find_elements(By.CLASS_NAME, 'product-price')
        for price_elem in prices:
            price = float(price_elem.text.replace('$', '').replace(',', ''))
            assert 500 <= price <= 1000

    def test_pagination(self, driver):
        """Test navigating through search result pages."""
        driver.get('http://localhost:3000/search?q=electronics')

        wait = WebDriverWait(driver, 10)

        # Get first page results
        first_page_results = driver.find_elements(By.CLASS_NAME, 'search-result')
        first_result_title = first_page_results[0].find_element(
            By.CLASS_NAME, 'product-title'
        ).text

        # Click next page
        next_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Next page"]')
        next_button.click()

        # Wait for new results
        wait.until(EC.staleness_of(first_page_results[0]))

        # Verify on page 2
        assert 'page=2' in driver.current_url

        second_page_results = driver.find_elements(By.CLASS_NAME, 'search-result')
        second_result_title = second_page_results[0].find_element(
            By.CLASS_NAME, 'product-title'
        ).text

        # Results should be different
        assert first_result_title != second_result_title

    def test_empty_search_results(self, driver):
        """Test handling of searches with no results."""
        driver.get('http://localhost:3000')

        search_box = driver.find_element(By.NAME, 'search')
        search_box.send_keys('xyznonexistentproduct123')
        search_box.send_keys(Keys.RETURN)

        wait = WebDriverWait(driver, 10)
        no_results = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'no-results'))
        )

        assert 'no results found' in no_results.text.lower()
        assert len(driver.find_elements(By.CLASS_NAME, 'search-result')) == 0
```

### 4. **Page Object Model Pattern**

```typescript
// pages/LoginPage.ts
import { Page, Locator } from '@playwright/test';

export class LoginPage {
  readonly page: Page;
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly errorMessage: Locator;

  constructor(page: Page) {
    this.page = page;
    this.emailInput = page.locator('[name="email"]');
    this.passwordInput = page.locator('[name="password"]');
    this.loginButton = page.locator('button[type="submit"]');
    this.errorMessage = page.locator('.error-message');
  }

  async goto() {
    await this.page.goto('/login');
  }

  async login(email: string, password: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }

  async getErrorMessage(): Promise<string> {
    return await this.errorMessage.textContent();
  }
}

// tests/login.spec.ts
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

test('login with invalid credentials', async ({ page }) => {
  const loginPage = new LoginPage(page);
  await loginPage.goto();
  await loginPage.login('invalid@example.com', 'wrongpassword');

  const error = await loginPage.getErrorMessage();
  expect(error).toContain('Invalid credentials');
});
```

## Best Practices

### ✅ DO
- Use data-testid attributes for stable selectors
- Implement Page Object Model for maintainability
- Test critical user journeys thoroughly
- Run tests in multiple browsers (cross-browser testing)
- Use explicit waits instead of sleep/timeouts
- Clean up test data after each test
- Take screenshots on failures
- Parallelize test execution where possible

### ❌ DON'T
- Use brittle CSS selectors (like nth-child)
- Test every possible UI combination (focus on critical paths)
- Share state between tests
- Use fixed delays (sleep/timeout)
- Ignore flaky tests
- Run E2E tests for unit-level testing
- Test third-party UI components in detail
- Skip mobile/responsive testing

## Tools & Frameworks

- **Playwright**: Modern, fast, reliable (Node.js, Python, Java, .NET)
- **Cypress**: Developer-friendly, fast feedback loop (JavaScript)
- **Selenium**: Cross-browser, mature ecosystem (multiple languages)
- **Puppeteer**: Chrome DevTools Protocol automation (Node.js)
- **WebDriverIO**: Next-gen browser automation (Node.js)

## Configuration Examples

```javascript
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e',
  timeout: 30000,
  retries: 2,
  workers: process.env.CI ? 2 : 4,

  use: {
    baseURL: 'http://localhost:3000',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    trace: 'on-first-retry',
  },

  projects: [
    { name: 'chromium', use: { browserName: 'chromium' } },
    { name: 'firefox', use: { browserName: 'firefox' } },
    { name: 'webkit', use: { browserName: 'webkit' } },
  ],

  webServer: {
    command: 'npm run start',
    port: 3000,
    reuseExistingServer: !process.env.CI,
  },
});
```

## Examples

See also: integration-testing, visual-regression-testing, accessibility-testing, test-automation-framework skills.
