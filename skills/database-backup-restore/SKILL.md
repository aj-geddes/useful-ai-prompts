---
name: database-backup-restore
description: >
  Implement backup and restore strategies for disaster recovery. Use when
  creating backup plans, testing restore procedures, or setting up automated
  backups.
---

# Database Backup & Restore

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive backup and disaster recovery strategies. Covers backup types, retention policies, restore testing, and recovery time objectives (RTO/RPO).

## When to Use

- Backup automation setup
- Disaster recovery planning
- Recovery testing procedures
- Backup retention policies
- Point-in-time recovery (PITR)
- Cross-region backup replication
- Compliance and audit requirements

## Quick Start

**pg_dump - Text Format:**

```bash
# Simple full backup
pg_dump -h localhost -U postgres -F p database_name > backup.sql

# With compression
pg_dump -h localhost -U postgres -F p database_name | gzip > backup.sql.gz

# Backup with verbose output
pg_dump -h localhost -U postgres -F p -v database_name > backup.sql 2>&1

# Exclude specific tables
pg_dump -h localhost -U postgres database_name \
  --exclude-table=temp_* --exclude-table=logs > backup.sql
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Full Database Backup](references/full-database-backup.md) | Full Database Backup |
| [Incremental & Differential Backups](references/incremental-differential-backups.md) | Incremental & Differential Backups |
| [Full Database Backup](references/full-database-backup-2.md) | Full Database Backup |
| [Binary Log Backups](references/binary-log-backups.md) | Binary Log Backups |
| [PostgreSQL Restore](references/postgresql-restore.md) | PostgreSQL Restore |
| [MySQL Restore](references/mysql-restore.md) | MySQL Restore |

## Best Practices

### ✅ DO

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
