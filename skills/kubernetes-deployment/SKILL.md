---
name: kubernetes-deployment
description: Deploy, manage, and scale containerized applications on Kubernetes clusters with best practices for production workloads, resource management, and rolling updates.
---

# Kubernetes Deployment

## Overview

Master Kubernetes deployments for managing containerized applications at scale, including multi-container services, resource allocation, health checks, and rolling deployment strategies.

## When to Use

- Container orchestration and management
- Multi-environment deployments (dev, staging, prod)
- Auto-scaling microservices
- Rolling updates and blue-green deployments
- Service discovery and load balancing
- Resource quota and limit management
- Pod networking and security policies

## Implementation Examples

### 1. **Complete Deployment with Resource Management**

```yaml
# kubernetes-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-service
  namespace: production
  labels:
    app: api-service
    version: v1
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: api-service
  template:
    metadata:
      labels:
        app: api-service
        version: v1
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
    spec:
      # Service account for RBAC
      serviceAccountName: api-service-sa

      # Security context
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 1000

      # Pod scheduling
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchExpressions:
                    - key: app
                      operator: In
                      values:
                        - api-service
                topologyKey: kubernetes.io/hostname

      # Pod termination grace period
      terminationGracePeriodSeconds: 30

      # Init containers
      initContainers:
        - name: wait-for-db
          image: busybox:1.35
          command: ['sh', '-c', 'until nc -z postgres-service 5432; do echo waiting for db; sleep 2; done']

      containers:
        - name: api-service
          image: myrepo/api-service:1.2.3
          imagePullPolicy: IfNotPresent

          # Ports
          ports:
            - name: http
              containerPort: 8080
              protocol: TCP
            - name: metrics
              containerPort: 9090
              protocol: TCP

          # Environment variables
          env:
            - name: NODE_ENV
              value: "production"
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: api-secrets
                  key: database-url
            - name: LOG_LEVEL
              valueFrom:
                configMapKeyRef:
                  name: api-config
                  key: log-level
            - name: REPLICA_NUM
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name

          # Resource requests and limits
          resources:
            requests:
              memory: "256Mi"
              cpu: "100m"
            limits:
              memory: "512Mi"
              cpu: "500m"

          # Liveness probe
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 30
            periodSeconds: 10
            timeoutSeconds: 5
            failureThreshold: 3

          # Readiness probe
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 5
            timeoutSeconds: 3
            failureThreshold: 2

          # Volume mounts
          volumeMounts:
            - name: config
              mountPath: /etc/config
              readOnly: true
            - name: cache
              mountPath: /var/cache
            - name: logs
              mountPath: /var/log

          # Security context
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL

      # Volumes
      volumes:
        - name: config
          configMap:
            name: api-config
        - name: cache
          emptyDir:
            sizeLimit: 1Gi
        - name: logs
          emptyDir:
            sizeLimit: 2Gi

---
apiVersion: v1
kind: Service
metadata:
  name: api-service
  namespace: production
spec:
  type: ClusterIP
  selector:
    app: api-service
  ports:
    - name: http
      port: 80
      targetPort: 8080
      protocol: TCP
    - name: metrics
      port: 9090
      targetPort: 9090
      protocol: TCP

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: api-config
  namespace: production
data:
  log-level: "INFO"
  max-connections: "100"

---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-service-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api-service
  minReplicas: 3
  maxReplicas: 10
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
```

### 2. **Deployment Script**

```bash
#!/bin/bash
# deploy-k8s.sh - Deploy to Kubernetes cluster

set -euo pipefail

NAMESPACE="${1:-production}"
DEPLOYMENT="${2:-api-service}"
IMAGE="${3:-myrepo/api-service:latest}"

echo "Deploying $DEPLOYMENT to namespace $NAMESPACE..."

# Check cluster connectivity
kubectl cluster-info

# Create namespace if not exists
kubectl create namespace "$NAMESPACE" --dry-run=client -o yaml | kubectl apply -f -

# Apply configuration
kubectl apply -f kubernetes-deployment.yaml -n "$NAMESPACE"

# Wait for rollout
echo "Waiting for deployment to rollout..."
kubectl rollout status deployment/"$DEPLOYMENT" -n "$NAMESPACE" --timeout=5m

# Verify pods are running
echo "Verification:"
kubectl get pods -n "$NAMESPACE" -l "app=$DEPLOYMENT"

# Check service
kubectl get svc -n "$NAMESPACE" -l "app=$DEPLOYMENT"

echo "Deployment complete!"
```

### 3. **Service Account and RBAC**

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: api-service-sa
  namespace: production

---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: api-service-role
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get", "list"]
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: api-service-rolebinding
  namespace: production
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: api-service-role
subjects:
  - kind: ServiceAccount
    name: api-service-sa
    namespace: production
```

## Deployment Patterns

### Rolling Update
- Gradually replace old pods with new ones
- Zero downtime deployments
- Automatic rollback on failure

### Blue-Green
- Maintain two identical environments
- Switch traffic instantly
- Easier rollback capability

### Canary
- Deploy to subset of users first
- Monitor metrics before full rollout
- Reduce risk of bad deployments

## Best Practices

### ✅ DO
- Use resource requests and limits
- Implement health checks (liveness, readiness)
- Use ConfigMaps for configuration
- Apply security context restrictions
- Use service accounts and RBAC
- Implement pod anti-affinity
- Use namespaces for isolation
- Enable pod security policies

### ❌ DON'T
- Use latest image tags in production
- Run containers as root
- Set unlimited resource usage
- Skip readiness probes
- Deploy without resource limits
- Mix configurations in container images
- Use default service accounts

## Resources

- [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)
- [CNCF Kubernetes Security Best Practices](https://www.cncf.io/blog/2021/12/15/build-a-secure-supply-chain-on-kubernetes/)
