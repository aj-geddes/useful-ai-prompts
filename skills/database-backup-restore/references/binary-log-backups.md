# Binary Log Backups

## Binary Log Backups

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
