# Issue: "Connection Timeout"

## Issue: "Connection Timeout"

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
  const response = await fetch("https://api.example.com/api/v1/data", {
    signal: controller.signal,
    headers: { Authorization: `Bearer ${apiKey}` },
  });
} finally {
  clearTimeout(timeout);
}
```

**Solution 2: Configure Proxy**

```javascript
// Node.js with proxy
const HttpsProxyAgent = require("https-proxy-agent");

const agent = new HttpsProxyAgent("http://proxy.example.com:8080");

fetch("https://api.example.com", { agent });
```

**Solution 3: Use Alternative Endpoint**

```bash
# If primary endpoint fails, try alternative
curl https://api-backup.example.com/health
```

---
