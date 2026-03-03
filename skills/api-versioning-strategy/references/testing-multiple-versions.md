# Testing Multiple Versions

## Testing Multiple Versions

```typescript
// api-version.test.ts
describe("API Versioning", () => {
  describe("v1", () => {
    it("should return user with v1 format", async () => {
      const response = await request(app).get("/api/v1/users/1").expect(200);

      expect(response.body).toHaveProperty("id");
      expect(response.body).toHaveProperty("name");
      expect(response.body).not.toHaveProperty("email");
    });
  });

  describe("v2", () => {
    it("should return user with v2 format", async () => {
      const response = await request(app).get("/api/v2/users/1").expect(200);

      expect(response.body).toHaveProperty("id");
      expect(response.body).toHaveProperty("name");
      expect(response.body).toHaveProperty("email");
      expect(response.body).toHaveProperty("profile");
    });

    it("should include deprecation headers for v1", async () => {
      const response = await request(app).get("/api/v1/users/1");

      expect(response.headers["deprecation"]).toBe("true");
      expect(response.headers["sunset"]).toBeDefined();
    });
  });

  describe("version negotiation", () => {
    it("should use version from header", async () => {
      const response = await request(app)
        .get("/api/users/1")
        .set("API-Version", "2")
        .expect(200);

      expect(response.body).toHaveProperty("email");
    });

    it("should default to v1 if no version specified", async () => {
      const response = await request(app).get("/api/users/1").expect(200);

      expect(response.body).not.toHaveProperty("email");
    });
  });
});
```
