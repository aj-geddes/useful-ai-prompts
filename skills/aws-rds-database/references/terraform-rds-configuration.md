# Terraform RDS Configuration

## Terraform RDS Configuration

```hcl
# rds.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# DB subnet group
resource "aws_db_subnet_group" "app" {
  name       = "app-db-subnet"
  subnet_ids = [aws_subnet.private1.id, aws_subnet.private2.id]

  tags = { Name = "app-db-subnet" }
}

# Security group
resource "aws_security_group" "rds" {
  name_prefix = "rds-"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.app.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# KMS key for encryption
resource "aws_kms_key" "rds" {
  description             = "RDS encryption key"
  deletion_window_in_days = 10
  enable_key_rotation     = true
}

resource "aws_kms_alias" "rds" {
  name          = "alias/rds-key"
  target_key_id = aws_kms_key.rds.key_id
}

# RDS instance
resource "aws_db_instance" "app" {
  identifier            = "myapp-db"
  engine               = "postgres"
  engine_version       = "15.2"
  instance_class       = "db.t3.micro"
  allocated_storage    = 100
  storage_type         = "gp3"
  storage_encrypted    = true
  kms_key_id           = aws_kms_key.rds.arn

  db_name  = "appdb"
  username = "admin"
  password = random_password.db_password.result

  db_subnet_group_name   = aws_db_subnet_group.app.name
  vpc_security_group_ids = [aws_security_group.rds.id]

  multi_az               = true
  publicly_accessible    = false

  backup_retention_period = 30
  backup_window           = "03:00-04:00"
  maintenance_window      = "mon:04:00-mon:05:00"
  copy_tags_to_snapshot   = true

  enabled_cloudwatch_logs_exports = ["postgresql"]

  enable_iam_database_authentication = true

  deletion_protection = true

  skip_final_snapshot       = false
  final_snapshot_identifier = "myapp-db-final-snapshot-${formatdate("YYYY-MM-DD-hhmm", timestamp())}"

  tags = {
    Name = "myapp-db"
  }
}

# Generate random password
resource "random_password" "db_password" {
  length  = 16
  special = true
}

# Store password in Secrets Manager
resource "aws_secretsmanager_secret" "db_password" {
  name_prefix             = "rds/myapp/"
  recovery_window_in_days = 7
}

resource "aws_secretsmanager_secret_version" "db_password" {
  secret_id = aws_secretsmanager_secret.db_password.id
  secret_string = jsonencode({
    username = aws_db_instance.app.username
    password = random_password.db_password.result
    engine   = "postgres"
    host     = aws_db_instance.app.address
    port     = aws_db_instance.app.port
    dbname   = aws_db_instance.app.db_name
  })
}

# Read replica
resource "aws_db_instance" "read_replica" {
  identifier     = "myapp-db-read"
  replicate_source_db = aws_db_instance.app.identifier
  instance_class      = "db.t3.micro"
  publicly_accessible = false

  tags = {
    Name = "myapp-db-read"
  }
}

# Enhanced monitoring role
resource "aws_iam_role" "rds_monitoring" {
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "monitoring.rds.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "rds_monitoring" {
  role       = aws_iam_role.rds_monitoring.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole"
}

# CloudWatch alarms
resource "aws_cloudwatch_metric_alarm" "db_cpu" {
  alarm_name          = "rds-high-cpu"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 2
  metric_name         = "CPUUtilization"
  namespace           = "AWS/RDS"
  period              = 300
  statistic           = "Average"
  threshold           = 80
  alarm_description   = "Alert when RDS CPU exceeds 80%"

  dimensions = {
    DBInstanceIdentifier = aws_db_instance.app.id
  }
}

resource "aws_cloudwatch_metric_alarm" "db_connections" {
  alarm_name          = "rds-high-connections"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "DatabaseConnections"
  namespace           = "AWS/RDS"
  period              = 300
  statistic           = "Average"
  threshold           = 80
  alarm_description   = "Alert when database connections exceed 80"

  dimensions = {
    DBInstanceIdentifier = aws_db_instance.app.id
  }
}

# Outputs
output "db_endpoint" {
  value       = aws_db_instance.app.endpoint
  description = "RDS endpoint address"
}

output "db_password_secret" {
  value       = aws_secretsmanager_secret.db_password.arn
  description = "Secret Manager ARN for database credentials"
}
```
