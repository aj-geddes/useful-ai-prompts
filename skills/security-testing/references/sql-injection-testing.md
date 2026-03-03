# SQL Injection Testing

## SQL Injection Testing

```typescript
// tests/security/sql-injection.test.ts
import { test, expect } from "@playwright/test";
import request from "supertest";
import { app } from "../../src/app";

test.describe("SQL Injection Protection", () => {
  const sqlInjectionPayloads = [
    "' OR '1'='1",
    "'; DROP TABLE users; --",
    "' UNION SELECT * FROM users --",
    "admin'--",
    "' OR 1=1--",
    "1' AND '1'='1",
  ];

  test("login should prevent SQL injection", async () => {
    for (const payload of sqlInjectionPayloads) {
      const response = await request(app).post("/api/auth/login").send({
        email: payload,
        password: payload,
      });

      // Should return 400/401, not 500 (SQL error)
      expect([400, 401]).toContain(response.status);
      expect(response.body).not.toMatch(/SQL|syntax|error/i);
    }
  });

  test("search should sanitize input", async () => {
    for (const payload of sqlInjectionPayloads) {
      const response = await request(app)
        .get("/api/products/search")
        .query({ q: payload });

      // Should not cause SQL error
      expect(response.status).toBeLessThan(500);
      expect(response.body).not.toMatch(/SQL|syntax/i);
    }
  });

  test("numeric parameters should be validated", async () => {
    const response = await request(app)
      .get("/api/users/abc") // Non-numeric ID
      .expect(400);

    expect(response.body.error).toBeTruthy();
  });
});
```
