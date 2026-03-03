# Kubernetes Cost Optimization

## Kubernetes Cost Optimization

```yaml
# k8s-cost-optimization.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cost-optimization-policies
  namespace: kube-system
data:
  policies.yaml: |
    # Resource quotas per namespace
    apiVersion: v1
    kind: ResourceQuota
    metadata:
      name: compute-quota
      namespace: production
    spec:
      hard:
        requests.cpu: "100"
        requests.memory: "200Gi"
        limits.cpu: "200"
        limits.memory: "400Gi"
        pods: "500"
      scopeSelector:
        matchExpressions:
          - operator: In
            scopeName: PriorityClass
            values: ["high", "medium"]

---
# Pod Disruption Budget for cost-effective scaling
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: cost-optimized-pdb
  namespace: production
spec:
  minAvailable: 1
  selector:
    matchLabels:
      tier: backend

---
# Prioritize spot instances with taints/tolerations
apiVersion: v1
kind: Node
metadata:
  name: spot-node-1
spec:
  taints:
    - key: cloud.google.com/gke-preemptible
      value: "true"
      effect: NoSchedule

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cost-optimized-app
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
      # Tolerate spot instances
      tolerations:
        - key: cloud.google.com/gke-preemptible
          operator: Equal
          value: "true"
          effect: NoSchedule

      # Prefer nodes with lower cost
      affinity:
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              preference:
                matchExpressions:
                  - key: karpenter.sh/capacity-type
                    operator: In
                    values: ["spot"]

      containers:
        - name: app
          image: myapp:latest
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi
```
