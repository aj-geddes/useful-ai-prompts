# DNS Monitoring and Validation

## DNS Monitoring and Validation

```yaml
# dns-monitoring.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: dns-health-check
  namespace: operations
spec:
  schedule: "*/5 * * * *" # Every 5 minutes
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: health-check
              image: curlimages/curl:latest
              command:
                - sh
                - -c
                - |
                  DOMAIN="myapp.com"
                  PRIMARY_IP=$(nslookup $DOMAIN | grep "Address:" | tail -1 | awk '{print $2}')

                  echo "Checking DNS resolution for $DOMAIN"
                  echo "Resolved to: $PRIMARY_IP"

                  # Verify connectivity
                  if curl -sf --max-time 10 "https://$PRIMARY_IP/health" > /dev/null 2>&1; then
                    echo "PASS: Primary endpoint is healthy"
                    exit 0
                  else
                    echo "FAIL: Primary endpoint is unreachable"
                    exit 1
                  fi
          restartPolicy: OnFailure
```
