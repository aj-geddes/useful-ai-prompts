# Database Backup Configuration

## Database Backup Configuration

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
  schedule: "0 2 * * *" # 2 AM daily
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
