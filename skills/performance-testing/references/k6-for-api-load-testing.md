# k6 for API Load Testing

## k6 for API Load Testing

```javascript
// load-test.js
import http from "k6/http";
import { check, sleep } from "k6";
import { Rate, Trend } from "k6/metrics";

// Custom metrics
const errorRate = new Rate("errors");
const orderDuration = new Trend("order_duration");

// Test configuration
export const options = {
  stages: [
    { duration: "2m", target: 10 }, // Ramp up to 10 users
    { duration: "5m", target: 10 }, // Stay at 10 users
    { duration: "2m", target: 50 }, // Ramp up to 50 users
    { duration: "5m", target: 50 }, // Stay at 50 users
    { duration: "2m", target: 0 }, // Ramp down to 0
  ],
  thresholds: {
    http_req_duration: ["p(95)<500"], // 95% of requests under 500ms
    http_req_failed: ["rate<0.01"], // Error rate under 1%
    errors: ["rate<0.1"], // Custom error rate under 10%
  },
};

// Test data
const BASE_URL = "https://api.example.com";
let authToken;

export function setup() {
  // Login once and get auth token
  const loginRes = http.post(`${BASE_URL}/auth/login`, {
    email: "test@example.com",
    password: "password123",
  });

  return { token: loginRes.json("token") };
}

export default function (data) {
  // Test 1: Get products (read-heavy)
  const productsRes = http.get(`${BASE_URL}/products`, {
    headers: { Authorization: `Bearer ${data.token}` },
  });

  check(productsRes, {
    "products status is 200": (r) => r.status === 200,
    "products response time < 200ms": (r) => r.timings.duration < 200,
    "has products array": (r) => Array.isArray(r.json("products")),
  }) || errorRate.add(1);

  sleep(1);

  // Test 2: Create order (write-heavy)
  const orderPayload = JSON.stringify({
    userId: "user-123",
    items: [
      { productId: "prod-1", quantity: 2 },
      { productId: "prod-2", quantity: 1 },
    ],
  });

  const orderRes = http.post(`${BASE_URL}/orders`, orderPayload, {
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${data.token}`,
    },
  });

  const orderSuccess = check(orderRes, {
    "order status is 201": (r) => r.status === 201,
    "order has id": (r) => r.json("id") !== undefined,
  });

  if (!orderSuccess) {
    errorRate.add(1);
  }

  orderDuration.add(orderRes.timings.duration);

  sleep(2);

  // Test 3: Get order details
  if (orderSuccess) {
    const orderId = orderRes.json("id");
    const orderDetailRes = http.get(`${BASE_URL}/orders/${orderId}`, {
      headers: { Authorization: `Bearer ${data.token}` },
    });

    check(orderDetailRes, {
      "order detail status is 200": (r) => r.status === 200,
    }) || errorRate.add(1);
  }

  sleep(1);
}

export function teardown(data) {
  // Cleanup if needed
}
```

```bash
# Run k6 test
k6 run load-test.js

# Run with different scenarios
k6 run --vus 100 --duration 30s load-test.js

# Output to InfluxDB for visualization
k6 run --out influxdb=http://localhost:8086/k6 load-test.js
```
