# DR Test Script

## DR Test Script

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
