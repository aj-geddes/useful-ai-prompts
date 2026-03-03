# Kubernetes Secrets Rotation

## Kubernetes Secrets Rotation

```yaml
# secrets-rotation-cronjob.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: secrets-rotation
  namespace: production
spec:
  schedule: "0 2 * * 0" # Weekly at 2 AM Sunday
  jobTemplate:
    spec:
      template:
        spec:
          serviceAccountName: secrets-rotator
          containers:
            - name: rotate
              image: secrets-rotator:latest
              env:
                - name: VAULT_ADDR
                  value: "http://vault:8200"
                - name: VAULT_TOKEN
                  valueFrom:
                    secretKeyRef:
                      name: vault-token
                      key: token
              command:
                - /bin/sh
                - -c
                - |
                  # Rotate secrets
                  python /app/rotate_secrets.py \
                    --secret database-password \
                    --secret api-keys \
                    --secret tls-certificates

          restartPolicy: OnFailure
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: secrets-rotator
  namespace: production
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: secrets-rotator
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get", "list", "update", "patch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: secrets-rotator
  namespace: production
subjects:
  - kind: ServiceAccount
    name: secrets-rotator
roleRef:
  kind: Role
  name: secrets-rotator
  apiGroup: rbac.authorization.k8s.io
```
