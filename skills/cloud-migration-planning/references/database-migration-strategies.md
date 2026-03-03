# Database Migration Strategies

## Database Migration Strategies

```bash
# AWS Database Migration Service (DMS)
aws dms create-replication-instance \
  --replication-instance-identifier my-replication-instance \
  --replication-instance-class dms.t3.large \
  --allocated-storage 100 \
  --vpc-security-group-ids sg-12345

# Create source endpoint
aws dms create-endpoint \
  --endpoint-identifier source-db \
  --endpoint-type source \
  --engine-name postgres \
  --server-name source-db.example.com \
  --port 5432 \
  --username sourceadmin \
  --password sourcepassword \
  --database-name sourcedb

# Create target endpoint
aws dms create-endpoint \
  --endpoint-identifier target-rds \
  --endpoint-type target \
  --engine-name postgres \
  --server-name my-db.xyz.us-east-1.rds.amazonaws.com \
  --port 5432 \
  --username targetadmin \
  --password targetpassword \
  --database-name targetdb

# Create migration task
aws dms create-replication-task \
  --replication-task-identifier postgres-migration \
  --source-endpoint-arn arn:aws:dms:region:account:endpoint/source-db \
  --target-endpoint-arn arn:aws:dms:region:account:endpoint/target-rds \
  --replication-instance-arn arn:aws:dms:region:account:rep:my-replication-instance \
  --migration-type fullload \
  --table-mappings file://mappings.json

# Monitor migration
aws dms describe-replication-tasks \
  --filters Name=replication-task-arn,Values=arn:aws:dms:region:account:task:task-id

# Start migration
aws dms start-replication-task \
  --replication-task-arn arn:aws:dms:region:account:task:postgres-migration \
  --start-replication-task-type start-replication
```
