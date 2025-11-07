---
name: data-replication-setup
description: Set up database replication for high availability and disaster recovery. Use when configuring master-slave replication, multi-master setups, or replication monitoring.
---

# Data Replication Setup

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

## PostgreSQL Replication

### Master-Slave (Primary-Standby) Setup

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

**PostgreSQL - Set Up Standby Server:**

```bash
# On standby server

# 1. Stop PostgreSQL if running
sudo systemctl stop postgresql

# 2. Take base backup from primary
pg_basebackup -h primary_ip -D /var/lib/postgresql/14/main \
  -U replication_user -v -P -W

# 3. Create standby.signal file
touch /var/lib/postgresql/14/main/standby.signal

# 4. Configure recovery: recovery.conf
# primary_conninfo = 'host=primary_ip user=replication_user password=password'

# 5. Start PostgreSQL
sudo systemctl start postgresql
```

**Monitor Replication Status:**

```sql
-- On primary: check connected standbys
SELECT pid, usename, application_name, client_addr, state
FROM pg_stat_replication;

-- On primary: check replication lag
SELECT slot_name, restart_lsn, confirmed_flush_lsn
FROM pg_replication_slots;

-- On standby: check recovery status
SELECT pg_is_wal_replay_paused();
SELECT extract(EPOCH FROM (now() - pg_last_xact_replay_timestamp())) as replication_lag_seconds;
```

### Logical Replication

**PostgreSQL - Logical Replication Setup:**

```sql
-- On publisher (primary)
CREATE PUBLICATION users_publication FOR TABLE users, orders;

-- Create replication slot
SELECT * FROM pg_create_logical_replication_slot('users_slot', 'pgoutput');

-- On subscriber (standby)
CREATE SUBSCRIPTION users_subscription
CONNECTION 'host=publisher_ip dbname=mydb user=repuser password=pwd'
PUBLICATION users_publication
WITH (copy_data = true);

-- Check subscription status
SELECT subname, subenabled, subconninfo
FROM pg_subscription;

-- Monitor replication status
SELECT slot_name, restart_lsn, confirmed_flush_lsn
FROM pg_replication_slots
WHERE slot_type = 'logical';
```

## MySQL Replication

### Master-Slave Setup

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

## Multi-Master Replication

**MySQL - Circular Replication:**

```sql
-- Server 1 (Master 1)
-- [mysqld]
-- server-id = 1
-- log-bin = mysql-bin
-- auto_increment_increment = 2
-- auto_increment_offset = 1

CHANGE MASTER TO
  MASTER_HOST = '192.168.1.101',
  MASTER_USER = 'replication',
  MASTER_PASSWORD = 'password',
  MASTER_LOG_FILE = 'mysql-bin.000001',
  MASTER_LOG_POS = 154;

START SLAVE;

-- Server 2 (Master 2)
-- [mysqld]
-- server-id = 2
-- log-bin = mysql-bin
-- auto_increment_increment = 2
-- auto_increment_offset = 2

CHANGE MASTER TO
  MASTER_HOST = '192.168.1.100',
  MASTER_USER = 'replication',
  MASTER_PASSWORD = 'password',
  MASTER_LOG_FILE = 'mysql-bin.000001',
  MASTER_LOG_POS = 154;

START SLAVE;
```

## Replication Monitoring

**PostgreSQL - Replication Health Check:**

```sql
-- Create monitoring function
CREATE OR REPLACE FUNCTION check_replication_health()
RETURNS TABLE (
  slot_name name,
  restart_lsn pg_lsn,
  confirmed_flush_lsn pg_lsn,
  lag_bytes bigint,
  status text
) AS $$
BEGIN
  RETURN QUERY
  SELECT
    rs.slot_name,
    rs.restart_lsn,
    rs.confirmed_flush_lsn,
    (pg_wal_lsn_diff(pg_current_wal_lsn(), rs.confirmed_flush_lsn))::bigint,
    CASE
      WHEN pg_wal_lsn_diff(pg_current_wal_lsn(), rs.confirmed_flush_lsn) < 1048576 THEN 'HEALTHY'
      WHEN pg_wal_lsn_diff(pg_current_wal_lsn(), rs.confirmed_flush_lsn) < 10485760 THEN 'WARNING'
      ELSE 'CRITICAL'
    END
  FROM pg_replication_slots rs
  WHERE slot_type = 'physical';
END;
$$ LANGUAGE plpgsql;

SELECT * FROM check_replication_health();
```

