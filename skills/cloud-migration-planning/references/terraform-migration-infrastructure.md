# Terraform Migration Infrastructure

## Terraform Migration Infrastructure

```hcl
# migration.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC for migration infrastructure
resource "aws_vpc" "migration" {
  cidr_block           = "10.100.0.0/16"
  enable_dns_hostnames = true

  tags = { Name = "migration-vpc" }
}

# Subnets for DMS
resource "aws_subnet" "migration" {
  count             = 2
  vpc_id            = aws_vpc.migration.id
  cidr_block        = "10.100.${count.index}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = { Name = "migration-subnet-${count.index}" }
}

# Replication subnet group
resource "aws_dms_replication_subnet_group" "migration" {
  replication_subnet_group_description = "Migration subnet group"
  replication_subnet_group_id          = "migration-subnet-group"
  subnet_ids                           = aws_subnet.migration[*].id
}

# Replication instance
resource "aws_dms_replication_instance" "migration" {
  allocated_storage           = 100
  apply_immediately           = true
  auto_minor_version_upgrade  = true
  engine_version              = "3.4.5"
  multi_az                    = true
  publicly_accessible         = false
  replication_instance_class  = "dms.c5.2xlarge"
  replication_instance_id     = "migration-instance"
  replication_subnet_group_id = aws_dms_replication_subnet_group.migration.id

  tags = { Name = "migration-instance" }
}

# Source database endpoint
resource "aws_dms_endpoint" "source" {
  endpoint_type   = "source"
  engine_name     = "postgres"
  server_name     = var.source_db_host
  port            = 5432
  username        = var.source_db_user
  password        = var.source_db_password
  database_name   = var.source_db_name
  endpoint_id     = "source-postgres"

  ssl_mode = "require"

  tags = { Name = "source-endpoint" }
}

# Target RDS endpoint
resource "aws_dms_endpoint" "target" {
  endpoint_type = "target"
  engine_name   = "postgres"
  server_name   = aws_db_instance.target.endpoint
  port          = 5432
  username      = aws_db_instance.target.username
  password      = var.target_db_password
  database_name = aws_db_instance.target.db_name
  endpoint_id   = "target-rds"

  tags = { Name = "target-endpoint" }
}

# Target RDS instance
resource "aws_db_instance" "target" {
  identifier          = "migration-target-db"
  allocated_storage   = 100
  engine              = "postgres"
  engine_version      = "15.2"
  instance_class      = "db.r5.2xlarge"
  username            = "postgres"
  password            = random_password.db.result
  db_name             = "targetdb"
  multi_az            = true
  publicly_accessible = false

  backup_retention_period = 30
  backup_window          = "03:00-04:00"

  skip_final_snapshot = false
  final_snapshot_identifier = "migration-target-final-snapshot"
}

# Replication task
resource "aws_dms_replication_task" "migration" {
  migration_type           = "full-load-and-cdc"
  replication_instance_arn = aws_dms_replication_instance.migration.replication_instance_arn
  replication_task_id      = "postgres-full-migration"
  source_endpoint_arn      = aws_dms_endpoint.source.endpoint_arn
  target_endpoint_arn      = aws_dms_endpoint.target.endpoint_arn

  table_mappings = jsonencode({
    rules = [
      {
        rule_type   = "selection"
        rule_id     = "1"
        rule_action = "include"
        object_locator = {
          schema_name = "%"
          table_name  = "%"
        }
      }
    ]
  })

  replication_task_settings = jsonencode({
    TargetMetadata = {
      TargetSchema        = "public"
      SupportLobs         = true
      FullLobMode         = false
      LobChunkSize        = 64
      LobMaxSize          = 32
    }
    FullLoadSettings = {
      TargetPrepMode             = "DROP_AND_CREATE"
      CreatePkAfterFullLoad      = false
      StopTaskCachedSourceNotApplied = false
    }
    Logging = {
      EnableLogging = true
      LogComponents = [
        {
          LogType = "SOURCE_UNSPECIFIED"
          Id      = "%COMMON_MESSAGES%"
          Severity = "LOGGER_SEVERITY_DEBUG"
        }
      ]
    }
  })

  tags = { Name = "postgres-migration" }

  depends_on = [
    aws_dms_endpoint.source,
    aws_dms_endpoint.target,
    aws_dms_replication_instance.migration
  ]
}

# Secrets Manager for credentials
resource "aws_secretsmanager_secret" "migration_creds" {
  name_prefix = "migration/"
}

resource "aws_secretsmanager_secret_version" "migration_creds" {
  secret_id = aws_secretsmanager_secret.migration_creds.id
  secret_string = jsonencode({
    source_db_password = var.source_db_password
    target_db_password = var.target_db_password
  })
}

# CloudWatch monitoring
resource "aws_cloudwatch_log_group" "dms" {
  name              = "/aws/dms/migration"
  retention_in_days = 7
}

resource "aws_cloudwatch_metric_alarm" "migration_failed" {
  alarm_name          = "dms-migration-failed"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "FailureCount"
  namespace           = "AWS/DMS"
  period              = 300
  statistic           = "Sum"
  threshold           = 1
  alarm_description   = "Alert on DMS migration failure"
}

# Random password
resource "random_password" "db" {
  length  = 16
  special = true
}

# Data source for AZs
data "aws_availability_zones" "available" {
  state = "available"
}

# Outputs
output "dms_instance_id" {
  value = aws_dms_replication_instance.migration.replication_instance_id
}

output "target_db_endpoint" {
  value = aws_db_instance.target.endpoint
}
```
