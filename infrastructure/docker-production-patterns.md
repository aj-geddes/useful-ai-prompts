# Docker Production Patterns

## Overview
Comprehensive Docker patterns for production deployments with security, performance, and reliability best practices.

## The Prompt

```
Create production-ready Docker configurations with comprehensive security and performance optimizations:

## 1. Multi-Stage Production Dockerfile

```dockerfile
# Multi-stage build for production optimization
FROM python:3.12-slim-bookworm AS builder

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install UV package manager for faster builds
RUN pip install --no-cache-dir uv

# Set working directory
WORKDIR /build

# Copy requirements first for better caching
COPY requirements.txt .
COPY requirements-prod.txt .

# Install Python dependencies
RUN uv pip install --system --no-cache-dir -r requirements-prod.txt

# Copy source code
COPY . .

# Build application (if needed)
RUN python -m compileall .

# Production stage
FROM python:3.12-slim-bookworm AS production

# Security updates and minimal runtime dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        dumb-init \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* /var/tmp/*

# Create non-root user with specific UID/GID
RUN groupadd -r -g 1001 appuser && \
    useradd -r -g appuser -u 1001 -d /app -s /bin/bash appuser && \
    mkdir -p /app /var/log/app /tmp/app && \
    chown -R appuser:appuser /app /var/log/app /tmp/app

# Set working directory
WORKDIR /app

# Copy Python packages from builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy application code with proper ownership
COPY --from=builder --chown=appuser:appuser /build/ .

