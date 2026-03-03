# Terraform Cost Management Configuration

## Terraform Cost Management Configuration

```hcl
# cost-management.tf
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

variable "monthly_budget" {
  default = 10000
  description = "Monthly budget limit"
}

# CloudWatch Cost Anomaly Detection
resource "aws_ce_anomaly_monitor" "cost_anomaly" {
  monitor_name    = "cost-anomaly-detection"
  monitor_type    = "DIMENSIONAL"
  monitor_dimension = "SERVICE"
  monitor_specification = jsonencode({
    Dimensions = {
      Key          = "SERVICE"
      Values       = ["Amazon EC2", "Amazon RDS", "AWS Lambda"]
    }
  })
}

# Anomaly alert
resource "aws_ce_anomaly_subscription" "cost_alert" {
  account_id    = data.aws_caller_identity.current.account_id
  display_name  = "Cost Alert"
  threshold     = 100
  frequency     = "DAILY"
  monitor_arn   = aws_ce_anomaly_monitor.cost_anomaly.arn
  subscription_type = "EMAIL"

  subscription_notification_type = "FORECASTED"
}

# Budget with alerts
resource "aws_budgets_budget" "monthly" {
  name              = "monthly-budget"
  budget_type       = "COST"
  limit_amount      = var.monthly_budget
  limit_unit        = "USD"
  time_period_start = "2024-01-01_00:00"
  time_period_end   = "2099-12-31_23:59"
  time_unit         = "MONTHLY"

  tags = {
    Name = "monthly-budget"
  }
}

# Budget notification
resource "aws_budgets_budget_notification" "monthly_alert" {
  account_id      = data.aws_caller_identity.current.account_id
  budget_name     = aws_budgets_budget.monthly.name
  comparison_operator = "GREATER_THAN"
  notification_type   = "ACTUAL"
  threshold       = 80
  threshold_type  = "PERCENTAGE"

  notification_subscribers {
    address              = "user@example.com"
    subscription_type    = "EMAIL"
  }
}

# Savings Plan Commitment
resource "aws_savingsplans_savings_plan" "compute" {
  commitment  = 10000
  payment_option = "ALL_UPFRONT"
  plan_type   = "COMPUTE_SAVINGS_PLAN"
  term_in_months = 12

  tags = {
    Name = "compute-savings"
  }
}

# Reserved Instances
resource "aws_ec2_instance" "app" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.medium"

  tags = {
    Name = "app-instance"
  }
}

# Reserve the instance
resource "aws_ec2_capacity_reservation" "app" {
  availability_zone       = "us-east-1a"
  instance_count          = 1
  instance_platform       = "Linux/UNIX"
  instance_type           = aws_ec2_instance.app.instance_type
  reservation_type        = "default"

  tags = {
    Name = "app-reservation"
  }
}

# CloudWatch Dashboard for cost monitoring
resource "aws_cloudwatch_dashboard" "cost_dashboard" {
  dashboard_name = "cost-dashboard"

  dashboard_body = jsonencode({
    widgets = [
      {
        type = "metric"
        properties = {
          metrics = [
            ["AWS/Billing", "EstimatedCharges", { stat = "Average" }]
          ]
          period = 86400
          stat   = "Average"
          region = var.aws_region
          title  = "Estimated Monthly Charges"
          yAxis = {
            left = {
              min = 0
            }
          }
        }
      }
    ]
  })
}

# Data for current account
data "aws_caller_identity" "current" {}

# Tag compliance and cost allocation
resource "aws_ec2_instance" "tagged_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.small"

  tags = {
    Name              = "cost-tracked-instance"
    CostCenter        = "engineering"
    Environment       = "production"
    Project           = "web-app"
    ManagedBy         = "terraform"
    ChargebackEmail   = "ops@example.com"
  }
}
```
