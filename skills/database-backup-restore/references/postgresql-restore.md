# PostgreSQL Restore

## PostgreSQL Restore

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
