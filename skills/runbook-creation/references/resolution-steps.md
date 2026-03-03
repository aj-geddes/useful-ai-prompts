# Resolution Steps

## Resolution Steps

### Option 1: Restart Pods (Quick Fix)

```bash
# Restart all pods (rolling restart)
kubectl rollout restart deployment/api -n production

# Watch restart progress
kubectl rollout status deployment/api -n production

# Verify pods are healthy
kubectl get pods -n production -l app=api
```

### Option 2: Scale Up (If Overload)

```bash
# Check current replicas
kubectl get deployment api -n production

# Scale up
kubectl scale deployment/api -n production --replicas=10

# Watch scaling
kubectl get pods -n production -l app=api -w
```

### Option 3: Rollback (If Bad Deploy)

```bash
# Check deployment history
kubectl rollout history deployment/api -n production

# Rollback to previous version
kubectl rollout undo deployment/api -n production

# Rollback to specific revision
kubectl rollout undo deployment/api -n production --to-revision=5

# Verify rollback
kubectl rollout status deployment/api -n production
```

### Option 4: Database Connection Reset

```bash
# If database connection pool exhausted
kubectl exec -it deployment/api -n production -- sh
kill -HUP 1  # Reload process, reset connections

# Or restart database connection pool
psql $DATABASE_URL -c "SELECT pg_terminate_backend(pid)
  FROM pg_stat_activity
  WHERE application_name = 'api'
  AND state = 'idle'"
```
