# Registry Monitoring

## Registry Monitoring

```yaml
# registry-monitoring.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: registry-monitoring
  namespace: monitoring
data:
  dashboards.json: |
    {
      "dashboard": {
        "title": "Container Registry",
        "panels": [
          {
            "title": "Images by Repository",
            "targets": [
              {
                "expr": "count by (repository) (aws_ecr_repository_images)"
              }
            ]
          },
          {
            "title": "Images with Vulnerabilities",
            "targets": [
              {
                "expr": "sum(aws_ecr_image_scan_findings{severity=~\"HIGH|CRITICAL\"})"
              }
            ]
          },
          {
            "title": "Registry Storage",
            "targets": [
              {
                "expr": "aws_ecr_repository_size_bytes"
              }
            ]
          }
        ]
      }
    }

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: registry-alerts
  namespace: monitoring
data:
  alerts.yaml: |
    groups:
      - name: registry_alerts
        rules:
          - alert: ImageWithCriticalVulnerabilities
            expr: aws_ecr_image_scan_findings{severity="CRITICAL"} > 0
            for: 5m
            labels:
              severity: critical
            annotations:
              summary: "Image has critical vulnerabilities"

          - alert: ImagePushFailure
            expr: aws_ecr_push_failures_total > 0
            for: 1m
            labels:
              severity: warning
            annotations:
              summary: "Image push failed"

          - alert: RegistryStorageHigh
            expr: aws_ecr_repository_size_bytes / 1024 / 1024 / 1024 > 100
            labels:
              severity: warning
            annotations:
              summary: "Registry storage usage is high"
```
