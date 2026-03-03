# Monitoring Autoscaling

## Monitoring Autoscaling

```yaml
# autoscaling-monitoring.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: autoscaling-alerts
  namespace: monitoring
data:
  alerts.yaml: |
    groups:
      - name: autoscaling
        rules:
          - alert: HpaMaxedOut
            expr: |
              kube_hpa_status_current_replicas == kube_hpa_status_desired_replicas
              and
              kube_hpa_status_desired_replicas == kube_hpa_spec_max_replicas
            for: 10m
            labels:
              severity: warning
            annotations:
              summary: "HPA {{ $labels.hpa }} is at maximum replicas"

          - alert: HpaMinedOut
            expr: |
              kube_hpa_status_current_replicas == kube_hpa_status_desired_replicas
              and
              kube_hpa_status_desired_replicas == kube_hpa_spec_min_replicas
            for: 30m
            labels:
              severity: info
            annotations:
              summary: "HPA {{ $labels.hpa }} is at minimum replicas"

          - alert: AsgCapacityLow
            expr: |
              aws_autoscaling_group_desired_capacity / aws_autoscaling_group_max_size < 0.2
            for: 10m
            labels:
              severity: warning
            annotations:
              summary: "ASG {{ $labels.auto_scaling_group_name }} has low capacity"
```
