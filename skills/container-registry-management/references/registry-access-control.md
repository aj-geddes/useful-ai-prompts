# Registry Access Control

## Registry Access Control

```yaml
# registry-access-control.yaml
apiVersion: v1
kind: Secret
metadata:
  name: ecr-pull-secret
  namespace: production
type: kubernetes.io/dockercfg
stringData:
  .dockercfg: |
    {
      "123456789012.dkr.ecr.us-east-1.amazonaws.com": {
        "auth": "base64-encoded-credentials",
        "email": "service-account@mycompany.com"
      }
    }

---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ecr-pull-sa
  namespace: production
imagePullSecrets:
  - name: ecr-pull-secret

---
apiVersion: v1
kind: Pod
metadata:
  name: myapp
  namespace: production
spec:
  serviceAccountName: ecr-pull-sa
  containers:
    - name: app
      image: 123456789012.dkr.ecr.us-east-1.amazonaws.com/myapp:latest
      imagePullPolicy: Always

---
# IAM policy for ECR access
apiVersion: iam.aws.amazon.com/v1
kind: IAMPolicy
metadata:
  name: ecr-read-only
spec:
  policyDocument:
    Version: "2012-10-17"
    Statement:
      - Effect: Allow
        Action:
          - ecr:GetDownloadUrlForLayer
          - ecr:BatchGetImage
          - ecr:GetImage
          - ecr:DescribeImages
        Resource: arn:aws:ecr:*:123456789012:repository/myapp
      - Effect: Allow
        Action:
          - ecr:GetAuthorizationToken
        Resource: "*"
```
