# Data Consistency Patterns

## Data Consistency Patterns

### Saga Pattern (Orchestration)

```typescript
// order-saga-orchestrator.ts
export class OrderSagaOrchestrator {
  async createOrder(orderData: CreateOrderRequest) {
    const sagaId = uuidv4();
    const saga = new SagaInstance(sagaId);

    try {
      // Step 1: Create order
      const order = await this.orderService.createOrder(orderData);
      saga.addCompensation(() => this.orderService.cancelOrder(order.id));

      // Step 2: Reserve inventory
      await this.inventoryService.reserveItems(order.items);
      saga.addCompensation(() =>
        this.inventoryService.releaseReservation(order.id),
      );

      // Step 3: Process payment
      const payment = await this.paymentService.charge(order.total);
      saga.addCompensation(() => this.paymentService.refund(payment.id));

      // Step 4: Confirm order
      await this.orderService.confirmOrder(order.id);

      return order;
    } catch (error) {
      // Compensate in reverse order
      await saga.compensate();
      throw error;
    }
  }
}
```

### Event Sourcing Pattern

```typescript
// order-aggregate.ts
export class OrderAggregate {
  private id: string;
  private status: OrderStatus;
  private items: OrderItem[];
  private events: DomainEvent[] = [];

  // Command handler
  createOrder(command: CreateOrderCommand) {
    // Validation
    if (this.id) throw new Error("Order already exists");

    // Apply event
    this.apply(
      new OrderCreatedEvent({
        orderId: command.orderId,
        userId: command.userId,
        items: command.items,
      }),
    );
  }

  // Event handler
  private apply(event: DomainEvent) {
    switch (event.type) {
      case "OrderCreated":
        this.id = event.orderId;
        this.items = event.items;
        this.status = OrderStatus.PENDING;
        break;
      case "OrderConfirmed":
        this.status = OrderStatus.CONFIRMED;
        break;
    }
    this.events.push(event);
  }

  getUncommittedEvents(): DomainEvent[] {
    return this.events;
  }
}
```
