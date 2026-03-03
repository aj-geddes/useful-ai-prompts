---
name: synthetic-monitoring
description: >
  Implement synthetic monitoring and automated testing to simulate user behavior
  and detect issues before users. Use when creating end-to-end test scenarios,
  monitoring API flows, or validating user workflows.
---

# Synthetic Monitoring

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Set up synthetic monitoring to automatically simulate real user journeys, API workflows, and critical business transactions to detect issues and validate performance.

## When to Use

- End-to-end workflow validation
- API flow testing
- User journey simulation
- Transaction monitoring
- Critical path validation

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Synthetic Tests with Playwright](references/synthetic-tests-with-playwright.md) | Synthetic Tests with Playwright |
| [API Synthetic Tests](references/api-synthetic-tests.md) | API Synthetic Tests |
| [Scheduled Synthetic Monitoring](references/scheduled-synthetic-monitoring.md) | Scheduled Synthetic Monitoring |

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
