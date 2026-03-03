# users

## users

Stores user account information.

**Columns:**

| Column             | Type         | Null | Default           | Description               |
| ------------------ | ------------ | ---- | ----------------- | ------------------------- |
| id                 | uuid         | NO   | gen_random_uuid() | Primary key               |
| email              | varchar(255) | NO   | -                 | User email (unique)       |
| password_hash      | varchar(255) | NO   | -                 | bcrypt hashed password    |
| name               | varchar(255) | NO   | -                 | User's full name          |
| email_verified     | boolean      | NO   | false             | Email verification status |
| two_factor_enabled | boolean      | NO   | false             | 2FA enabled flag          |
| two_factor_secret  | varchar(32)  | YES  | -                 | TOTP secret               |
| created_at         | timestamp    | NO   | now()             | Record creation time      |
| updated_at         | timestamp    | NO   | now()             | Last update time          |
| deleted_at         | timestamp    | YES  | -                 | Soft delete timestamp     |
| last_login_at      | timestamp    | YES  | -                 | Last login timestamp      |

**Indexes:**

```sql
CREATE UNIQUE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at);
CREATE INDEX idx_users_deleted_at ON users(deleted_at) WHERE deleted_at IS NULL;
```

**Constraints:**

```sql
ALTER TABLE users
  ADD CONSTRAINT users_email_format
  CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

ALTER TABLE users
  ADD CONSTRAINT users_name_length
  CHECK (length(name) >= 2);
```

**Triggers:**

```sql
-- Update updated_at timestamp
CREATE TRIGGER update_users_updated_at
  BEFORE UPDATE ON users
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();
```

**Sample Data:**

```sql
INSERT INTO users (email, password_hash, name, email_verified)
VALUES
  ('john@example.com', '$2b$12$...', 'John Doe', true),
  ('jane@example.com', '$2b$12$...', 'Jane Smith', true);
```

---
