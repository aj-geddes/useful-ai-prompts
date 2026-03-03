# Service Boundary Design

## Service Boundary Design

### Domain-Driven Design (DDD) Approach

```
Bounded Contexts:
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  Order Service  │  │  User Service   │  │ Payment Service │
│                 │  │                 │  │                 │
│ - Create Order  │  │ - User Profile  │  │ - Process Pay   │
│ - Order Status  │  │ - Auth          │  │ - Refund        │
│ - Order History │  │ - Preferences   │  │ - Transactions  │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

**Decomposition Strategies:**

1. **By Business Capability**

```
E-commerce System:
- Product Catalog Service
- Shopping Cart Service
- Order Management Service
- Payment Service
- Inventory Service
- Shipping Service
- User Account Service
```

2. **By Subdomain**

```
Healthcare System:
- Patient Management (Core Domain)
- Appointment Scheduling (Core Domain)
- Billing (Supporting Domain)
- Notifications (Generic Domain)
- Reporting (Generic Domain)
```

### Service Design Example

```typescript
// order-service/src/domain/order.ts
export class OrderService {
  constructor(
    private orderRepository: OrderRepository,
    private eventBus: EventBus,
    private paymentClient: PaymentClient,
    private inventoryClient: InventoryClient,
  ) {}

  async createOrder(request: CreateOrderRequest): Promise<Order> {
    // 1. Validate order
    const order = Order.create(request);

    // 2. Check inventory (synchronous call)
    const available = await this.inventoryClient.checkAvailability(order.items);
    if (!available) {
      throw new InsufficientInventoryError();
    }

    // 3. Save order
    await this.orderRepository.save(order);

    // 4. Publish event (asynchronous)
    await this.eventBus.publish(new OrderCreatedEvent(order));

    return order;
  }
}
```
