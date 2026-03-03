# External Service Integration

## External Service Integration

### Testing with Test Containers

```javascript
// test/integration/payment-service.test.js
const { GenericContainer } = require("testcontainers");
const PaymentService = require("../../src/services/payment");

describe("Payment Service Integration", () => {
  let container;
  let paymentService;

  beforeAll(async () => {
    // Start PostgreSQL container
    container = await new GenericContainer("postgres:14")
      .withEnvironment({
        POSTGRES_DB: "test",
        POSTGRES_USER: "test",
        POSTGRES_PASSWORD: "test",
      })
      .withExposedPorts(5432)
      .start();

    const connectionString = `postgresql://test:test@${container.getHost()}:${container.getMappedPort(5432)}/test`;
    paymentService = new PaymentService(connectionString);
    await paymentService.initialize();
  }, 60000);

  afterAll(async () => {
    await paymentService.close();
    await container.stop();
  });

  test("should process payment and update database", async () => {
    const payment = {
      orderId: "order-123",
      amount: 99.99,
      currency: "USD",
      paymentMethod: "credit_card",
    };

    const result = await paymentService.processPayment(payment);

    expect(result.status).toBe("completed");
    expect(result.transactionId).toBeDefined();

    // Verify in database
    const stored = await paymentService.getPayment(result.id);
    expect(stored.orderId).toBe("order-123");
    expect(stored.status).toBe("completed");
  });
});
```
