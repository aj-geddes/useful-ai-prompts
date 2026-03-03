---
name: data-replication-setup
description: >
  Set up database replication for high availability and disaster recovery. Use
  when configuring master-slave replication, multi-master setups, or replication
  monitoring.
---

# Data Replication Setup

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Configure database replication for disaster recovery, load distribution, and high availability. Covers master-slave, multi-master replication, and monitoring strategies.

## When to Use

- High availability setup
- Disaster recovery planning
- Read replica configuration
- Multi-region replication
- Replication monitoring and maintenance
- Failover automation
- Cross-region backup strategies

## Quick Start

**PostgreSQL - Configure Primary Server:**

```sql
-- On primary server: postgresql.conf
-- wal_level = replica
-- max_wal_senders = 10
-- wal_keep_size = 1GB

-- Create replication user
CREATE ROLE replication_user WITH REPLICATION ENCRYPTED PASSWORD 'secure_password';

-- Allow replication connections: pg_hba.conf
-- host    replication     replication_user   standby_ip/32    md5

-- Enable WAL archiving for continuous backup
-- archive_mode = on
-- archive_command = 'test ! -f /archive/%f && cp %p /archive/%f'
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Master-Slave (Primary-Standby) Setup](references/master-slave-primary-standby-setup.md) | Master-Slave (Primary-Standby) Setup |
| [Logical Replication](references/logical-replication.md) | Logical Replication |
| [Master-Slave Setup](references/master-slave-setup.md) | Master-Slave Setup |

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
