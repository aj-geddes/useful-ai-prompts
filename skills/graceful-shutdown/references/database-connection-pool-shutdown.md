# Database Connection Pool Shutdown

## Database Connection Pool Shutdown

```typescript
import { Pool } from "pg";

class DatabaseShutdown {
  private pool: Pool;
  private activeQueries = new Set<Promise<any>>();

  constructor(pool: Pool) {
    this.pool = pool;
    this.setupQueryTracking();
  }

  private setupQueryTracking(): void {
    const originalQuery = this.pool.query.bind(this.pool);

    this.pool.query = (...args: any[]) => {
      const queryPromise = originalQuery(...args);

      this.activeQueries.add(queryPromise);

      queryPromise.finally(() => {
        this.activeQueries.delete(queryPromise);
      });

      return queryPromise;
    };
  }

  async shutdown(): Promise<void> {
    console.log("Shutting down database connections...");

    // Wait for active queries
    if (this.activeQueries.size > 0) {
      console.log(`Waiting for ${this.activeQueries.size} active queries...`);

      await Promise.race([
        Promise.all(Array.from(this.activeQueries)),
        new Promise((resolve) => setTimeout(resolve, 5000)),
      ]);
    }

    // Close pool
    console.log("Ending pool...");
    await this.pool.end();

    console.log("Database connections closed");
  }
}
```
