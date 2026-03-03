# Database Encryption (PostgreSQL)

## Database Encryption (PostgreSQL)

```sql
-- Database-level encryption using pgcrypto

-- Enable pgcrypto extension
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Create table with encrypted columns
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    -- Encrypted sensitive data
    ssn BYTEA,
    credit_card BYTEA,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Insert encrypted data
INSERT INTO users (email, ssn, credit_card)
VALUES (
    'user@example.com',
    pgp_sym_encrypt('123-45-6789', 'encryption-key'),
    pgp_sym_encrypt('4111-1111-1111-1111', 'encryption-key')
);

-- Query encrypted data
SELECT
    email,
    pgp_sym_decrypt(ssn, 'encryption-key') AS ssn,
    pgp_sym_decrypt(credit_card, 'encryption-key') AS credit_card
FROM users
WHERE email = 'user@example.com';

-- Create function for transparent encryption
CREATE OR REPLACE FUNCTION encrypt_sensitive_data()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.ssn IS NOT NULL THEN
        NEW.ssn := pgp_sym_encrypt(NEW.ssn::TEXT, current_setting('app.encryption_key'));
    END IF;

    IF NEW.credit_card IS NOT NULL THEN
        NEW.credit_card := pgp_sym_encrypt(NEW.credit_card::TEXT, current_setting('app.encryption_key'));
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Attach trigger
CREATE TRIGGER encrypt_before_insert
    BEFORE INSERT ON users
    FOR EACH ROW
    EXECUTE FUNCTION encrypt_sensitive_data();
```
