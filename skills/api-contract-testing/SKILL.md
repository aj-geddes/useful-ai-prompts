---
name: api-contract-testing
description: Verify API contracts between services to ensure compatibility and prevent breaking changes. Use for contract testing, Pact, API contract validation, schema validation, and consumer-driven contracts.
---

# API Contract Testing

## Overview

Contract testing verifies that APIs honor their contracts between consumers and providers. It ensures that service changes don't break dependent consumers without requiring full integration tests. Contract tests validate request/response formats, data types, and API behavior independently.

## When to Use

- Testing microservices communication
- Preventing breaking API changes
- Validating API versioning
- Testing consumer-provider contracts
- Ensuring backward compatibility
- Validating OpenAPI/Swagger specifications
- Testing third-party API integrations
- Catching contract violations in CI

## Key Concepts

- **Consumer**: Service that calls an API
- **Provider**: Service that exposes the API
- **Contract**: Agreement on API request/response format
- **Pact**: Consumer-defined expectations
- **Schema**: Structure definition (OpenAPI, JSON Schema)
- **Stub**: Generated mock from contract
- **Broker**: Central repository for contracts

## Instructions

### 1. **Pact for Consumer-Driven Contracts**

#### Consumer Test (Jest/Pact)
```typescript
// tests/pact/user-service.pact.test.ts
import { PactV3, MatchersV3 } from '@pact-foundation/pact';
import { UserService } from '../../src/services/UserService';

const { like, eachLike, iso8601DateTimeWithMillis } = MatchersV3;

const provider = new PactV3({
  consumer: 'OrderService',
  provider: 'UserService',
  port: 1234,
  dir: './pacts',
});

describe('User Service Contract', () => {
  const userService = new UserService('http://localhost:1234');

  describe('GET /users/:id', () => {
    test('returns user when found', async () => {
      await provider
        .given('user with ID 123 exists')
        .uponReceiving('a request for user 123')
        .withRequest({
          method: 'GET',
          path: '/users/123',
          headers: {
            Authorization: like('Bearer token'),
          },
        })
        .willRespondWith({
          status: 200,
          headers: {
            'Content-Type': 'application/json',
          },
          body: {
            id: like('123'),
            email: like('user@example.com'),
            name: like('John Doe'),
            age: like(30),
            createdAt: iso8601DateTimeWithMillis('2024-01-01T00:00:00.000Z'),
            role: like('user'),
          },
        })
        .executeTest(async (mockServer) => {
          const user = await userService.getUser('123');

          expect(user.id).toBe('123');
          expect(user.email).toBeDefined();
          expect(user.name).toBeDefined();
        });
    });

    test('returns 404 when user not found', async () => {
      await provider
        .given('user with ID 999 does not exist')
        .uponReceiving('a request for non-existent user')
        .withRequest({
          method: 'GET',
          path: '/users/999',
        })
        .willRespondWith({
          status: 404,
          headers: {
            'Content-Type': 'application/json',
          },
          body: {
            error: like('User not found'),
            code: like('USER_NOT_FOUND'),
          },
        })
        .executeTest(async (mockServer) => {
          await expect(userService.getUser('999')).rejects.toThrow(
            'User not found'
          );
        });
    });
  });

  describe('POST /users', () => {
    test('creates new user', async () => {
      await provider
        .given('user does not exist')
        .uponReceiving('a request to create user')
        .withRequest({
          method: 'POST',
          path: '/users',
          headers: {
            'Content-Type': 'application/json',
          },
          body: {
            email: like('newuser@example.com'),
            name: like('New User'),
            age: like(25),
          },
        })
        .willRespondWith({
          status: 201,
          headers: {
            'Content-Type': 'application/json',
          },
          body: {
            id: like('new-123'),
            email: like('newuser@example.com'),
            name: like('New User'),
            age: like(25),
            createdAt: iso8601DateTimeWithMillis(),
            role: 'user',
          },
        })
        .executeTest(async (mockServer) => {
          const user = await userService.createUser({
            email: 'newuser@example.com',
            name: 'New User',
            age: 25,
          });

          expect(user.id).toBeDefined();
          expect(user.email).toBe('newuser@example.com');
        });
    });
  });

  describe('GET /users/:id/orders', () => {
    test('returns user orders', async () => {
      await provider
        .given('user 123 has orders')
        .uponReceiving('a request for user orders')
        .withRequest({
          method: 'GET',
          path: '/users/123/orders',
          query: {
            limit: '10',
            offset: '0',
          },
        })
        .willRespondWith({
          status: 200,
          body: {
            orders: eachLike({
              id: like('order-1'),
              total: like(99.99),
              status: like('completed'),
              createdAt: iso8601DateTimeWithMillis(),
            }),
            total: like(5),
            hasMore: like(false),
          },
        })
        .executeTest(async (mockServer) => {
          const response = await userService.getUserOrders('123', {
            limit: 10,
            offset: 0,
          });

          expect(response.orders).toBeDefined();
          expect(Array.isArray(response.orders)).toBe(true);
          expect(response.total).toBeDefined();
        });
    });
  });
});
```

