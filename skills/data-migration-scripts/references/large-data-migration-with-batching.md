# Large Data Migration with Batching

## Large Data Migration with Batching

```typescript
import { Knex } from "knex";

interface MigrationProgress {
  total: number;
  processed: number;
  errors: number;
  startTime: number;
}

class LargeDataMigration {
  private batchSize = 1000;
  private progress: MigrationProgress = {
    total: 0,
    processed: 0,
    errors: 0,
    startTime: Date.now(),
  };

  async migrate(knex: Knex): Promise<void> {
    console.log("Starting large data migration...");

    // Get total count
    const result = await knex("old_table").count("* as count").first();
    this.progress.total = parseInt((result?.count as string) || "0");

    console.log(`Total records to migrate: ${this.progress.total}`);

    // Process in batches
    let offset = 0;
    while (offset < this.progress.total) {
      await this.processBatch(knex, offset);
      offset += this.batchSize;

      // Log progress
      this.logProgress();

      // Small delay to avoid overwhelming the database
      await this.delay(100);
    }

    console.log("Migration complete!");
    this.logProgress();
  }

  private async processBatch(knex: Knex, offset: number): Promise<void> {
    const trx = await knex.transaction();

    try {
      // Fetch batch
      const records = await trx("old_table")
        .select("*")
        .limit(this.batchSize)
        .offset(offset);

      // Transform and insert
      const transformed = records.map((record) => this.transformRecord(record));

      if (transformed.length > 0) {
        await trx("new_table").insert(transformed).onConflict("id").merge(); // Upsert
      }

      await trx.commit();

      this.progress.processed += records.length;
    } catch (error) {
      await trx.rollback();
      console.error(`Batch failed at offset ${offset}:`, error);
      this.progress.errors += this.batchSize;

      // Continue or abort based on error severity
      throw error;
    }
  }

  private transformRecord(record: any): any {
    return {
      id: record.id,
      user_id: record.userId,
      data: JSON.stringify(record.legacyData),
      created_at: record.createdAt,
      updated_at: new Date(),
    };
  }

  private logProgress(): void {
    const percent = (
      (this.progress.processed / this.progress.total) *
      100
    ).toFixed(2);
    const elapsed = Date.now() - this.progress.startTime;
    const rate = this.progress.processed / (elapsed / 1000);

    console.log(
      `Progress: ${this.progress.processed}/${this.progress.total} (${percent}%) ` +
        `Errors: ${this.progress.errors} ` +
        `Rate: ${rate.toFixed(2)} records/sec`,
    );
  }

  private delay(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}

// Usage in migration
export async function up(knex: Knex): Promise<void> {
  const migration = new LargeDataMigration();
  await migration.migrate(knex);
}
```
