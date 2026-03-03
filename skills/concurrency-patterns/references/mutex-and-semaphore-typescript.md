# Mutex and Semaphore (TypeScript)

## Mutex and Semaphore (TypeScript)

```typescript
class Mutex {
  private locked = false;
  private queue: Array<() => void> = [];

  async acquire(): Promise<void> {
    if (!this.locked) {
      this.locked = true;
      return;
    }

    return new Promise((resolve) => {
      this.queue.push(resolve);
    });
  }

  release(): void {
    if (this.queue.length > 0) {
      const resolve = this.queue.shift()!;
      resolve();
    } else {
      this.locked = false;
    }
  }

  async runExclusive<T>(fn: () => Promise<T>): Promise<T> {
    await this.acquire();
    try {
      return await fn();
    } finally {
      this.release();
    }
  }
}

class Semaphore {
  private available: number;
  private queue: Array<() => void> = [];

  constructor(private max: number) {
    this.available = max;
  }

  async acquire(): Promise<void> {
    if (this.available > 0) {
      this.available--;
      return;
    }

    return new Promise((resolve) => {
      this.queue.push(resolve);
    });
  }

  release(): void {
    if (this.queue.length > 0) {
      const resolve = this.queue.shift()!;
      resolve();
    } else {
      this.available++;
    }
  }

  async runExclusive<T>(fn: () => Promise<T>): Promise<T> {
    await this.acquire();
    try {
      return await fn();
    } finally {
      this.release();
    }
  }
}

// Usage
const mutex = new Mutex();
let counter = 0;

async function incrementCounter() {
  await mutex.runExclusive(async () => {
    const current = counter;
    await new Promise((resolve) => setTimeout(resolve, 10));
    counter = current + 1;
  });
}

// Database connection pool with semaphore
const dbSemaphore = new Semaphore(10); // Max 10 concurrent connections

async function queryDatabase(query: string) {
  return dbSemaphore.runExclusive(async () => {
    // Execute query
    return executeQuery(query);
  });
}

async function executeQuery(query: string) {
  // Query logic
}
```
