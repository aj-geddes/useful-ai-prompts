# Full Database Backup

## Full Database Backup

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
