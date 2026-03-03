# Issue: "Authentication Failed"

## Issue: "Authentication Failed"

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
