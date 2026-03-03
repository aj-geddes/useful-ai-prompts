# Load Balancer Health Check Script

## Load Balancer Health Check Script

```bash
#!/bin/bash
# health-check.sh - Monitor backend health

set -euo pipefail

BACKENDS=("10.0.1.10:8080" "10.0.1.11:8080" "10.0.1.12:8080")
HEALTH_ENDPOINT="/health"
TIMEOUT=5
ALERT_EMAIL="ops@myapp.com"

check_backend_health() {
    local backend=$1
    local host=${backend%:*}
    local port=${backend#*:}

    if timeout "$TIMEOUT" bash -c "echo >/dev/tcp/$host/$port" 2>/dev/null; then
        if curl -sf --max-time "$TIMEOUT" "http://$backend$HEALTH_ENDPOINT" > /dev/null; then
            return 0
        fi
    fi
    return 1
}

main() {
    local unhealthy_backends=()

    for backend in "${BACKENDS[@]}"; do
        if ! check_backend_health "$backend"; then
            unhealthy_backends+=("$backend")
            echo "WARNING: Backend $backend is unhealthy"
        else
            echo "OK: Backend $backend is healthy"
        fi
    done

    if [ ${#unhealthy_backends[@]} -gt 0 ]; then
        local message="Unhealthy backends detected: ${unhealthy_backends[*]}"
        echo "$message"
        echo "$message" | mail -s "Load Balancer Alert" "$ALERT_EMAIL"
        exit 1
    fi
}

main "$@"
```
