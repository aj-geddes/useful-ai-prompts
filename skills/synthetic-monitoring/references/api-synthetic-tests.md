# API Synthetic Tests

## API Synthetic Tests

```javascript
// api-synthetic-tests.js
const axios = require("axios");

class APISyntheticTests {
  constructor(config = {}) {
    this.baseUrl = config.baseUrl || "https://api.example.com";
    this.client = axios.create({ baseURL: this.baseUrl });
  }

  async testAuthenticationFlow() {
    const results = { steps: {}, status: "success" };

    try {
      const registerStart = Date.now();
      const registerRes = await this.client.post("/auth/register", {
        email: `test-${Date.now()}@example.com`,
        password: "Test@123456",
      });
      results.steps.register = Date.now() - registerStart;

      if (registerRes.status !== 201) throw new Error("Registration failed");

      const loginStart = Date.now();
      const loginRes = await this.client.post("/auth/login", {
        email: registerRes.data.email,
        password: "Test@123456",
      });
      results.steps.login = Date.now() - loginStart;

      const token = loginRes.data.token;

      const authStart = Date.now();
      await this.client.get("/api/profile", {
        headers: { Authorization: `Bearer ${token}` },
      });
      results.steps.authenticatedRequest = Date.now() - authStart;

      const logoutStart = Date.now();
      await this.client.post(
        "/auth/logout",
        {},
        {
          headers: { Authorization: `Bearer ${token}` },
        },
      );
      results.steps.logout = Date.now() - logoutStart;

      return results;
    } catch (error) {
      results.status = "failed";
      results.error = error.message;
      return results;
    }
  }

  async testTransactionFlow() {
    const results = { steps: {}, status: "success" };

    try {
      const orderStart = Date.now();
      const orderRes = await this.client.post(
        "/api/orders",
        {
          items: [{ sku: "ITEM-001", quantity: 2 }],
        },
        {
          headers: { "X-Idempotency-Key": `order-${Date.now()}` },
        },
      );
      results.steps.createOrder = Date.now() - orderStart;

      const getStart = Date.now();
      const getRes = await this.client.get(`/api/orders/${orderRes.data.id}`);
      results.steps.getOrder = Date.now() - getStart;

      const paymentStart = Date.now();
      await this.client.post(`/api/orders/${orderRes.data.id}/payment`, {
        method: "credit_card",
        amount: getRes.data.total,
      });
      results.steps.processPayment = Date.now() - paymentStart;

      return results;
    } catch (error) {
      results.status = "failed";
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
      p95ResponseTime: 0,
    };

    const responseTimes = [];

    const makeRequest = async () => {
      const reqStart = Date.now();
      try {
        await this.client.get("/api/health");
        results.successfulRequests++;
        responseTimes.push(Date.now() - reqStart);
      } catch {
        results.failedRequests++;
      }
      results.totalRequests++;
    };

    const userSimulations = Array(concurrentUsers)
      .fill(null)
      .map(async () => {
        while (Date.now() - startTime < duration) {
          await makeRequest();
          await new Promise((r) => setTimeout(r, Math.random() * 1000));
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