#### Provider Test (Verify Contract)
```typescript
// tests/pact/user-service.provider.test.ts
import { Verifier } from '@pact-foundation/pact';
import path from 'path';
import { app } from '../../src/app';
import { setupTestDB, teardownTestDB } from '../helpers/db';

describe('Pact Provider Verification', () => {
  let server;

  beforeAll(async () => {
    await setupTestDB();
    server = app.listen(3001);
  });

  afterAll(async () => {
    await teardownTestDB();
    server.close();
  });

  test('validates the expectations of OrderService', () => {
    return new Verifier({
      provider: 'UserService',
      providerBaseUrl: 'http://localhost:3001',
      pactUrls: [
        path.resolve(__dirname, '../../pacts/orderservice-userservice.json'),
      ],
      // Provider state setup
      stateHandlers: {
        'user with ID 123 exists': async () => {
          await createTestUser({ id: '123', name: 'John Doe' });
        },
        'user with ID 999 does not exist': async () => {
          await deleteUser('999');
        },
        'user 123 has orders': async () => {
          await createTestUser({ id: '123' });
          await createTestOrder({ userId: '123' });
        },
      },
    })
      .verifyProvider()
      .then((output) => {
        console.log('Pact Verification Complete!');
      });
  });
});
```

### 2. **OpenAPI Schema Validation**

```typescript
// tests/contract/openapi.test.ts
import request from 'supertest';
import { app } from '../../src/app';
import OpenAPIValidator from 'express-openapi-validator';
import fs from 'fs';
import yaml from 'js-yaml';

describe('OpenAPI Contract Validation', () => {
  let validator;

  beforeAll(() => {
    const spec = yaml.load(
      fs.readFileSync('./openapi.yaml', 'utf8')
    );

    validator = OpenAPIValidator.middleware({
      apiSpec: spec,
      validateRequests: true,
      validateResponses: true,
    });
  });

  test('GET /users/:id matches schema', async () => {
    const response = await request(app)
      .get('/users/123')
      .expect(200);

    // Validate against OpenAPI schema
    expect(response.body).toMatchObject({
      id: expect.any(String),
      email: expect.stringMatching(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/),
      name: expect.any(String),
      age: expect.any(Number),
      createdAt: expect.stringMatching(/^\d{4}-\d{2}-\d{2}T/),
    });
  });

  test('POST /users validates request body', async () => {
    const invalidUser = {
      email: 'invalid-email',  // Should fail validation
      name: 'Test',
    };

    await request(app)
      .post('/users')
      .send(invalidUser)
      .expect(400);
  });
});
```

### 3. **JSON Schema Validation**

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

### 4. **REST Assured for Java**

