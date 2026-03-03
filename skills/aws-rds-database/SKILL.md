---
name: aws-rds-database
description: >
  Deploy and manage relational databases using RDS with Multi-AZ, read replicas,
  backups, and encryption. Use for PostgreSQL, MySQL, MariaDB, and Oracle.
---

# AWS RDS Database

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Amazon RDS simplifies relational database deployment and operations. Support multiple database engines with automated backups, replication, encryption, and high availability through Multi-AZ deployments.

## When to Use

- PostgreSQL and MySQL applications
- Transactional databases and OLTP
- Oracle and Microsoft SQL Server workloads
- Read-heavy applications with replicas
- Development and staging environments
- Data requiring ACID compliance
- Applications needing automatic backups
- Disaster recovery scenarios

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [RDS Instance Creation with AWS CLI](references/rds-instance-creation-with-aws-cli.md) | RDS Instance Creation with AWS CLI |
| [Terraform RDS Configuration](references/terraform-rds-configuration.md) | Terraform RDS Configuration |
| [Database Connection and Configuration](references/database-connection-and-configuration.md) | Database Connection and Configuration |

## Best Practices

### ✅ DO

- Use Multi-AZ for production
- Enable automated backups
- Use encryption at rest and in transit
- Implement IAM database authentication
- Create read replicas for scaling
- Monitor performance metrics
- Set up CloudWatch alarms
- Store credentials in Secrets Manager
- Use parameter groups for configuration

### ❌ DON'T

- Store passwords in code
- Disable encryption
- Use public accessibility in production
- Ignore backup retention
- Skip automated backups
- Create databases without Multi-AZ
