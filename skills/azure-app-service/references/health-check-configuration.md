# Health Check Configuration

## Health Check Configuration

```bash
# Enable health check
az webapp config set \
  --resource-group myapp-rg \
  --name myapp-web \
  --generic-configurations HEALTHCHECK_PATH=/health

# Monitor health
az monitor metrics list-definitions \
  --resource /subscriptions/{subscription}/resourceGroups/myapp-rg/providers/Microsoft.Web/sites/myapp-web
```
