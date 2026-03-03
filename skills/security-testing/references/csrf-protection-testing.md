# CSRF Protection Testing

## CSRF Protection Testing

```python
# tests/security/test_csrf.py
import pytest
from flask import session

class TestCSRFProtection:
    def test_post_without_csrf_token_rejected(self, client):
        """POST requests without CSRF token should be rejected."""
        response = client.post('/api/users', json={
            'email': 'test@example.com',
            'name': 'Test'
        })

        assert response.status_code == 403
        assert 'CSRF' in response.json['error']

    def test_post_with_invalid_csrf_token_rejected(self, client):
        """POST with invalid CSRF token should be rejected."""
        response = client.post('/api/users',
            json={'email': 'test@example.com'},
            headers={'X-CSRF-Token': 'invalid-token'}
        )

        assert response.status_code == 403

    def test_post_with_valid_csrf_token_accepted(self, client):
        """POST with valid CSRF token should be accepted."""
        # Get CSRF token
        response = client.get('/api/csrf-token')
        csrf_token = response.json['csrfToken']

        # Use token in POST
        response = client.post('/api/users',
            json={'email': 'test@example.com', 'name': 'Test'},
            headers={'X-CSRF-Token': csrf_token}
        )

        assert response.status_code == 201
```
