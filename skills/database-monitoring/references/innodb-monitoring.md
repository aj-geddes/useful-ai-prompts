# InnoDB Monitoring

## InnoDB Monitoring

**MySQL - InnoDB Buffer Pool:**

```sql
-- Buffer pool statistics
SHOW STATUS LIKE 'Innodb_buffer_pool%';

-- Calculate hit ratio
-- (Innodb_buffer_pool_read_requests - Innodb_buffer_pool_reads) /
-- Innodb_buffer_pool_read_requests

-- View InnoDB transactions
SELECT * FROM INFORMATION_SCHEMA.INNODB_TRX
ORDER BY trx_started DESC;

-- View InnoDB locks
SELECT * FROM INFORMATION_SCHEMA.INNODB_LOCKS;

-- Monitor InnoDB pages
SHOW STATUS LIKE 'Innodb_pages%';
```

**MySQL - Table and Index Statistics:**

```sql
-- Table statistics
SELECT
  TABLE_SCHEMA,
  TABLE_NAME,
  ROUND(((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024), 2) as Size_MB,
  TABLE_ROWS
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA != 'information_schema'
ORDER BY (DATA_LENGTH + INDEX_LENGTH) DESC;

-- Index cardinality
SELECT
  TABLE_SCHEMA,
  TABLE_NAME,
  COLUMN_NAME,
  SEQ_IN_INDEX,
  CARDINALITY
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = 'your_database'
ORDER BY TABLE_NAME, SEQ_IN_INDEX;
```
