---
name: data-migration-scripts
description: Create safe, reversible database migration scripts with rollback capabilities, data validation, and zero-downtime deployments. Use when changing database schemas, migrating data between systems, or performing large-scale data transformations.
---

# Data Migration Scripts

## Overview

Create robust, safe, and reversible data migration scripts for database schema changes and data transformations with minimal downtime.

## When to Use

- Database schema changes
- Adding/removing/modifying columns
- Migrating between database systems
- Data transformations and cleanup
- Splitting or merging tables
- Changing data types
- Adding indexes and constraints
- Backfilling data
- Multi-tenant data migrations

## Migration Principles

1. **Reversible** - Every migration should have a rollback
2. **Idempotent** - Safe to run multiple times
3. **Atomic** - All-or-nothing execution
4. **Tested** - Test on production-like data
5. **Monitored** - Track progress and errors
6. **Documented** - Clear purpose and side effects

## Implementation Examples

### 1. **Knex.js Migrations (Node.js)**

```typescript
import { Knex } from 'knex';

// migrations/20240101000000_add_user_preferences.ts
export async function up(knex: Knex): Promise<void> {
  // Create new table
  await knex.schema.createTable('user_preferences', (table) => {
    table.uuid('id').primary().defaultTo(knex.raw('gen_random_uuid()'));
    table.uuid('user_id').notNullable().references('id').inTable('users').onDelete('CASCADE');
    table.jsonb('preferences').defaultTo('{}');
    table.timestamp('created_at').defaultTo(knex.fn.now());
    table.timestamp('updated_at').defaultTo(knex.fn.now());

    table.index('user_id');
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

  console.log('Migrated user preferences for', await knex('user_preferences').count());
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
  await knex.schema.dropTableIfExists('user_preferences');
}
```

```typescript
// migrations/20240102000000_add_email_verification.ts
export async function up(knex: Knex): Promise<void> {
  // Add new columns
  await knex.schema.table('users', (table) => {
    table.boolean('email_verified').defaultTo(false);
    table.timestamp('email_verified_at').nullable();
    table.string('verification_token').nullable();
  });

  // Backfill verified status for existing users
  await knex('users')
    .where('created_at', '<', knex.raw("NOW() - INTERVAL '30 days'"))
    .update({
      email_verified: true,
      email_verified_at: knex.fn.now()
    });

  // Add index
  await knex.schema.table('users', (table) => {
    table.index('verification_token');
  });
}

export async function down(knex: Knex): Promise<void> {
  await knex.schema.table('users', (table) => {
    table.dropIndex('verification_token');
    table.dropColumn('email_verified');
    table.dropColumn('email_verified_at');
    table.dropColumn('verification_token');
  });
}
```

### 2. **Alembic Migrations (Python/SQLAlchemy)**

```python
"""Add user roles and permissions

Revision ID: a1b2c3d4e5f6
Revises: previous_revision
Create Date: 2024-01-01 00:00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers
revision = 'a1b2c3d4e5f6'
down_revision = 'previous_revision'
branch_labels = None
depends_on = None


def upgrade():
    # Create roles table
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(50), unique=True, nullable=False),
        sa.Column('description', sa.Text()),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # Create user_roles junction table
    op.create_table(
        'user_roles',
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE')),
        sa.Column('role_id', sa.Integer(), sa.ForeignKey('roles.id', ondelete='CASCADE')),
        sa.Column('assigned_at', sa.DateTime(), server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('user_id', 'role_id')
    )

    # Create indexes
    op.create_index('idx_user_roles_user_id', 'user_roles', ['user_id'])
    op.create_index('idx_user_roles_role_id', 'user_roles', ['role_id'])

    # Insert default roles
    op.execute("""
        INSERT INTO roles (name, description) VALUES
        ('admin', 'Administrator with full access'),
        ('user', 'Standard user'),
        ('guest', 'Guest with limited access')
    """)

    # Migrate existing users to default role
    op.execute("""
        INSERT INTO user_roles (user_id, role_id)
        SELECT u.id, r.id
        FROM users u
        CROSS JOIN roles r
        WHERE r.name = 'user'
    """)


def downgrade():
    # Drop tables in reverse order
    op.drop_index('idx_user_roles_role_id', 'user_roles')
    op.drop_index('idx_user_roles_user_id', 'user_roles')
    op.drop_table('user_roles')
    op.drop_table('roles')
```

