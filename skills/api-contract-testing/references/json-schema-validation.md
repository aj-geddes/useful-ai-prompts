# JSON Schema Validation

## JSON Schema Validation

```python
# tests/contract/test_schema_validation.py
import pytest
import jsonschema
from jsonschema import validate
import json

# Define schemas
USER_SCHEMA = {
    "type": "object",
    "required": ["id", "email", "name"],
    "properties": {
        "id": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 0, "maximum": 150},
        "role": {"type": "string", "enum": ["user", "admin"]},
        "createdAt": {"type": "string", "format": "date-time"},
    },
    "additionalProperties": False
}

ORDER_SCHEMA = {
    "type": "object",
    "required": ["id", "userId", "total", "status"],
    "properties": {
        "id": {"type": "string"},
        "userId": {"type": "string"},
        "total": {"type": "number", "minimum": 0},
        "status": {
            "type": "string",
            "enum": ["pending", "paid", "shipped", "delivered", "cancelled"]
        },
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["productId", "quantity", "price"],
                "properties": {
                    "productId": {"type": "string"},
                    "quantity": {"type": "integer", "minimum": 1},
                    "price": {"type": "number", "minimum": 0},
                }
            }
        }
    }
}

class TestAPIContracts:
    def test_get_user_response_schema(self, api_client):
        """Validate user endpoint response against schema."""
        response = api_client.get('/api/users/123')

        assert response.status_code == 200
        data = response.json()

        # Validate against schema
        validate(instance=data, schema=USER_SCHEMA)

    def test_create_user_request_schema(self, api_client):
        """Validate create user request body."""
        valid_user = {
            "email": "test@example.com",
            "name": "Test User",
            "age": 30,
        }

        response = api_client.post('/api/users', json=valid_user)
        assert response.status_code == 201

        # Response should also match schema
        validate(instance=response.json(), schema=USER_SCHEMA)

    def test_invalid_request_rejected(self, api_client):
        """Invalid requests should be rejected."""
        invalid_user = {
            "email": "not-an-email",
            "age": -5,  # Invalid age
        }

        response = api_client.post('/api/users', json=invalid_user)
        assert response.status_code == 400

    def test_order_response_schema(self, api_client):
        """Validate order endpoint response."""
        response = api_client.get('/api/orders/order-123')

        assert response.status_code == 200
        validate(instance=response.json(), schema=ORDER_SCHEMA)

    def test_order_items_array_validation(self, api_client):
        """Validate nested array schema."""
        order_data = {
            "userId": "user-123",
            "items": [
                {"productId": "prod-1", "quantity": 2, "price": 29.99},
                {"productId": "prod-2", "quantity": 1, "price": 49.99},
            ]
        }

        response = api_client.post('/api/orders', json=order_data)
        assert response.status_code == 201

        result = response.json()
        validate(instance=result, schema=ORDER_SCHEMA)
```
