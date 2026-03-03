# Promise Pool (TypeScript)

## Promise Pool (TypeScript)

```typescript
class PromisePool {
  private queue: Array<() => Promise<any>> = [];
  private active = 0;

  constructor(private concurrency: number) {}

  async add<T>(fn: () => Promise<T>): Promise<T> {
    while (this.active >= this.concurrency) {
      await this.waitForSlot();
    }

    this.active++;

    try {
      return await fn();
    } finally {
      this.active--;
    }
  }

  private async waitForSlot(): Promise<void> {
    return new Promise((resolve) => {
      const checkSlot = () => {
        if (this.active < this.concurrency) {
          resolve();
        } else {
          setTimeout(checkSlot, 10);
        }
      };
      checkSlot();
    });
  }

  async map<T, R>(items: T[], fn: (item: T) => Promise<R>): Promise<R[]> {
    return Promise.all(items.map((item) => this.add(() => fn(item))));
  }
}

// Usage
const pool = new PromisePool(5);

const urls = Array.from(
  { length: 100 },
  (_, i) => `https://api.example.com/item/${i}`,
);

const results = await pool.map(urls, async (url) => {
  const response = await fetch(url);
  return response.json();
});
```
