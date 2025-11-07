---
name: autoscaling-configuration
description: Configure autoscaling for Kubernetes, VMs, and serverless workloads based on metrics, schedules, and custom indicators.
---

# Autoscaling Configuration

## Overview

Implement autoscaling strategies to automatically adjust resource capacity based on demand, ensuring cost efficiency while maintaining performance and availability.

## When to Use

- Traffic-driven workload scaling
- Time-based scheduled scaling
- Resource utilization optimization
- Cost reduction
- High-traffic event handling
- Batch processing optimization
- Database connection pooling

## Implementation Examples

### 1. **Kubernetes Horizontal Pod Autoscaler**

```yaml
# hpa-configuration.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
    - type: Pods
      pods:
        metric:
          name: http_requests_per_second
        target:
          type: AverageValue
          averageValue: "1000"
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 50
          periodSeconds: 15
        - type: Pods
          value: 2
          periodSeconds: 60
      selectPolicy: Min
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
        - type: Percent
          value: 100
          periodSeconds: 15
        - type: Pods
          value: 4
          periodSeconds: 15
      selectPolicy: Max

---
# Vertical Pod Autoscaler for resource optimization
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: myapp-vpa
  namespace: production
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  updatePolicy:
    updateMode: "Auto"
  resourcePolicy:
    containerPolicies:
      - containerName: myapp
        minAllowed:
          cpu: 50m
          memory: 64Mi
        maxAllowed:
          cpu: 1000m
          memory: 512Mi
        controlledResources:
          - cpu
          - memory
```

### 2. **AWS Auto Scaling**

```yaml
# aws-autoscaling.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: autoscaling-config
  namespace: production
data:
  setup-asg.sh: |
    #!/bin/bash
    set -euo pipefail

    ASG_NAME="myapp-asg"
    MIN_SIZE=2
    MAX_SIZE=10
    DESIRED_CAPACITY=3
    TARGET_CPU=70
    TARGET_MEMORY=80

    echo "Creating Auto Scaling Group..."

    # Create launch template
    aws ec2 create-launch-template \
      --launch-template-name myapp-template \
      --version-description "Production version" \
      --launch-template-data '{
        "ImageId": "ami-0c55b159cbfafe1f0",
        "InstanceType": "t3.medium",
        "KeyName": "myapp-key",
        "SecurityGroupIds": ["sg-0123456789abcdef0"],
        "UserData": "#!/bin/bash\ncd /app && docker-compose up -d",
        "TagSpecifications": [{
          "ResourceType": "instance",
          "Tags": [{"Key": "Name", "Value": "myapp-instance"}]
        }]
      }' || true

    # Create Auto Scaling Group
    aws autoscaling create-auto-scaling-group \
      --auto-scaling-group-name "$ASG_NAME" \
      --launch-template LaunchTemplateName=myapp-template \
      --min-size $MIN_SIZE \
      --max-size $MAX_SIZE \
      --desired-capacity $DESIRED_CAPACITY \
      --availability-zones us-east-1a us-east-1b us-east-1c \
      --target-group-arns arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/myapp/abcdef123456 \
      --health-check-type ELB \
      --health-check-grace-period 300 \
      --tags "Key=Name,Value=myapp,PropagateAtLaunch=true"

    # Create CPU scaling policy
    aws autoscaling put-scaling-policy \
      --auto-scaling-group-name "$ASG_NAME" \
      --policy-name myapp-cpu-scaling \
      --policy-type TargetTrackingScaling \
      --target-tracking-configuration '{
        "TargetValue": '$TARGET_CPU',
        "PredefinedMetricSpecification": {
          "PredefinedMetricType": "ASGAverageCPUUtilization"
        },
        "ScaleOutCooldown": 60,
        "ScaleInCooldown": 300
      }'

    echo "Auto Scaling Group created: $ASG_NAME"

---
apiVersion: batch/v1
kind: CronJob
metadata:
  name: scheduled-autoscaling
  namespace: production
spec:
  # Scale up at 8 AM
  - schedule: "0 8 * * 1-5"
    jobTemplate:
      spec:
        template:
          spec:
            containers:
              - name: autoscale
                image: amazon/aws-cli:latest
                command:
                  - sh
                  - -c
                  - |
                    aws autoscaling set-desired-capacity \
                      --auto-scaling-group-name myapp-asg \
                      --desired-capacity 10
            restartPolicy: OnFailure

  # Scale down at 6 PM
  - schedule: "0 18 * * 1-5"
    jobTemplate:
      spec:
        template:
          spec:
            containers:
              - name: autoscale
                image: amazon/aws-cli:latest
                command:
                  - sh
                  - -c
                  - |
                    aws autoscaling set-desired-capacity \
                      --auto-scaling-group-name myapp-asg \
                      --desired-capacity 3
            restartPolicy: OnFailure
```

### 3. **Custom Metrics Autoscaling**

```yaml
# custom-metrics-hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: custom-metrics-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 1
  maxReplicas: 50
  metrics:
    # Queue depth from custom metrics
    - type: Pods
      pods:
        metric:
          name: job_queue_depth
        target:
          type: AverageValue
          averageValue: "100"

    # Request rate from custom metrics
    - type: Pods
      pods:
        metric:
          name: http_requests_per_second
        target:
          type: AverageValue
          averageValue: "1000"

    # Custom business metric
    - type: Pods
      pods:
        metric:
          name: active_connections
        target:
          type: AverageValue
          averageValue: "500"

---
# Prometheus ServiceMonitor for custom metrics
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: myapp-metrics
  namespace: production
spec:
  selector:
    matchLabels:
      app: myapp
  endpoints:
    - port: metrics
      interval: 30s
      path: /metrics
```

### 4. **Autoscaling Script**

```bash
#!/bin/bash
# autoscaling-setup.sh - Complete autoscaling configuration

set -euo pipefail

ENVIRONMENT="${1:-production}"
DEPLOYMENT="${2:-myapp}"

echo "Setting up autoscaling for $DEPLOYMENT in $ENVIRONMENT"

# Create HPA
cat <<EOF | kubectl apply -f -
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ${DEPLOYMENT}-hpa
  namespace: ${ENVIRONMENT}
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ${DEPLOYMENT}
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 50
          periodSeconds: 15
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
        - type: Percent
          value: 100
          periodSeconds: 15
EOF

echo "HPA created successfully"

# Monitor autoscaling
echo "Monitoring autoscaling events..."
kubectl get hpa ${DEPLOYMENT}-hpa -n $ENVIRONMENT -w
```

### 5. **Monitoring Autoscaling**

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

## Best Practices

### ✅ DO
- Set appropriate min/max replicas
- Monitor metric aggregation window
- Implement cooldown periods
- Use multiple metrics
- Test scaling behavior
- Monitor scaling events
- Plan for peak loads
- Implement fallback strategies

### ❌ DON'T
- Set min replicas to 1
- Scale too aggressively
- Ignore cooldown periods
- Use single metric only
- Forget to test scaling
- Scale below resource needs
- Neglect monitoring
- Deploy without capacity tests

## Scaling Metrics

- **CPU Utilization**: Most common metric
- **Memory Utilization**: Heap-bound applications
- **Request Rate**: API-driven scaling
- **Queue Depth**: Async job processing
- **Custom Metrics**: Business-specific indicators

## Resources

- [Kubernetes HPA Documentation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
- [AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/)
- [KEDA - Event Scaling](https://keda.sh/)
- [Vertical Pod Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler)
