# Third-Party Client Wrapper

## Third-Party Client Wrapper

```javascript
const axios = require("axios");

class ThirdPartyClient {
  constructor(config) {
    this.apiKey = config.apiKey;
    this.baseUrl = config.baseUrl;
    this.timeout = config.timeout || 30000;
    this.retryAttempts = config.retryAttempts || 3;
    this.retryDelay = config.retryDelay || 1000;
    this.client = axios.create({
      baseURL: this.baseUrl,
      timeout: this.timeout,
      headers: {
        Authorization: `Bearer ${this.apiKey}`,
        "Content-Type": "application/json",
      },
    });
  }

  async request(method, endpoint, data = null, options = {}) {
    let lastError;

    for (let attempt = 0; attempt < this.retryAttempts; attempt++) {
      try {
        const response = await this.client({
          method,
          url: endpoint,
          data,
          timeout: this.timeout,
          ...options,
        });

        return {
          success: true,
          data: response.data,
          statusCode: response.status,
          headers: response.headers,
        };
      } catch (error) {
        lastError = error;

        // Check if error is retryable
        if (!this.isRetryable(error) || attempt === this.retryAttempts - 1) {
          break;
        }

        // Exponential backoff
        const delay = this.retryDelay * Math.pow(2, attempt);
        await this.sleep(delay);
      }
    }

    return this.handleError(lastError);
  }

  isRetryable(error) {
    if (!error.response) return true; // Network error

    const status = error.response.status;
    // Retry on 5xx and specific 4xx errors
    return status >= 500 || [408, 429].includes(status);
  }

  handleError(error) {
    if (error.response) {
      return {
        success: false,
        error: {
          message: error.response.data?.message || error.message,
          code: error.response.data?.code || error.response.status,
          status: error.response.status,
          data: error.response.data,
        },
      };
    }

    return {
      success: false,
      error: {
        message: error.message,
        code: "NETWORK_ERROR",
      },
    };
  }

  sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  async get(endpoint) {
    return this.request("GET", endpoint);
  }

  async post(endpoint, data) {
    return this.request("POST", endpoint, data);
  }

  async put(endpoint, data) {
    return this.request("PUT", endpoint, data);
  }

  async delete(endpoint) {
    return this.request("DELETE", endpoint);
  }
}

// Usage
const stripeClient = new ThirdPartyClient({
  apiKey: process.env.STRIPE_API_KEY,
  baseUrl: "https://api.stripe.com/v1",
  timeout: 30000,
  retryAttempts: 3,
});

const result = await stripeClient.post("/charges", {
  amount: 10000,
  currency: "usd",
  source: "tok_visa",
});
```
