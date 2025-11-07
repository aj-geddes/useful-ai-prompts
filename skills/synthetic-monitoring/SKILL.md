---
name: synthetic-monitoring
description: Implement synthetic monitoring and automated testing to simulate user behavior and detect issues before users. Use when creating end-to-end test scenarios, monitoring API flows, or validating user workflows.
---

# Synthetic Monitoring

## Overview

Set up synthetic monitoring to automatically simulate real user journeys, API workflows, and critical business transactions to detect issues and validate performance.

## When to Use

- End-to-end workflow validation
- API flow testing
- User journey simulation
- Transaction monitoring
- Critical path validation

## Instructions

### 1. **Synthetic Tests with Playwright**

```javascript
// synthetic-tests.js
const { chromium } = require('playwright');

class SyntheticMonitor {
  constructor(config = {}) {
    this.baseUrl = config.baseUrl || 'https://app.example.com';
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
      await page.goto(`${this.baseUrl}/login`, { waitUntil: 'networkidle' });
      metrics.steps.navigation = Date.now() - stepStart;

      // Step 2: Perform login
      stepStart = Date.now();
      await page.fill('input[name="email"]', 'test@example.com');
      await page.fill('input[name="password"]', 'password123');
      await page.click('button[type="submit"]');
      await page.waitForNavigation({ waitUntil: 'networkidle' });
      metrics.steps.login = Date.now() - stepStart;

      // Step 3: Navigate to dashboard
      stepStart = Date.now();
      await page.goto(`${this.baseUrl}/dashboard`, { waitUntil: 'networkidle' });
      metrics.steps.dashboard = Date.now() - stepStart;

      // Step 4: Search for products
      stepStart = Date.now();
      await page.fill('input[placeholder="Search products"]', 'laptop');
      await page.waitForSelector('.product-list');
      metrics.steps.search = Date.now() - stepStart;

      // Step 5: Add to cart
      stepStart = Date.now();
      const firstProduct = await page.$('.product-item');
      if (firstProduct) {
        await firstProduct.click();
        await page.click('button:has-text("Add to Cart")');
        await page.waitForSelector('[data-testid="cart-count"]');
      }
      metrics.steps.addToCart = Date.now() - stepStart;

      metrics.totalTime = Date.now() - startTime;
      metrics.status = 'success';
    } catch (error) {
      metrics.status = 'failed';
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
      ...chromium.devices['iPhone 12']
    });
    const page = await context.newPage();

    try {
      const metrics = { device: 'iPhone 12', steps: {} };
      const startTime = Date.now();

      let stepStart = Date.now();
      await page.goto(this.baseUrl, { waitUntil: 'networkidle' });
      metrics.steps.navigation = Date.now() - stepStart;

      const viewport = page.viewportSize();
      metrics.viewport = viewport;

      stepStart = Date.now();
      await page.click('.menu-toggle');
      await page.waitForSelector('.mobile-menu.open');
      metrics.steps.mobileInteraction = Date.now() - stepStart;

      metrics.totalTime = Date.now() - startTime;
      metrics.status = 'success';

      return metrics;
    } catch (error) {
      return { status: 'failed', error: error.message, device: 'iPhone 12' };
    } finally {
      await browser.close();
    }
  }

  async testWithPerformanceMetrics() {
    const browser = await chromium.launch();
    const page = await browser.newPage();

    try {
      await page.goto(this.baseUrl, { waitUntil: 'networkidle' });

      const perfMetrics = JSON.parse(
        await page.evaluate(() => JSON.stringify(window.performance.timing))
      );

      const metrics = {
        navigationTiming: {
          domInteractive: perfMetrics.domInteractive - perfMetrics.navigationStart,
          domComplete: perfMetrics.domComplete - perfMetrics.navigationStart,
          loadComplete: perfMetrics.loadEventEnd - perfMetrics.navigationStart
        },
        status: 'success'
      };

      return metrics;
    } catch (error) {
      return { status: 'failed', error: error.message };
    } finally {
      await browser.close();
    }
  }

  async recordMetrics(testName, metrics) {
    try {
      await axios.post('http://monitoring-service/synthetic-results', {
        testName,
        timestamp: new Date(),
        metrics,
        passed: metrics.status === 'success'
      });
    } catch (error) {
      console.error('Failed to record metrics:', error);
    }
  }
}

module.exports = SyntheticMonitor;
```

### 2. **API Synthetic Tests**

