# Verification

## Verification

```bash
# 1. Check health endpoint
curl https://api.example.com/health
# Expected: {"status": "healthy"}

# 2. Check API endpoints
curl https://api.example.com/api/v1/users
# Expected: Valid JSON response

# 3. Check metrics
# Visit https://grafana.example.com
# Verify:
# - Error rate < 1%
# - Response time < 500ms
# - All pods healthy

# 4. Check logs for errors
kubectl logs deployment/api -n production --tail=100 | grep -i error
# Expected: No new errors
```
