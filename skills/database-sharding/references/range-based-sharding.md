# Range-Based Sharding

## Range-Based Sharding

**PostgreSQL - Range Sharding Implementation:**

```sql
-- Define shard ranges
-- Shard 0: user_id 0-999999
-- Shard 1: user_id 1000000-1999999
-- Shard 2: user_id 2000000-2999999

CREATE TABLE users_shard_0 (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id BIGINT NOT NULL,
  email VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  CONSTRAINT shard_0_range CHECK (user_id BETWEEN 0 AND 999999)
);

CREATE TABLE users_shard_1 (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id BIGINT NOT NULL,
  email VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  CONSTRAINT shard_1_range CHECK (user_id BETWEEN 1000000 AND 1999999)
);

-- Function to determine shard
CREATE OR REPLACE FUNCTION get_shard_id(p_user_id BIGINT)
RETURNS INT AS $$
BEGIN
  RETURN (p_user_id / 1000000)::INT;
END;
$$ LANGUAGE plpgsql IMMUTABLE;
```
