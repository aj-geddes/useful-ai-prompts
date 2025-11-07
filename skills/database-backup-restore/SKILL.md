---
name: database-backup-restore
description: Implement backup and restore strategies for disaster recovery. Use when creating backup plans, testing restore procedures, or setting up automated backups.
---

# Database Backup & Restore

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

## PostgreSQL Backup Strategies

### Full Database Backup

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

**pg_dump - Custom Binary Format:**

```bash
# Custom binary format (better for large databases)
pg_dump -h localhost -U postgres -F c database_name > backup.dump

# Parallel jobs for faster backup (PostgreSQL 9.3+)
pg_dump -h localhost -U postgres -F c -j 4 \
  --load-via-partition-root database_name > backup.dump

# Backup specific schema
pg_dump -h localhost -U postgres -n public database_name > backup.dump

# Get backup info
pg_dump_all -h localhost -U postgres > all_databases.sql
```

**pg_basebackup - Physical Backup:**

```bash
# Take base backup for streaming replication
pg_basebackup -h localhost -D ./backup_data -U replication_user -v -P

# Label backup for archival
pg_basebackup -h localhost -D ./backup_data \
  -U replication_user -l "backup_$(date +%Y%m%d)" -v -P

# Tar format with compression
pg_basebackup -h localhost -D - -U replication_user \
  -Ft -z -l "backup_$(date +%s)" | tar -xz -C ./backups/
```

### Incremental & Differential Backups

**WAL Archiving Setup:**

```sql
-- postgresql.conf configuration
-- wal_level = replica
-- archive_mode = on
-- archive_command = 'test ! -f /archive/%f && cp %p /archive/%f'
-- archive_timeout = 300

-- Monitor WAL archiving
SELECT
  name,
  setting
FROM pg_settings
WHERE name LIKE 'archive%';

-- Check WAL directory
-- ls -lh $PGDATA/pg_wal/

-- List archived WALs
-- ls -lh /archive/
```

**Continuous WAL Backup:**

```bash
#!/bin/bash
# Backup script with WAL archiving

BACKUP_DIR="/backups"
DB_NAME="production"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Create base backup
pg_basebackup -h localhost -D $BACKUP_DIR/base_$TIMESTAMP \
  -U backup_user -v

# Archive WAL files
WAL_DIR=$BACKUP_DIR/wal_$TIMESTAMP
mkdir -p $WAL_DIR
cp /var/lib/postgresql/14/main/pg_wal/* $WAL_DIR/

# Compress backup
tar -czf $BACKUP_DIR/backup_$TIMESTAMP.tar.gz \
  $BACKUP_DIR/base_$TIMESTAMP $BACKUP_DIR/wal_$TIMESTAMP

# Verify backup
pg_basebackup -h localhost -U backup_user --analyze

# Upload to S3
aws s3 cp $BACKUP_DIR/backup_$TIMESTAMP.tar.gz \
  s3://backup-bucket/postgres/
```

## MySQL Backup Strategies

### Full Database Backup

**mysqldump - Text Format:**

```bash
# Simple full backup
mysqldump -h localhost -u root -p database_name > backup.sql

# All databases
mysqldump -h localhost -u root -p --all-databases > all_databases.sql

# With flush privileges and triggers
mysqldump -h localhost -u root -p \
  --flush-privileges --triggers --routines \
  database_name > backup.sql

# Parallel backup (MySQL 5.7.11+)
mydumper -h localhost -u root -p password \
  -o ./backup_dir --threads 4 --compress
```

**Backup Specific Tables:**

```bash
# Backup specific tables
mysqldump -h localhost -u root -p database_name table1 table2 > tables.sql

# Exclude tables
mysqldump -h localhost -u root -p database_name \
  --ignore-table=database_name.temp_table \
  --ignore-table=database_name.logs > backup.sql
```

### Binary Log Backups

**Enable Binary Logging:**

```sql
-- Check binary logging status
SHOW VARIABLES LIKE 'log_bin%';

-- Configure in my.cnf
-- [mysqld]
-- log-bin = mysql-bin
-- binlog_format = ROW

-- View binary logs
SHOW BINARY LOGS;

-- Get current position
SHOW MASTER STATUS;
```

**Binary Log Backup:**

```bash
# Backup binary logs
MYSQL_PWD="password" mysqldump -h localhost -u root \
  --single-transaction --flush-logs --all-databases > backup.sql

# Copy binary logs
cp /var/log/mysql/mysql-bin.* /backup/binlogs/

# Backup incremental changes
mysqlbinlog /var/log/mysql/mysql-bin.000001 > binlog_backup.sql
```

## Restore Procedures

### PostgreSQL Restore

**Restore from Text Backup:**

```bash
# Drop and recreate database
psql -h localhost -U postgres -c "DROP DATABASE IF EXISTS database_name;"
psql -h localhost -U postgres -c "CREATE DATABASE database_name;"

# Restore from text backup
psql -h localhost -U postgres database_name < backup.sql

# Restore with verbose output
psql -h localhost -U postgres -1 database_name < backup.sql 2>&1 | tee restore.log
```

**Restore from Binary Backup:**

```bash
# Restore from custom format
pg_restore -h localhost -U postgres -d database_name \
  -v backup.dump

# Parallel restore (faster)
pg_restore -h localhost -U postgres -d database_name \
  -j 4 -v backup.dump

# Dry run (test restore without committing)
pg_restore --list backup.dump > restore_plan.txt
```

**Point-in-Time Recovery (PITR):**

