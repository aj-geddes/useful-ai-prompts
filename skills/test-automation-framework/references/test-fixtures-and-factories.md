# Test Fixtures and Factories

## Test Fixtures and Factories

```typescript
// framework/fixtures/database.ts
import { test as base } from "@playwright/test";
import { PrismaClient } from "@prisma/client";

export const test = base.extend<{
  db: PrismaClient;
  testUser: User;
  cleanupData: () => Promise<void>;
}>({
  db: async ({}, use) => {
    const db = new PrismaClient();
    await use(db);
    await db.$disconnect();
  },

  testUser: async ({ db }, use) => {
    const user = await db.user.create({
      data: {
        email: `test-${Date.now()}@example.com`,
        name: "Test User",
        password: await hashPassword("password123"),
      },
    });
    await use(user);
    await db.user.delete({ where: { id: user.id } });
  },

  cleanupData: async ({ db }, use) => {
    const cleanup = async () => {
      await db.order.deleteMany({});
      await db.product.deleteMany({});
    };
    await use(cleanup);
  },
});

export { expect } from "@playwright/test";

// Usage in tests
import { test, expect } from "../framework/fixtures/database";

test("user can create order", async ({ db, testUser }) => {
  const product = await db.product.create({
    data: { name: "Test Product", price: 99.99 },
  });

  const order = await db.order.create({
    data: {
      userId: testUser.id,
      items: {
        create: [{ productId: product.id, quantity: 1 }],
      },
    },
  });

  expect(order.userId).toBe(testUser.id);
});
```
