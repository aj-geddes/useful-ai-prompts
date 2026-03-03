# Python Flask Security Headers

## Python Flask Security Headers

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
