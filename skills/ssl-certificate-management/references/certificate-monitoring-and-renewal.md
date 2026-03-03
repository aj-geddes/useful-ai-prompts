# Certificate Monitoring and Renewal

## Certificate Monitoring and Renewal

```bash
#!/bin/bash
# certificate-monitor.sh - Monitor and alert on certificate expiration

set -euo pipefail

ALERT_DAYS=30
ALERT_EMAIL="admin@myapp.com"

# Check certificate expiration in Kubernetes
check_k8s_certificates() {
    echo "Checking Kubernetes certificate expiration..."

    kubectl get secrets -A -o json | jq -r '.items[] | select(.type=="kubernetes.io/tls") | "\(.metadata.name) \(.metadata.namespace)"' | \
    while read secret namespace; do
        cert=$(kubectl get secret "$secret" -n "$namespace" -o jsonpath='{.data.tls\.crt}' | base64 -d)
        expiry=$(echo "$cert" | openssl x509 -noout -enddate | cut -d= -f2)
        expiry_epoch=$(date -d "$expiry" +%s)
        now_epoch=$(date +%s)
        days_until=$((($expiry_epoch - $now_epoch) / 86400))

        if [ $days_until -lt $ALERT_DAYS ]; then
            echo "WARNING: Certificate $secret in namespace $namespace expires in $days_until days"
            echo "Certificate $secret expires on $expiry" | \
                mail -s "Certificate Expiration Alert" "$ALERT_EMAIL"
        fi
    done
}

# Check AWS ACM certificates
check_acm_certificates() {
    echo "Checking AWS ACM certificate expiration..."

    aws acm list-certificates \
        --query 'CertificateSummaryList[*].CertificateArn' \
        --output text | tr '\t' '\n' | \
    while read arn; do
        expiry=$(aws acm describe-certificate --certificate-arn "$arn" \
            --query 'Certificate.NotAfter' --output text)
        expiry_epoch=$(date -d "$expiry" +%s)
        now_epoch=$(date +%s)
        days_until=$((($expiry_epoch - $now_epoch) / 86400))

        if [ $days_until -lt $ALERT_DAYS ]; then
            domain=$(aws acm describe-certificate --certificate-arn "$arn" \
                --query 'Certificate.DomainName' --output text)
            echo "WARNING: Certificate for $domain expires in $days_until days"
            echo "ACM Certificate $domain expires on $expiry" | \
                mail -s "Certificate Expiration Alert" "$ALERT_EMAIL"
        fi
    done
}

# Main execution
check_k8s_certificates
check_acm_certificates

echo "Certificate check complete"
```
