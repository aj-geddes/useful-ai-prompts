# Kubernetes Secrets

## Kubernetes Secrets

```yaml
# kubernetes-secrets.yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-credentials
  namespace: production
type: Opaque
stringData:
  database_url: "postgresql://user:pass@postgres:5432/myapp"
  api_key: "sk_live_xxxxxxxxxxxxxx"
  jwt_secret: "your-jwt-secret-key"

---
apiVersion: v1
kind: Secret
metadata:
  name: docker-registry
  namespace: production
type: kubernetes.io/dockercfg
data:
  .dockercfg: <base64-encoded-dockerconfig>

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      # Use external secrets operator
      serviceAccountName: myapp
      containers:
        - name: app
          image: myapp:latest
          env:
            # From Kubernetes secret
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: app-credentials
                  key: database_url
            # From mounted secret
            - name: API_KEY
              valueFrom:
                secretKeyRef:
                  name: app-credentials
                  key: api_key
          volumeMounts:
            - name: secrets
              mountPath: /app/secrets
              readOnly: true
      volumes:
        - name: secrets
          secret:
            secretName: app-credentials
            defaultMode: 0400

---
# External Secrets Operator
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: aws-secret-store
  namespace: production
spec:
  provider:
    aws:
      service: SecretsManager
      region: us-east-1
      auth:
        jwt:
          serviceAccountRef:
            name: external-secrets-sa

---
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secrets
  namespace: production
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secret-store
    kind: SecretStore
  target:
    name: app-external-secret
    creationPolicy: Owner
  data:
    - secretKey: database_url
      remoteRef:
        key: prod/database/url
    - secretKey: api_key
      remoteRef:
        key: prod/api/key
```
