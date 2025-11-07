---
name: deployment-documentation
description: Document deployment processes, infrastructure setup, CI/CD pipelines, and configuration management. Use when creating deployment guides, infrastructure docs, or CI/CD documentation.
---

# Deployment Documentation

## Overview

Create comprehensive deployment documentation covering infrastructure setup, CI/CD pipelines, deployment procedures, and rollback strategies.

## When to Use

- Deployment guides
- Infrastructure documentation
- CI/CD pipeline setup
- Configuration management
- Container orchestration
- Cloud infrastructure docs
- Release procedures
- Rollback procedures

## Deployment Guide Template

```markdown
# Deployment Guide

## Overview

This document describes the deployment process for [Application Name].

**Deployment Methods:**
- Manual deployment (emergency only)
- Automated CI/CD (preferred)
- Blue-green deployment
- Canary deployment

**Environments:**
- Development: https://dev.example.com
- Staging: https://staging.example.com
- Production: https://example.com

---

## Prerequisites

### Required Tools

```bash
# Install required tools
brew install node@18
brew install postgresql@14
brew install redis
brew install docker
brew install kubectl
brew install helm
brew install aws-cli
```

### Access Requirements

- [ ] GitHub repository access
- [ ] AWS console access (IAM user with deployment policy)
- [ ] Kubernetes cluster access (kubeconfig)
- [ ] Docker Hub credentials
- [ ] Datadog API key (monitoring)
- [ ] PagerDuty access (on-call)

### Environment Variables

```bash
# .env.production
NODE_ENV=production
DATABASE_URL=postgresql://user:pass@db.example.com:5432/prod
REDIS_URL=redis://cache.example.com:6379
API_KEY=your-api-key
JWT_SECRET=your-jwt-secret
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=...
```

---

## CI/CD Pipeline

### GitHub Actions Workflow

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm test
      - run: npm run lint

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Login to Amazon ECR
        uses: aws-actions/amazon-ecr-login@v1

      - name: Build and push Docker image
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          IMAGE_TAG: ${{ github.sha }}
        run: |
          docker build -t $ECR_REGISTRY/app:$IMAGE_TAG .
          docker push $ECR_REGISTRY/app:$IMAGE_TAG
          docker tag $ECR_REGISTRY/app:$IMAGE_TAG $ECR_REGISTRY/app:latest
          docker push $ECR_REGISTRY/app:latest

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Configure kubectl
        uses: azure/k8s-set-context@v3
        with:
          method: kubeconfig
          kubeconfig: ${{ secrets.KUBECONFIG }}

      - name: Deploy to Kubernetes
        env:
          IMAGE_TAG: ${{ github.sha }}
        run: |
          kubectl set image deployment/app \
            app=your-registry/app:$IMAGE_TAG \
            -n production

          kubectl rollout status deployment/app -n production

      - name: Notify Datadog
        run: |
          curl -X POST "https://api.datadoghq.com/api/v1/events" \
            -H "DD-API-KEY: ${{ secrets.DATADOG_API_KEY }}" \
            -d '{
              "title": "Deployment to Production",
              "text": "Deployed version ${{ github.sha }}",
              "tags": ["environment:production", "service:app"]
            }'

      - name: Notify Slack
        if: always()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "Deployment ${{ job.status }}: ${{ github.sha }}"
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

---

## Docker Configuration

### Dockerfile

```dockerfile
# Multi-stage build for optimization
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY . .

# Build application
RUN npm run build

# Production stage
FROM node:18-alpine

# Security: Run as non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

WORKDIR /app

# Copy built application from builder
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=builder --chown=nodejs:nodejs /app/package*.json ./

# Switch to non-root user
USER nodejs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node healthcheck.js

# Start application
CMD ["node", "dist/server.js"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgresql://postgres:password@db:5432/app
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "node", "healthcheck.js"]
      interval: 30s
      timeout: 3s
      retries: 3

  db:
    image: postgres:14-alpine
    environment:
      - POSTGRES_DB=app
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
```

---

## Kubernetes Deployment

### Deployment Manifest

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
  namespace: production
  labels:
    app: app
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
      app: app
  template:
    metadata:
      labels:
        app: app
        version: v1
    spec:
      containers:
      - name: app
        image: your-registry/app:latest
        imagePullPolicy: Always
        ports:
        - containerPort: 3000
          name: http
        env:
        - name: NODE_ENV
          value: "production"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: database-url
        - name: REDIS_URL
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: redis-url
        resources:
          requests:
            cpu: 500m
            memory: 512Mi
          limits:
            cpu: 1000m
            memory: 1Gi
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 3
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
          initialDelaySeconds: 10
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 2

---
apiVersion: v1
kind: Service
metadata:
  name: app
  namespace: production
spec:
  selector:
    app: app
  ports:
  - port: 80
    targetPort: 3000
  type: ClusterIP

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app
  namespace: production
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - example.com
    secretName: app-tls
  rules:
  - host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app
            port:
              number: 80
```

---

## Deployment Procedures

### 1. Pre-Deployment Checklist

