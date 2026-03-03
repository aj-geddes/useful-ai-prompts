# Directory-Based Sharding

## Directory-Based Sharding

**PostgreSQL - Lookup Table Approach:**

```sql
-- Create shard directory
CREATE TABLE shard_directory (
  shard_key VARCHAR(255) PRIMARY KEY,
  shard_id INT NOT NULL,
  shard_host VARCHAR(255) NOT NULL,
  shard_port INT DEFAULT 5432,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_shard_id ON shard_directory(shard_id);

-- Insert shard configuration
INSERT INTO shard_directory (shard_key, shard_id, shard_host) VALUES
('user_1', 0, 'shard0.example.com'),
('user_2', 1, 'shard1.example.com'),
('tenant_a', 2, 'shard2.example.com'),
('tenant_b', 3, 'shard3.example.com');

-- Function to get shard from directory
CREATE OR REPLACE FUNCTION get_shard_info(p_key VARCHAR)
RETURNS TABLE (shard_id INT, host VARCHAR, port INT) AS $$
BEGIN
  RETURN QUERY
  SELECT sd.shard_id, sd.shard_host, sd.shard_port
  FROM shard_directory sd
  WHERE sd.shard_key = p_key;
END;
$$ LANGUAGE plpgsql;
```
