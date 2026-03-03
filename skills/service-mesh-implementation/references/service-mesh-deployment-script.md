# Service Mesh Deployment Script

## Service Mesh Deployment Script

```bash
#!/bin/bash
# deploy-istio.sh - Install and configure Istio

set -euo pipefail

VERSION="1.13.0"
NAMESPACE="istio-system"

echo "Installing Istio $VERSION..."

# Download Istio
if [ ! -d "istio-$VERSION" ]; then
    echo "Downloading Istio..."
    curl -L https://istio.io/downloadIstio | ISTIO_VERSION=$VERSION sh -
fi

cd "istio-$VERSION"

# Add istioctl to PATH
export PATH=$PWD/bin:$PATH

# Verify cluster
echo "Verifying cluster compatibility..."
istioctl analyze

# Install Istio
echo "Installing Istio on cluster..."
istioctl install --set profile=production -y

# Verify installation
echo "Verifying installation..."
kubectl get ns $NAMESPACE
kubectl get pods -n $NAMESPACE

# Label namespaces for sidecar injection
echo "Configuring sidecar injection..."
kubectl label namespace production istio-injection=enabled --overwrite

# Wait for sidecars
echo "Waiting for sidecars to be injected..."
kubectl rollout restart deployment -n production

echo "Istio installation complete!"

# Show status
istioctl version
```
