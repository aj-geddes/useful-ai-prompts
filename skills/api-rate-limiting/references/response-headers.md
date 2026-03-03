# Response Headers

## Response Headers

```javascript
// Standard rate limit headers
res.setHeader('X-RateLimit-Limit', maxRequests);          // Total requests allowed
res.setHeader('X-RateLimit-Remaining', remaining);        // Remaining requests
res.setHeader('X-RateLimit-Reset', resetTime);            // Unix timestamp of reset
res.setHeader('Retry-After', secondsToWait);              // How long to wait

// 429 Too Many Requests response
{
  "error": "Rate limit exceeded",
  "code": "RATE_LIMIT_EXCEEDED",
  "retryAfter": 60,
  "resetAt": "2025-01-15T15:00:00Z"
}
```
