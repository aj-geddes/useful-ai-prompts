# Projections (Read Models)

## Projections (Read Models)

```typescript
interface AccountReadModel {
  id: string;
  balance: number;
  transactionCount: number;
  lastActivity: number;
}

class AccountProjection {
  private accounts = new Map<string, AccountReadModel>();

  async project(event: DomainEvent): Promise<void> {
    switch (event.eventType) {
      case "AccountOpened":
        await this.handleAccountOpened(event);
        break;

      case "MoneyDeposited":
        await this.handleMoneyDeposited(event);
        break;

      case "MoneyWithdrawn":
        await this.handleMoneyWithdrawn(event);
        break;
    }
  }

  private async handleAccountOpened(event: DomainEvent): Promise<void> {
    this.accounts.set(event.aggregateId, {
      id: event.aggregateId,
      balance: event.data.initialDeposit,
      transactionCount: 1,
      lastActivity: event.metadata.timestamp,
    });
  }

  private async handleMoneyDeposited(event: DomainEvent): Promise<void> {
    const account = this.accounts.get(event.aggregateId);
    if (!account) return;

    account.balance += event.data.amount;
    account.transactionCount++;
    account.lastActivity = event.metadata.timestamp;
  }

  private async handleMoneyWithdrawn(event: DomainEvent): Promise<void> {
    const account = this.accounts.get(event.aggregateId);
    if (!account) return;

    account.balance -= event.data.amount;
    account.transactionCount++;
    account.lastActivity = event.metadata.timestamp;
  }

  getAccount(id: string): AccountReadModel | undefined {
    return this.accounts.get(id);
  }

  getAllAccounts(): AccountReadModel[] {
    return Array.from(this.accounts.values());
  }
}
```
