# Blue-Green Deployment

## Blue-Green Deployment

```bash
#!/bin/bash
# Deploy green, run tests, switch traffic
helm upgrade --install myapp-green ./chart --set version=v2.0.0 --wait
kubectl run smoke-test --image=postman/newman --rm -- run tests/smoke.json

if [ $? -eq 0 ]; then
  kubectl patch service myapp -p '{"spec":{"selector":{"version":"v2.0.0"}}}'
  echo "✅ Traffic switched to green"
else
  helm uninstall myapp-green
  exit 1
fi
```
