# RDS Instance Creation with AWS CLI

## RDS Instance Creation with AWS CLI

```bash
# Create DB subnet group
aws rds create-db-subnet-group \
  --db-subnet-group-name app-db-subnet \
  --db-subnet-group-description "App database subnet" \
  --subnet-ids subnet-12345 subnet-67890

# Create security group for RDS
aws ec2 create-security-group \
  --group-name rds-sg \
  --description "RDS security group" \
  --vpc-id vpc-12345

# Allow inbound PostgreSQL
aws ec2 authorize-security-group-ingress \
  --group-id sg-rds123 \
  --protocol tcp \
  --port 5432 \
  --source-security-group-id sg-app123

# Create RDS instance
aws rds create-db-instance \
  --db-instance-identifier myapp-db \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --engine-version 15.2 \
  --master-username admin \
  --master-user-password MySecurePassword123! \
  --allocated-storage 100 \
  --storage-type gp3 \
  --db-subnet-group-name app-db-subnet \
  --vpc-security-group-ids sg-rds123 \
  --multi-az \
  --storage-encrypted \
  --kms-key-id arn:aws:kms:region:account:key/id \
  --backup-retention-period 30 \
  --preferred-backup-window "03:00-04:00" \
  --preferred-maintenance-window "mon:04:00-mon:05:00" \
  --enable-clouwatch-logs-exports postgresql \
  --enable-iam-database-authentication

# Create read replica
aws rds create-db-instance-read-replica \
  --db-instance-identifier myapp-db-read \
  --source-db-instance-identifier myapp-db

# Take manual snapshot
aws rds create-db-snapshot \
  --db-snapshot-identifier myapp-db-backup-2024 \
  --db-instance-identifier myapp-db

# Describe RDS instance
aws rds describe-db-instances \
  --db-instance-identifier myapp-db \
  --query 'DBInstances[0].[DBInstanceIdentifier,DBInstanceStatus,Endpoint.Address]'
```
