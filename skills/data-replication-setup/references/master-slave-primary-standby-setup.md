# Master-Slave (Primary-Standby) Setup

## Master-Slave (Primary-Standby) Setup

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
