# Debugging Checklist

## Debugging Checklist

```yaml
Container Issues:

[ ] Container starts without error
[ ] Ports mapped correctly
[ ] Logs show no errors
[ ] Environment variables set
[ ] Volumes mounted correctly
[ ] Network connectivity works
[ ] Resource limits appropriate
[ ] Permissions correct
[ ] Dependencies installed
[ ] Entrypoint working

Kubernetes Issues:

[ ] Pod running (not Pending/CrashLoop)
[ ] All containers started
[ ] Readiness probes passing
[ ] Liveness probes passing
[ ] Resource requests/limits set
[ ] Network policies allow traffic
[ ] Secrets/ConfigMaps available
[ ] Logs show no errors

Tools:

docker:
  - logs
  - stats
  - inspect
  - exec

docker-compose:
  - logs
  - ps
  - config

kubectl (Kubernetes):
  - logs
  - describe pod
  - get events
  - port-forward
```
