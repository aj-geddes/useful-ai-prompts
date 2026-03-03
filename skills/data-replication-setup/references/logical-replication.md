# Logical Replication

## Logical Replication

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
