# CloudFlare DNS Configuration

## CloudFlare DNS Configuration

```bash
#!/bin/bash
# cloudflare-dns.sh - CloudFlare DNS management

set -euo pipefail

CF_EMAIL="${CF_EMAIL}"
CF_API_KEY="${CF_API_KEY}"
DOMAIN="${1:-myapp.com}"
ZONE_ID="${2:-}"

# Get zone ID
if [ -z "$ZONE_ID" ]; then
    ZONE_ID=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones?name=$DOMAIN" \
        -H "X-Auth-Email: $CF_EMAIL" \
        -H "X-Auth-Key: $CF_API_KEY" \
        -H "Content-Type: application/json" \
        | jq -r '.result[0].id')
fi

echo "Zone ID: $ZONE_ID"

# Create DNS record
create_record() {
    local type="$1"
    local name="$2"
    local content="$3"
    local ttl="${4:-3600}"

    curl -s -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records" \
        -H "X-Auth-Email: $CF_EMAIL" \
        -H "X-Auth-Key: $CF_API_KEY" \
        -H "Content-Type: application/json" \
        --data '{
            "type":"'$type'",
            "name":"'$name'",
            "content":"'$content'",
            "ttl":'$ttl',
            "proxied":true
        }' | jq '.'
}

# List records
list_records() {
    curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records" \
        -H "X-Auth-Email: $CF_EMAIL" \
        -H "X-Auth-Key: $CF_API_KEY" \
        -H "Content-Type: application/json" | jq '.result[] | {id, type, name, content}'
}

list_records
```
