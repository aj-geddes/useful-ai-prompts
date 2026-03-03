# Knex.js Migrations (Node.js)

## Knex.js Migrations (Node.js)

```typescript
import { Knex } from "knex";

// migrations/20240101000000_add_user_preferences.ts
export async function up(knex: Knex): Promise<void> {
  // Create new table
  await knex.schema.createTable("user_preferences", (table) => {
    table.uuid("id").primary().defaultTo(knex.raw("gen_random_uuid()"));
    table
      .uuid("user_id")
      .notNullable()
      .references("id")
      .inTable("users")
      .onDelete("CASCADE");
    table.jsonb("preferences").defaultTo("{}");
    table.timestamp("created_at").defaultTo(knex.fn.now());
    table.timestamp("updated_at").defaultTo(knex.fn.now());

    table.index("user_id");
  });

  // Migrate existing data
  await knex.raw(`
    INSERT INTO user_preferences (user_id, preferences)
    SELECT id, jsonb_build_object(
      'theme', COALESCE(theme, 'light'),
      'notifications', COALESCE(notifications_enabled, true)
    )
    FROM users
    WHERE theme IS NOT NULL OR notifications_enabled IS NOT NULL
  `);

  console.log(
    "Migrated user preferences for",
    await knex("user_preferences").count(),
  );
}

export async function down(knex: Knex): Promise<void> {
  // Restore data to original table
  await knex.raw(`
    UPDATE users u
    SET
      theme = (p.preferences->>'theme'),
      notifications_enabled = (p.preferences->>'notifications')::boolean
    FROM user_preferences p
    WHERE u.id = p.user_id
  `);

  // Drop new table
  await knex.schema.dropTableIfExists("user_preferences");
}
```

```typescript
// migrations/20240102000000_add_email_verification.ts
export async function up(knex: Knex): Promise<void> {
  // Add new columns
  await knex.schema.table("users", (table) => {
    table.boolean("email_verified").defaultTo(false);
    table.timestamp("email_verified_at").nullable();
    table.string("verification_token").nullable();
  });

  // Backfill verified status for existing users
  await knex("users")
    .where("created_at", "<", knex.raw("NOW() - INTERVAL '30 days'"))
    .update({
      email_verified: true,
      email_verified_at: knex.fn.now(),
    });

  // Add index
  await knex.schema.table("users", (table) => {
    table.index("verification_token");
  });
}

export async function down(knex: Knex): Promise<void> {
  await knex.schema.table("users", (table) => {
    table.dropIndex("verification_token");
    table.dropColumn("email_verified");
    table.dropColumn("email_verified_at");
    table.dropColumn("verification_token");
  });
}
```
