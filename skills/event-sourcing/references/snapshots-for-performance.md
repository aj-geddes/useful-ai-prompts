# Snapshots for Performance

## Snapshots for Performance

```typescript
interface Snapshot {
  aggregateId: string;
  version: number;
  state: any;
  createdAt: number;
}

class SnapshotStore {
  private snapshots = new Map<string, Snapshot>();

  async save(snapshot: Snapshot): Promise<void> {
    this.snapshots.set(snapshot.aggregateId, snapshot);
  }

  async get(aggregateId: string): Promise<Snapshot | null> {
    return this.snapshots.get(aggregateId) || null;
  }
}

class SnapshotRepository {
  constructor(
    private eventStore: EventStore,
    private snapshotStore: SnapshotStore,
    private snapshotInterval: number = 10,
  ) {}

  async load(id: string): Promise<BankAccount> {
    // Try to load from snapshot
    const snapshot = await this.snapshotStore.get(id);
    const fromVersion = snapshot?.version || 0;

    // Load events since snapshot
    const events = await this.eventStore.getEvents(id);
    const recentEvents = events.filter((e) => e.metadata.version > fromVersion);

    const account = new BankAccount(id);

    // Restore from snapshot
    if (snapshot) {
      Object.assign(account, snapshot.state);
    }

    // Apply recent events
    recentEvents.forEach((event) => account.apply(event));

    return account;
  }

  async save(account: BankAccount): Promise<void> {
    const events = account.getUncommittedEvents();

    if (events.length === 0) return;

    await this.eventStore.appendEvents(account.id, account.version, events);

    // Create snapshot if needed
    if (account.version % this.snapshotInterval === 0) {
      await this.snapshotStore.save({
        aggregateId: account.id,
        version: account.version,
        state: account.getState(),
        createdAt: Date.now(),
      });
    }

    account.clearUncommittedEvents();
  }
}
```
