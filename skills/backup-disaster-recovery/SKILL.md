---
name: backup-disaster-recovery
description: Implement backup strategies, disaster recovery plans, and data restoration procedures for protecting critical infrastructure and data.
---

# Backup and Disaster Recovery

## Overview

Design and implement comprehensive backup and disaster recovery strategies to ensure data protection, business continuity, and rapid recovery from infrastructure failures.

## When to Use

- Data protection and compliance
- Business continuity planning
- Disaster recovery planning
- Point-in-time recovery
- Cross-region failover
- Data migration
- Compliance and audit requirements
- Recovery time objective (RTO) optimization

## Implementation Examples

### 1. **Database Backup Configuration**

```yaml
# postgres-backup-cronjob.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: backup-script
  namespace: databases
data:
  backup.sh: |
    #!/bin/bash
    set -euo pipefail

    BACKUP_DIR="/backups/postgresql"
    RETENTION_DAYS=30
    DB_HOST="${POSTGRES_HOST}"
    DB_PORT="${POSTGRES_PORT:-5432}"
    DB_USER="${POSTGRES_USER}"
    DB_PASSWORD="${POSTGRES_PASSWORD}"

    export PGPASSWORD="$DB_PASSWORD"

    # Create backup directory
    mkdir -p "$BACKUP_DIR"

    # Full backup
    BACKUP_FILE="$BACKUP_DIR/full-$(date +%Y%m%d-%H%M%S).sql"
    echo "Starting backup to $BACKUP_FILE"
    pg_dump -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -v \
      --format=plain --no-owner --no-privileges > "$BACKUP_FILE"

    # Compress backup
    gzip "$BACKUP_FILE"
    echo "Backup compressed: ${BACKUP_FILE}.gz"

    # Upload to S3
    aws s3 cp "${BACKUP_FILE}.gz" \
      "s3://my-backups/postgres/$(date +%Y/%m/%d)/"

    # Clean local old backups
    find "$BACKUP_DIR" -type f -mtime +7 -delete

    # Verify backup
    if pg_restore -d "postgresql://$DB_USER@$DB_HOST:$DB_PORT/test_restore" \
       "${BACKUP_FILE}.gz" --single-transaction 2>/dev/null; then
      echo "Backup verification successful"
      dropdb -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" test_restore
    fi

    echo "Backup complete: ${BACKUP_FILE}.gz"

---
apiVersion: batch/v1
kind: CronJob
metadata:
  name: postgres-backup
  namespace: databases
spec:
  schedule: "0 2 * * *"  # 2 AM daily
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 3
  jobTemplate:
    spec:
      template:
        spec:
          serviceAccountName: backup-sa
          containers:
            - name: backup
              image: postgres:15-alpine
              env:
                - name: POSTGRES_HOST
                  valueFrom:
                    secretKeyRef:
                      name: postgres-credentials
                      key: host
                - name: POSTGRES_USER
                  valueFrom:
                    secretKeyRef:
                      name: postgres-credentials
                      key: username
                - name: POSTGRES_PASSWORD
                  valueFrom:
                    secretKeyRef:
                      name: postgres-credentials
                      key: password
                - name: AWS_ACCESS_KEY_ID
                  valueFrom:
                    secretKeyRef:
                      name: aws-credentials
                      key: access-key
                - name: AWS_SECRET_ACCESS_KEY
                  valueFrom:
                    secretKeyRef:
                      name: aws-credentials
                      key: secret-key
              volumeMounts:
                - name: backup-script
                  mountPath: /backup
                - name: backup-storage
                  mountPath: /backups
              command:
                - sh
                - -c
                - apk add --no-cache aws-cli && bash /backup/backup.sh
          volumes:
            - name: backup-script
              configMap:
                name: backup-script
                defaultMode: 0755
            - name: backup-storage
              emptyDir:
                sizeLimit: 100Gi
          restartPolicy: OnFailure
```

### 2. **Disaster Recovery Plan Template**