```javascript
// api-synthetic-tests.js
const axios = require('axios');

class APISyntheticTests {
  constructor(config = {}) {
    this.baseUrl = config.baseUrl || 'https://api.example.com';
    this.client = axios.create({ baseURL: this.baseUrl });
  }

  async testAuthenticationFlow() {
    const results = { steps: {}, status: 'success' };

    try {
      const registerStart = Date.now();
      const registerRes = await this.client.post('/auth/register', {
        email: `test-${Date.now()}@example.com`,
        password: 'Test@123456'
      });
      results.steps.register = Date.now() - registerStart;

      if (registerRes.status !== 201) throw new Error('Registration failed');

      const loginStart = Date.now();
      const loginRes = await this.client.post('/auth/login', {
        email: registerRes.data.email,
        password: 'Test@123456'
      });
      results.steps.login = Date.now() - loginStart;

      const token = loginRes.data.token;

      const authStart = Date.now();
      await this.client.get('/api/profile', {
        headers: { Authorization: `Bearer ${token}` }
      });
      results.steps.authenticatedRequest = Date.now() - authStart;

      const logoutStart = Date.now();
      await this.client.post('/auth/logout', {}, {
        headers: { Authorization: `Bearer ${token}` }
      });
      results.steps.logout = Date.now() - logoutStart;

      return results;
    } catch (error) {
      results.status = 'failed';
      results.error = error.message;
      return results;
    }
  }

  async testTransactionFlow() {
    const results = { steps: {}, status: 'success' };

    try {
      const orderStart = Date.now();
      const orderRes = await this.client.post('/api/orders', {
        items: [{ sku: 'ITEM-001', quantity: 2 }]
      }, {
        headers: { 'X-Idempotency-Key': `order-${Date.now()}` }
      });
      results.steps.createOrder = Date.now() - orderStart;

      const getStart = Date.now();
      const getRes = await this.client.get(`/api/orders/${orderRes.data.id}`);
      results.steps.getOrder = Date.now() - getStart;

      const paymentStart = Date.now();
      await this.client.post(`/api/orders/${orderRes.data.id}/payment`, {
        method: 'credit_card',
        amount: getRes.data.total
      });
      results.steps.processPayment = Date.now() - paymentStart;

      return results;
    } catch (error) {
      results.status = 'failed';
      results.error = error.message;
      return results;
    }
  }

  async testUnderLoad(concurrentUsers = 10, duration = 60000) {
    const startTime = Date.now();
    const results = {
      totalRequests: 0,
      successfulRequests: 0,
      failedRequests: 0,
      averageResponseTime: 0,
      p95ResponseTime: 0
    };

    const responseTimes = [];

    const makeRequest = async () => {
      const reqStart = Date.now();
      try {
        await this.client.get('/api/health');
        results.successfulRequests++;
        responseTimes.push(Date.now() - reqStart);
      } catch {
        results.failedRequests++;
      }
      results.totalRequests++;
    };

    const userSimulations = Array(concurrentUsers).fill(null).map(async () => {
      while (Date.now() - startTime < duration) {
        await makeRequest();
        await new Promise(r => setTimeout(r, Math.random() * 1000));
      }
    });

    await Promise.all(userSimulations);

    responseTimes.sort((a, b) => a - b);
    results.averageResponseTime =
      responseTimes.reduce((a, b) => a + b, 0) / responseTimes.length;
    results.p95ResponseTime =
      responseTimes[Math.floor(responseTimes.length * 0.95)];

    return results;
  }
}

module.exports = APISyntheticTests;
```

### 3. **Scheduled Synthetic Monitoring**

```javascript
// scheduled-monitor.js
const cron = require('node-cron');
const SyntheticMonitor = require('./synthetic-tests');
const APISyntheticTests = require('./api-synthetic-tests');
const axios = require('axios');

class ScheduledSyntheticMonitor {
  constructor(config = {}) {
    this.eMonitor = new SyntheticMonitor(config);
    this.apiTests = new APISyntheticTests(config);
    this.alertThreshold = config.alertThreshold || 5000;
  }

  start() {
    cron.schedule('*/5 * * * *', () => this.runE2ETests());
    cron.schedule('*/2 * * * *', () => this.runAPITests());
    cron.schedule('0 * * * *', () => this.runLoadTest());
  }

  async runE2ETests() {
    try {
      const metrics = await this.eMonitor.testUserFlow();
      await this.recordResults('e2e-user-flow', metrics);

      if (metrics.totalTime > this.alertThreshold) {
        await this.sendAlert('e2e-user-flow', metrics);
      }
    } catch (error) {
      console.error('E2E test failed:', error);
    }
  }

  async runAPITests() {
    try {
      const authMetrics = await this.apiTests.testAuthenticationFlow();
      const transactionMetrics = await this.apiTests.testTransactionFlow();

      await this.recordResults('api-auth-flow', authMetrics);
      await this.recordResults('api-transaction-flow', transactionMetrics);

      if (authMetrics.status === 'failed' || transactionMetrics.status === 'failed') {
        await this.sendAlert('api-tests', { authMetrics, transactionMetrics });
      }
    } catch (error) {
      console.error('API test failed:', error);
    }
  }

  async runLoadTest() {
    try {
      const results = await this.apiTests.testUnderLoad(10, 30000);
      await this.recordResults('load-test', results);

      if (results.failedRequests > 0) {
        await this.sendAlert('load-test', results);
      }
    } catch (error) {
      console.error('Load test failed:', error);
    }
  }

  async recordResults(testName, metrics) {
    try {
      await axios.post('http://monitoring-service/synthetic-results', {
        testName,
        timestamp: new Date(),
        metrics
      });
      console.log(`Recorded: ${testName}`, metrics);
    } catch (error) {
      console.error('Failed to record results:', error);
    }
  }

  async sendAlert(testName, metrics) {
    try {
      await axios.post('http://alerting-service/alerts', {
        type: 'synthetic_monitoring',
        testName,
        severity: 'warning',
        message: `Synthetic test '${testName}' has issues`,
        metrics,
        timestamp: new Date()
      });
      console.log(`Alert sent for ${testName}`);
    } catch (error) {
      console.error('Failed to send alert:', error);
    }
  }
}

module.exports = ScheduledSyntheticMonitor;
```

## Best Practices

### ✅ DO
- Test critical user journeys
- Simulate real browser conditions
- Monitor from multiple locations
- Track response times
- Alert on test failures
- Rotate test data
- Test mobile and desktop
- Include error scenarios

### ❌ DON'T
- Test with production data
- Reuse test accounts
- Skip timeout configurations
- Ignore test maintenance
- Test too frequently
- Hard-code credentials
- Ignore geographic variations
- Test only happy paths

## Key Metrics

- Response time
- Success rate
- Availability
- Core Web Vitals
- Error rate
