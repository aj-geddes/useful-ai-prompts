# Security Headers Testing Script

## Security Headers Testing Script

```javascript
// test-security-headers.js
const axios = require("axios");

async function testSecurityHeaders(url) {
  console.log(`\n=== Testing Security Headers for ${url} ===\n`);

  try {
    const response = await axios.get(url, {
      validateStatus: () => true,
    });

    const headers = response.headers;

    const tests = {
      "Strict-Transport-Security": {
        present: !!headers["strict-transport-security"],
        value: headers["strict-transport-security"],
        recommended: "max-age=31536000; includeSubDomains; preload",
      },
      "X-Frame-Options": {
        present: !!headers["x-frame-options"],
        value: headers["x-frame-options"],
        recommended: "DENY or SAMEORIGIN",
      },
      "X-Content-Type-Options": {
        present: !!headers["x-content-type-options"],
        value: headers["x-content-type-options"],
        recommended: "nosniff",
      },
      "X-XSS-Protection": {
        present: !!headers["x-xss-protection"],
        value: headers["x-xss-protection"],
        recommended: "1; mode=block",
      },
      "Content-Security-Policy": {
        present: !!headers["content-security-policy"],
        value: headers["content-security-policy"],
        recommended: "Define strict CSP",
      },
      "Referrer-Policy": {
        present: !!headers["referrer-policy"],
        value: headers["referrer-policy"],
        recommended: "strict-origin-when-cross-origin",
      },
      "Permissions-Policy": {
        present: !!headers["permissions-policy"],
        value: headers["permissions-policy"],
        recommended: "Restrict dangerous features",
      },
    };

    let passed = 0;
    let failed = 0;

    for (const [header, test] of Object.entries(tests)) {
      if (test.present) {
        console.log(`✓ ${header}: ${test.value}`);
        passed++;
      } else {
        console.log(`✗ ${header}: MISSING`);
        console.log(`  Recommended: ${test.recommended}`);
        failed++;
      }
    }

    console.log(`\n=== Summary ===`);
    console.log(`Passed: ${passed}/${Object.keys(tests).length}`);
    console.log(`Failed: ${failed}/${Object.keys(tests).length}`);

    const score = (passed / Object.keys(tests).length) * 100;
    console.log(`Security Score: ${score.toFixed(0)}%`);
  } catch (error) {
    console.error("Error testing headers:", error.message);
  }
}

// Usage
testSecurityHeaders("https://example.com");
```
