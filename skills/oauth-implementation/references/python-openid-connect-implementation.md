# Python OpenID Connect Implementation

## Python OpenID Connect Implementation

```python
# oidc_provider.py
from flask import Flask, request, jsonify, redirect
from authlib.integrations.flask_oauth2 import AuthorizationServer
from authlib.integrations.flask_oauth2 import ResourceProtector
from authlib.oauth2.rfc6749 import grants
from authlib.jose import jwt
import secrets
import time
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)

class OIDCProvider:
    def __init__(self):
        self.clients = {}
        self.authorization_codes = {}
        self.access_tokens = {}
        self.id_tokens = {}

        # RSA keys for JWT signing
        self.private_key = self._load_private_key()
        self.public_key = self._load_public_key()

    def _load_private_key(self):
        # Load from environment or key management service
        return """-----BEGIN RSA PRIVATE KEY-----
        ... Your private key ...
        -----END RSA PRIVATE KEY-----"""

    def _load_public_key(self):
        return """-----BEGIN PUBLIC KEY-----
        ... Your public key ...
        -----END PUBLIC KEY-----"""

    def register_client(self, client_id, client_secret, redirect_uris, scopes):
        """Register OIDC client"""
        self.clients[client_id] = {
            'client_secret': client_secret,
            'redirect_uris': redirect_uris,
            'scopes': scopes,
            'response_types': ['code', 'id_token', 'token']
        }

    def generate_id_token(self, user_id, client_id, nonce=None):
        """Generate OpenID Connect ID Token"""
        now = int(time.time())

        payload = {
            'iss': 'https://auth.example.com',
            'sub': user_id,
            'aud': client_id,
            'exp': now + 3600,
            'iat': now,
            'auth_time': now,
            'nonce': nonce
        }

        # Add optional claims
        payload.update({
            'email': f'{user_id}@example.com',
            'email_verified': True,
            'name': 'John Doe',
            'given_name': 'John',
            'family_name': 'Doe',
            'picture': 'https://example.com/avatar.jpg'
        })

        header = {'alg': 'RS256', 'typ': 'JWT'}

        return jwt.encode(header, payload, self.private_key)

    def generate_access_token(self, user_id, client_id, scope):
        """Generate OAuth 2.0 access token"""
        token = secrets.token_urlsafe(32)

        self.access_tokens[token] = {
            'user_id': user_id,
            'client_id': client_id,
            'scope': scope,
            'expires_at': datetime.now() + timedelta(hours=1)
        }

        return token

    def verify_token(self, token):
        """Verify JWT token"""
        try:
            claims = jwt.decode(token, self.public_key)
            claims.validate()
            return claims
        except Exception as e:
            return None

# OIDC Endpoints
provider = OIDCProvider()

@app.route('/.well-known/openid-configuration')
def openid_configuration():
    """OpenID Connect Discovery endpoint"""
    return jsonify({
        'issuer': 'https://auth.example.com',
        'authorization_endpoint': 'https://auth.example.com/oauth/authorize',
        'token_endpoint': 'https://auth.example.com/oauth/token',
        'userinfo_endpoint': 'https://auth.example.com/oauth/userinfo',
        'jwks_uri': 'https://auth.example.com/.well-known/jwks.json',
        'response_types_supported': ['code', 'id_token', 'token id_token'],
        'subject_types_supported': ['public'],
        'id_token_signing_alg_values_supported': ['RS256'],
        'scopes_supported': ['openid', 'profile', 'email'],
        'token_endpoint_auth_methods_supported': ['client_secret_basic', 'client_secret_post'],
        'claims_supported': ['sub', 'iss', 'aud', 'exp', 'iat', 'name', 'email']
    })

@app.route('/.well-known/jwks.json')
def jwks():
    """JSON Web Key Set endpoint"""
    # Return public key in JWK format
    return jsonify({
        'keys': [
            {
                'kty': 'RSA',
                'use': 'sig',
                'kid': '1',
                'n': '...',  # Public key modulus
                'e': 'AQAB'
            }
        ]
    })

@app.route('/oauth/userinfo')
def userinfo():
    """UserInfo endpoint"""
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'invalid_token'}), 401

    token = auth_header[7:]
    claims = provider.verify_token(token)

    if not claims:
        return jsonify({'error': 'invalid_token'}), 401

    return jsonify({
        'sub': claims['sub'],
        'email': claims.get('email'),
        'name': claims.get('name'),
        'picture': claims.get('picture')
    })

# Register sample client
provider.register_client(
    'sample-app',
    'secret123',
    ['https://myapp.com/callback'],
    ['openid', 'profile', 'email']
)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
```
