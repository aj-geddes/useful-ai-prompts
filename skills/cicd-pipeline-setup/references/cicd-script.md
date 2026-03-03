# CI/CD Script

## CI/CD Script

```bash
#!/bin/bash
# ci-pipeline.sh - Local pipeline validation

set -euo pipefail

echo "Starting CI/CD pipeline..."

# Code quality
echo "Running code quality checks..."
npm run lint
npm run type-check

# Testing
echo "Running tests..."
npm run test:coverage

# Build
echo "Building application..."
npm run build

# Docker build
echo "Building Docker image..."
docker build -t myapp:latest .

# Security scanning
echo "Running security scans..."
trivy image myapp:latest --exit-code 0 --severity HIGH

echo "All pipeline stages completed successfully!"
```
