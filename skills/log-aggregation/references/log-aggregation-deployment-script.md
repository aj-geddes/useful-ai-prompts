# Log Aggregation Deployment Script

## Log Aggregation Deployment Script

```bash
#!/bin/bash
# deploy-logging.sh - Deploy logging infrastructure

set -euo pipefail

NAMESPACE="logging"
ENV="${1:-production}"

echo "Deploying logging stack to $ENV..."

# Create namespace
kubectl create namespace "$NAMESPACE" --dry-run=client -o yaml | kubectl apply -f -

# Deploy Elasticsearch
echo "Deploying Elasticsearch..."
kubectl apply -f elasticsearch-deployment.yaml -n "$NAMESPACE"
kubectl rollout status deployment/elasticsearch -n "$NAMESPACE" --timeout=5m

# Deploy Logstash
echo "Deploying Logstash..."
kubectl apply -f logstash-deployment.yaml -n "$NAMESPACE"
kubectl rollout status deployment/logstash -n "$NAMESPACE" --timeout=5m

# Deploy Kibana
echo "Deploying Kibana..."
kubectl apply -f kibana-deployment.yaml -n "$NAMESPACE"
kubectl rollout status deployment/kibana -n "$NAMESPACE" --timeout=5m

# Deploy Filebeat as DaemonSet
echo "Deploying Filebeat..."
kubectl apply -f filebeat-daemonset.yaml -n "$NAMESPACE"

# Wait for all pods
echo "Waiting for all logging services..."
kubectl wait --for=condition=ready pod -l app=elasticsearch -n "$NAMESPACE" --timeout=300s

# Create default index pattern
echo "Setting up Kibana index pattern..."
kubectl exec -it -n "$NAMESPACE" svc/kibana -- curl -X POST \
  http://localhost:5601/api/saved_objects/index-pattern/logs \
  -H 'kbn-xsrf: true' \
  -H 'Content-Type: application/json' \
  -d '{"attributes":{"title":"logs-*","timeFieldName":"@timestamp"}}'

echo "Logging stack deployed successfully!"
echo "Kibana: http://localhost:5601"
```
