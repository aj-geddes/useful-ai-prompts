# PostgreSQL Index Types

## PostgreSQL Index Types

**B-tree Indexes (Default):**

```sql
-- Standard equality and range queries
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_created_at ON orders(created_at DESC);

-- Composite indexes for multi-column queries
CREATE INDEX idx_orders_user_status
ON orders(user_id, status)
WHERE cancelled_at IS NULL;
```

**Hash Indexes:**

```sql
-- Exact match queries only
CREATE INDEX idx_product_sku USING hash ON products(sku);

-- Good for equality lookups on large text fields
CREATE INDEX idx_uuid_hash USING hash ON sessions(session_id);
```

**BRIN Indexes (Block Range):**

```sql
-- For large tables with monotonically increasing columns
CREATE INDEX idx_events_timestamp USING brin ON events(created_at)
WITH (pages_per_range = 128);

-- Excellent for time-series data
CREATE INDEX idx_logs_timestamp USING brin
ON application_logs(log_timestamp);
```

**GiST & GIN Indexes:**

```sql
-- GiST for spatial data and complex types
CREATE INDEX idx_locations_geom USING gist ON locations(geom);

-- GIN for JSONB and array columns
CREATE INDEX idx_products_metadata USING gin ON products(metadata);
CREATE INDEX idx_user_tags USING gin ON users(tags);
```
