# Event Store (TypeScript)

## Event Store (TypeScript)

```typescript
interface DomainEvent {
  id: string;
  aggregateId: string;
  aggregateType: string;
  eventType: string;
  data: any;
  metadata: {
    userId?: string;
    timestamp: number;
    version: number;
  };
}

interface Aggregate {
  id: string;
  version: number;
}

class EventStore {
  private events: DomainEvent[] = [];

  async appendEvents(
    aggregateId: string,
    expectedVersion: number,
    events: Omit<DomainEvent, "id" | "metadata">[],
  ): Promise<void> {
    // Optimistic concurrency check
    const currentVersion = await this.getCurrentVersion(aggregateId);

    if (currentVersion !== expectedVersion) {
      throw new Error("Concurrency conflict");
    }

    const newEvents = events.map((event, index) => ({
      ...event,
      id: crypto.randomUUID(),
      metadata: {
        timestamp: Date.now(),
        version: expectedVersion + index + 1,
      },
    }));

    this.events.push(...newEvents);
  }

  async getEvents(aggregateId: string): Promise<DomainEvent[]> {
    return this.events
      .filter((e) => e.aggregateId === aggregateId)
      .sort((a, b) => a.metadata.version - b.metadata.version);
  }

  async getCurrentVersion(aggregateId: string): Promise<number> {
    const events = await this.getEvents(aggregateId);
    return events.length > 0 ? events[events.length - 1].metadata.version : 0;
  }
}

// Bank Account Aggregate
interface BankAccountState {
  id: string;
  balance: number;
  isOpen: boolean;
  version: number;
}

class BankAccount implements Aggregate {
  id: string;
  version: number;
  private balance: number = 0;
  private isOpen: boolean = false;
  private uncommittedEvents: DomainEvent[] = [];

  constructor(id: string) {
    this.id = id;
    this.version = 0;
  }

  // Commands
  open(initialDeposit: number): void {
    if (this.isOpen) {
      throw new Error("Account already open");
    }

    this.applyEvent({
      eventType: "AccountOpened",
      data: { initialDeposit },
    });
  }

  deposit(amount: number): void {
    if (!this.isOpen) {
      throw new Error("Account not open");
    }

    if (amount <= 0) {
      throw new Error("Amount must be positive");
    }

    this.applyEvent({
      eventType: "MoneyDeposited",
      data: { amount },
    });
  }

  withdraw(amount: number): void {
    if (!this.isOpen) {
      throw new Error("Account not open");
    }

    if (amount <= 0) {
      throw new Error("Amount must be positive");
    }

    if (this.balance < amount) {
      throw new Error("Insufficient funds");
    }

    this.applyEvent({
      eventType: "MoneyWithdrawn",
      data: { amount },
    });
  }

  close(): void {
    if (!this.isOpen) {
      throw new Error("Account not open");
    }

    if (this.balance > 0) {
      throw new Error("Cannot close account with positive balance");
    }

    this.applyEvent({
      eventType: "AccountClosed",
      data: {},
    });
  }

  // Event Application
  private applyEvent(event: Partial<DomainEvent>): void {
    const fullEvent: any = {
      aggregateId: this.id,
      aggregateType: "BankAccount",
      ...event,
    };

    this.apply(fullEvent);
    this.uncommittedEvents.push(fullEvent);
  }

  apply(event: DomainEvent): void {
    switch (event.eventType) {
      case "AccountOpened":
        this.isOpen = true;
        this.balance = event.data.initialDeposit;
        break;

      case "MoneyDeposited":
        this.balance += event.data.amount;
        break;

      case "MoneyWithdrawn":
        this.balance -= event.data.amount;
        break;

      case "AccountClosed":
        this.isOpen = false;
        break;
    }

    if (event.metadata) {
      this.version = event.metadata.version;
    }
  }

  getUncommittedEvents(): DomainEvent[] {
    return this.uncommittedEvents;
  }

  clearUncommittedEvents(): void {
    this.uncommittedEvents = [];
  }

  getState(): BankAccountState {
    return {
      id: this.id,
      balance: this.balance,
      isOpen: this.isOpen,
      version: this.version,
    };
  }
}

// Repository
class BankAccountRepository {
  constructor(private eventStore: EventStore) {}

  async save(account: BankAccount): Promise<void> {
    const events = account.getUncommittedEvents();

    if (events.length === 0) return;

    await this.eventStore.appendEvents(account.id, account.version, events);

    account.clearUncommittedEvents();
  }

  async load(id: string): Promise<BankAccount> {
    const events = await this.eventStore.getEvents(id);
    const account = new BankAccount(id);

    events.forEach((event) => account.apply(event));

    return account;
  }
}

// Usage
const eventStore = new EventStore();
const repository = new BankAccountRepository(eventStore);

// Create and use account
const account = new BankAccount("acc-123");
account.open(1000);
account.deposit(500);
account.withdraw(200);

await repository.save(account);

// Load account
const loadedAccount = await repository.load("acc-123");
console.log(loadedAccount.getState());
```
