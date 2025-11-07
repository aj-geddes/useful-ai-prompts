---
name: security-headers-configuration
description: Configure HTTP security headers including CSP, HSTS, X-Frame-Options, and XSS protection. Use when hardening web applications against common attacks.
---

# Security Headers Configuration

## Overview

Implement comprehensive HTTP security headers to protect web applications from XSS, clickjacking, MIME sniffing, and other browser-based attacks.

## When to Use

- New web application deployment
- Security audit remediation
- Compliance requirements
- Browser security hardening
- API security
- Static site protection

## Implementation Examples

### 1. **Node.js/Express Security Headers**

```javascript
// security-headers.js
const helmet = require('helmet');

function configureSecurityHeaders(app) {
  // Comprehensive Helmet configuration
  app.use(helmet({
    // Content Security Policy
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        scriptSrc: [
          "'self'",
          "'unsafe-inline'", // Remove in production
          "https://cdn.example.com",
          "https://www.google-analytics.com"
        ],
        styleSrc: [
          "'self'",
          "'unsafe-inline'",
          "https://fonts.googleapis.com"
        ],
        fontSrc: [
          "'self'",
          "https://fonts.gstatic.com"
        ],
        imgSrc: [
          "'self'",
          "data:",
          "https:",
          "blob:"
        ],
        connectSrc: [
          "'self'",
          "https://api.example.com"
        ],
        frameSrc: ["'none'"],
        objectSrc: ["'none'"],
        upgradeInsecureRequests: []
      }
    },

    // Strict Transport Security
    hsts: {
      maxAge: 31536000, // 1 year
      includeSubDomains: true,
      preload: true
    },

    // X-Frame-Options
    frameguard: {
      action: 'deny'
    },

    // X-Content-Type-Options
    noSniff: true,

    // X-XSS-Protection
    xssFilter: true,

    // Referrer-Policy
    referrerPolicy: {
      policy: 'strict-origin-when-cross-origin'
    },

    // Permissions-Policy (formerly Feature-Policy)
    permittedCrossDomainPolicies: {
      permittedPolicies: 'none'
    }
  }));

  // Additional custom headers
  app.use((req, res, next) => {
    // Permissions Policy
    res.setHeader(
      'Permissions-Policy',
      'geolocation=(), microphone=(), camera=(), payment=(), usb=()'
    );

    // Expect-CT
    res.setHeader(
      'Expect-CT',
      'max-age=86400, enforce'
    );

    // Cross-Origin policies
    res.setHeader('Cross-Origin-Embedder-Policy', 'require-corp');
    res.setHeader('Cross-Origin-Opener-Policy', 'same-origin');
    res.setHeader('Cross-Origin-Resource-Policy', 'same-origin');

    // Remove powered-by header
    res.removeHeader('X-Powered-By');

    next();
  });
}

// CSP Violation Reporter
app.post('/api/csp-report', express.json({ type: 'application/csp-report' }), (req, res) => {
  const report = req.body['csp-report'];

  console.error('CSP Violation:', {
    documentUri: report['document-uri'],
    violatedDirective: report['violated-directive'],
    blockedUri: report['blocked-uri'],
    sourceFile: report['source-file'],
    lineNumber: report['line-number']
  });

  // Store in database or send to monitoring service
  // monitoringService.logCSPViolation(report);

  res.status(204).end();
});

module.exports = { configureSecurityHeaders };
```

### 2. **Nginx Security Headers Configuration**

```nginx
# nginx-security-headers.conf

server {
    listen 443 ssl http2;
    server_name example.com;

    # SSL Configuration
    ssl_certificate /etc/ssl/certs/example.com.crt;
    ssl_certificate_key /etc/ssl/private/example.com.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # Security Headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    add_header X-Frame-Options "DENY" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;

    # Content Security Policy
    add_header Content-Security-Policy "default-src 'self'; script-src 'self' https://cdn.example.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self' https://api.example.com; frame-ancestors 'none'; base-uri 'self'; form-action 'self'; report-uri /api/csp-report" always;

    # Cross-Origin Policies
    add_header Cross-Origin-Embedder-Policy "require-corp" always;
    add_header Cross-Origin-Opener-Policy "same-origin" always;
    add_header Cross-Origin-Resource-Policy "same-origin" always;

    # Expect-CT
    add_header Expect-CT "max-age=86400, enforce" always;

    # Hide server version
    server_tokens off;

    location / {
        root /var/www/html;
        index index.html;
    }

    # API endpoints
    location /api/ {
        proxy_pass http://backend:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Remove backend headers that might leak info
        proxy_hide_header X-Powered-By;
        proxy_hide_header Server;
    }
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name example.com;
    return 301 https://$server_name$request_uri;
}
```

### 3. **Python Flask Security Headers**

