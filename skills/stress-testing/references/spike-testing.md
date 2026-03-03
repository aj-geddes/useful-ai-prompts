# Spike Testing

## Spike Testing

```javascript
// spike-test.js
import http from "k6/http";
import { check } from "k6";

export const options = {
  stages: [
    { duration: "30s", target: 10 }, // Normal baseline
    { duration: "1m", target: 10 }, // Stable baseline
    { duration: "10s", target: 1000 }, // SPIKE! 100x increase
    { duration: "3m", target: 1000 }, // Maintain spike
    { duration: "10s", target: 10 }, // Drop back
    { duration: "3m", target: 10 }, // Recovery period
  ],
  thresholds: {
    http_req_duration: ["p(95)<5000"], // Allow degradation during spike
    http_req_failed: ["rate<0.1"], // Allow 10% errors during spike
  },
};

export default function () {
  const res = http.get("http://api.example.com/health");

  check(res, {
    "system responsive": (r) => r.status === 200 || r.status === 429,
    "response received": (r) => r.body.length > 0,
  });
}
```
