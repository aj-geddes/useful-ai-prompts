# Token Refresh Endpoint

## Token Refresh Endpoint

```python
# Flask token refresh endpoint
from flask import request, jsonify
from functools import wraps

@app.route('/api/auth/refresh', methods=['POST'])
def refresh_token():
    data = request.get_json()
    refresh_token = data.get('refresh_token')

    if not refresh_token:
        return jsonify({'error': 'Refresh token required'}), 400

    token_manager = TokenManager()
    tokens, error = token_manager.refresh_access_token(refresh_token)

    if error:
        return jsonify({'error': error}), 401

    return jsonify(tokens), 200

@app.route('/api/auth/logout', methods=['POST'])
@require_auth
def logout():
    token = request.headers['Authorization'].split(' ')[1]
    session_manager = RedisSessionManager()
    session_manager.destroy_session(token)

    return jsonify({'message': 'Logged out successfully'}), 200
```
