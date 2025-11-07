---
name: database-schema-design
description: Design database schemas with normalization, relationships, and constraints. Use when creating new database schemas, designing tables, or planning data models for PostgreSQL and MySQL.
---

# Database Schema Design

## Overview

Design scalable, normalized database schemas with proper relationships, constraints, and data types. Includes normalization techniques, relationship patterns, and constraint strategies.

## When to Use

- New database schema design
- Data model planning
- Table structure definition
- Relationship design (1:1, 1:N, N:N)
- Normalization analysis
- Constraint and trigger planning
- Performance optimization at schema level

## Normalization Strategy

### First Normal Form (1NF)

**PostgreSQL - Eliminate Repeating Groups:**

```sql
-- NOT 1NF: repeating group in single column
CREATE TABLE orders_bad (
  id UUID PRIMARY KEY,
  customer_name VARCHAR(255),
  product_ids VARCHAR(255)  -- "1,2,3" - repeating group
);

-- 1NF: separate table for repeating data
CREATE TABLE orders (
  id UUID PRIMARY KEY,
  customer_name VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE order_items (
  id UUID PRIMARY KEY,
  order_id UUID NOT NULL,
  product_id UUID NOT NULL,
  quantity INTEGER NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
);
```

### Second Normal Form (2NF)

**PostgreSQL - Remove Partial Dependencies:**

```sql
-- NOT 2NF: non-key attribute depends on part of composite key
CREATE TABLE enrollment_bad (
  student_id UUID,
  course_id UUID,
  professor_name VARCHAR(255),  -- depends on course_id only
  PRIMARY KEY (student_id, course_id)
);

-- 2NF: separate tables
CREATE TABLE enrollments (
  id UUID PRIMARY KEY,
  student_id UUID NOT NULL,
  course_id UUID NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (course_id) REFERENCES courses(id),
  UNIQUE(student_id, course_id)
);

CREATE TABLE courses (
  id UUID PRIMARY KEY,
  name VARCHAR(255),
  professor_id UUID NOT NULL,
  FOREIGN KEY (professor_id) REFERENCES professors(id)
);
```

### Third Normal Form (3NF)

**PostgreSQL - Remove Transitive Dependencies:**

```sql
-- NOT 3NF: transitive dependency (customer_city depends on customer_state)
CREATE TABLE orders_bad (
  id UUID PRIMARY KEY,
  customer_city VARCHAR(100),
  customer_state VARCHAR(50),
  state_tax_rate DECIMAL(5,3)  -- depends on customer_state
);

-- 3NF: separate tables
CREATE TABLE states (
  id UUID PRIMARY KEY,
  code VARCHAR(2) UNIQUE,
  name VARCHAR(100),
  tax_rate DECIMAL(5,3)
);

CREATE TABLE orders (
  id UUID PRIMARY KEY,
  customer_city VARCHAR(100),
  state_id UUID NOT NULL,
  FOREIGN KEY (state_id) REFERENCES states(id)
);
```

## Table Design Patterns

### Entity-Relationship Patterns

**PostgreSQL - One-to-Many:**

```sql
-- One user has many orders
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE orders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL,
  order_date TIMESTAMP DEFAULT NOW(),
  total DECIMAL(10,2),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  INDEX idx_user_id (user_id)
);
```

**PostgreSQL - One-to-One:**

