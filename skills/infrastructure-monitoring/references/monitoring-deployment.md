# Monitoring Deployment

## Monitoring Deployment

```bash
#!/bin/bash
# deploy-monitoring.sh - Deploy Prometheus and Grafana

set -euo pipefail

NAMESPACE="monitoring"
PROMETHEUS_VERSION="v2.40.0"
GRAFANA_VERSION="9.3.2"

echo "Creating monitoring namespace..."
kubectl create namespace "$NAMESPACE" --dry-run=client -o yaml | kubectl apply -f -

# Deploy Prometheus
echo "Deploying Prometheus..."
kubectl apply -f prometheus-configmap.yaml -n "$NAMESPACE"
kubectl apply -f prometheus-deployment.yaml -n "$NAMESPACE"
kubectl apply -f prometheus-service.yaml -n "$NAMESPACE"

# Deploy Alertmanager
echo "Deploying Alertmanager..."
kubectl apply -f alertmanager-configmap.yaml -n "$NAMESPACE"
kubectl apply -f alertmanager-deployment.yaml -n "$NAMESPACE"
kubectl apply -f alertmanager-service.yaml -n "$NAMESPACE"

# Deploy Grafana
echo "Deploying Grafana..."
kubectl apply -f grafana-deployment.yaml -n "$NAMESPACE"
kubectl apply -f grafana-service.yaml -n "$NAMESPACE"

# Wait for deployments
echo "Waiting for deployments to be ready..."
kubectl rollout status deployment/prometheus -n "$NAMESPACE" --timeout=5m
kubectl rollout status deployment/alertmanager -n "$NAMESPACE" --timeout=5m
kubectl rollout status deployment/grafana -n "$NAMESPACE" --timeout=5m

# Port forward for access
echo "Port forwarding to services..."
kubectl port-forward -n "$NAMESPACE" svc/prometheus 9090:9090 &
kubectl port-forward -n "$NAMESPACE" svc/grafana 3000:3000 &

echo "Monitoring stack deployed successfully!"
echo "Prometheus: http://localhost:9090"
echo "Grafana: http://localhost:3000"
```
