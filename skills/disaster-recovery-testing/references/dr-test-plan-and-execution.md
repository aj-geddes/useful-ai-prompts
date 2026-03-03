# DR Test Plan and Execution

## DR Test Plan and Execution

```yaml
# dr-test-plan.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: dr-test-procedures
  namespace: operations
data:
  dr-test-plan.md: |
    # Disaster Recovery Test Plan

    ## Test Objectives
    - Validate backup restoration procedures
    - Verify failover mechanisms
    - Test DNS failover
    - Validate data integrity post-recovery
    - Measure RTO and RPO
    - Train incident response team

    ## Pre-Test Checklist
    - [ ] Notify stakeholders
    - [ ] Schedule 4-6 hour window
    - [ ] Disable alerting to prevent noise
    - [ ] Backup production data
    - [ ] Ensure DR environment is isolated
    - [ ] Have rollback plan ready

    ## Test Scope
    - Primary database failover to standby
    - Application failover to DR site
    - DNS resolution update
    - Load balancer health checks
    - Data synchronization verification

    ## Success Criteria
    - RTO: < 1 hour
    - RPO: < 15 minutes
    - Zero data loss
    - All services operational
    - Alerts functional

    ## Post-Test Activities
    - Document timeline
    - Identify gaps
    - Update procedures
    - Schedule post-mortem
    - Update team documentation

---
apiVersion: batch/v1
kind: Job
metadata:
  name: dr-test-executor
  namespace: operations
spec:
  template:
    spec:
      serviceAccountName: dr-test-sa
      containers:
        - name: executor
          image: alpine:latest
          env:
            - name: TEST_ID
              value: "dr-test-$(date +%s)"
            - name: BACKUP_BUCKET
              value: "s3://my-backups"
            - name: DR_NAMESPACE
              value: "dr-test"
          command:
            - sh
            - -c
            - |
              apk add --no-cache aws-cli kubectl jq postgresql-client mysql-client

              echo "Starting DR Test: $TEST_ID"

              # Step 1: Create test namespace
              echo "Creating isolated test environment..."
              kubectl create namespace "$DR_NAMESPACE" --dry-run=client -o yaml | kubectl apply -f -

              # Step 2: Restore database from backup
              echo "Restoring database from latest backup..."
              LATEST_BACKUP=$(aws s3 ls "$BACKUP_BUCKET/databases/" | \
                sort | tail -n 1 | awk '{print $4}')

              aws s3 cp "$BACKUP_BUCKET/databases/$LATEST_BACKUP" - | \
                gunzip | psql postgres://user:pass@dr-db:5432/testdb

              # Step 3: Deploy application to DR namespace
              echo "Deploying application to DR environment..."
              kubectl set image deployment/myapp \
                myapp=myrepo/myapp:production \
                -n "$DR_NAMESPACE"

              # Step 4: Run health checks
              echo "Running health checks..."
              for i in {1..30}; do
                if curl -sf http://myapp-dr/health > /dev/null; then
                  echo "Health check passed"
                  break
                fi
                echo "Waiting for service to be healthy... ($i/30)"
                sleep 10
              done

              # Step 5: Run smoke tests
              echo "Running smoke tests..."
              kubectl exec -it deployment/myapp -n "$DR_NAMESPACE" -- \
                npm run test:smoke || exit 1

              # Step 6: Validate data integrity
              echo "Validating data integrity..."
              PROD_RECORD_COUNT=$(psql postgres://user:pass@prod-db:5432/mydb \
                -t -c "SELECT COUNT(*) FROM users;")
              DR_RECORD_COUNT=$(psql postgres://user:pass@dr-db:5432/testdb \
                -t -c "SELECT COUNT(*) FROM users;")

              if [ "$PROD_RECORD_COUNT" -eq "$DR_RECORD_COUNT" ]; then
                echo "Data integrity verified"
              else
                echo "Data integrity check failed"
                exit 1
              fi

              # Step 7: Record metrics
              echo "Recording DR test metrics..."
              kubectl logs deployment/myapp -n "$DR_NAMESPACE" | \
                grep "startup_time" | jq '.' > /tmp/dr-metrics-$TEST_ID.json

              echo "DR Test Complete: $TEST_ID"

          restartPolicy: Never

---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: dr-test-sa
  namespace: operations

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: dr-test
rules:
  - apiGroups: [""]
    resources: ["namespaces"]
    verbs: ["create", "get", "list"]
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["create", "get", "list", "patch", "set"]
  - apiGroups: [""]
    resources: ["pods", "pods/log"]
    verbs: ["get", "list"]
  - apiGroups: [""]
    resources: ["pods/exec"]
    verbs: ["create", "get"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: dr-test
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: dr-test
subjects:
  - kind: ServiceAccount
    name: dr-test-sa
    namespace: operations
```
