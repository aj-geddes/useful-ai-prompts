---
name: disaster-recovery-testing
description: Execute comprehensive disaster recovery tests, validate recovery procedures, and document lessons learned from DR exercises.
---

# Disaster Recovery Testing

## Overview

Implement systematic disaster recovery testing to validate recovery procedures, measure RTO/RPO, identify gaps, and ensure team readiness for actual incidents.

## When to Use

- Annual DR exercises
- Infrastructure changes
- New service deployments
- Compliance requirements
- Team training
- Recovery procedure validation
- Cross-region failover testing

## Implementation Examples

### 1. **DR Test Plan and Execution**

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

### 2. **DR Test Script**

```bash
#!/bin/bash
# execute-dr-test.sh - Comprehensive DR test execution

set -euo pipefail

TEST_ID="dr-test-$(date +%Y%m%d-%H%M%S)"
LOG_FILE="/tmp/dr-test-${TEST_ID}.log"
METRICS_FILE="/tmp/dr-metrics-${TEST_ID}.json"

# Logging
exec 1> >(tee -a "$LOG_FILE")
exec 2>&1

log_info() {
    echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') $1"
}

log_error() {
    echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') $1"
}

# Start time
START_TIME=$(date +%s)

log_info "Starting DR Test: $TEST_ID"

# Disable production monitoring
log_info "Disabling production alerts..."
aws sns set-topic-attributes \
    --topic-arn "arn:aws:sns:us-east-1:123456789012:prod-alerts" \
    --attribute-name DisplayName \
    --attribute-value "DR Test - Alerts Disabled"

# Phase 1: Backup Validation
log_info "Phase 1: Validating backups..."
if ! aws s3 ls s3://my-backups/databases/ | grep -q "sql.gz"; then
    log_error "No valid backups found"
    exit 1
fi

# Phase 2: Environment Setup
log_info "Phase 2: Setting up DR environment..."
LATEST_BACKUP=$(aws s3 ls s3://my-backups/databases/ | \
    sort | tail -n 1 | awk '{print $4}')

log_info "Using backup: $LATEST_BACKUP"
aws s3 cp "s3://my-backups/databases/$LATEST_BACKUP" - | gunzip > /tmp/restore.sql

# Phase 3: Database Restoration
log_info "Phase 3: Restoring database..."
psql -h dr-db.internal -U postgres -d postgres -f /tmp/restore.sql > /dev/null 2>&1

# Phase 4: Application Deployment
log_info "Phase 4: Deploying application..."
kubectl create namespace dr-test --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -f dr-deployment.yaml -n dr-test
kubectl rollout status deployment/myapp -n dr-test --timeout=10m

# Phase 5: Health Checks
log_info "Phase 5: Running health checks..."
HEALTH_CHECK_START=$(date +%s)

for i in {1..60}; do
    if curl -sf --max-time 5 http://myapp-dr.internal/health > /dev/null 2>&1; then
        HEALTH_CHECK_TIME=$(($(date +%s) - HEALTH_CHECK_START))
        log_info "Health check passed in ${HEALTH_CHECK_TIME}s"
        break
    fi
    if [ $i -eq 60 ]; then
        log_error "Health check timeout"
        exit 1
    fi
    sleep 10
done

# Phase 6: Data Integrity
log_info "Phase 6: Validating data integrity..."
PROD_HASH=$(psql -h prod-db.internal -U postgres -d mydb -t -c \
    "SELECT md5(string_agg(CAST(id AS text), ',')) FROM users ORDER BY id;")
DR_HASH=$(psql -h dr-db.internal -U postgres -d mydb -t -c \
    "SELECT md5(string_agg(CAST(id AS text), ',')) FROM users ORDER BY id;")

if [ "$PROD_HASH" = "$DR_HASH" ]; then
    log_info "Data integrity verified"
else
    log_error "Data integrity check failed: $PROD_HASH != $DR_HASH"
fi

# Phase 7: Smoke Tests
log_info "Phase 7: Running smoke tests..."
kubectl exec -it deployment/myapp -n dr-test -- npm run test:smoke || \
    log_error "Smoke tests failed"

# Record metrics
END_TIME=$(date +%s)
TOTAL_TIME=$((END_TIME - START_TIME))
RTO=$TOTAL_TIME
RPO=$(date -d "$(aws s3api head-object --bucket my-backups --key databases/$LATEST_BACKUP --query 'LastModified' --output text)" +%s)

log_info "DR Test Complete"
log_info "Total time: ${TOTAL_TIME}s"
log_info "RTO: ${RTO}s (target: 3600s)"
log_info "RPO: $(date -d @$RPO)"

# Generate report
cat > "$METRICS_FILE" <<EOF
{
  "test_id": "$TEST_ID",
  "start_time": $START_TIME,
  "end_time": $END_TIME,
  "rto_seconds": $RTO,
  "rpo_timestamp": $RPO,
  "data_integrity": "PASS",
  "health_check": "PASS",
  "smoke_tests": "PASS"
}
EOF

log_info "Metrics saved to: $METRICS_FILE"

# Re-enable monitoring
log_info "Re-enabling production alerts..."
aws sns set-topic-attributes \
    --topic-arn "arn:aws:sns:us-east-1:123456789012:prod-alerts" \
    --attribute-name DisplayName \
    --attribute-value "Production Alerts"

log_info "Test artifacts: $LOG_FILE, $METRICS_FILE"
```

### 3. **DR Test Automation**

```yaml
# scheduled-dr-tests.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: quarterly-dr-test
  namespace: operations
spec:
  # Run quarterly on first Monday of each quarter at 2 AM
  schedule: "0 2 2-8 1,4,7,10 MON"
  jobTemplate:
    spec:
      backoffLimit: 0
      template:
        spec:
          serviceAccountName: dr-test-sa
          containers:
            - name: dr-test
              image: myrepo/dr-test:latest
              command:
                - /usr/local/bin/execute-dr-test.sh
              env:
                - name: SLACK_WEBHOOK
                  valueFrom:
                    secretKeyRef:
                      name: dr-notifications
                      key: slack-webhook
                - name: TEST_MODE
                  value: "full"
          restartPolicy: Never
```

## Best Practices

### ✅ DO
- Schedule regular DR tests
- Document procedures in advance
- Test in isolated environments
- Measure actual RTO/RPO
- Involve all teams
- Automate validation
- Record findings
- Update procedures based on results

### ❌ DON'T
- Skip DR testing
- Test during business hours
- Test against production
- Ignore test failures
- Neglect post-test analysis
- Forget to re-enable monitoring
- Use stale backup processes
- Test only once a year

## DR Test Levels

- **Tabletop**: Documentation and discussion
- **Simulation**: Controlled partial failover
- **Full DR**: Complete system failover
- **Continuous**: Ongoing shadow operations

## Key Metrics

- **RTO**: Recovery Time Objective
- **RPO**: Recovery Point Objective
- **MTPD**: Mean Time to Detect
- **MTTR**: Mean Time to Recover

## Resources

- [AWS Disaster Recovery](https://aws.amazon.com/disaster-recovery/)
- [Disaster Recovery Testing Best Practices](https://www.gartner.com/smarterwithgartner/5-best-practices-for-disaster-recovery-testing)
- [NIST Disaster Recovery Planning](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
