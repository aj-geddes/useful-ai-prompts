# Issue: "Rate Limit Exceeded"

## Issue: "Rate Limit Exceeded"

**Error Code:** `429 Too Many Requests`

**Error Message:**

```json
{
  "error": "Rate limit exceeded",
  "code": "RATE_001",
  "message": "You have exceeded the rate limit",
  "limit": 100,
  "remaining": 0,
  "reset": 1642694400
}
```

**Understanding Rate Limits:**

| Plan       | Rate Limit | Burst      | Reset Period |
| ---------- | ---------- | ---------- | ------------ |
| Free       | 100/hour   | 10/second  | 1 hour       |
| Pro        | 1000/hour  | 50/second  | 1 hour       |
| Enterprise | 10000/hour | 100/second | 1 hour       |

**Solutions:**

**Option 1: Implement Exponential Backoff**

```javascript
async function fetchWithRetry(url, options = {}, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      const response = await fetch(url, options);

      if (response.status === 429) {
        const resetTime = response.headers.get("X-RateLimit-Reset");
        const waitTime = resetTime
          ? resetTime * 1000 - Date.now()
          : Math.pow(2, i) * 1000;

        console.log(`Rate limited. Waiting ${waitTime}ms...`);
        await new Promise((resolve) => setTimeout(resolve, waitTime));
        continue;
      }

      return response;
    } catch (error) {
      if (i === maxRetries - 1) throw error;
    }
  }
}
```

**Option 2: Check Rate Limit Headers**

```javascript
const response = await fetch("https://api.example.com/api/v1/data", {
  headers: { Authorization: `Bearer ${apiKey}` },
});

console.log("Limit:", response.headers.get("X-RateLimit-Limit"));
console.log("Remaining:", response.headers.get("X-RateLimit-Remaining"));
console.log("Reset:", response.headers.get("X-RateLimit-Reset"));
```

**Option 3: Batch Requests**

```javascript
// ❌ Don't do this - 100 separate requests
for (const id of userIds) {
  await fetchUser(id);
}

// ✅ Do this - 1 batch request
await fetchUsers(userIds); // API supports bulk fetch
```

**Option 4: Upgrade Plan**

- Visit [Pricing](https://example.com/pricing)
- Upgrade to higher tier for increased limits

---
