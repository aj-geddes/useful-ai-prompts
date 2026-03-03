# Opossum-Style Circuit Breaker (Node.js)

## Opossum-Style Circuit Breaker (Node.js)

```typescript
import CircuitBreaker from "opossum";

// Create circuit breaker
const options = {
  timeout: 3000, // 3 seconds
  errorThresholdPercentage: 50,
  resetTimeout: 30000, // 30 seconds
  rollingCountTimeout: 10000,
  rollingCountBuckets: 10,
  name: "api-breaker",
};

const breaker = new CircuitBreaker(callExternalAPI, options);

// Event handlers
breaker.on("open", () => {
  console.log("Circuit breaker opened");
});

breaker.on("halfOpen", () => {
  console.log("Circuit breaker half-opened");
});

breaker.on("close", () => {
  console.log("Circuit breaker closed");
});

breaker.on("success", (result) => {
  console.log("Request succeeded:", result);
});

breaker.on("failure", (error) => {
  console.error("Request failed:", error);
});

breaker.on("timeout", () => {
  console.error("Request timed out");
});

breaker.on("reject", () => {
  console.warn("Request rejected by circuit breaker");
});

// Fallback
breaker.fallback(() => {
  return { data: "fallback data" };
});

// Use circuit breaker
async function callExternalAPI() {
  const response = await fetch("https://api.example.com/data");
  if (!response.ok) throw new Error("API error");
  return response.json();
}

// Execute with circuit breaker
breaker
  .fire()
  .then((data) => console.log(data))
  .catch((err) => console.error(err));
```
