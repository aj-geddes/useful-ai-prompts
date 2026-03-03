# Multi-Cloud Kubernetes Deployment

## Multi-Cloud Kubernetes Deployment

```yaml
# Kubernetes deployment across multiple clouds
apiVersion: v1
kind: Namespace
metadata:
  name: multi-cloud-app

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: cloud-config
  namespace: multi-cloud-app
data:
  cloud-provider: "kubernetes" # Abstracted from specific cloud
  region: "global"
  environment: "production"

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-deployment
  namespace: multi-cloud-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: multi-cloud-app
      cloud: "any"
  template:
    metadata:
      labels:
        app: multi-cloud-app
        cloud: "any"
    spec:
      # Node affinity for multi-cloud
      affinity:
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 50
              preference:
                matchExpressions:
                  - key: cloud.provider
                    operator: In
                    values: ["aws", "azure", "gcp"]
            - weight: 30
              preference:
                matchExpressions:
                  - key: topology.kubernetes.io/region
                    operator: In
                    values: ["us-east-1", "eastus", "us-central1"]

      containers:
        - name: app
          image: myregistry/my-app:latest
          ports:
            - containerPort: 8080
          env:
            - name: CLOUD_NATIVE
              value: "true"
            - name: LOG_LEVEL
              value: "info"
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi

---
apiVersion: v1
kind: Service
metadata:
  name: app-service
  namespace: multi-cloud-app
spec:
  type: LoadBalancer
  selector:
    app: multi-cloud-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```