# Set secure file permissions
RUN chmod -R 755 /app && \
    chmod -R 644 /app/*.py /app/*.txt /app/*.md 2>/dev/null || true && \
    chmod +x /app/entrypoint.sh 2>/dev/null || true

# Switch to non-root user
USER appuser

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app \
    PATH=/home/appuser/.local/bin:$PATH \
    HOME=/home/appuser

# Expose port (non-privileged)
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Use dumb-init for proper signal handling
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["python", "-u", "server.py"]
```

## 2. Production Docker Compose

```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      target: production
      args:
        - BUILD_DATE=${BUILD_DATE:-$(date -u +'%Y-%m-%dT%H:%M:%SZ')}
        - VCS_REF=${VCS_REF:-$(git rev-parse --short HEAD)}
    
    image: "myapp:${TAG:-latest}"
    container_name: myapp-production
    restart: unless-stopped
    
    ports:
      - "127.0.0.1:8000:8000"  # Bind to localhost only
    
    environment:
      - APP_ENV=production
      - LOG_LEVEL=INFO
      - WORKERS=4
      - TIMEOUT=30
    
    volumes:
      # Application data (read-only)
      - ./data:/app/data:ro
      # Logs directory
      - app-logs:/var/log/app
    
    networks:
      - app-network
    
    # Security configurations
    security_opt:
      - no-new-privileges:true
    
    cap_drop:
      - ALL
    
    cap_add:
      - NET_BIND_SERVICE  # Only if needed for port 80/443
    
    read_only: true
    
    tmpfs:
      - /tmp:noexec,nosuid,size=100m
      - /var/tmp:noexec,nosuid,size=50m
    
    ulimits:
      nproc: 65535
      nofile:
        soft: 20000
        hard: 40000
    
    # Resource limits
    mem_limit: 512m
    mem_reservation: 256m
    cpus: '1.0'
    
    # Health check configuration
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    
    # Logging configuration
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
        labels: "service,environment"
        tag: "{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}"

# Network definitions
networks:
  app-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
          gateway: 172.20.0.1

# Volume definitions
volumes:
  app-logs:
    driver: local
```

## 3. Production Build Scripts

### build.sh (Linux/macOS)
```bash
#!/bin/bash
set -euo pipefail

# Configuration
IMAGE_NAME="myapp"
REGISTRY="registry.company.com"
TAG="${1:-latest}"
BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ')
VCS_REF=$(git rev-parse --short HEAD)
VERSION=$(cat VERSION 2>/dev/null || echo "unknown")

echo "🐳 Building production Docker image..."
echo "Image: $REGISTRY/$IMAGE_NAME:$TAG"
echo "Build Date: $BUILD_DATE"
echo "VCS Ref: $VCS_REF"
echo "Version: $VERSION"

# Security scan before build
echo "🔍 Running security checks..."
if command -v trivy &> /dev/null; then
    trivy fs --severity HIGH,CRITICAL .
else
    echo "⚠️  Trivy not installed, skipping security scan"
fi

# Build multi-platform image
echo "🔨 Building Docker image..."
docker buildx build \
    --platform linux/amd64,linux/arm64 \
    --target production \
    --build-arg BUILD_DATE="$BUILD_DATE" \
    --build-arg VCS_REF="$VCS_REF" \
    --build-arg VERSION="$VERSION" \
    --label "org.opencontainers.image.created=$BUILD_DATE" \
    --label "org.opencontainers.image.revision=$VCS_REF" \
    --label "org.opencontainers.image.version=$VERSION" \
    --tag "$REGISTRY/$IMAGE_NAME:$TAG" \
    --tag "$REGISTRY/$IMAGE_NAME:$VCS_REF" \
    --push \
    .

# Security scan of built image
echo "🔍 Scanning built image for vulnerabilities..."
if command -v trivy &> /dev/null; then
    trivy image --severity HIGH,CRITICAL "$REGISTRY/$IMAGE_NAME:$TAG"
else
    echo "⚠️  Trivy not installed, skipping image scan"
fi

# Test the image
echo "🧪 Testing built image..."
docker run --rm \
    --name "$IMAGE_NAME-test" \
    --user 1001:1001 \
    --read-only \
    --tmpfs /tmp:noexec,nosuid,size=100m \
    --security-opt no-new-privileges:true \
    --cap-drop ALL \
    "$REGISTRY/$IMAGE_NAME:$TAG" \
    python -c "import sys; print(f'Python {sys.version}'); print('✅ Image test passed')"

echo "✅ Build completed successfully!"
echo "📦 Image: $REGISTRY/$IMAGE_NAME:$TAG"
echo "🏷️  Tags: $TAG, $VCS_REF"
```

Requirements:
- Use multi-stage builds for optimized production images
- Implement comprehensive security controls (non-root user, read-only filesystem, capability dropping)
- Add proper health checks and monitoring integration
- Include resource limits and security options
- Implement secrets management
- Add comprehensive logging configuration
- Include security scanning in build pipeline
- Provide zero-downtime deployment scripts
- Add monitoring and metrics collection
- Follow container security best practices
```

## Key Security Features

### Container Security
- **Non-root Execution**: Dedicated user with specific UID/GID
- **Read-only Filesystem**: Prevents runtime modifications
- **Capability Dropping**: Removes unnecessary privileges
- **Security Options**: No new privileges, AppArmor/SELinux
- **Resource Limits**: Memory, CPU, and process restrictions

### Network Security
- **Custom Networks**: Isolated container communication
- **Port Binding**: Localhost-only exposure
- **Reverse Proxy**: SSL termination and routing
- **Network Policies**: Traffic restriction and monitoring

### Build Optimizations
- **Multi-stage Builds**: Smaller production images
- **Layer Caching**: Optimized build order
- **UV Package Manager**: Faster dependency installation
- **Multi-platform**: ARM64 and AMD64 support

## Benefits
- **Production Ready**: Enterprise-grade configurations
- **Security First**: Comprehensive security controls
- **Zero Downtime**: Rolling deployment support
- **Monitoring**: Built-in observability
- **Scalable**: Kubernetes-ready patterns
- **Maintainable**: Clear documentation and automation

## Tags
`docker` `production` `security` `monitoring` `deployment` `containers` `devops`