```python
# security_headers.py
from flask import Flask, make_response
from functools import wraps

app = Flask(__name__)

def add_security_headers(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        resp = make_response(f(*args, **kwargs))

        # Strict Transport Security
        resp.headers['Strict-Transport-Security'] = \
            'max-age=31536000; includeSubDomains; preload'

        # X-Frame-Options
        resp.headers['X-Frame-Options'] = 'DENY'

        # X-Content-Type-Options
        resp.headers['X-Content-Type-Options'] = 'nosniff'

        # X-XSS-Protection
        resp.headers['X-XSS-Protection'] = '1; mode=block'

        # Referrer-Policy
        resp.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'

        # Permissions-Policy
        resp.headers['Permissions-Policy'] = \
            'geolocation=(), microphone=(), camera=(), payment=()'

        # Content Security Policy
        csp = {
            "default-src": ["'self'"],
            "script-src": ["'self'", "https://cdn.example.com"],
            "style-src": ["'self'", "'unsafe-inline'"],
            "img-src": ["'self'", "data:", "https:"],
            "font-src": ["'self'"],
            "connect-src": ["'self'", "https://api.example.com"],
            "frame-ancestors": ["'none'"],
            "base-uri": ["'self'"],
            "form-action": ["'self'"],
            "report-uri": ["/api/csp-report"]
        }

        csp_string = "; ".join([
            f"{key} {' '.join(values)}"
            for key, values in csp.items()
        ])

        resp.headers['Content-Security-Policy'] = csp_string

        # Cross-Origin Policies
        resp.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
        resp.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
        resp.headers['Cross-Origin-Resource-Policy'] = 'same-origin'

        # Expect-CT
        resp.headers['Expect-CT'] = 'max-age=86400, enforce'

        # Remove server header
        resp.headers.pop('Server', None)

        return resp

    return decorated_function

# Apply to all routes
@app.after_request
def apply_security_headers(response):
    # Same headers as above
    response.headers['Strict-Transport-Security'] = \
        'max-age=31536000; includeSubDomains; preload'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'

    return response

# CSP Violation endpoint
@app.route('/api/csp-report', methods=['POST'])
def csp_report():
    report = request.get_json()

    print(f"CSP Violation: {report}")

    # Log to monitoring service
    # monitoring.log_csp_violation(report)

    return '', 204

if __name__ == '__main__':
    # Run with HTTPS only
    app.run(ssl_context='adhoc', port=443)
```

### 4. **Apache .htaccess Configuration**

```apache
# .htaccess - Apache security headers

# Strict Transport Security
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"

# X-Frame-Options
Header always set X-Frame-Options "DENY"

# X-Content-Type-Options
Header always set X-Content-Type-Options "nosniff"

# X-XSS-Protection
Header always set X-XSS-Protection "1; mode=block"

# Referrer-Policy
Header always set Referrer-Policy "strict-origin-when-cross-origin"

# Permissions-Policy
Header always set Permissions-Policy "geolocation=(), microphone=(), camera=()"

# Content Security Policy
Header always set Content-Security-Policy "default-src 'self'; script-src 'self' https://cdn.example.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; frame-ancestors 'none'"

# Cross-Origin Policies
Header always set Cross-Origin-Embedder-Policy "require-corp"
Header always set Cross-Origin-Opener-Policy "same-origin"
Header always set Cross-Origin-Resource-Policy "same-origin"

# Remove server signature
ServerSignature Off
Header unset Server
Header unset X-Powered-By

# Force HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

### 5. **Security Headers Testing Script**

```javascript
// test-security-headers.js
const axios = require('axios');

async function testSecurityHeaders(url) {
  console.log(`\n=== Testing Security Headers for ${url} ===\n`);

  try {
    const response = await axios.get(url, {
      validateStatus: () => true
    });

    const headers = response.headers;

    const tests = {
      'Strict-Transport-Security': {
        present: !!headers['strict-transport-security'],
        value: headers['strict-transport-security'],
        recommended: 'max-age=31536000; includeSubDomains; preload'
      },
      'X-Frame-Options': {
        present: !!headers['x-frame-options'],
        value: headers['x-frame-options'],
        recommended: 'DENY or SAMEORIGIN'
      },
      'X-Content-Type-Options': {
        present: !!headers['x-content-type-options'],
        value: headers['x-content-type-options'],
        recommended: 'nosniff'
      },
      'X-XSS-Protection': {
        present: !!headers['x-xss-protection'],
        value: headers['x-xss-protection'],
        recommended: '1; mode=block'
      },
      'Content-Security-Policy': {
        present: !!headers['content-security-policy'],
        value: headers['content-security-policy'],
        recommended: 'Define strict CSP'
      },
      'Referrer-Policy': {
        present: !!headers['referrer-policy'],
        value: headers['referrer-policy'],
        recommended: 'strict-origin-when-cross-origin'
      },
      'Permissions-Policy': {
        present: !!headers['permissions-policy'],
        value: headers['permissions-policy'],
        recommended: 'Restrict dangerous features'
      }
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
    console.error('Error testing headers:', error.message);
  }
}

// Usage
testSecurityHeaders('https://example.com');
```

## Best Practices

### ✅ DO
- Use HTTPS everywhere
- Implement strict CSP
- Enable HSTS with preload
- Block framing with X-Frame-Options
- Prevent MIME sniffing
- Report CSP violations
- Test headers regularly
- Use security scanners

### ❌ DON'T
- Allow unsafe-inline in CSP
- Skip HSTS on subdomains
- Ignore CSP violations
- Use overly permissive policies
- Forget to test changes

## Security Headers Checklist

- [ ] Strict-Transport-Security
- [ ] Content-Security-Policy
- [ ] X-Frame-Options
- [ ] X-Content-Type-Options
- [ ] X-XSS-Protection
- [ ] Referrer-Policy
- [ ] Permissions-Policy
- [ ] Cross-Origin policies
- [ ] Expect-CT
- [ ] Remove server signatures

## Testing Tools

- [Security Headers](https://securityheaders.com/)
- [Mozilla Observatory](https://observatory.mozilla.org/)
- [CSP Evaluator](https://csp-evaluator.withgoogle.com/)

## Resources

- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security)
- [CSP Reference](https://content-security-policy.com/)
