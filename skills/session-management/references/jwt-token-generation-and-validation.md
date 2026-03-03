# JWT Token Generation and Validation

## JWT Token Generation and Validation

```python
# Python/Flask Example
from flask import current_app
from datetime import datetime, timedelta
import jwt
import os

class TokenManager:
    def __init__(self, secret_key=None):
        self.secret_key = secret_key or os.getenv('JWT_SECRET')
        self.algorithm = 'HS256'
        self.access_token_expires_hours = 1
        self.refresh_token_expires_days = 7

    def generate_tokens(self, user_id, email, role='user'):
        """Generate both access and refresh tokens"""
        now = datetime.utcnow()

        # Access token
        access_payload = {
            'user_id': user_id,
            'email': email,
            'role': role,
            'type': 'access',
            'iat': now,
            'exp': now + timedelta(hours=self.access_token_expires_hours)
        }
        access_token = jwt.encode(access_payload, self.secret_key, algorithm=self.algorithm)

        # Refresh token
        refresh_payload = {
            'user_id': user_id,
            'type': 'refresh',
            'iat': now,
            'exp': now + timedelta(days=self.refresh_token_expires_days)
        }
        refresh_token = jwt.encode(refresh_payload, self.secret_key, algorithm=self.algorithm)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'expires_in': self.access_token_expires_hours * 3600,
            'token_type': 'Bearer'
        }

    def verify_token(self, token, token_type='access'):
        """Verify and decode JWT token"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])

            # Check token type matches
            if payload.get('type') != token_type:
                return None, 'Invalid token type'

            return payload, None
        except jwt.ExpiredSignatureError:
            return None, 'Token expired'
        except jwt.InvalidTokenError:
            return None, 'Invalid token'

    def refresh_access_token(self, refresh_token):
        """Generate new access token from refresh token"""
        payload, error = self.verify_token(refresh_token, token_type='refresh')
        if error:
            return None, error

        new_access_token = self.generate_tokens(
            payload['user_id'],
            payload.get('email', ''),
            payload.get('role', 'user')
        )

        return new_access_token, None
```
