# Python Authentication Implementation

## Python Authentication Implementation

```python
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret-key'
jwt = JWTManager(app)

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401

    access_token = create_access_token(
        identity=user.id,
        additional_claims={'email': user.email, 'role': user.role}
    )

    return jsonify({
        'accessToken': access_token,
        'user': {'id': user.id, 'email': user.email}
    }), 200

@app.route('/api/protected', methods=['GET'])
@jwt_required()
def protected():
    from flask_jwt_extended import get_jwt_identity
    user_id = get_jwt_identity()
    return jsonify({'userId': user_id}), 200

def require_role(role):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            from flask_jwt_extended import get_jwt
            claims = get_jwt()
            if claims.get('role') != role:
                return jsonify({'error': 'Forbidden'}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/api/admin', methods=['GET'])
@require_role('admin')
def admin_endpoint():
    return jsonify({'message': 'Admin data'}), 200
```
