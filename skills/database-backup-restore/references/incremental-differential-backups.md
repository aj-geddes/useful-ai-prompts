# Incremental & Differential Backups

## Incremental & Differential Backups

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
