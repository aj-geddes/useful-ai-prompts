---
name: cloud-migration-planning
description: Plan and execute cloud migrations with assessment, database migration, application refactoring, and cutover strategies across AWS, Azure, and GCP.
---

# Cloud Migration Planning

## Overview

Cloud migration planning involves assessing current infrastructure, designing migration strategies, executing migrations with minimal downtime, and validating outcomes. Support lift-and-shift, replatforming, and refactoring approaches for smooth cloud adoption.

## When to Use

- Moving from on-premises to cloud
- Cloud platform consolidation
- Legacy system modernization
- Reducing data center costs
- Improving scalability and availability
- Meeting compliance requirements
- Disaster recovery enhancement
- Technology refresh initiatives

## Implementation Examples

### 1. **Migration Assessment and Planning**

```python
# Cloud migration assessment tool
from enum import Enum
from typing import Dict, List, Tuple
from dataclasses import dataclass

class MigrationStrategy(Enum):
    LIFT_AND_SHIFT = "lift_and_shift"  # Rehost
    REPLATFORM = "replatform"          # Rehost with optimizations
    REFACTOR = "refactor"              # Rebuild for cloud
    REPURCHASE = "repurchase"          # Switch to SaaS
    RETIRE = "retire"                  # Decommission

class ApplicationComplexity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass
class ApplicationAssessment:
    name: str
    complexity: ApplicationComplexity
    dependencies: List[str]
    estimated_effort: int  # days
    business_criticality: int  # 1-10
    current_costs: float  # annual
    cloud_costs_estimate: float  # annual

class CloudMigrationPlanner:
    def __init__(self):
        self.applications: List[ApplicationAssessment] = []
        self.total_effort = 0
        self.total_cost_savings = 0

    def add_application(self, app: ApplicationAssessment):
        """Add application to migration assessment"""
        self.applications.append(app)

    def recommend_migration_strategy(self, app: ApplicationAssessment) -> MigrationStrategy:
        """Recommend migration strategy based on application characteristics"""
        if app.complexity == ApplicationComplexity.LOW:
            return MigrationStrategy.LIFT_AND_SHIFT

        elif app.complexity == ApplicationComplexity.MEDIUM:
            # Check if cost savings justify refactoring
            annual_savings = app.current_costs - app.cloud_costs_estimate
            refactor_cost = app.estimated_effort * 500  # cost per day
            payback_months = (refactor_cost / annual_savings) * 12 if annual_savings > 0 else float('inf')

            if payback_months < 6:
                return MigrationStrategy.REFACTOR
            else:
                return MigrationStrategy.REPLATFORM

        else:  # HIGH complexity
            # Evaluate if modernization is worthwhile
            if app.business_criticality >= 8:
                return MigrationStrategy.REFACTOR
            else:
                return MigrationStrategy.RETIRE  # Consider retiring

    def create_migration_wave_plan(self) -> Dict:
        """Create phased migration plan"""
        # Sort by criticality and dependencies
        sorted_apps = sorted(
            self.applications,
            key=lambda x: (len(x.dependencies), -x.business_criticality)
        )

        waves = {
            'wave_1': [],  # Low-risk, few dependencies
            'wave_2': [],  # Medium-risk
            'wave_3': []   # High-risk or critical
        }

        migrated = set()

        for app in sorted_apps:
            # Check if dependencies are satisfied
            deps_satisfied = all(dep in migrated for dep in app.dependencies)

            if not deps_satisfied:
                continue

            if app.complexity == ApplicationComplexity.LOW:
                waves['wave_1'].append(app.name)
            elif app.complexity == ApplicationComplexity.MEDIUM:
                waves['wave_2'].append(app.name)
            else:
                waves['wave_3'].append(app.name)

            migrated.add(app.name)

        return {
            'waves': waves,
            'total_applications': len(self.applications),
            'migrated_count': len(migrated),
            'total_effort_days': sum(app.estimated_effort for app in self.applications)
        }

    def calculate_roi(self) -> Dict:
        """Calculate migration ROI"""
        total_current_costs = sum(app.current_costs for app in self.applications)
        total_cloud_costs = sum(app.cloud_costs_estimate for app in self.applications)
        annual_savings = total_current_costs - total_cloud_costs

        # Estimate migration costs
        total_effort = sum(app.estimated_effort for app in self.applications)
        migration_cost = total_effort * 250  # cost per day

        payback_months = (migration_cost / annual_savings) * 12 if annual_savings > 0 else float('inf')

        return {
            'total_current_costs': total_current_costs,
            'total_cloud_costs': total_cloud_costs,
            'annual_savings': annual_savings,
            'migration_cost': migration_cost,
            'payback_months': payback_months,
            'year1_savings': annual_savings - migration_cost,
            'year3_savings': (annual_savings * 3) - migration_cost
        }

# Usage
planner = CloudMigrationPlanner()

app1 = ApplicationAssessment(
    name="Web Frontend",
    complexity=ApplicationComplexity.LOW,
    dependencies=[],
    estimated_effort=5,
    business_criticality=7,
    current_costs=50000,
    cloud_costs_estimate=30000
)

app2 = ApplicationAssessment(
    name="API Backend",
    complexity=ApplicationComplexity.MEDIUM,
    dependencies=["Database"],
    estimated_effort=20,
    business_criticality=9,
    current_costs=80000,
    cloud_costs_estimate=40000
)

app3 = ApplicationAssessment(
    name="Database",
    complexity=ApplicationComplexity.HIGH,
    dependencies=[],
    estimated_effort=30,
    business_criticality=10,
    current_costs=120000,
    cloud_costs_estimate=80000
)

planner.add_application(app1)
planner.add_application(app2)
planner.add_application(app3)

print("Migration Wave Plan:")
print(planner.create_migration_wave_plan())

print("\nROI Analysis:")
print(planner.calculate_roi())
```