### 3. **Large Data Migration with Batching**

```typescript
import { Knex } from 'knex';

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
    startTime: Date.now()
  };

  async migrate(knex: Knex): Promise<void> {
    console.log('Starting large data migration...');

    // Get total count
    const result = await knex('old_table').count('* as count').first();
    this.progress.total = parseInt(result?.count as string || '0');

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

    console.log('Migration complete!');
    this.logProgress();
  }

  private async processBatch(knex: Knex, offset: number): Promise<void> {
    const trx = await knex.transaction();

    try {
      // Fetch batch
      const records = await trx('old_table')
        .select('*')
        .limit(this.batchSize)
        .offset(offset);

      // Transform and insert
      const transformed = records.map(record => this.transformRecord(record));

      if (transformed.length > 0) {
        await trx('new_table')
          .insert(transformed)
          .onConflict('id')
          .merge(); // Upsert
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
      updated_at: new Date()
    };
  }

  private logProgress(): void {
    const percent = ((this.progress.processed / this.progress.total) * 100).toFixed(2);
    const elapsed = Date.now() - this.progress.startTime;
    const rate = this.progress.processed / (elapsed / 1000);

    console.log(
      `Progress: ${this.progress.processed}/${this.progress.total} (${percent}%) ` +
      `Errors: ${this.progress.errors} ` +
      `Rate: ${rate.toFixed(2)} records/sec`
    );
  }

  private delay(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}

// Usage in migration
export async function up(knex: Knex): Promise<void> {
  const migration = new LargeDataMigration();
  await migration.migrate(knex);
}
```

### 4. **Zero-Downtime Migration Pattern**

```typescript
// Phase 1: Add new column (nullable)
export async function up_phase1(knex: Knex): Promise<void> {
  await knex.schema.table('users', (table) => {
    table.string('email_new').nullable();
  });

  console.log('Phase 1: Added new column');
}

// Phase 2: Backfill data
export async function up_phase2(knex: Knex): Promise<void> {
  const batchSize = 1000;
  let processed = 0;

  while (true) {
    const result = await knex('users')
      .whereNull('email_new')
      .whereNotNull('email')
      .limit(batchSize)
      .update({
        email_new: knex.raw('email')
      });

    processed += result;

    if (result < batchSize) break;

    console.log(`Backfilled ${processed} records`);
    await new Promise(resolve => setTimeout(resolve, 100));
  }

  console.log(`Phase 2: Backfilled ${processed} total records`);
}

// Phase 3: Add constraint
export async function up_phase3(knex: Knex): Promise<void> {
  await knex.schema.alterTable('users', (table) => {
    table.string('email_new').notNullable().alter();
    table.unique('email_new');
  });

  console.log('Phase 3: Added constraints');
}

// Phase 4: Drop old column
export async function up_phase4(knex: Knex): Promise<void> {
  await knex.schema.table('users', (table) => {
    table.dropColumn('email');
  });

  await knex.schema.table('users', (table) => {
    table.renameColumn('email_new', 'email');
  });

  console.log('Phase 4: Completed migration');
}
```

### 5. **Migration Validation**

