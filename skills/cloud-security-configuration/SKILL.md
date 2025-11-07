---
name: cloud-security-configuration
description: Implement comprehensive cloud security across AWS, Azure, and GCP with IAM, encryption, network security, compliance, and threat detection.
---

# Cloud Security Configuration

## Overview

Cloud security requires comprehensive strategies spanning identity management, encryption, network controls, compliance, and threat detection. Implement defense-in-depth with multiple layers of protection and continuous monitoring.

## When to Use

- Protecting sensitive data in cloud
- Compliance with regulations (GDPR, HIPAA, PCI-DSS)
- Implementing zero-trust security
- Securing multi-cloud environments
- Threat detection and response
- Identity and access management
- Network isolation and segmentation
- Encryption and key management

## Implementation Examples

### 1. **AWS Security Configuration**

```bash
# Enable GuardDuty (threat detection)
aws guardduty create-detector \
  --enable \
  --finding-publishing-frequency FIFTEEN_MINUTES

# Enable CloudTrail (audit logging)
aws cloudtrail create-trail \
  --name organization-trail \
  --s3-bucket-name audit-bucket \
  --is-multi-region-trail

# Enable S3 bucket encryption by default
aws s3api put-bucket-encryption \
  --bucket my-bucket \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "aws:kms",
        "KMSMasterKeyID": "arn:aws:kms:region:account:key/key-id"
      },
      "BucketKeyEnabled": true
    }]
  }'

# Enable VPC Flow Logs
aws ec2 create-flow-logs \
  --resource-type VPC \
  --resource-ids vpc-12345 \
  --traffic-type ALL \
  --log-destination-type cloud-watch-logs \
  --log-group-name /aws/vpc/flowlogs

# Configure Security Groups
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345 \
  --protocol tcp \
  --port 443 \
  --cidr 0.0.0.0/0

# Enable MFA for root account
aws iam get-account-summary

# Create password policy
aws iam update-account-password-policy \
  --minimum-password-length 14 \
  --require-symbols \
  --require-numbers \
  --require-uppercase-characters \
  --require-lowercase-characters \
  --allow-users-to-change-password \
  --expire-passwords \
  --max-password-age 90
```

### 2. **Terraform Security Configuration**

