# Database Connection and Configuration

## Database Connection and Configuration

```bash
# Connect to RDS instance
psql -h myapp-db.xxxx.us-east-1.rds.amazonaws.com \
     -U admin \
     -d appdb \
     -p 5432

# Create database user with IAM authentication
psql -h myapp-db.xxxx.us-east-1.rds.amazonaws.com \
     -U admin \
     -d appdb << EOF
CREATE USER app_user;
GRANT CONNECT ON DATABASE appdb TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
ALTER ROLE app_user WITH PASSWORD 'MySecurePassword123!';
EOF

# Export database
pg_dump -h myapp-db.xxxx.us-east-1.rds.amazonaws.com \
        -U admin \
        appdb > backup.sql

# Import database
psql -h myapp-db.xxxx.us-east-1.rds.amazonaws.com \
     -U admin \
     appdb < backup.sql
```
