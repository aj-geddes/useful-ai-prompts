# Backup and Restore Script

## Backup and Restore Script

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
