# MySQL Restore

## MySQL Restore

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
