# Issue: "Slow Performance"

## Issue: "Slow Performance"

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
const response = await fetch("/api/v1/users");
const users = await response.json(); // 10,000 users!

// ✅ Fetch paginated data
const response = await fetch("/api/v1/users?page=1&limit=50");
const { data, pagination } = await response.json();
```

**Solution 2: Use Field Selection**

```javascript
// ❌ Fetching all fields
const response = await fetch("/api/v1/users/123");

// ✅ Select only needed fields
const response = await fetch("/api/v1/users/123?fields=id,name,email");
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
    timestamp: Date.now(),
  });

  return data;
}
```

**Solution 4: Use CDN**

```javascript
// Use CDN endpoint for static assets
const cdnUrl = "https://cdn.example.com/api/v1/data";
```

---