### 2. **Database Migration Strategies**

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

### 3. **Terraform Migration Infrastructure**

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

### 4. **Cutover Validation Checklist**

```yaml
# cutover-validation.yaml
pre_cutover:
  - name: "Source Database Health Check"
    steps:
      - command: "SELECT COUNT(*) FROM pg_stat_replication;"
      - validate: "Replication lag < 1 second"
      - expected: "All replicas in sync"

  - name: "Target Database Readiness"
    steps:
      - command: "SELECT datname, pg_size_pretty(pg_database_size(datname)) FROM pg_database;"
      - validate: "Target DB size matches source"
      - expected: "Exact match"

  - name: "Network Connectivity"
    steps:
      - test: "Source to Target connectivity"
      - command: "nc -zv target-db.rds.amazonaws.com 5432"
      - expected: "Connection successful"

  - name: "Backup Validation"
    steps:
      - verify: "Recent backup exists"
      - test: "Restore to test instance"
      - expected: "Restore successful"

cutover:
  - name: "Pre-Cutover Tasks"
    steps:
      - "Notify stakeholders"
      - "Stop application writes"
      - "Verify replication lag < 1 second"
      - "Capture final metrics from source"

  - name: "DNS Cutover"
    steps:
      - "Update DNS to point to target"
      - "Verify DNS propagation"
      - "Test connectivity from test client"

  - name: "Application Failover"
    steps:
      - "Update connection strings"
      - "Restart application servers"
      - "Verify application health"
      - "Run smoke tests"

post_cutover:
  - name: "Validation"
    steps:
      - "Run test suite on production"
      - "Verify data integrity"
      - "Check application logs"
      - "Monitor error rates"

  - name: "Cleanup"
    steps:
      - "Document final metrics"
      - "Archive source database"
      - "Update documentation"
      - "Schedule post-migration review"

validation_criteria:
  - "Zero data loss"
  - "Application response time < 200ms"
  - "Error rate < 0.1%"
  - "All user journeys pass"
  - "Database replication successful"
```

## Best Practices

### ✅ DO
- Perform thorough discovery and assessment
- Run parallel systems during transition
- Test thoroughly before cutover
- Have rollback plan ready
- Monitor closely post-migration
- Document all changes
- Train operations team
- Maintain previous systems temporarily

### ❌ DON'T
- Rush migration without planning
- Migrate without testing
- Forget rollback procedures
- Ignore dependencies
- Skip stakeholder communication
- Migrate everything at once
- Forget to update documentation

## Migration Phases

1. **Assessment** (2-4 weeks): Discover, evaluate, plan
2. **Pilot** (2-8 weeks): Migrate non-critical application
3. **Wave Migration** (8-16 weeks): Migrate by priority
4. **Optimization** (4+ weeks): Fine-tune cloud resources
5. **Closure** (1-2 weeks): Decommission source systems

## Resources

- [AWS Migration Accelerator Program](https://aws.amazon.com/migration/accelerate/)
- [Azure Migration Guide](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/migrate/)
- [GCP Migration Center](https://cloud.google.com/solutions/migration-center)
- [AWS Database Migration Service](https://aws.amazon.com/dms/)