```sql
-- One user has one profile
CREATE TABLE user_profiles (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID UNIQUE NOT NULL,
  bio TEXT,
  avatar_url VARCHAR(500),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

**PostgreSQL - Many-to-Many:**

```sql
-- Students and courses (many-to-many)
CREATE TABLE students (
  id UUID PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE courses (
  id UUID PRIMARY KEY,
  title VARCHAR(255)
);

-- Junction table
CREATE TABLE course_enrollments (
  id UUID PRIMARY KEY,
  student_id UUID NOT NULL,
  course_id UUID NOT NULL,
  enrolled_at TIMESTAMP DEFAULT NOW(),
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
  UNIQUE(student_id, course_id)
);
```

## Constraint Strategy

**PostgreSQL - Data Integrity:**

```sql
-- NOT NULL constraints
CREATE TABLE products (
  id UUID PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  sku VARCHAR(100) NOT NULL,
  price DECIMAL(10,2) NOT NULL
);

-- UNIQUE constraints
ALTER TABLE products
ADD CONSTRAINT unique_sku UNIQUE(sku);

-- CHECK constraints
ALTER TABLE products
ADD CONSTRAINT price_positive CHECK (price > 0);

ALTER TABLE orders
ADD CONSTRAINT valid_status
CHECK (status IN ('pending', 'processing', 'completed', 'cancelled'));

-- DEFAULT values
CREATE TABLE audit_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  table_name VARCHAR(100) NOT NULL,
  operation VARCHAR(10) NOT NULL,
  user_id UUID,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Data Type Selection

**PostgreSQL - Optimal Data Types:**

```sql
CREATE TABLE users (
  -- Identifiers
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Text fields
  email VARCHAR(255),          -- Fixed length for emails
  name TEXT,                   -- Unbounded text
  bio TEXT,

  -- Numeric data
  age SMALLINT,                -- 0-32767
  balance DECIMAL(15,2),       -- Financial data (precise)
  rating NUMERIC(3,1),         -- Range 0.0-9.9

  -- Boolean
  is_active BOOLEAN DEFAULT true,
  email_verified BOOLEAN,

  -- Dates and Times
  birth_date DATE,
  last_login TIMESTAMP WITH TIME ZONE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  -- JSON/Binary
  metadata JSONB,
  profile_image BYTEA,

  -- Arrays (PostgreSQL specific)
  tags TEXT[] DEFAULT ARRAY[]::TEXT[]
);
```

**MySQL - Compatible Data Types:**

```sql
CREATE TABLE users (
  id CHAR(36) PRIMARY KEY,       -- UUID as CHAR

  email VARCHAR(255),
  name VARCHAR(255),

  age TINYINT UNSIGNED,
  balance DECIMAL(15,2),

  is_active BOOLEAN DEFAULT true,

  birth_date DATE,
  last_login TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  metadata JSON,

  KEY idx_email (email)
);
```

## Schema Evolution

**PostgreSQL - Backward Compatible Changes:**

```sql
-- Add column with default
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Add column for new feature
ALTER TABLE orders
ADD COLUMN notes TEXT DEFAULT '';

-- Add constraint on new column
ALTER TABLE orders
ADD CONSTRAINT check_notes CHECK (LENGTH(notes) <= 500);

-- Deprecate column safely
ALTER TABLE users RENAME COLUMN old_field TO old_field_deprecated;
```

**MySQL - Schema Changes:**

```sql
-- Add column with default
ALTER TABLE users ADD COLUMN phone VARCHAR(20) DEFAULT '';

-- Add multiple columns
ALTER TABLE orders
ADD COLUMN notes TEXT DEFAULT '',
ADD COLUMN internal_status VARCHAR(50);

-- Modify column
ALTER TABLE users MODIFY COLUMN bio TEXT;
```

## Performance Considerations

**PostgreSQL - Partitioning Large Tables:**

```sql
-- Partition by date range for time-series data
CREATE TABLE events (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL,
  event_type VARCHAR(100),
  created_at TIMESTAMP NOT NULL
) PARTITION BY RANGE (DATE_TRUNC('month', created_at));

CREATE TABLE events_2024_01 PARTITION OF events
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
```

## Schema Design Checklist

- Identify entities and relationships
- Apply normalization rules (1NF, 2NF, 3NF)
- Define primary keys for all tables
- Create foreign keys for relationships
- Add constraints for data integrity
- Select appropriate data types
- Plan indexes for common queries
- Design for scalability (denormalization if needed)
- Document table purposes and relationships
- Plan for schema evolution

## Common Pitfalls

❌ Don't skip normalization for convenience
❌ Don't use VARCHAR(MAX) for all text fields
❌ Don't forget to add foreign key constraints
❌ Don't use natural keys as primary keys
❌ Don't store calculated values in base tables

✅ DO use UUIDs or sequences for primary keys
✅ DO normalize data appropriately
✅ DO add CHECK constraints for data validity
✅ DO create indexes on foreign keys
✅ DO use TIMESTAMP for audit trails

## Resources

- [PostgreSQL Data Types](https://www.postgresql.org/docs/current/datatype.html)
- [MySQL Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)
- [Database Normalization Guide](https://en.wikipedia.org/wiki/Database_normalization)
- [Draw.io](https://draw.io/) - Schema diagram tool
