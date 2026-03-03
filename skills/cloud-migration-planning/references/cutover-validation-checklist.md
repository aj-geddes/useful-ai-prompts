# Cutover Validation Checklist

## Cutover Validation Checklist

```yaml
# cutover-validation.yaml
pre_cutover:
  - name: "Source Database Health Check"
    steps:
      - command: "SELECT COUNT(*) FROM pg_stat_replication;"
      - validate: "Replication lag < 1 second"
      - expected: "All replicas in sync"

  - name: "Target Database Readiness"
    steps:
      - command: "SELECT datname, pg_size_pretty(pg_database_size(datname)) FROM pg_database;"
      - validate: "Target DB size matches source"
      - expected: "Exact match"

  - name: "Network Connectivity"
    steps:
      - test: "Source to Target connectivity"
      - command: "nc -zv target-db.rds.amazonaws.com 5432"
      - expected: "Connection successful"

  - name: "Backup Validation"
    steps:
      - verify: "Recent backup exists"
      - test: "Restore to test instance"
      - expected: "Restore successful"

cutover:
  - name: "Pre-Cutover Tasks"
    steps:
      - "Notify stakeholders"
      - "Stop application writes"
      - "Verify replication lag < 1 second"
      - "Capture final metrics from source"

  - name: "DNS Cutover"
    steps:
      - "Update DNS to point to target"
      - "Verify DNS propagation"
      - "Test connectivity from test client"

  - name: "Application Failover"
    steps:
      - "Update connection strings"
      - "Restart application servers"
      - "Verify application health"
      - "Run smoke tests"

post_cutover:
  - name: "Validation"
    steps:
      - "Run test suite on production"
      - "Verify data integrity"
      - "Check application logs"
      - "Monitor error rates"

  - name: "Cleanup"
    steps:
      - "Document final metrics"
      - "Archive source database"
      - "Update documentation"
      - "Schedule post-migration review"

validation_criteria:
  - "Zero data loss"
  - "Application response time < 200ms"
  - "Error rate < 0.1%"
  - "All user journeys pass"
  - "Database replication successful"
```
