# Synthetic Tests with Playwright

## Synthetic Tests with Playwright

```javascript
// synthetic-tests.js
const { chromium } = require("playwright");

class SyntheticMonitor {
  constructor(config = {}) {
    this.baseUrl = config.baseUrl || "https://app.example.com";
    this.timeout = config.timeout || 30000;
  }

  async testUserFlow() {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    const metrics = { steps: {} };
    const startTime = Date.now();

    try {
      // Step 1: Navigate to login
      let stepStart = Date.now();
      await page.goto(`${this.baseUrl}/login`, { waitUntil: "networkidle" });
      metrics.steps.navigation = Date.now() - stepStart;

      // Step 2: Perform login
      stepStart = Date.now();
      await page.fill('input[name="email"]', "test@example.com");
      await page.fill('input[name="password"]', "password123");
      await page.click('button[type="submit"]');
      await page.waitForNavigation({ waitUntil: "networkidle" });
      metrics.steps.login = Date.now() - stepStart;

      // Step 3: Navigate to dashboard
      stepStart = Date.now();
      await page.goto(`${this.baseUrl}/dashboard`, {
        waitUntil: "networkidle",
      });
      metrics.steps.dashboard = Date.now() - stepStart;

      // Step 4: Search for products
      stepStart = Date.now();
      await page.fill('input[placeholder="Search products"]', "laptop");
      await page.waitForSelector(".product-list");
      metrics.steps.search = Date.now() - stepStart;

      // Step 5: Add to cart
      stepStart = Date.now();
      const firstProduct = await page.$(".product-item");
      if (firstProduct) {
        await firstProduct.click();
        await page.click('button:has-text("Add to Cart")');
        await page.waitForSelector('[data-testid="cart-count"]');
      }
      metrics.steps.addToCart = Date.now() - stepStart;

      metrics.totalTime = Date.now() - startTime;
      metrics.status = "success";
    } catch (error) {
      metrics.status = "failed";
      metrics.error = error.message;
      metrics.totalTime = Date.now() - startTime;
    } finally {
      await browser.close();
    }

    return metrics;
  }

  async testMobileUserFlow() {
    const browser = await chromium.launch();
    const context = await browser.createBrowserContext({
      ...chromium.devices["iPhone 12"],
    });
    const page = await context.newPage();

    try {
      const metrics = { device: "iPhone 12", steps: {} };
      const startTime = Date.now();

      let stepStart = Date.now();
      await page.goto(this.baseUrl, { waitUntil: "networkidle" });
      metrics.steps.navigation = Date.now() - stepStart;

      const viewport = page.viewportSize();
      metrics.viewport = viewport;

      stepStart = Date.now();
      await page.click(".menu-toggle");
      await page.waitForSelector(".mobile-menu.open");
      metrics.steps.mobileInteraction = Date.now() - stepStart;

      metrics.totalTime = Date.now() - startTime;
      metrics.status = "success";

      return metrics;
    } catch (error) {
      return { status: "failed", error: error.message, device: "iPhone 12" };
    } finally {
      await browser.close();
    }
  }

  async testWithPerformanceMetrics() {
    const browser = await chromium.launch();
    const page = await browser.newPage();

    try {
      await page.goto(this.baseUrl, { waitUntil: "networkidle" });

      const perfMetrics = JSON.parse(
        await page.evaluate(() => JSON.stringify(window.performance.timing)),
      );

      const metrics = {
        navigationTiming: {
          domInteractive:
            perfMetrics.domInteractive - perfMetrics.navigationStart,
          domComplete: perfMetrics.domComplete - perfMetrics.navigationStart,
          loadComplete: perfMetrics.loadEventEnd - perfMetrics.navigationStart,
        },
        status: "success",
      };

      return metrics;
    } catch (error) {
      return { status: "failed", error: error.message };
    } finally {
      await browser.close();
    }
  }

  async recordMetrics(testName, metrics) {
    try {
      await axios.post("http://monitoring-service/synthetic-results", {
        testName,
        timestamp: new Date(),
        metrics,
        passed: metrics.status === "success",
      });
    } catch (error) {
      console.error("Failed to record metrics:", error);
    }
  }
}

module.exports = SyntheticMonitor;
```
