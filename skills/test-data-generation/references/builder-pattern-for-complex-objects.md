# Builder Pattern for Complex Objects

## Builder Pattern for Complex Objects

```typescript
// tests/builders/OrderBuilder.ts
import { faker } from "@faker-js/faker";

export class OrderBuilder {
  private order: Partial<Order> = {
    id: faker.string.uuid(),
    status: "pending",
    items: [],
    total: 0,
    createdAt: new Date(),
  };

  withId(id: string): this {
    this.order.id = id;
    return this;
  }

  withStatus(status: OrderStatus): this {
    this.order.status = status;
    return this;
  }

  withUser(user: User): this {
    this.order.userId = user.id;
    this.order.user = user;
    return this;
  }

  withItems(items: OrderItem[]): this {
    this.order.items = items;
    this.order.total = items.reduce(
      (sum, item) => sum + item.price * item.quantity,
      0,
    );
    return this;
  }

  addItem(product: Product, quantity: number = 1): this {
    const item: OrderItem = {
      productId: product.id,
      product,
      quantity,
      price: product.price,
      subtotal: product.price * quantity,
    };

    this.order.items = [...(this.order.items || []), item];
    this.order.total = (this.order.total || 0) + item.subtotal;
    return this;
  }

  withShippingAddress(address: Address): this {
    this.order.shippingAddress = address;
    return this;
  }

  asPaid(): this {
    this.order.status = "paid";
    this.order.paidAt = new Date();
    return this;
  }

  asShipped(): this {
    this.order.status = "shipped";
    this.order.shippedAt = new Date();
    return this;
  }

  build(): Order {
    return this.order as Order;
  }
}

// Usage in tests
describe("Order Processing", () => {
  it("should calculate total correctly", () => {
    const product1 = ProductBuilder.aProduct().withPrice(10.0).build();
    const product2 = ProductBuilder.aProduct().withPrice(25.0).build();

    const order = new OrderBuilder()
      .withUser(UserBuilder.aUser().build())
      .addItem(product1, 2) // $20
      .addItem(product2, 1) // $25
      .build();

    expect(order.total).toBe(45.0);
    expect(order.items).toHaveLength(2);
  });

  it("should process paid orders", () => {
    const order = new OrderBuilder()
      .withUser(UserBuilder.aUser().build())
      .addItem(ProductBuilder.aProduct().build())
      .asPaid()
      .build();

    expect(order.status).toBe("paid");
    expect(order.paidAt).toBeDefined();
  });
});
```
