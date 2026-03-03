# AWS Route53 Configuration

## AWS Route53 Configuration

```yaml
# route53-setup.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: route53-config
  namespace: operations
data:
  setup-dns.sh: |
    #!/bin/bash
    set -euo pipefail

    DOMAIN="myapp.com"
    HOSTED_ZONE_ID="Z1234567890ABC"
    PRIMARY_ENDPOINT="myapp-primary.example.com"
    SECONDARY_ENDPOINT="myapp-secondary.example.com"

    echo "Setting up Route53 DNS for $DOMAIN"

    # Create health check for primary
    PRIMARY_HEALTH=$(aws route53 create-health-check \
      --health-check-config '{
        "Type": "HTTPS",
        "ResourcePath": "/health",
        "FullyQualifiedDomainName": "'${PRIMARY_ENDPOINT}'",
        "Port": 443,
        "RequestInterval": 30,
        "FailureThreshold": 3
      }' --query 'HealthCheck.Id' --output text)

    echo "Created health check: $PRIMARY_HEALTH"

    # Create failover record for primary
    aws route53 change-resource-record-sets \
      --hosted-zone-id "$HOSTED_ZONE_ID" \
      --change-batch '{
        "Changes": [{
          "Action": "UPSERT",
          "ResourceRecordSet": {
            "Name": "'$DOMAIN'",
            "Type": "A",
            "TTL": 60,
            "SetIdentifier": "Primary",
            "Failover": "PRIMARY",
            "AliasTarget": {
              "HostedZoneId": "Z35SXDOTRQ7X7K",
              "DNSName": "'${PRIMARY_ENDPOINT}'",
              "EvaluateTargetHealth": true
            },
            "HealthCheckId": "'${PRIMARY_HEALTH}'"
          }
        }]
      }'

    # Create failover record for secondary
    aws route53 change-resource-record-sets \
      --hosted-zone-id "$HOSTED_ZONE_ID" \
      --change-batch '{
        "Changes": [{
          "Action": "UPSERT",
          "ResourceRecordSet": {
            "Name": "'$DOMAIN'",
            "Type": "A",
            "TTL": 60,
            "SetIdentifier": "Secondary",
            "Failover": "SECONDARY",
            "AliasTarget": {
              "HostedZoneId": "Z35SXDOTRQ7X7K",
              "DNSName": "'${SECONDARY_ENDPOINT}'",
              "EvaluateTargetHealth": false
            }
          }
        }]
      }'

    echo "DNS failover configured"

---
# Terraform Route53 configuration
resource "aws_route53_zone" "myapp" {
  name = "myapp.com"

  tags = {
    Name = "myapp-zone"
  }
}

# Health check for primary region
resource "aws_route53_health_check" "primary" {
  ip_address = aws_lb.primary.ip_address
  port       = 443
  type       = "HTTPS"
  resource_path = "/health"

  failure_threshold = 3
  request_interval  = 30

  tags = {
    Name = "primary-health-check"
  }
}

# Primary failover record
resource "aws_route53_record" "primary" {
  zone_id       = aws_route53_zone.myapp.zone_id
  name          = "myapp.com"
  type          = "A"
  ttl           = 60
  set_identifier = "Primary"

  failover_routing_policy {
    type = "PRIMARY"
  }

  alias {
    name                   = aws_lb.primary.dns_name
    zone_id                = aws_lb.primary.zone_id
    evaluate_target_health = true
  }

  health_check_id = aws_route53_health_check.primary.id
}

# Secondary failover record
resource "aws_route53_record" "secondary" {
  zone_id       = aws_route53_zone.myapp.zone_id
  name          = "myapp.com"
  type          = "A"
  ttl           = 60
  set_identifier = "Secondary"

  failover_routing_policy {
    type = "SECONDARY"
  }

  alias {
    name                   = aws_lb.secondary.dns_name
    zone_id                = aws_lb.secondary.zone_id
    evaluate_target_health = false
  }
}

# Weighted routing for canary deployments
resource "aws_route53_record" "canary" {
  zone_id       = aws_route53_zone.myapp.zone_id
  name          = "api.myapp.com"
  type          = "A"
  ttl           = 60
  set_identifier = "Canary"

  weighted_routing_policy {
    weight = 10
  }

  alias {
    name                   = aws_lb.canary.dns_name
    zone_id                = aws_lb.canary.zone_id
    evaluate_target_health = true
  }
}

# Geolocation routing
resource "aws_route53_record" "geo_us" {
  zone_id       = aws_route53_zone.myapp.zone_id
  name          = "myapp.com"
  type          = "A"
  ttl           = 60
  set_identifier = "US"

  geolocation_routing_policy {
    country = "US"
  }

  alias {
    name                   = aws_lb.us_east.dns_name
    zone_id                = aws_lb.us_east.zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "geo_eu" {
  zone_id       = aws_route53_zone.myapp.zone_id
  name          = "myapp.com"
  type          = "A"
  ttl           = 60
  set_identifier = "EU"

  geolocation_routing_policy {
    continent = "EU"
  }

  alias {
    name                   = aws_lb.eu_west.dns_name
    zone_id                = aws_lb.eu_west.zone_id
    evaluate_target_health = true
  }
}
```
