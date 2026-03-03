# Writing Tests

## Writing Tests

**Unit Test Example:**

```javascript
// tests/unit/user.service.test.js
const { expect } = require("chai");
const UserService = require("../../src/services/user.service");

describe("UserService", () => {
  describe("createUser", () => {
    it("should create a new user", async () => {
      const userData = {
        email: "test@example.com",
        password: "password123",
        name: "Test User",
      };

      const user = await UserService.createUser(userData);

      expect(user).to.have.property("id");
      expect(user.email).to.equal(userData.email);
      expect(user.password).to.not.equal(userData.password); // Should be hashed
    });

    it("should throw error for duplicate email", async () => {
      const userData = { email: "existing@example.com" };

      await expect(UserService.createUser(userData)).to.be.rejectedWith(
        "Email already exists",
      );
    });
  });
});
```

**Integration Test Example:**

```javascript
// tests/integration/auth.test.js
const request = require("supertest");
const app = require("../../src/app");

describe("Auth API", () => {
  describe("POST /api/auth/register", () => {
    it("should register a new user", async () => {
      const response = await request(app)
        .post("/api/auth/register")
        .send({
          email: "newuser@example.com",
          password: "password123",
          name: "New User",
        })
        .expect(201);

      expect(response.body).to.have.property("token");
      expect(response.body.user).to.have.property("id");
    });
  });
});
```