```yaml
# disaster-recovery-plan.yaml
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: dr-procedures
  namespace: operations
data:
  dr-runbook.md: |
    # Disaster Recovery Runbook

    ## RTO and RPO Targets
    - RTO (Recovery Time Objective): 4 hours
    - RPO (Recovery Point Objective): 1 hour

    ## Pre-Disaster Checklist
    - [ ] Verify backups are current
    - [ ] Test backup restoration process
    - [ ] Verify DR site resources are provisioned
    - [ ] Confirm failover DNS is configured

    ## Primary Region Failure

    ### Detection (0-15 minutes)
    - Alerting system detects primary region down
    - Incident commander declared
    - War room opened in Slack #incidents

    ### Initial Actions (15-30 minutes)
    - Verify primary region is truly down
    - Check backup systems in secondary region
    - Validate latest backup timestamp

    ### Failover Procedure (30 minutes - 2 hours)
    1. Validate backup integrity
    2. Restore database from latest backup
    3. Update application configuration
    4. Perform DNS failover to secondary region
    5. Verify application health

    ### Recovery Steps
    1. Restore from backup: `restore-backup.sh --backup-id=latest`
    2. Update DNS: `aws route53 change-resource-record-sets --cli-input-json file://failover.json`
    3. Verify: `curl https://myapp.com/health`
    4. Run smoke tests
    5. Monitor error rates and performance

    ## Post-Disaster
    - Document timeline and RCA
    - Update runbooks
    - Schedule post-mortem
    - Test backups again

---
apiVersion: v1
kind: Secret
metadata:
  name: dr-credentials
  namespace: operations
type: Opaque
stringData:
  backup_aws_access_key: "AKIAIOSFODNN7EXAMPLE"
  backup_aws_secret_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
  dr_site_password: "secure-password-here"
```

### 3. **Backup and Restore Script**

```bash
#!/bin/bash
# backup-restore.sh - Complete backup and restore utilities

set -euo pipefail

BACKUP_BUCKET="s3://my-backups"
BACKUP_RETENTION_DAYS=30
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

# Backup function
backup_all() {
    local environment=$1
    log_info "Starting backup for $environment environment"

    # Backup databases
    log_info "Backing up databases..."
    for db in myapp_db analytics_db; do
        local backup_file="$BACKUP_BUCKET/$environment/databases/${db}-${TIMESTAMP}.sql.gz"
        pg_dump "$db" | gzip | aws s3 cp - "$backup_file"
        log_info "Backed up $db to $backup_file"
    done

    # Backup Kubernetes resources
    log_info "Backing up Kubernetes resources..."
    kubectl get all,configmap,secret,ingress,pvc -A -o yaml | \
        gzip | aws s3 cp - "$BACKUP_BUCKET/$environment/kubernetes-${TIMESTAMP}.yaml.gz"
    log_info "Kubernetes resources backed up"

    # Backup volumes
    log_info "Backing up persistent volumes..."
    for pvc in $(kubectl get pvc -A -o name); do
        local pvc_name=$(echo $pvc | cut -d'/' -f2)
        log_info "Backing up PVC: $pvc_name"
        kubectl exec -n default -it backup-pod -- \
            tar czf - /data | aws s3 cp - "$BACKUP_BUCKET/$environment/volumes/${pvc_name}-${TIMESTAMP}.tar.gz"
    done

    log_info "All backups completed successfully"
}

# Restore function
restore_all() {
    local environment=$1
    local backup_date=$2

    log_warn "Restoring from backup date: $backup_date"
    read -p "Are you sure? (yes/no): " confirm
    if [ "$confirm" != "yes" ]; then
        log_error "Restore cancelled"
        exit 1
    fi

    # Restore databases
    log_info "Restoring databases..."
    for db in myapp_db analytics_db; do
        local backup_file="$BACKUP_BUCKET/$environment/databases/${db}-${backup_date}.sql.gz"
        log_info "Restoring $db from $backup_file"
        aws s3 cp "$backup_file" - | gunzip | psql "$db"
    done

    # Restore Kubernetes resources
    log_info "Restoring Kubernetes resources..."
    local k8s_backup="$BACKUP_BUCKET/$environment/kubernetes-${backup_date}.yaml.gz"
    aws s3 cp "$k8s_backup" - | gunzip | kubectl apply -f -

    log_info "Restore completed successfully"
}

# Test restore
test_restore() {
    local environment=$1

    log_info "Testing restore procedure..."

    # Get latest backup
    local latest_backup=$(aws s3 ls "$BACKUP_BUCKET/$environment/databases/" | \
        sort | tail -n 1 | awk '{print $4}')

    if [ -z "$latest_backup" ]; then
        log_error "No backups found"
        exit 1
    fi

    log_info "Testing restore from: $latest_backup"

    # Create test database
    psql -c "CREATE DATABASE test_restore_$(date +%s);"

    # Download and restore
    aws s3 cp "$BACKUP_BUCKET/$environment/databases/$latest_backup" - | \
        gunzip | psql "test_restore_$(date +%s)"

    log_info "Test restore successful"
}