**MySQL - Replication Lag Monitoring:**

```sql
-- Monitor replication lag across multiple slaves
CREATE TABLE replication_monitoring (
  slave_host VARCHAR(50),
  slave_port INT,
  master_log_file VARCHAR(50),
  read_master_log_pos BIGINT,
  relay_log_file VARCHAR(50),
  relay_log_pos BIGINT,
  seconds_behind_master INT,
  checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert monitoring data
INSERT INTO replication_monitoring
SELECT
  @@hostname,
  @@port,
  Master_Log_File,
  Read_Master_Log_Pos,
  Relay_Log_File,
  Relay_Log_Pos,
  Seconds_Behind_Master,
  CURRENT_TIMESTAMP
FROM INFORMATION_SCHEMA.TABLES
LIMIT 1;  -- Use SHOW SLAVE STATUS values
```

## Replication Failover

**PostgreSQL - Promote Standby to Primary:**

```bash
# On standby server
# Promote standby to primary
pg_ctl promote -D /var/lib/postgresql/14/main

# Or use SQL command
SELECT pg_promote();
```

**MySQL - Promote Slave to Master:**

```sql
-- On slave
-- 1. Stop slave and wait for replication to complete
STOP SLAVE;
SHOW SLAVE STATUS\G  -- Verify Slave_IO_Running and Slave_SQL_Running are OFF

-- 2. Promote to master
RESET SLAVE ALL;

-- 3. Reset binary log
RESET MASTER;

-- 4. Old master becomes new slave
-- Configure old master as slave of new master
CHANGE MASTER TO
  MASTER_HOST = 'new_master_ip',
  MASTER_USER = 'replication',
  MASTER_PASSWORD = 'password',
  MASTER_AUTO_POSITION = 1;

START SLAVE;
```

## Replication Configuration Best Practices

**PostgreSQL - postgresql.conf settings:**

```conf
# WAL configuration
wal_level = replica
max_wal_senders = 10
wal_keep_size = 1GB
wal_receiver_timeout = 60s
wal_receiver_status_interval = 10s

# Hot standby
hot_standby = on
max_standby_streaming_delay = 3min

# Replication timeout
wal_sender_timeout = 300s
```

**MySQL - my.cnf settings:**

```conf
[mysqld]
# Replication configuration
server-id = 1
log-bin = mysql-bin
binlog_format = ROW
binlog-row-image = FULL

# Slave configuration
relay-log = mysql-relay-bin
relay-log-index = mysql-relay-bin.index
relay-log-info-repository = TABLE

# Safety
log_replica_updates = ON
slave_parallel_workers = 4
slave_parallel_type = LOGICAL_CLOCK
```

## Troubleshooting Replication

**PostgreSQL - Replication Issues:**

```sql
-- Check for missing files
SELECT slot_name, restart_lsn, wal_status
FROM pg_replication_slots;

-- Restart replication slot
SELECT pg_replication_slot_advance('slot_name', pg_current_wal_lsn());

-- Synchronize replication
SYNCHRONOUS_COMMIT = remote_apply;
```

**MySQL - Common Issues:**

```sql
-- Check duplicate entry error
SHOW SLAVE STATUS\G
-- Look for Last_SQL_Error

-- Skip error
SET GLOBAL SQL_SLAVE_SKIP_COUNTER = 1;
START SLAVE;

-- Reset replication
RESET SLAVE;
RESET MASTER;
```

## Replication Verification

- Test failover in non-production first
- Verify data consistency after replication
- Monitor replication lag continuously
- Document all replication configurations
- Test backup/recovery procedures
- Schedule regular replication audits

## Resources

- [PostgreSQL Streaming Replication](https://www.postgresql.org/docs/current/warm-standby.html)
- [MySQL Replication](https://dev.mysql.com/doc/refman/8.0/en/replication.html)
- [PostgreSQL Logical Replication](https://www.postgresql.org/docs/current/logical-replication.html)