- [ ] All tests passing
- [ ] Code review approved
- [ ] Security scan passed
- [ ] Database migrations ready
- [ ] Rollback plan documented
- [ ] Monitoring dashboard ready
- [ ] Team notified
- [ ] Maintenance window scheduled (if needed)

### 2. Deployment Steps

```bash
# 1. Tag release
git tag -a v1.2.3 -m "Release v1.2.3"
git push origin v1.2.3

# 2. Build Docker image
docker build -t your-registry/app:v1.2.3 .
docker tag your-registry/app:v1.2.3 your-registry/app:latest
docker push your-registry/app:v1.2.3
docker push your-registry/app:latest

# 3. Run database migrations
kubectl exec -it deployment/app -n production -- npm run db:migrate

# 4. Deploy to Kubernetes
kubectl apply -f k8s/
kubectl set image deployment/app app=your-registry/app:v1.2.3 -n production

# 5. Wait for rollout
kubectl rollout status deployment/app -n production

# 6. Verify deployment
kubectl get pods -n production
kubectl logs -f deployment/app -n production

# 7. Smoke test
curl https://example.com/health
curl https://example.com/api/v1/status
```

### 3. Post-Deployment Verification

```bash
# Check pod status
kubectl get pods -n production -l app=app

# Check logs for errors
kubectl logs -f deployment/app -n production --tail=100

# Check metrics
curl https://example.com/metrics

# Run smoke tests
npm run test:smoke:production

# Verify in monitoring
# - Check Datadog dashboard
# - Check error rates
# - Check response times
# - Check resource usage
```

---

## Rollback Procedures

### Automatic Rollback

```bash
# Rollback to previous version
kubectl rollout undo deployment/app -n production

# Rollback to specific revision
kubectl rollout undo deployment/app -n production --to-revision=2

# Check rollback status
kubectl rollout status deployment/app -n production
```

### Manual Rollback

```bash
# 1. Identify last working version
kubectl rollout history deployment/app -n production

# 2. Deploy previous version
kubectl set image deployment/app \
  app=your-registry/app:v1.2.2 \
  -n production

# 3. Rollback database migrations (if needed)
kubectl exec -it deployment/app -n production -- \
  npm run db:migrate:undo

# 4. Verify rollback
kubectl get pods -n production
curl https://example.com/health
```

---

## Blue-Green Deployment

```bash
# 1. Deploy green environment
kubectl apply -f k8s/deployment-green.yaml

# 2. Wait for green to be ready
kubectl rollout status deployment/app-green -n production

# 3. Test green environment
curl https://green.example.com/health

# 4. Switch traffic to green
kubectl patch service app -n production \
  -p '{"spec":{"selector":{"version":"green"}}}'

# 5. Monitor for issues
# If issues: Switch back to blue
kubectl patch service app -n production \
  -p '{"spec":{"selector":{"version":"blue"}}}'

# 6. If successful: Remove blue deployment
kubectl delete deployment app-blue -n production
```

---

## Monitoring & Alerting

### Health Check Endpoints

```javascript
// healthcheck.js
const http = require('http');

const options = {
  host: 'localhost',
  port: 3000,
  path: '/health',
  timeout: 2000
};

const healthCheck = http.request(options, (res) => {
  if (res.statusCode === 200) {
    process.exit(0);
  } else {
    process.exit(1);
  }
});

healthCheck.on('error', () => {
  process.exit(1);
});

healthCheck.end();
```

### Monitoring Checklist

- [ ] CPU usage < 70%
- [ ] Memory usage < 80%
- [ ] Error rate < 1%
- [ ] Response time p95 < 500ms
- [ ] Database connections healthy
- [ ] Redis connections healthy
- [ ] All pods running
- [ ] No pending deployments

---

## Infrastructure as Code

### Terraform Configuration

```hcl
# main.tf
provider "aws" {
  region = "us-east-1"
}

resource "aws_ecs_cluster" "main" {
  name = "app-cluster"
}

resource "aws_ecs_service" "app" {
  name            = "app-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = 3

  load_balancer {
    target_group_arn = aws_lb_target_group.app.arn
    container_name   = "app"
    container_port   = 3000
  }
}

resource "aws_ecs_task_definition" "app" {
  family                   = "app"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "512"
  memory                   = "1024"

  container_definitions = jsonencode([
    {
      name      = "app"
      image     = "your-registry/app:latest"
      essential = true
      portMappings = [
        {
          containerPort = 3000
          protocol      = "tcp"
        }
      ]
      environment = [
        {
          name  = "NODE_ENV"
          value = "production"
        }
      ]
    }
  ])
}
```

```

## Best Practices

### ✅ DO
- Use infrastructure as code
- Implement CI/CD pipelines
- Use container orchestration
- Implement health checks
- Use rolling deployments
- Have rollback procedures
- Monitor deployments
- Document emergency procedures
- Use secrets management
- Implement blue-green or canary deployments

### ❌ DON'T
- Deploy directly to production
- Skip testing before deploy
- Forget to backup before migrations
- Deploy without rollback plan
- Skip monitoring after deployment
- Hardcode credentials
- Deploy during peak hours (unless necessary)

## Resources

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [AWS ECS](https://docs.aws.amazon.com/ecs/)
- [Terraform](https://www.terraform.io/docs)
