# Master-Slave Setup

## Master-Slave Setup

**MySQL - Configure Master Server:**

```sql
-- In MySQL config (my.cnf / my.ini)
-- [mysqld]
-- server-id = 1
-- log-bin = mysql-bin
-- binlog-format = ROW

-- Create replication user
CREATE USER 'replication'@'%' IDENTIFIED BY 'replication_password';
GRANT REPLICATION SLAVE ON *.* TO 'replication'@'%';
FLUSH PRIVILEGES;

-- Get binary log position
SHOW MASTER STATUS;
-- File: mysql-bin.000001
-- Position: 154
```

**MySQL - Configure Slave Server:**

```sql
-- In MySQL config (my.cnf / my.ini)
-- [mysqld]
-- server-id = 2
-- relay-log = mysql-relay-bin
-- binlog-format = ROW

-- Configure replication
CHANGE MASTER TO
  MASTER_HOST = '192.168.1.100',
  MASTER_USER = 'replication',
  MASTER_PASSWORD = 'replication_password',
  MASTER_LOG_FILE = 'mysql-bin.000001',
  MASTER_LOG_POS = 154;

-- Start replication
START SLAVE;

-- Check slave status
SHOW SLAVE STATUS\G
-- Should show: Slave_IO_Running: Yes, Slave_SQL_Running: Yes
```

**Monitor MySQL Replication:**

```sql
-- Check slave replication status
SHOW SLAVE STATUS\G

-- Check for replication errors
SHOW SLAVE STATUS\G
-- Look at Last_Error field

-- Stop and resume replication
STOP SLAVE;
-- Fix any issues...
START SLAVE;

-- Monitor replication lag
SHOW SLAVE STATUS\G
-- Check: Seconds_Behind_Master
```
