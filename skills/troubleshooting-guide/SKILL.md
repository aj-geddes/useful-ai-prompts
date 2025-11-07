---
name: troubleshooting-guide
description: Create comprehensive troubleshooting guides, FAQ documents, known issues lists, and debug guides. Use when documenting common problems, error messages, or debugging procedures.
---

# Troubleshooting Guide

## Overview

Create structured troubleshooting documentation that helps users and support teams quickly diagnose and resolve common issues.

## When to Use

- FAQ documentation
- Common error messages
- Debug guides
- Known issues lists
- Error code reference
- Performance troubleshooting
- Configuration issues
- Installation problems

## Troubleshooting Guide Template

```markdown
# Troubleshooting Guide

## Quick Diagnosis

### Is the Service Working?

Check our [Status Page](https://status.example.com) first.

### Quick Health Checks

```bash
# 1. Check service is running
curl https://api.example.com/health

# 2. Check your API key
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.example.com/api/v1/status

# 3. Check network connectivity
ping api.example.com

# 4. Check DNS resolution
nslookup api.example.com
```

## Common Issues

### Issue: "Authentication Failed"

**Error Code:** `401 Unauthorized`

**Error Message:**
```json
{
  "error": "Authentication failed",
  "code": "AUTH_001",
  "message": "Invalid or expired API key"
}
```

**Possible Causes:**
1. Invalid API key
2. Expired API key
3. API key not included in request
4. Wrong authentication method

**Solution:**

**Step 1: Verify API Key Format**
```bash
# API keys should be 32 characters, alphanumeric
# Format: ak_1234567890abcdef1234567890abcdef

# Check your key
echo $API_KEY | wc -c  # Should be 32
```

**Step 2: Test API Key**
```bash
curl -H "Authorization: Bearer $API_KEY" \
  https://api.example.com/api/v1/auth/verify

# Expected response:
# {"valid": true, "expires": "2025-12-31T23:59:59Z"}
```

**Step 3: Generate New Key (if needed)**
1. Log in to [Dashboard](https://dashboard.example.com)
2. Navigate to Settings > API Keys
3. Click "Generate New Key"
4. Copy and save the key securely
5. Update your application configuration

**Step 4: Verify Configuration**
```javascript
// ✅ Correct
const response = await fetch('https://api.example.com/api/v1/data', {
  headers: {
    'Authorization': `Bearer ${apiKey}`,
    'Content-Type': 'application/json'
  }
});

// ❌ Incorrect - missing Bearer prefix
headers: {
  'Authorization': apiKey
}

