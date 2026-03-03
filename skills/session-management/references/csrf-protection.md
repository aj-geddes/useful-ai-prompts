# CSRF Protection

## CSRF Protection

```python
# Flask CSRF Protection
from flask_wtf.csrf import CSRFProtect
from flask import session, request

csrf = CSRFProtect()

@app.route('/login', methods=['POST'])
@csrf.protect
def login():
    # CSRF token is automatically verified
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.verify_password(password):
        session['user_id'] = user.id
        session['csrf_token'] = csrf.generate_csrf()
        return jsonify({'success': True}), 200

    return jsonify({'error': 'Invalid credentials'}), 401

# JavaScript client
async function login(email, password) {
    const response = await fetch('/csrf-token');
    const { csrfToken } = await response.json();

    return fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRF-Token': csrfToken
        },
        body: JSON.stringify({ email, password })
    });
}
```
