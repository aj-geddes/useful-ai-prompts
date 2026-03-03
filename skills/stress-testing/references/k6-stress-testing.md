# k6 Stress Testing

## k6 Stress Testing

```javascript
// stress-test.js
import http from "k6/http";
import { check, sleep } from "k6";
import { Rate } from "k6/metrics";

const errorRate = new Rate("errors");

export const options = {
  stages: [
    // Stress testing: Progressive load increase
    { duration: "2m", target: 100 }, // Normal load
    { duration: "5m", target: 100 }, // Sustain normal
    { duration: "2m", target: 200 }, // Above normal
    { duration: "5m", target: 200 }, // Sustain above normal
    { duration: "2m", target: 300 }, // Breaking point approaching
    { duration: "5m", target: 300 }, // Sustain high load
    { duration: "2m", target: 400 }, // Beyond capacity
    { duration: "5m", target: 400 }, // System under stress
    { duration: "5m", target: 0 }, // Gradual recovery
  ],
  thresholds: {
    http_req_duration: ["p(99)<1000"], // 99% under 1s during stress
    http_req_failed: ["rate<0.05"], // Allow 5% error rate under stress
    errors: ["rate<0.1"],
  },
};

const BASE_URL = __ENV.BASE_URL || "http://localhost:3000";

export function setup() {
  // Prepare test data
  const res = http.post(`${BASE_URL}/api/auth/login`, {
    email: "stress-test@example.com",
    password: "test123",
  });

  return { token: res.json("token") };
}

export default function (data) {
  const headers = {
    Authorization: `Bearer ${data.token}`,
    "Content-Type": "application/json",
  };

  // Heavy database query
  const productsRes = http.get(`${BASE_URL}/api/products?page=1&limit=100`, {
    headers,
  });

  const productsCheck = check(productsRes, {
    "products loaded": (r) => r.status === 200,
    "has products": (r) => r.json("products").length > 0,
  });

  if (!productsCheck) {
    errorRate.add(1);
    console.error(`Products failed: ${productsRes.status} ${productsRes.body}`);
  }

  sleep(1);

  // Write operation - stress database
  const orderPayload = JSON.stringify({
    items: [{ productId: Math.floor(Math.random() * 100), quantity: 2 }],
  });

  const orderRes = http.post(`${BASE_URL}/api/orders`, orderPayload, {
    headers,
  });

  const orderCheck = check(orderRes, {
    "order created": (r) => r.status === 201 || r.status === 503,
    "response within 5s": (r) => r.timings.duration < 5000,
  });

  if (!orderCheck) {
    errorRate.add(1);
  }

  // Monitor degradation
  if (orderRes.status === 503) {
    console.log("Service unavailable - system at capacity");
  }

  sleep(1);
}

export function teardown(data) {
  // Log final metrics
  console.log("Stress test completed");
}
```