```hcl
# security.tf
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

# KMS key for encryption
resource "aws_kms_key" "main" {
  description             = "Master encryption key"
  deletion_window_in_days = 10
  enable_key_rotation     = true

  tags = { Name = "master-key" }
}

resource "aws_kms_alias" "main" {
  name          = "alias/master-key"
  target_key_id = aws_kms_key.main.key_id
}

# Secrets Manager for sensitive data
resource "aws_secretsmanager_secret" "db_password" {
  name_prefix             = "db/"
  recovery_window_in_days = 7
  kms_key_id              = aws_kms_key.main.id
}

resource "aws_secretsmanager_secret_version" "db_password" {
  secret_id       = aws_secretsmanager_secret.db_password.id
  secret_string   = random_password.db.result
}

# IAM role with least privilege
resource "aws_iam_role" "app_role" {
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy" "app_policy" {
  role = aws_iam_role.app_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:ListBucket"
        ]
        Resource = [
          aws_s3_bucket.data.arn,
          "${aws_s3_bucket.data.arn}/*"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "kms:Decrypt",
          "kms:DescribeKey"
        ]
        Resource = aws_kms_key.main.arn
      },
      {
        Effect = "Allow"
        Action = [
          "secretsmanager:GetSecretValue"
        ]
        Resource = aws_secretsmanager_secret.db_password.arn
      },
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "arn:aws:logs:*:*:*"
      }
    ]
  })
}

# VPC with security
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = { Name = "main-vpc" }
}

# Public subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = data.aws_availability_zones.available.names[0]
  map_public_ip_on_launch = false

  tags = { Name = "public-subnet" }
}

# Private subnet
resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.10.0/24"
  availability_zone = data.aws_availability_zones.available.names[0]

  tags = { Name = "private-subnet" }
}

# Network ACL for defense in depth
resource "aws_network_acl" "main" {
  vpc_id = aws_vpc.main.id

  ingress {
    protocol   = "tcp"
    rule_no    = 100
    action     = "allow"
    cidr_block = "0.0.0.0/0"
    from_port  = 443
    to_port    = 443
  }

  ingress {
    protocol   = "tcp"
    rule_no    = 110
    action     = "allow"
    cidr_block = "0.0.0.0/0"
    from_port  = 80
    to_port    = 80
  }

  egress {
    protocol   = "-1"
    rule_no    = 100
    action     = "allow"
    cidr_block = "0.0.0.0/0"
    from_port  = 0
    to_port    = 0
  }
}

# Security group
resource "aws_security_group" "app" {
  name_prefix = "app-"
  vpc_id      = aws_vpc.main.id

  # Egress rule (deny by default)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# WAF Web ACL
resource "aws_wafv2_web_acl" "main" {
  scope = "REGIONAL"
  name  = "app-waf"

  default_action {
    allow {}
  }

  rule {
    name     = "AWSManagedRulesCommonRuleSet"
    priority = 1

    action {
      block {}
    }

    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesCommonRuleSet"
        vendor_name = "AWS"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "AWSManagedRulesCommonRuleSet"
      sampled_requests_enabled   = true
    }
  }

  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name                = "app-waf"
    sampled_requests_enabled   = true
  }
}

# GuardDuty for threat detection
resource "aws_guardduty_detector" "main" {
  enable = true

  datasources {
    flow_logs {
      enable = true
    }
    s3_logs {
      enable = true
    }
    kubernetes {
      audit_logs {
        enable = true
      }
    }
  }
}

# CloudTrail for audit logging
resource "aws_cloudtrail" "main" {
  name                          = "organization-trail"
  s3_bucket_name                = aws_s3_bucket.audit_logs.id
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_log_file_validation    = true
  depends_on                    = [aws_s3_bucket_policy.audit_logs]

  event_selector {
    read_write_type           = "All"
    include_management_events = true

    data_resource {
      type   = "AWS::S3::Object"
      values = ["arn:aws:s3:::*/"]
    }
  }
}

# Audit logs bucket
resource "aws_s3_bucket" "audit_logs" {
  bucket = "audit-logs-${data.aws_caller_identity.current.account_id}"
}

resource "aws_s3_bucket_policy" "audit_logs" {
  bucket = aws_s3_bucket.audit_logs.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowCloudTrailAcl"
        Effect = "Allow"
        Principal = {
          Service = "cloudtrail.amazonaws.com"
        }
        Action   = "s3:GetBucketAcl"
        Resource = aws_s3_bucket.audit_logs.arn
      },
      {
        Sid    = "AllowCloudTrailPutObject"
        Effect = "Allow"
        Principal = {
          Service = "cloudtrail.amazonaws.com"
        }
        Action   = "s3:PutObject"
        Resource = "${aws_s3_bucket.audit_logs.arn}/*"
        Condition = {
          StringEquals = {
            "s3:x-amz-acl" = "bucket-owner-full-control"
          }
        }
      }
    ]
  })
}

# Config for compliance monitoring
resource "aws_config_configuration_recorder" "main" {
  name       = "main"
  role_arn   = aws_iam_role.config.arn
  depends_on = [aws_iam_role_policy_attachment.config]

  recording_group {
    all_supported = true
    include_global = true
  }
}

resource "aws_config_configuration_recorder_status" "main" {
  name              = aws_config_configuration_recorder.main.name
  depends_on        = [aws_config_delivery_channel.main]
  is_enabled        = true
  start_recording   = true
}

# Config delivery channel
resource "aws_config_delivery_channel" "main" {
  name          = "main"
  s3_bucket_name = aws_s3_bucket.config.id
  depends_on    = [aws_config_configuration_recorder.main]
}

# CloudWatch for security monitoring
resource "aws_cloudwatch_metric_alarm" "unauthorized_actions" {
  alarm_name          = "unauthorized-api-calls"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "UnauthorizedOperationCount"
  namespace           = "CloudTrailMetrics"
  period              = 300
  statistic           = "Sum"
  threshold           = 5
  alarm_description   = "Alert on unauthorized API calls"
}

# Data source
data "aws_caller_identity" "current" {}
data "aws_availability_zones" "available" {
  state = "available"
}

# Random password
resource "random_password" "db" {
  length  = 16
  special = true
}

# IAM role for Config
resource "aws_iam_role" "config" {
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "config.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "config" {
  role       = aws_iam_role.config.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/ConfigRole"
}

resource "aws_s3_bucket" "config" {
  bucket = "config-bucket-${data.aws_caller_identity.current.account_id}"
}
```