// ❌ Incorrect - wrong header name
headers: {
  'X-API-Key': apiKey
}
```

**Still Not Working?**
- Check if API key has required permissions
- Verify account is active and not suspended
- Check if IP whitelist is configured correctly
- Contact support with request ID from error response

---

### Issue: "Rate Limit Exceeded"

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

| Plan | Rate Limit | Burst | Reset Period |
|------|------------|-------|--------------|
| Free | 100/hour | 10/second | 1 hour |
| Pro | 1000/hour | 50/second | 1 hour |
| Enterprise | 10000/hour | 100/second | 1 hour |

**Solutions:**

**Option 1: Implement Exponential Backoff**
```javascript
async function fetchWithRetry(url, options = {}, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      const response = await fetch(url, options);

      if (response.status === 429) {
        const resetTime = response.headers.get('X-RateLimit-Reset');
        const waitTime = resetTime
          ? (resetTime * 1000) - Date.now()
          : Math.pow(2, i) * 1000;

        console.log(`Rate limited. Waiting ${waitTime}ms...`);
        await new Promise(resolve => setTimeout(resolve, waitTime));
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
const response = await fetch('https://api.example.com/api/v1/data', {
  headers: { 'Authorization': `Bearer ${apiKey}` }
});

console.log('Limit:', response.headers.get('X-RateLimit-Limit'));
console.log('Remaining:', response.headers.get('X-RateLimit-Remaining'));
console.log('Reset:', response.headers.get('X-RateLimit-Reset'));
```

**Option 3: Batch Requests**
```javascript
// ❌ Don't do this - 100 separate requests
for (const id of userIds) {
  await fetchUser(id);
}

// ✅ Do this - 1 batch request
await fetchUsers(userIds);  // API supports bulk fetch
```

**Option 4: Upgrade Plan**
- Visit [Pricing](https://example.com/pricing)
- Upgrade to higher tier for increased limits

---

### Issue: "Connection Timeout"

**Error Message:**
```
Error: connect ETIMEDOUT
Error: socket hang up
```

**Possible Causes:**
1. Network connectivity issues
2. Firewall blocking outbound connections
3. DNS resolution failure
4. Service temporarily unavailable
5. Incorrect endpoint URL

**Diagnostic Steps:**

**1. Check Network Connectivity**
```bash
# Test basic connectivity
ping api.example.com

# Test HTTPS connectivity
curl -v https://api.example.com

# Test with timeout
curl --max-time 10 https://api.example.com/health
```

**2. Check DNS Resolution**
```bash
# Check DNS
nslookup api.example.com

# Expected output:
# Name:    api.example.com
# Address: 93.184.216.34

# Try alternative DNS
nslookup api.example.com 8.8.8.8
```

**3. Check Firewall/Proxy**
```bash
# Test if using proxy
curl -v --proxy http://proxy.example.com:8080 \
  https://api.example.com

# Check if port 443 is open
nc -zv api.example.com 443
```

**4. Test from Different Network**
```bash
# Test from different network to isolate issue
# Try mobile hotspot, different WiFi, etc.
```

**Solutions:**

**Solution 1: Increase Timeout**
```javascript
// ✅ Set reasonable timeout
const controller = new AbortController();
const timeout = setTimeout(() => controller.abort(), 30000); // 30 seconds

try {
  const response = await fetch('https://api.example.com/api/v1/data', {
    signal: controller.signal,
    headers: { 'Authorization': `Bearer ${apiKey}` }
  });
} finally {
  clearTimeout(timeout);
}
```

**Solution 2: Configure Proxy**
```javascript
// Node.js with proxy
const HttpsProxyAgent = require('https-proxy-agent');

const agent = new HttpsProxyAgent('http://proxy.example.com:8080');

fetch('https://api.example.com', { agent });
```

**Solution 3: Use Alternative Endpoint**
```bash
# If primary endpoint fails, try alternative
curl https://api-backup.example.com/health
```

---

### Issue: "Invalid JSON Response"

**Error Message:**
```
SyntaxError: Unexpected token < in JSON at position 0
```

**Possible Causes:**
1. Server returned HTML error page instead of JSON
2. Response is not valid JSON
3. Empty response body
4. Content-Type mismatch

**Diagnostic Steps:**

**1. Inspect Raw Response**
```bash
curl -v https://api.example.com/api/v1/data \
  -H "Authorization: Bearer $API_KEY"

# Look at:
# - Status code
# - Content-Type header
# - Response body
```

**2. Check Content-Type**
```javascript
const response = await fetch('https://api.example.com/api/v1/data');
console.log('Content-Type:', response.headers.get('Content-Type'));
// Expected: "application/json"
```

**3. Check Response Body**
```javascript
const response = await fetch('https://api.example.com/api/v1/data');
const text = await response.text();
console.log('Raw response:', text);

// Then try to parse
try {
  const data = JSON.parse(text);
} catch (error) {
  console.error('Invalid JSON:', error.message);
}
```

**Solutions:**

**Solution 1: Validate Before Parsing**
```javascript
async function fetchJSON(url, options) {
  const response = await fetch(url, options);

  // Check status
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
  }

  // Check content type
  const contentType = response.headers.get('Content-Type');
  if (!contentType || !contentType.includes('application/json')) {
    const text = await response.text();
    throw new Error(`Expected JSON but got: ${text.substring(0, 100)}`);
  }

  // Parse JSON
  return response.json();
}
```

**Solution 2: Handle Empty Responses**
```javascript
const response = await fetch('https://api.example.com/api/v1/data');
const text = await response.text();

// Handle empty response
if (!text || text.trim() === '') {
  return null;
}

return JSON.parse(text);
```

---

### Issue: "Slow Performance"

**Symptoms:**
- API requests taking > 5 seconds
- Timeouts
- Application feels sluggish

**Diagnostic Steps:**

**1. Measure Request Time**
```bash
# Using curl
time curl https://api.example.com/api/v1/data

# Detailed timing
curl -w "@curl-format.txt" -o /dev/null -s \
  https://api.example.com/api/v1/data

# curl-format.txt:
#     time_namelookup:  %{time_namelookup}s\n
#        time_connect:  %{time_connect}s\n
#     time_appconnect:  %{time_appconnect}s\n
#    time_pretransfer:  %{time_pretransfer}s\n
#       time_redirect:  %{time_redirect}s\n
#  time_starttransfer:  %{time_starttransfer}s\n
#                     ----------\n
#          time_total:  %{time_total}s\n
```

**2. Check Response Size**
```bash
curl -I https://api.example.com/api/v1/data
# Look at Content-Length header
```

**3. Test from Different Locations**
```bash
# Use online tools to test from different regions
# - https://www.dotcom-tools.com/website-speed-test.aspx
# - https://tools.pingdom.com/
```

**Solutions:**

**Solution 1: Use Pagination**
```javascript
// ❌ Fetching all data at once
const response = await fetch('/api/v1/users');
const users = await response.json(); // 10,000 users!

// ✅ Fetch paginated data
const response = await fetch('/api/v1/users?page=1&limit=50');
const { data, pagination } = await response.json();
```

**Solution 2: Use Field Selection**
```javascript
// ❌ Fetching all fields
const response = await fetch('/api/v1/users/123');

// ✅ Select only needed fields
const response = await fetch('/api/v1/users/123?fields=id,name,email');
```

**Solution 3: Implement Caching**
```javascript
const cache = new Map();
const CACHE_TTL = 5 * 60 * 1000; // 5 minutes

async function fetchWithCache(url) {
  const cached = cache.get(url);
  if (cached && Date.now() - cached.timestamp < CACHE_TTL) {
    return cached.data;
  }

  const response = await fetch(url);
  const data = await response.json();

  cache.set(url, {
    data,
    timestamp: Date.now()
  });

  return data;
}
```

**Solution 4: Use CDN**
```javascript
// Use CDN endpoint for static assets
const cdnUrl = 'https://cdn.example.com/api/v1/data';
```

---

## Error Code Reference

| Code | HTTP | Description | Solution |
|------|------|-------------|----------|
| AUTH_001 | 401 | Invalid API key | Regenerate API key |
| AUTH_002 | 401 | Expired API key | Generate new key |
| AUTH_003 | 403 | Insufficient permissions | Check API key scopes |
| RATE_001 | 429 | Rate limit exceeded | Wait or upgrade plan |
| RATE_002 | 429 | Concurrent request limit | Reduce parallelism |
| VAL_001 | 400 | Missing required field | Check request body |
| VAL_002 | 400 | Invalid field format | Validate input |
| RES_001 | 404 | Resource not found | Check resource ID |
| RES_002 | 409 | Resource already exists | Use update instead |
| SRV_001 | 500 | Internal server error | Contact support |
| SRV_002 | 503 | Service unavailable | Retry with backoff |

---

## Getting Help

### Before Contacting Support

1. Check [Status Page](https://status.example.com)
2. Search [Documentation](https://docs.example.com)
3. Check [Community Forum](https://community.example.com)
4. Review this troubleshooting guide

### When Contacting Support

Include the following:
- Error message and error code
- Request ID (from response headers)
- Timestamp of the issue
- API endpoint being called
- Code snippet (without credentials!)
- Steps to reproduce

**Example Support Request:**
```
Subject: Error 429 on /api/v1/users endpoint

Hi,

I'm getting a 429 error when calling the /api/v1/users endpoint.

Error message:
{
  "error": "Rate limit exceeded",
  "code": "RATE_001",
  "request_id": "req_abc123"
}

Details:
- Timestamp: 2025-01-15T14:30:00Z
- Request ID: req_abc123
- Endpoint: GET /api/v1/users
- Account: user@example.com
- Plan: Pro

I'm only making ~50 requests per hour, which should be within
the limit. Can you help investigate?

Thanks!
```

### Useful Links

- **Documentation:** https://docs.example.com
- **Status Page:** https://status.example.com
- **Community:** https://community.example.com
- **Support:** support@example.com
- **GitHub Issues:** https://github.com/example/repo/issues
```

## Best Practices

### ✅ DO
- Start with most common issues
- Include error messages verbatim
- Provide step-by-step diagnostics
- Show expected vs actual output
- Include code examples
- Document error codes
- Add screenshots/videos
- Link to related documentation
- Keep solutions up-to-date
- Include workarounds
- Test all solutions

### ❌ DON'T
- Use vague descriptions
- Skip diagnostic steps
- Forget to show examples
- Assume technical knowledge
- Skip verification steps
- Forget edge cases

## Resources

- [Google's Technical Writing Guide](https://developers.google.com/tech-writing)
- [Microsoft Troubleshooting Guide](https://docs.microsoft.com/troubleshoot/)
- [Stack Overflow Documentation](https://stackoverflow.com/documentation)
