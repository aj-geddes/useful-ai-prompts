# Migration Validation

## Migration Validation

```typescript
class MigrationValidator {
  async validate(knex: Knex, migration: string): Promise<boolean> {
    console.log(`Validating migration: ${migration}`);

    const checks = [
      this.checkDataIntegrity(knex),
      this.checkConstraints(knex),
      this.checkIndexes(knex),
      this.checkRowCounts(knex),
    ];

    const results = await Promise.all(checks);
    const passed = results.every((r) => r);

    if (passed) {
      console.log("✓ All validation checks passed");
    } else {
      console.error("✗ Validation failed");
    }

    return passed;
  }

  private async checkDataIntegrity(knex: Knex): Promise<boolean> {
    // Check for orphaned records
    const orphaned = await knex("user_roles")
      .leftJoin("users", "user_roles.user_id", "users.id")
      .whereNull("users.id")
      .count("* as count")
      .first();

    const count = parseInt((orphaned?.count as string) || "0");

    if (count > 0) {
      console.error(`Found ${count} orphaned user_roles records`);
      return false;
    }

    console.log("✓ Data integrity check passed");
    return true;
  }

  private async checkConstraints(knex: Knex): Promise<boolean> {
    // Verify constraints exist
    const result = await knex.raw(`
      SELECT COUNT(*) as count
      FROM information_schema.table_constraints
      WHERE table_name = 'users'
      AND constraint_type = 'UNIQUE'
      AND constraint_name LIKE '%email%'
    `);

    const hasConstraint = result.rows[0].count > 0;

    if (!hasConstraint) {
      console.error("Email unique constraint missing");
      return false;
    }

    console.log("✓ Constraints check passed");
    return true;
  }

  private async checkIndexes(knex: Knex): Promise<boolean> {
    // Verify indexes exist
    const result = await knex.raw(`
      SELECT indexname
      FROM pg_indexes
      WHERE tablename = 'users'
      AND indexname LIKE '%email%'
    `);

    if (result.rows.length === 0) {
      console.error("Email index missing");
      return false;
    }

    console.log("✓ Indexes check passed");
    return true;
  }

  private async checkRowCounts(knex: Knex): Promise<boolean> {
    const [oldCount, newCount] = await Promise.all([
      knex("users").count("* as count").first(),
      knex("user_preferences").count("* as count").first(),
    ]);

    const old = parseInt((oldCount?.count as string) || "0");
    const new_ = parseInt((newCount?.count as string) || "0");

    if (Math.abs(old - new_) > old * 0.01) {
      console.error(`Row count mismatch: ${old} vs ${new_}`);
      return false;
    }

    console.log("✓ Row counts check passed");
    return true;
  }
}

// Usage
export async function up(knex: Knex): Promise<void> {
  // Run migration
  await performMigration(knex);

  // Validate
  const validator = new MigrationValidator();
  const valid = await validator.validate(knex, "add_user_preferences");

  if (!valid) {
    throw new Error("Migration validation failed");
  }
}
```
