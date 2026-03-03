# Issue: "Invalid JSON Response"

## Issue: "Invalid JSON Response"

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
const response = await fetch("https://api.example.com/api/v1/data");
console.log("Content-Type:", response.headers.get("Content-Type"));
// Expected: "application/json"
```

**3. Check Response Body**

```javascript
const response = await fetch("https://api.example.com/api/v1/data");
const text = await response.text();
console.log("Raw response:", text);

// Then try to parse
try {
  const data = JSON.parse(text);
} catch (error) {
  console.error("Invalid JSON:", error.message);
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
  const contentType = response.headers.get("Content-Type");
  if (!contentType || !contentType.includes("application/json")) {
    const text = await response.text();
    throw new Error(`Expected JSON but got: ${text.substring(0, 100)}`);
  }

  // Parse JSON
  return response.json();
}
```

**Solution 2: Handle Empty Responses**

```javascript
const response = await fetch("https://api.example.com/api/v1/data");
const text = await response.text();

// Handle empty response
if (!text || text.trim() === "") {
  return null;
}

return JSON.parse(text);
```

---
