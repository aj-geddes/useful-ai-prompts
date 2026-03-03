# AWS Auto Scaling

## AWS Auto Scaling

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
