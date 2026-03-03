# Hash-Based Sharding

## Hash-Based Sharding

**PostgreSQL - Consistent Hash Sharding:**

```sql
-- Hash-based distribution across 4 shards
CREATE OR REPLACE FUNCTION get_hash_shard(
  p_key VARCHAR,
  p_shard_count INT DEFAULT 4
)
RETURNS INT AS $$
DECLARE
  hash_val BIGINT;
BEGIN
  -- Use PostgreSQL's hashtext function
  hash_val := abs(hashtext(p_key)::BIGINT);
  RETURN (hash_val % p_shard_count)::INT;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- Create sharded tables
CREATE TABLE users_shard_0 (
  id UUID PRIMARY KEY,
  user_key VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE users_shard_1 AS TABLE users_shard_0;
CREATE TABLE users_shard_2 AS TABLE users_shard_0;
CREATE TABLE users_shard_3 AS TABLE users_shard_0;

-- Insert with shard routing
INSERT INTO users_shard_0
SELECT * FROM users WHERE get_hash_shard(user_key, 4) = 0;

INSERT INTO users_shard_1
SELECT * FROM users WHERE get_hash_shard(user_key, 4) = 1;
```

**Consistent Hashing for Resilience:**

```sql
-- Virtual nodes for better load distribution
CREATE TABLE shard_mapping (
  virtual_node_id INT PRIMARY KEY,
  actual_shard_id INT NOT NULL,
  shard_host VARCHAR(255),
  shard_port INT
);

INSERT INTO shard_mapping VALUES
(0, 0, 'shard0.example.com', 5432),
(1, 1, 'shard1.example.com', 5432),
(2, 2, 'shard2.example.com', 5432),
(3, 3, 'shard3.example.com', 5432),
(4, 1, 'shard1.example.com', 5432),  -- Virtual node
(5, 2, 'shard2.example.com', 5432);

-- Find shard for key
CREATE OR REPLACE FUNCTION find_shard_host(p_key VARCHAR)
RETURNS TABLE (shard_id INT, host VARCHAR, port INT) AS $$
BEGIN
  RETURN QUERY
  SELECT sm.actual_shard_id, sm.shard_host, sm.shard_port
  FROM shard_mapping sm
  WHERE sm.virtual_node_id = (
    abs(hashtext(p_key)::BIGINT) %
    (SELECT COUNT(*) FROM shard_mapping)
  )::INT
  LIMIT 1;
END;
$$ LANGUAGE plpgsql;
```
