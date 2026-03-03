# Event Store with PostgreSQL

## Event Store with PostgreSQL

```typescript
import { Pool } from "pg";

class PostgresEventStore {
  constructor(private pool: Pool) {
    this.createTables();
  }

  private async createTables(): Promise<void> {
    await this.pool.query(`
      CREATE TABLE IF NOT EXISTS events (
        id UUID PRIMARY KEY,
        aggregate_id VARCHAR(255) NOT NULL,
        aggregate_type VARCHAR(100) NOT NULL,
        event_type VARCHAR(100) NOT NULL,
        data JSONB NOT NULL,
        metadata JSONB NOT NULL,
        version INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT NOW(),
        UNIQUE(aggregate_id, version)
      );

      CREATE INDEX IF NOT EXISTS idx_events_aggregate
      ON events (aggregate_id, version);

      CREATE INDEX IF NOT EXISTS idx_events_type
      ON events (event_type);
    `);
  }

  async appendEvents(
    aggregateId: string,
    expectedVersion: number,
    events: Omit<DomainEvent, "id" | "metadata">[],
  ): Promise<void> {
    const client = await this.pool.connect();

    try {
      await client.query("BEGIN");

      // Check version
      const result = await client.query(
        "SELECT MAX(version) as version FROM events WHERE aggregate_id = $1",
        [aggregateId],
      );

      const currentVersion = result.rows[0].version || 0;

      if (currentVersion !== expectedVersion) {
        throw new Error("Concurrency conflict");
      }

      // Insert events
      for (let i = 0; i < events.length; i++) {
        const event = events[i];
        const version = expectedVersion + i + 1;

        await client.query(
          `
          INSERT INTO events (
            id, aggregate_id, aggregate_type, event_type,
            data, metadata, version
          )
          VALUES ($1, $2, $3, $4, $5, $6, $7)
        `,
          [
            crypto.randomUUID(),
            aggregateId,
            event.aggregateType,
            event.eventType,
            JSON.stringify(event.data),
            JSON.stringify({ timestamp: Date.now(), version }),
            version,
          ],
        );
      }

      await client.query("COMMIT");
    } catch (error) {
      await client.query("ROLLBACK");
      throw error;
    } finally {
      client.release();
    }
  }

  async getEvents(
    aggregateId: string,
    fromVersion: number = 0,
  ): Promise<DomainEvent[]> {
    const result = await this.pool.query(
      `SELECT * FROM events
       WHERE aggregate_id = $1 AND version > $2
       ORDER BY version ASC`,
      [aggregateId, fromVersion],
    );

    return result.rows.map((row) => ({
      id: row.id,
      aggregateId: row.aggregate_id,
      aggregateType: row.aggregate_type,
      eventType: row.event_type,
      data: row.data,
      metadata: row.metadata,
    }));
  }

  async getEventsByType(
    eventType: string,
    fromTimestamp: number = 0,
  ): Promise<DomainEvent[]> {
    const result = await this.pool.query(
      `SELECT * FROM events
       WHERE event_type = $1
       AND (metadata->>'timestamp')::bigint > $2
       ORDER BY created_at ASC`,
      [eventType, fromTimestamp],
    );

    return result.rows.map((row) => ({
      id: row.id,
      aggregateId: row.aggregate_id,
      aggregateType: row.aggregate_type,
      eventType: row.event_type,
      data: row.data,
      metadata: row.metadata,
    }));
  }

  async getAllEvents(
    fromPosition: number = 0,
    limit: number = 100,
  ): Promise<DomainEvent[]> {
    const result = await this.pool.query(
      `SELECT * FROM events
       WHERE id > $1
       ORDER BY created_at ASC
       LIMIT $2`,
      [fromPosition, limit],
    );

    return result.rows.map((row) => ({
      id: row.id,
      aggregateId: row.aggregate_id,
      aggregateType: row.aggregate_type,
      eventType: row.event_type,
      data: row.data,
      metadata: row.metadata,
    }));
  }
}
```
