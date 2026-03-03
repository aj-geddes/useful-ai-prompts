# Investigation Steps

## Investigation Steps

### Check Application Health

```bash
# 1. Check pod status
kubectl get pods -n production -l app=api

# Expected output: All pods Running
# NAME                   READY   STATUS    RESTARTS   AGE
# api-7d8c9f5b6d-4xk2p   1/1     Running   0          2h
# api-7d8c9f5b6d-7nm8r   1/1     Running   0          2h

# 2. Check pod logs for errors
kubectl logs -f deployment/api -n production --tail=100 | grep -i error

# 3. Check application endpoints
curl -v https://api.example.com/health
curl -v https://api.example.com/api/v1/status

# 4. Check database connectivity
kubectl exec -it deployment/api -n production -- sh
psql $DATABASE_URL -c "SELECT 1"
```

### Check Infrastructure

```bash
# 1. Check load balancer
aws elb describe-target-health \
  --target-group-arn arn:aws:elasticloadbalancing:... \
  --query 'TargetHealthDescriptions[*].[Target.Id,TargetHealth.State]' \
  --output table

# 2. Check DNS resolution
dig api.example.com
nslookup api.example.com

# 3. Check SSL certificates
echo | openssl s_client -connect api.example.com:443 2>/dev/null | \
  openssl x509 -noout -dates

# 4. Check network connectivity
kubectl exec -it deployment/api -n production -- \
  curl -v https://database.example.com:5432
```

### Check Database

```bash
# 1. Check database connections
psql $DATABASE_URL -c "SELECT count(*) FROM pg_stat_activity"

# 2. Check for locks
psql $DATABASE_URL -c "
  SELECT pid, usename, pg_blocking_pids(pid) as blocked_by, query
  FROM pg_stat_activity
  WHERE cardinality(pg_blocking_pids(pid)) > 0
"

# 3. Check database size
psql $DATABASE_URL -c "
  SELECT pg_size_pretty(pg_database_size(current_database()))
"

# 4. Check long-running queries
psql $DATABASE_URL -c "
  SELECT pid, now() - query_start as duration, query
  FROM pg_stat_activity
  WHERE state = 'active'
  ORDER BY duration DESC
  LIMIT 10
"
```