### 3. **Azure Security Configuration**

```bash
# Enable Azure Security Center
az security auto-provisioning-setting update \
  --auto-provision on

# Enable Azure Defender
az security atp storage update \
  --storage-account myaccount \
  --is-enabled true

# Configure NSG rules
az network nsg rule create \
  --resource-group mygroup \
  --nsg-name mynsg \
  --name AllowHTTPS \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes '*' \
  --source-port-ranges '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 443

# Enable Azure Policy
az policy assignment create \
  --name EnforceHttps \
  --policy /subscriptions/{subscription}/providers/Microsoft.Authorization/policyDefinitions/{policyId}

# Create Key Vault
az keyvault create \
  --resource-group mygroup \
  --name mykeyvault \
  --enable-rbac-authorization
```

### 4. **GCP Security Configuration**

```bash
# Enable Cloud Armor
gcloud compute security-policies create my-policy \
  --description "Security policy"

# Add rules
gcloud compute security-policies rules create 100 \
  --security-policy=my-policy \
  --action "deny-403" \
  --expression "origin.country_code == 'CN'"

# Enable Cloud KMS
gcloud kms keyrings create my-keyring --location us-east1

gcloud kms keys create my-key \
  --location us-east1 \
  --keyring my-keyring \
  --purpose encryption

# Set IAM bindings
gcloud projects add-iam-policy-binding MY_PROJECT \
  --member=serviceAccount:my-sa@MY_PROJECT.iam.gserviceaccount.com \
  --role=roles/container.developer

# Enable Binary Authorization
gcloud container binauthz policy import policy.yaml

# VPC Service Controls
gcloud access-context-manager perimeters create my-perimeter \
  --resources=projects/MY_PROJECT
```

## Best Practices

### ✅ DO
- Implement least privilege access
- Enable MFA everywhere
- Use service accounts for applications
- Encrypt data at rest and in transit
- Enable comprehensive logging
- Implement network segmentation
- Use secrets management
- Enable threat detection
- Regular security assessments
- Keep systems patched

### ❌ DON'T
- Use root/default credentials
- Store secrets in code
- Over-permissive security groups
- Disable encryption
- Ignore logs and monitoring
- Share credentials
- Skip compliance requirements
- Trust unverified data sources

## Compliance Standards

- GDPR: Data protection
- HIPAA: Healthcare data
- PCI-DSS: Payment card data
- SOC 2: Security controls
- ISO 27001: Information security
- CIS Benchmarks: Security hardening

## Security Layers

1. **Identity & Access**: IAM, MFA, SSO
2. **Network**: VPCs, Security Groups, WAF
3. **Data**: Encryption, Secrets, DLP
4. **Application**: Input validation, patches
5. **Monitoring**: Logging, Alerting, Threat Detection

## Resources

- [AWS Security Hub](https://docs.aws.amazon.com/securityhub/)
- [Azure Security Benchmark](https://docs.microsoft.com/en-us/azure/security/benchmarks/)
- [GCP Security Best Practices](https://cloud.google.com/security/best-practices)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [CIS Cloud Security Benchmarks](https://www.cisecurity.org/cis-benchmarks/)
