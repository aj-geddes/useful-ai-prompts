# Cross-Region Failover

## Cross-Region Failover

```yaml
# route53-failover.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: failover-config
  namespace: operations
data:
  failover.sh: |
    #!/bin/bash
    set -euo pipefail

    PRIMARY_REGION="us-east-1"
    SECONDARY_REGION="us-west-2"
    DOMAIN="myapp.com"
    HOSTED_ZONE_ID="Z1234567890ABC"

    echo "Initiating failover to $SECONDARY_REGION"

    # Get primary endpoint
    PRIMARY_ENDPOINT=$(aws elbv2 describe-load-balancers \
      --region "$PRIMARY_REGION" \
      --query 'LoadBalancers[0].DNSName' \
      --output text)

    # Get secondary endpoint
    SECONDARY_ENDPOINT=$(aws elbv2 describe-load-balancers \
      --region "$SECONDARY_REGION" \
      --query 'LoadBalancers[0].DNSName' \
      --output text)

    # Update Route53 to failover
    aws route53 change-resource-record-sets \
      --hosted-zone-id "$HOSTED_ZONE_ID" \
      --change-batch '{
        "Changes": [
          {
            "Action": "UPSERT",
            "ResourceRecordSet": {
              "Name": "'$DOMAIN'",
              "Type": "A",
              "TTL": 60,
              "SetIdentifier": "Primary",
              "Failover": "PRIMARY",
              "AliasTarget": {
                "HostedZoneId": "Z35SXDOTRQ7X7K",
                "DNSName": "'$PRIMARY_ENDPOINT'",
                "EvaluateTargetHealth": true
              }
            }
          },
          {
            "Action": "UPSERT",
            "ResourceRecordSet": {
              "Name": "'$DOMAIN'",
              "Type": "A",
              "TTL": 60,
              "SetIdentifier": "Secondary",
              "Failover": "SECONDARY",
              "AliasTarget": {
                "HostedZoneId": "Z35SXDOTRQ7X7K",
                "DNSName": "'$SECONDARY_ENDPOINT'",
                "EvaluateTargetHealth": false
              }
            }
          }
        ]
      }'

    echo "Failover completed"
```
