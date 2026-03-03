# Loki Configuration (Kubernetes)

## Loki Configuration (Kubernetes)

```yaml
# loki-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: loki-config
  namespace: logging
data:
  loki-config.yaml: |
    auth_enabled: false

    ingester:
      chunk_idle_period: 3m
      chunk_retain_period: 1m
      max_chunk_age: 1h
      chunk_encoding: snappy
      chunk_target_size: 1048576

    limits_config:
      enforce_metric_name: false
      reject_old_samples: true
      reject_old_samples_max_age: 168h

    schema_config:
      configs:
        - from: 2020-05-15
          store: boltdb-shipper
          object_store: filesystem
          schema: v11
          index:
            prefix: index_
            period: 24h

    server:
      http_listen_port: 3100

    storage_config:
      boltdb_shipper:
        active_index_directory: /loki/index
        cache_location: /loki/cache
        shared_store: filesystem
      filesystem:
        directory: /loki/chunks

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: loki
  namespace: logging
spec:
  replicas: 1
  selector:
    matchLabels:
      app: loki
  template:
    metadata:
      labels:
        app: loki
    spec:
      containers:
        - name: loki
          image: grafana/loki:2.8.0
          ports:
            - containerPort: 3100
          volumeMounts:
            - name: loki-config
              mountPath: /etc/loki
            - name: loki-storage
              mountPath: /loki
          args:
            - -config.file=/etc/loki/loki-config.yaml
      volumes:
        - name: loki-config
          configMap:
            name: loki-config
        - name: loki-storage
          emptyDir: {}

---
apiVersion: v1
kind: Service
metadata:
  name: loki
  namespace: logging
spec:
  selector:
    app: loki
  ports:
    - port: 3100
      targetPort: 3100
```