```bash
# List available backups and WAL archives
ls -lh /archive/

# Restore to specific point in time
pg_basebackup -h localhost -D ./recovery_data \
  -U replication_user -c fast

# Create recovery.conf
cat > ./recovery_data/recovery.conf << EOF
recovery_target_timeline = 'latest'
recovery_target_xid = '1000000'
recovery_target_time = '2024-01-15 14:30:00'
recovery_target_name = 'before_bad_update'
EOF

# Start PostgreSQL with recovery
pg_ctl -D ./recovery_data start
```

### MySQL Restore

**Restore from SQL Backup:**

```bash
# Restore full database
mysql -h localhost -u root -p < backup.sql

# Restore specific database
mysql -h localhost -u root -p database_name < database_backup.sql

# Restore with progress
pv backup.sql | mysql -h localhost -u root -p database_name
```

**Restore with Binary Logs:**

```bash
# Restore from backup then apply binary logs
mysql -h localhost -u root -p < backup.sql

# Get starting binary log position from backup
grep "SET @@GLOBAL.GTID_PURGED=" backup.sql

# Apply binary logs after backup
mysqlbinlog /var/log/mysql/mysql-bin.000005 \
  --start-position=12345 | \
  mysql -h localhost -u root -p database_name
```

**Point-in-Time Recovery:**

```bash
# Restore base backup
mysql -h localhost -u root -p database_name < base_backup.sql

# Apply binary logs up to specific time
mysqlbinlog /var/log/mysql/mysql-bin.000005 \
  --stop-datetime='2024-01-15 14:30:00' | \
  mysql -h localhost -u root -p database_name
```

## Backup Validation

**PostgreSQL - Backup Integrity Check:**

```bash
# Verify backup file
pg_dump --analyze --schema-only database_name > /dev/null && echo "Backup OK"

# Test restore procedure
createdb test_restore
pg_restore -d test_restore backup.dump
psql -d test_restore -c "SELECT COUNT(*) FROM information_schema.tables;"
dropdb test_restore
```

**MySQL - Backup Integrity:**

```bash
# Check backup file syntax
mysql -h localhost -u root -p < backup.sql --dry-run

# Verify checksum
md5sum backup.sql
# Save checksum: echo "abc123def456 backup.sql" > backup.sql.md5
md5sum -c backup.sql.md5
```

## Automated Backup Schedule

**PostgreSQL - Cron Backup:**

```bash
#!/bin/bash
# backup.sh - Daily backup script

BACKUP_DIR="/backups/postgresql"
RETENTION_DAYS=30
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Create backup
pg_dump -h localhost -U postgres mydb | gzip > \
  $BACKUP_DIR/backup_$TIMESTAMP.sql.gz

# Delete old backups
find $BACKUP_DIR -name "backup_*.sql.gz" -mtime +$RETENTION_DAYS -delete

# Upload to S3
aws s3 cp $BACKUP_DIR/backup_$TIMESTAMP.sql.gz \
  s3://backup-bucket/postgresql/

# Log backup
echo "$TIMESTAMP: Backup completed" >> /var/log/db_backup.log
```

**Crontab Entry:**

```bash
# Daily backup at 2 AM
0 2 * * * /scripts/backup.sh

# Hourly backup
0 * * * * /scripts/hourly_backup.sh

# Weekly full backup
0 3 0 * * /scripts/weekly_backup.sh
```

## Backup Retention Policy

**PostgreSQL - Retention Strategy:**

```sql
-- Create retention tracking
CREATE TABLE backup_retention_policy (
  backup_id UUID PRIMARY KEY,
  database_name VARCHAR(255),
  backup_date TIMESTAMP,
  backup_type VARCHAR(20),  -- 'full', 'incremental', 'wal'
  retention_days INT,
  expires_at TIMESTAMP GENERATED ALWAYS AS
    (backup_date + INTERVAL '1 day' * retention_days) STORED
);

-- Example retention periods
INSERT INTO backup_retention_policy VALUES
('backup-001', 'production', NOW(), 'full', 30),
('backup-002', 'production', NOW(), 'incremental', 7),
('backup-003', 'staging', NOW(), 'full', 7);

-- Query expiring backups
SELECT backup_id, expires_at
FROM backup_retention_policy
WHERE expires_at < NOW();
```

## RTO/RPO Planning

```
Recovery Time Objective (RTO): How quickly must the system recover
Recovery Point Objective (RPO): How much data loss is acceptable

Example:
- RTO: 1 hour (system must be recovered within 1 hour)
- RPO: 15 minutes (no more than 15 minutes of data loss acceptable)

Backup frequency: Every 15 minutes (to meet RPO)
Replication lag: < 5 minutes (for RTO)
```

## Best Practices Checklist

✅ DO test restore procedures regularly
✅ DO implement automated backups
✅ DO monitor backup success
✅ DO encrypt backup files
✅ DO store backups offsite
✅ DO document recovery procedures
✅ DO track backup retention policies
✅ DO monitor backup performance

❌ DON'T rely on untested backups
❌ DON'T skip backup verification
❌ DON'T store backups on same server
❌ DON'T use weak encryption
❌ DON'T forget backup retention limits

## Resources

- [PostgreSQL Backup & Restore](https://www.postgresql.org/docs/current/backup.html)
- [MySQL Backup & Recovery](https://dev.mysql.com/doc/refman/8.0/en/backup-and-recovery.html)
- [Percona Backup for MongoDB](https://www.percona.com/mongodb-backup)
- [AWS RDS Automated Backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)
