---
name: database-migration-management
description: >
  Manage database migrations and schema versioning. Use when planning
  migrations, version control, rollback strategies, or data transformations in
  PostgreSQL and MySQL.
---

# Database Migration Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement robust database migration systems with version control, rollback capabilities, and data transformation strategies. Includes migration frameworks and production deployment patterns.

## When to Use

- Schema versioning and evolution
- Data transformations and cleanup
- Adding/removing tables and columns
- Index creation and optimization
- Migration testing and validation
- Rollback planning and execution
- Multi-environment deployments

## Quick Start

Minimal working example:

```sql
-- Create migrations tracking table
CREATE TABLE schema_migrations (
  version BIGINT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  duration_ms INTEGER,
  checksum VARCHAR(64)
);

-- Create migration log table
CREATE TABLE migration_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  version BIGINT NOT NULL,
  status VARCHAR(20) NOT NULL,
  error_message TEXT,
  rolled_back_at TIMESTAMP,
  executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Function to record migration
CREATE OR REPLACE FUNCTION record_migration(
  p_version BIGINT,
  p_name VARCHAR,
  p_duration_ms INTEGER
) RETURNS void AS $$
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Adding Columns](references/adding-columns.md) | Adding Columns |
| [Renaming Columns](references/renaming-columns.md) | Renaming Columns |
| [Creating Indexes Non-blocking](references/creating-indexes-non-blocking.md) | Creating Indexes Non-blocking |
| [Data Transformations](references/data-transformations.md) | Data Transformations |
| [Table Structure Changes](references/table-structure-changes.md) | Table Structure Changes |

## Best Practices

### ✅ DO

- Write every migration with a matching rollback (down) script tested before deploying
- Use non-locking operations (e.g., CREATE INDEX CONCURRENTLY, ADD COLUMN without DEFAULT on older PG)
- Deploy schema changes separately from data backfills to keep transactions short
- Record checksums for each migration file to detect accidental modifications
- Test migrations against a production-size dataset copy, not just an empty schema
- Add column with NULL first, backfill, then add NOT NULL constraint in a separate migration

### ❌ DON'T

- Run destructive DDL (DROP COLUMN, DROP TABLE) without a verified backup and rollback plan
- Combine multiple unrelated schema changes in a single migration file
- Rename columns in-place on high-traffic tables — use an expand-contract pattern instead
- Assume migrations that pass on an empty database will succeed on production data