```typescript
class MigrationValidator {
  async validate(knex: Knex, migration: string): Promise<boolean> {
    console.log(`Validating migration: ${migration}`);

    const checks = [
      this.checkDataIntegrity(knex),
      this.checkConstraints(knex),
      this.checkIndexes(knex),
      this.checkRowCounts(knex)
    ];

    const results = await Promise.all(checks);
    const passed = results.every(r => r);

    if (passed) {
      console.log('✓ All validation checks passed');
    } else {
      console.error('✗ Validation failed');
    }

    return passed;
  }

  private async checkDataIntegrity(knex: Knex): Promise<boolean> {
    // Check for orphaned records
    const orphaned = await knex('user_roles')
      .leftJoin('users', 'user_roles.user_id', 'users.id')
      .whereNull('users.id')
      .count('* as count')
      .first();

    const count = parseInt(orphaned?.count as string || '0');

    if (count > 0) {
      console.error(`Found ${count} orphaned user_roles records`);
      return false;
    }

    console.log('✓ Data integrity check passed');
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
      console.error('Email unique constraint missing');
      return false;
    }

    console.log('✓ Constraints check passed');
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
      console.error('Email index missing');
      return false;
    }

    console.log('✓ Indexes check passed');
    return true;
  }

  private async checkRowCounts(knex: Knex): Promise<boolean> {
    const [oldCount, newCount] = await Promise.all([
      knex('users').count('* as count').first(),
      knex('user_preferences').count('* as count').first()
    ]);

    const old = parseInt(oldCount?.count as string || '0');
    const new_ = parseInt(newCount?.count as string || '0');

    if (Math.abs(old - new_) > old * 0.01) {
      console.error(`Row count mismatch: ${old} vs ${new_}`);
      return false;
    }

    console.log('✓ Row counts check passed');
    return true;
  }
}

// Usage
export async function up(knex: Knex): Promise<void> {
  // Run migration
  await performMigration(knex);

  // Validate
  const validator = new MigrationValidator();
  const valid = await validator.validate(knex, 'add_user_preferences');

  if (!valid) {
    throw new Error('Migration validation failed');
  }
}
```

### 6. **Cross-Database Migration**

```python
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
import logging

logger = logging.getLogger(__name__)

class CrossDatabaseMigration:
    def __init__(self, source_url: str, target_url: str):
        self.source_engine = create_engine(source_url)
        self.target_engine = create_engine(target_url)

        self.source_session = sessionmaker(bind=self.source_engine)()
        self.target_session = sessionmaker(bind=self.target_engine)()

    def migrate_table(self, table_name: str, batch_size: int = 1000):
        """Migrate table from source to target database."""
        logger.info(f"Starting migration of table: {table_name}")

        # Get table metadata
        metadata = MetaData()
        source_table = Table(
            table_name,
            metadata,
            autoload_with=self.source_engine
        )

        # Get total count
        total = self.source_session.execute(
            source_table.select().with_only_columns(func.count())
        ).scalar()

        logger.info(f"Total records to migrate: {total}")

        # Migrate in batches
        offset = 0
        while offset < total:
            # Fetch batch from source
            results = self.source_session.execute(
                source_table.select()
                .limit(batch_size)
                .offset(offset)
            ).fetchall()

            if not results:
                break

            # Transform and insert to target
            rows = [dict(row._mapping) for row in results]
            transformed = [self.transform_row(row) for row in rows]

            self.target_session.execute(
                source_table.insert(),
                transformed
            )
            self.target_session.commit()

            offset += batch_size
            logger.info(f"Migrated {offset}/{total} records")

        logger.info(f"Completed migration of {table_name}")

    def transform_row(self, row: dict) -> dict:
        """Transform row data if needed."""
        # Apply any transformations
        return row

    def cleanup(self):
        """Close connections."""
        self.source_session.close()
        self.target_session.close()
```

## Best Practices

### ✅ DO
- Always write both `up` and `down` migrations
- Test migrations on production-like data
- Use transactions for atomic operations
- Process large datasets in batches
- Add indexes after data insertion
- Validate data after migration
- Log progress and errors
- Use feature flags for application code changes
- Back up database before running migrations
- Test rollback procedures
- Document migration side effects
- Version control all migrations
- Use idempotent operations

### ❌ DON'T
- Run untested migrations on production
- Make breaking changes without backwards compatibility
- Process millions of rows in single transaction
- Skip rollback implementation
- Ignore migration failures
- Modify old migrations
- Delete data without backups
- Run migrations manually in production

## Migration Checklist

- [ ] Migration has both up and down
- [ ] Tested on production-like dataset
- [ ] Transactions used appropriately
- [ ] Large datasets processed in batches
- [ ] Indexes added after data insertion
- [ ] Data validation included
- [ ] Progress logging implemented
- [ ] Error handling included
- [ ] Rollback tested
- [ ] Documentation written
- [ ] Backup taken
- [ ] Team reviewed

## Resources

- [Knex.js Migrations](https://knexjs.org/guide/migrations.html)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Liquibase](https://www.liquibase.org/)
- [Flyway](https://flywaydb.org/)
