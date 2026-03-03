# Structured Logging

## Structured Logging

```javascript
// Good: Structured logs (machine-readable)
logger.info({
  level: 'INFO',
  timestamp: '2024-01-15T10:30:00Z',
  service: 'auth-service',
  user_id: '12345',
  action: 'user_login',
  status: 'success',
  duration_ms: 150,
  ip_address: '192.168.1.1'
});

// Bad: Unstructured logs (hard to parse)
console.log('User 12345 logged in successfully in 150ms from 192.168.1.1');

// JSON Format (Elasticsearch friendly)
{
  "@timestamp": "2024-01-15T10:30:00Z",
  "level": "ERROR",
  "service": "api-gateway",
  "trace_id": "abc123",
  "message": "Database connection failed",
  "error": {
    "type": "ConnectionError",
    "code": "ECONNREFUSED"
  },
  "context": {
    "database": "users",
    "operation": "SELECT"
  }
}
```
