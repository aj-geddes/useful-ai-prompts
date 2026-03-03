# Vault Kubernetes Integration

## Vault Kubernetes Integration

```yaml
# vault-kubernetes.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: vault-auth
  namespace: vault

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: vault-auth-delegator
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:auth-delegator
subjects:
  - kind: ServiceAccount
    name: vault-auth
    namespace: vault

---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: vault
  namespace: vault
spec:
  replicas: 3
  serviceName: vault
  selector:
    matchLabels:
      app: vault
  template:
    metadata:
      labels:
        app: vault
    spec:
      serviceAccountName: vault-auth
      containers:
        - name: vault
          image: vault:1.15.0
          args:
            - "server"
            - "-config=/vault/config/vault.hcl"
          ports:
            - containerPort: 8200
              name: api
            - containerPort: 8201
              name: cluster
          securityContext:
            runAsNonRoot: true
            runAsUser: 100
            capabilities:
              add:
                - IPC_LOCK
          env:
            - name: VAULT_CLUSTER_ADDR
              value: "https://127.0.0.1:8201"
            - name: VAULT_API_ADDR
              value: "https://127.0.0.1:8200"
            - name: VAULT_SKIP_VERIFY
              value: "false"
          volumeMounts:
            - name: vault-config
              mountPath: /vault/config
            - name: vault-data
              mountPath: /vault/data
            - name: vault-logs
              mountPath: /vault/logs
          livenessProbe:
            httpGet:
              path: /v1/sys/health
              port: 8200
              scheme: HTTPS
            initialDelaySeconds: 60
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /v1/sys/health
              port: 8200
              scheme: HTTPS
            initialDelaySeconds: 30
            periodSeconds: 5
      volumes:
        - name: vault-config
          configMap:
            name: vault-config
        - name: vault-logs
          emptyDir: {}
  volumeClaimTemplates:
    - metadata:
        name: vault-data
      spec:
        accessModes: [ReadWriteOnce]
        resources:
          requests:
            storage: 10Gi

---
apiVersion: v1
kind: Service
metadata:
  name: vault
  namespace: vault
spec:
  clusterIP: None
  ports:
    - port: 8200
      targetPort: 8200
      name: api
    - port: 8201
      targetPort: 8201
      name: cluster
  selector:
    app: vault

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: vault-config
  namespace: vault
data:
  vault.hcl: |
    storage "raft" {
      path    = "/vault/data"
      node_id = "node1"
    }

    listener "tcp" {
      address       = "0.0.0.0:8200"
      tls_cert_file = "/vault/config/vault.crt"
      tls_key_file  = "/vault/config/vault.key"
    }

    api_addr     = "https://vault:8200"
    cluster_addr = "https://vault:8201"
    ui = true
```
