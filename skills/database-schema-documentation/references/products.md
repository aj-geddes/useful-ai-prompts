# products

## products

Stores product catalog information.

**Columns:**

| Column           | Type          | Null | Default           | Description                 |
| ---------------- | ------------- | ---- | ----------------- | --------------------------- |
| id               | uuid          | NO   | gen_random_uuid() | Primary key                 |
| name             | varchar(255)  | NO   | -                 | Product name                |
| slug             | varchar(255)  | NO   | -                 | URL-friendly name (unique)  |
| description      | text          | YES  | -                 | Product description         |
| price            | decimal(10,2) | NO   | -                 | Product price in USD        |
| compare_at_price | decimal(10,2) | YES  | -                 | Original price (for sales)  |
| sku              | varchar(100)  | NO   | -                 | Stock keeping unit (unique) |
| category_id      | uuid          | NO   | -                 | Foreign key to categories   |
| brand            | varchar(100)  | YES  | -                 | Product brand               |
| active           | boolean       | NO   | true              | Product visibility          |
| featured         | boolean       | NO   | false             | Featured product flag       |
| metadata         | jsonb         | YES  | -                 | Additional product metadata |
| created_at       | timestamp     | NO   | now()             | Record creation time        |
| updated_at       | timestamp     | NO   | now()             | Last update time            |

**Indexes:**

```sql
CREATE UNIQUE INDEX idx_products_slug ON products(slug);
CREATE UNIQUE INDEX idx_products_sku ON products(sku);
CREATE INDEX idx_products_category_id ON products(category_id);
CREATE INDEX idx_products_active ON products(active);
CREATE INDEX idx_products_featured ON products(featured) WHERE featured = true;
CREATE INDEX idx_products_metadata ON products USING gin(metadata);
```

**Foreign Keys:**

```sql
ALTER TABLE products
  ADD CONSTRAINT fk_products_category
  FOREIGN KEY (category_id)
  REFERENCES categories(id)
  ON DELETE RESTRICT;
```

**Full-Text Search:**

```sql
-- Add full-text search column
ALTER TABLE products ADD COLUMN search_vector tsvector;

-- Create full-text index
CREATE INDEX idx_products_search ON products USING gin(search_vector);

-- Trigger to update search vector
CREATE TRIGGER products_search_vector_update
  BEFORE INSERT OR UPDATE ON products
  FOR EACH ROW
  EXECUTE FUNCTION
    tsvector_update_trigger(
      search_vector, 'pg_catalog.english',
      name, description, brand
    );
```

---
