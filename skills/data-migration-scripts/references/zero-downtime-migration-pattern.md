# Zero-Downtime Migration Pattern

## Zero-Downtime Migration Pattern

```typescript
// Phase 1: Add new column (nullable)
export async function up_phase1(knex: Knex): Promise<void> {
  await knex.schema.table("users", (table) => {
    table.string("email_new").nullable();
  });

  console.log("Phase 1: Added new column");
}

// Phase 2: Backfill data
export async function up_phase2(knex: Knex): Promise<void> {
  const batchSize = 1000;
  let processed = 0;

  while (true) {
    const result = await knex("users")
      .whereNull("email_new")
      .whereNotNull("email")
      .limit(batchSize)
      .update({
        email_new: knex.raw("email"),
      });

    processed += result;

    if (result < batchSize) break;

    console.log(`Backfilled ${processed} records`);
    await new Promise((resolve) => setTimeout(resolve, 100));
  }

  console.log(`Phase 2: Backfilled ${processed} total records`);
}

// Phase 3: Add constraint
export async function up_phase3(knex: Knex): Promise<void> {
  await knex.schema.alterTable("users", (table) => {
    table.string("email_new").notNullable().alter();
    table.unique("email_new");
  });

  console.log("Phase 3: Added constraints");
}

// Phase 4: Drop old column
export async function up_phase4(knex: Knex): Promise<void> {
  await knex.schema.table("users", (table) => {
    table.dropColumn("email");
  });

  await knex.schema.table("users", (table) => {
    table.renameColumn("email_new", "email");
  });

  console.log("Phase 4: Completed migration");
}
```