```java
// ContractTest.java
import io.restassured.RestAssured;
import io.restassured.module.jsv.JsonSchemaValidator;
import org.junit.jupiter.api.Test;
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

public class UserAPIContractTest {

    @Test
    public void getUserShouldMatchSchema() {
        given()
            .pathParam("id", "123")
        .when()
            .get("/api/users/{id}")
        .then()
            .statusCode(200)
            .body(JsonSchemaValidator.matchesJsonSchemaInClasspath("schemas/user-schema.json"))
            .body("id", notNullValue())
            .body("email", matchesPattern("^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$"))
            .body("age", greaterThanOrEqualTo(0));
    }

    @Test
    public void createUserShouldValidateRequest() {
        String userJson = """
            {
                "email": "test@example.com",
                "name": "Test User",
                "age": 30
            }
            """;

        given()
            .contentType("application/json")
            .body(userJson)
        .when()
            .post("/api/users")
        .then()
            .statusCode(201)
            .body("id", notNullValue())
            .body("email", equalTo("test@example.com"))
            .body("createdAt", matchesPattern("\\d{4}-\\d{2}-\\d{2}T.*"));
    }

    @Test
    public void getUserOrdersShouldReturnArray() {
        given()
            .pathParam("id", "123")
            .queryParam("limit", 10)
        .when()
            .get("/api/users/{id}/orders")
        .then()
            .statusCode(200)
            .body("orders", isA(java.util.List.class))
            .body("orders[0].id", notNullValue())
            .body("orders[0].status", isIn(Arrays.asList(
                "pending", "paid", "shipped", "delivered", "cancelled"
            )))
            .body("total", greaterThanOrEqualTo(0));
    }

    @Test
    public void invalidRequestShouldReturn400() {
        String invalidUser = """
            {
                "email": "not-an-email",
                "age": -5
            }
            """;

        given()
            .contentType("application/json")
            .body(invalidUser)
        .when()
            .post("/api/users")
        .then()
            .statusCode(400)
            .body("error", notNullValue());
    }
}
```

### 5. **Contract Testing with Postman**

```json
// postman-collection.json
{
  "info": {
    "name": "User API Contract Tests"
  },
  "item": [
    {
      "name": "Get User",
      "request": {
        "method": "GET",
        "url": "{{baseUrl}}/users/{{userId}}"
      },
      "test": "
        pm.test('Response status is 200', () => {
          pm.response.to.have.status(200);
        });

        pm.test('Response matches schema', () => {
          const schema = {
            type: 'object',
            required: ['id', 'email', 'name'],
            properties: {
              id: { type: 'string' },
              email: { type: 'string', format: 'email' },
              name: { type: 'string' },
              age: { type: 'integer' }
            }
          };

          pm.response.to.have.jsonSchema(schema);
        });

        pm.test('Email format is valid', () => {
          const data = pm.response.json();
          pm.expect(data.email).to.match(/^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$/);
        });
      "
    }
  ]
}
```

### 6. **Pact Broker Integration**

```yaml
# .github/workflows/contract-tests.yml
name: Contract Tests

on: [push, pull_request]

jobs:
  consumer-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3

      - run: npm ci
      - run: npm run test:pact

      - name: Publish Pacts
        run: |
          npx pact-broker publish ./pacts \
            --consumer-app-version=${{ github.sha }} \
            --broker-base-url=${{ secrets.PACT_BROKER_URL }} \
            --broker-token=${{ secrets.PACT_BROKER_TOKEN }}

  provider-tests:
    runs-on: ubuntu-latest
    needs: consumer-tests
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3

      - run: npm ci
      - run: npm run test:pact:provider

      - name: Can I Deploy?
        run: |
          npx pact-broker can-i-deploy \
            --pacticipant=UserService \
            --version=${{ github.sha }} \
            --to-environment=production \
            --broker-base-url=${{ secrets.PACT_BROKER_URL }} \
            --broker-token=${{ secrets.PACT_BROKER_TOKEN }}
```

## Best Practices

### ✅ DO
- Test contracts from consumer perspective
- Use matchers for flexible matching
- Validate schema structure, not specific values
- Version your contracts
- Test error responses
- Use Pact broker for contract sharing
- Run contract tests in CI
- Test backward compatibility

### ❌ DON'T
- Test business logic in contract tests
- Hard-code specific values in contracts
- Skip error scenarios
- Test UI in contract tests
- Ignore contract versioning
- Deploy without contract verification
- Test implementation details
- Mock contract tests

## Tools

- **Pact**: Consumer-driven contracts (multiple languages)
- **Spring Cloud Contract**: JVM contract testing
- **OpenAPI/Swagger**: API specification and validation
- **Postman**: API contract testing
- **REST Assured**: Java API testing
- **Dredd**: OpenAPI/API Blueprint testing
- **Spectral**: OpenAPI linting

## Examples

See also: integration-testing, api-versioning-strategy, continuous-testing for comprehensive API testing strategies.
