# Nginx Configuration Script

## Nginx Configuration Script

```bash
#!/bin/bash
# nginx-deploy.sh - Deploy and validate Nginx configuration

set -euo pipefail

echo "Deploying Nginx configuration..."

# Test configuration
echo "Testing Nginx configuration..."
nginx -t

# Check if running
if pgrep -x nginx > /dev/null; then
    echo "Reloading Nginx..."
    systemctl reload nginx
else
    echo "Starting Nginx..."
    systemctl start nginx
fi

# Verify
echo "Verifying deployment..."
sleep 2

# Check service status
if systemctl is-active --quiet nginx; then
    echo "Nginx is running"
else
    echo "ERROR: Nginx failed to start"
    systemctl status nginx
    exit 1
fi

# Test connectivity
echo "Testing endpoints..."
curl -k https://localhost/health || echo "Warning: Health check failed"

# Log status
echo "Nginx configuration deployed successfully"
journalctl -u nginx -n 20 --no-pager
```
