# Dependency Injection

## Dependency Injection

Invert control by injecting dependencies.

```typescript
// Bad: Hard-coded dependencies
class OrderService {
  private db = new MySQLDatabase(); // Tightly coupled
  private email = new GmailService(); // Tightly coupled

  createOrder(order: Order) {
    this.db.save(order);
    this.email.send(order.customer_email, "Order created");
  }
}

// Good: Dependency injection
interface Database {
  save(entity: any): void;
}

interface EmailService {
  send(to: string, subject: string): void;
}

class OrderService {
  constructor(
    private db: Database,
    private email: EmailService,
  ) {}

  createOrder(order: Order) {
    this.db.save(order);
    this.email.send(order.customer_email, "Order created");
  }
}

// Usage - easy to test with mocks
const service = new OrderService(new MySQLDatabase(), new GmailService());

// Test with mocks
const testService = new OrderService(
  new MockDatabase(),
  new MockEmailService(),
);
```
