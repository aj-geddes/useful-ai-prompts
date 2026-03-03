# Pact for Consumer-Driven Contracts

## Pact for Consumer-Driven Contracts

### Consumer Test (Jest/Pact)

```typescript
// tests/pact/user-service.pact.test.ts
import { PactV3, MatchersV3 } from "@pact-foundation/pact";
import { UserService } from "../../src/services/UserService";

const { like, eachLike, iso8601DateTimeWithMillis } = MatchersV3;

const provider = new PactV3({
  consumer: "OrderService",
  provider: "UserService",
  port: 1234,
  dir: "./pacts",
});

describe("User Service Contract", () => {
  const userService = new UserService("http://localhost:1234");

  describe("GET /users/:id", () => {
    test("returns user when found", async () => {
      await provider
        .given("user with ID 123 exists")
        .uponReceiving("a request for user 123")
        .withRequest({
          method: "GET",
          path: "/users/123",
          headers: {
            Authorization: like("Bearer token"),
          },
        })
        .willRespondWith({
          status: 200,
          headers: {
            "Content-Type": "application/json",
          },
          body: {
            id: like("123"),
            email: like("user@example.com"),
            name: like("John Doe"),
            age: like(30),
            createdAt: iso8601DateTimeWithMillis("2024-01-01T00:00:00.000Z"),
            role: like("user"),
          },
        })
        .executeTest(async (mockServer) => {
          const user = await userService.getUser("123");

          expect(user.id).toBe("123");
          expect(user.email).toBeDefined();
          expect(user.name).toBeDefined();
        });
    });

    test("returns 404 when user not found", async () => {
      await provider
        .given("user with ID 999 does not exist")
        .uponReceiving("a request for non-existent user")
        .withRequest({
          method: "GET",
          path: "/users/999",
        })
        .willRespondWith({
          status: 404,
          headers: {
            "Content-Type": "application/json",
          },
          body: {
            error: like("User not found"),
            code: like("USER_NOT_FOUND"),
          },
        })
        .executeTest(async (mockServer) => {
          await expect(userService.getUser("999")).rejects.toThrow(
            "User not found",
          );
        });
    });
  });

  describe("POST /users", () => {
    test("creates new user", async () => {
      await provider
        .given("user does not exist")
        .uponReceiving("a request to create user")
        .withRequest({
          method: "POST",
          path: "/users",
          headers: {
            "Content-Type": "application/json",
          },
          body: {
            email: like("newuser@example.com"),
            name: like("New User"),
            age: like(25),
          },
        })
        .willRespondWith({
          status: 201,
          headers: {
            "Content-Type": "application/json",
          },
          body: {
            id: like("new-123"),
            email: like("newuser@example.com"),
            name: like("New User"),
            age: like(25),
            createdAt: iso8601DateTimeWithMillis(),
            role: "user",
          },
        })
        .executeTest(async (mockServer) => {
          const user = await userService.createUser({
            email: "newuser@example.com",
            name: "New User",
            age: 25,
          });

          expect(user.id).toBeDefined();
          expect(user.email).toBe("newuser@example.com");
        });
    });
  });

  describe("GET /users/:id/orders", () => {
    test("returns user orders", async () => {
      await provider
        .given("user 123 has orders")
        .uponReceiving("a request for user orders")
        .withRequest({
          method: "GET",
          path: "/users/123/orders",
          query: {
            limit: "10",
            offset: "0",
          },
        })
        .willRespondWith({
          status: 200,
          body: {
            orders: eachLike({
              id: like("order-1"),
              total: like(99.99),
              status: like("completed"),
              createdAt: iso8601DateTimeWithMillis(),
            }),
            total: like(5),
            hasMore: like(false),
          },
        })
        .executeTest(async (mockServer) => {
          const response = await userService.getUserOrders("123", {
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

### Provider Test (Verify Contract)

```typescript
// tests/pact/user-service.provider.test.ts
import { Verifier } from "@pact-foundation/pact";
import path from "path";
import { app } from "../../src/app";
import { setupTestDB, teardownTestDB } from "../helpers/db";

describe("Pact Provider Verification", () => {
  let server;

  beforeAll(async () => {
    await setupTestDB();
    server = app.listen(3001);
  });

  afterAll(async () => {
    await teardownTestDB();
    server.close();
  });

  test("validates the expectations of OrderService", () => {
    return new Verifier({
      provider: "UserService",
      providerBaseUrl: "http://localhost:3001",
      pactUrls: [
        path.resolve(__dirname, "../../pacts/orderservice-userservice.json"),
      ],
      // Provider state setup
      stateHandlers: {
        "user with ID 123 exists": async () => {
          await createTestUser({ id: "123", name: "John Doe" });
        },
        "user with ID 999 does not exist": async () => {
          await deleteUser("999");
        },
        "user 123 has orders": async () => {
          await createTestUser({ id: "123" });
          await createTestOrder({ userId: "123" });
        },
      },
    })
      .verifyProvider()
      .then((output) => {
        console.log("Pact Verification Complete!");
      });
  });
});
```
