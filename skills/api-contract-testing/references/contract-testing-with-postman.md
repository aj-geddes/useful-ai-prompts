# Contract Testing with Postman

## Contract Testing with Postman

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
