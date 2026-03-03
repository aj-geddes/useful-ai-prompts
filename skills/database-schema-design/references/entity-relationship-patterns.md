# Entity-Relationship Patterns

## Entity-Relationship Patterns

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
