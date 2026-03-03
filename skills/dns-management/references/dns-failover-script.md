# DNS Failover Script

## DNS Failover Script

```bash
#!/bin/bash
# dns-failover.sh - Manage DNS failover

set -euo pipefail

DOMAIN="${1:-myapp.com}"
HOSTED_ZONE_ID="${2:-Z1234567890ABC}"
NEW_PRIMARY="${3:-}"

if [ -z "$NEW_PRIMARY" ]; then
    echo "Usage: $0 <domain> <hosted-zone-id> <new-primary-endpoint>"
    exit 1
fi

echo "Initiating DNS failover for $DOMAIN"

# Get current primary
CURRENT_PRIMARY=$(aws route53 list-resource-record-sets \
    --hosted-zone-id "$HOSTED_ZONE_ID" \
    --query "ResourceRecordSets[?Name=='$DOMAIN.' && SetIdentifier=='Primary'].AliasTarget.DNSName" \
    --output text)

echo "Current primary: $CURRENT_PRIMARY"
echo "New primary: $NEW_PRIMARY"

# Verify new endpoint is healthy
echo "Verifying new endpoint health..."
if ! curl -sf --max-time 5 "https://${NEW_PRIMARY}/health" > /dev/null; then
    echo "ERROR: New endpoint is not healthy"
    exit 1
fi

# Update primary record
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
                    "DNSName": "'$NEW_PRIMARY'",
                    "EvaluateTargetHealth": true
                }
            }
        }]
    }'

echo "DNS failover completed: $NEW_PRIMARY is now primary"
```
