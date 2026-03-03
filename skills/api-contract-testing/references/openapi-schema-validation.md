# OpenAPI Schema Validation

## OpenAPI Schema Validation

```typescript
// tests/contract/openapi.test.ts
import request from "supertest";
import { app } from "../../src/app";
import OpenAPIValidator from "express-openapi-validator";
import fs from "fs";
import yaml from "js-yaml";

describe("OpenAPI Contract Validation", () => {
  let validator;

  beforeAll(() => {
    const spec = yaml.load(fs.readFileSync("./openapi.yaml", "utf8"));

    validator = OpenAPIValidator.middleware({
      apiSpec: spec,
      validateRequests: true,
      validateResponses: true,
    });
  });

  test("GET /users/:id matches schema", async () => {
    const response = await request(app).get("/users/123").expect(200);

    // Validate against OpenAPI schema
    expect(response.body).toMatchObject({
      id: expect.any(String),
      email: expect.stringMatching(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/),
      name: expect.any(String),
      age: expect.any(Number),
      createdAt: expect.stringMatching(/^\d{4}-\d{2}-\d{2}T/),
    });
  });

  test("POST /users validates request body", async () => {
    const invalidUser = {
      email: "invalid-email", // Should fail validation
      name: "Test",
    };

    await request(app).post("/users").send(invalidUser).expect(400);
  });
});
```
