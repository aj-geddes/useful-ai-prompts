# Python Flask CSRF Protection

## Python Flask CSRF Protection

```python
# csrf_protection.py
from flask import Flask, session, request, jsonify
from flask_wtf.csrf import CSRFProtect, generate_csrf, validate_csrf
from functools import wraps
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['WTF_CSRF_TIME_LIMIT'] = 3600  # 1 hour
app.config['WTF_CSRF_SSL_STRICT'] = True

csrf = CSRFProtect(app)

# Cookie configuration
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Strict'
)

@app.before_request
def csrf_protect():
    """Validate CSRF token for state-changing methods"""
    if request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
        token = request.headers.get('X-CSRF-Token') or request.form.get('csrf_token')

        if not token:
            return jsonify({'error': 'CSRF token missing'}), 403

        try:
            validate_csrf(token)
        except:
            return jsonify({'error': 'Invalid CSRF token'}), 403

@app.route('/api/csrf-token', methods=['GET'])
def get_csrf_token():
    """Provide CSRF token to clients"""
    token = generate_csrf()
    return jsonify({'csrfToken': token})

@app.route('/api/transfer', methods=['POST'])
def transfer_funds():
    """Protected endpoint"""
    data = request.get_json()

    return jsonify({
        'message': 'Transfer successful',
        'amount': data.get('amount')
    })

# Custom CSRF decorator
def require_csrf(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method in ['POST', 'PUT', 'DELETE']:
            token = request.headers.get('X-CSRF-Token')

            if not token:
                return jsonify({'error': 'CSRF token required'}), 403

            try:
                validate_csrf(token)
            except:
                return jsonify({'error': 'Invalid CSRF token'}), 403

        return f(*args, **kwargs)

    return decorated_function

@app.route('/api/sensitive-action', methods=['POST'])
@require_csrf
def sensitive_action():
    return jsonify({'message': 'Action completed'})

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
```
