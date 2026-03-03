# Authentication & Authorization Testing

## Authentication & Authorization Testing

```typescript
// tests/security/auth.test.ts
describe("Authentication Security", () => {
  test("should reject weak passwords", async () => {
    const weakPasswords = [
      "password",
      "12345678",
      "qwerty",
      "abc123",
      "password123",
    ];

    for (const password of weakPasswords) {
      const response = await request(app).post("/api/users").send({
        email: "test@example.com",
        password,
      });

      expect(response.status).toBe(400);
      expect(response.body.error).toMatch(
        /password.*weak|password.*requirements/i,
      );
    }
  });

  test("should rate limit login attempts", async () => {
    const credentials = {
      email: "test@example.com",
      password: "wrongpassword",
    };

    // Try 10 failed logins
    for (let i = 0; i < 10; i++) {
      await request(app).post("/api/auth/login").send(credentials);
    }

    // 11th attempt should be rate limited
    const response = await request(app)
      .post("/api/auth/login")
      .send(credentials);

    expect(response.status).toBe(429);
    expect(response.body.error).toMatch(/too many attempts|rate limit/i);
  });

  test("should prevent unauthorized access", async () => {
    const response = await request(app).get("/api/admin/users").expect(401);
  });

  test("should prevent privilege escalation", async () => {
    const regularUserToken = await getRegularUserToken();

    const response = await request(app)
      .delete("/api/users/999") // Try to delete another user
      .set("Authorization", `Bearer ${regularUserToken}`)
      .expect(403);
  });

  test("JWT tokens should expire", async () => {
    // Create expired token
    const expiredToken = jwt.sign({ userId: "123" }, JWT_SECRET, {
      expiresIn: "-1s",
    });

    const response = await request(app)
      .get("/api/protected")
      .set("Authorization", `Bearer ${expiredToken}`)
      .expect(401);
  });
});
```