# List backups
list_backups() {
    local environment=$1
    log_info "Available backups for $environment:"
    aws s3 ls "$BACKUP_BUCKET/$environment/" --recursive | grep -E "\.sql\.gz|\.yaml\.gz|\.tar\.gz"
}

# Cleanup old backups
cleanup_old_backups() {
    local environment=$1
    log_info "Cleaning up backups older than $BACKUP_RETENTION_DAYS days"

    find "$BACKUP_BUCKET/$environment" -type f -mtime "+$BACKUP_RETENTION_DAYS" -delete
    log_info "Cleanup completed"
}

# Main
main() {
    case "${1:-}" in
        backup)
            backup_all "${2:-production}"
            ;;
        restore)
            restore_all "${2:-production}" "${3:-}"
            ;;
        test)
            test_restore "${2:-production}"
            ;;
        list)
            list_backups "${2:-production}"
            ;;
        cleanup)
            cleanup_old_backups "${2:-production}"
            ;;
        *)
            echo "Usage: $0 {backup|restore|test|list|cleanup} [environment] [backup-date]"
            exit 1
            ;;
    esac
}

main "$@"
```

### 4. **Cross-Region Failover**

```yaml
# route53-failover.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: failover-config
  namespace: operations
data:
  failover.sh: |
    #!/bin/bash
    set -euo pipefail

    PRIMARY_REGION="us-east-1"
    SECONDARY_REGION="us-west-2"
    DOMAIN="myapp.com"
    HOSTED_ZONE_ID="Z1234567890ABC"

    echo "Initiating failover to $SECONDARY_REGION"

    # Get primary endpoint
    PRIMARY_ENDPOINT=$(aws elbv2 describe-load-balancers \
      --region "$PRIMARY_REGION" \
      --query 'LoadBalancers[0].DNSName' \
      --output text)

    # Get secondary endpoint
    SECONDARY_ENDPOINT=$(aws elbv2 describe-load-balancers \
      --region "$SECONDARY_REGION" \
      --query 'LoadBalancers[0].DNSName' \
      --output text)

    # Update Route53 to failover
    aws route53 change-resource-record-sets \
      --hosted-zone-id "$HOSTED_ZONE_ID" \
      --change-batch '{
        "Changes": [
          {
            "Action": "UPSERT",
            "ResourceRecordSet": {
              "Name": "'$DOMAIN'",
              "Type": "A",
              "TTL": 60,
              "SetIdentifier": "Primary",
              "Failover": "PRIMARY",
              "AliasTarget": {
                "HostedZoneId": "Z35SXDOTRQ7X7K",
                "DNSName": "'$PRIMARY_ENDPOINT'",
                "EvaluateTargetHealth": true
              }
            }
          },
          {
            "Action": "UPSERT",
            "ResourceRecordSet": {
              "Name": "'$DOMAIN'",
              "Type": "A",
              "TTL": 60,
              "SetIdentifier": "Secondary",
              "Failover": "SECONDARY",
              "AliasTarget": {
                "HostedZoneId": "Z35SXDOTRQ7X7K",
                "DNSName": "'$SECONDARY_ENDPOINT'",
                "EvaluateTargetHealth": false
              }
            }
          }
        ]
      }'

    echo "Failover completed"
```

## Best Practices

### ✅ DO
- Perform regular backup testing
- Use multiple backup locations
- Implement automated backups
- Document recovery procedures
- Test failover procedures regularly
- Monitor backup completion
- Use immutable backups
- Encrypt backups at rest and in transit

### ❌ DON'T
- Rely on a single backup location
- Ignore backup failures
- Store backups with production data
- Skip testing recovery procedures
- Over-compress backups beyond recovery speed needs
- Forget to verify backup integrity
- Store encryption keys with backups
- Assume backups are automatically working

## Resources

- [AWS Backup Documentation](https://docs.aws.amazon.com/backup/)
- [Kubernetes Backup Best Practices](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)
- [PostgreSQL Backup and Recovery](https://www.postgresql.org/docs/current/backup.html)
- [Velero - Kubernetes Native Disaster Recovery](https://velero.io/)
