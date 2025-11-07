---
name: docker-containerization
description: Create optimized Docker containers with multi-stage builds, security best practices, and minimal image sizes. Use when containerizing applications, creating Dockerfiles, optimizing container images, or setting up Docker Compose services.
---

# Docker Containerization

## Overview

Build production-ready Docker containers following best practices for security, performance, and maintainability.

## When to Use

- Containerizing applications for deployment
- Creating Dockerfiles for new services
- Optimizing existing container images
- Setting up development environments
- Building CI/CD container pipelines
- Implementing microservices

## Instructions

### 1. **Multi-Stage Builds**

```dockerfile
# Multi-stage build for Node.js application
# Stage 1: Build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:18-alpine
WORKDIR /app
# Copy only production dependencies and built files
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY package*.json ./

# Security: Run as non-root user
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
USER nodejs

EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### 2. **Optimization Techniques**

#### Layer Caching
```dockerfile
# ❌ Poor caching - changes in source code invalidate dependency install
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

# ✅ Good caching - dependencies cached separately
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
```

#### Minimize Image Size
```dockerfile
# ❌ Large image (~800MB)
FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip

# ✅ Minimal image (~50MB)
FROM python:3.11-alpine
```

### 3. **Security Best Practices**

```dockerfile
FROM node:18-alpine

# Update packages for security patches
RUN apk update && apk upgrade

# Don't run as root
RUN addgroup -g 1001 appgroup && adduser -S -u 1001 -G appgroup appuser
USER appuser

# Use specific versions, not 'latest'
WORKDIR /app

# Scan for vulnerabilities
# Run: docker scan your-image:tag
```

### 4. **Environment Configuration**

```dockerfile
# Use build arguments for flexibility
ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s \
  CMD node healthcheck.js || exit 1

# Labels for metadata
LABEL maintainer="team@example.com" \
      version="1.0.0" \
      description="Production API service"
```

### 5. **Docker Compose for Multi-Container**

```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        NODE_ENV: production
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/myapp
      - REDIS_URL=redis://redis:6379
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    networks:
      - app-network
    volumes:
      - ./uploads:/app/uploads
    restart: unless-stopped

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: myapp
      POSTGRES_PASSWORD: password
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - app-network

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    networks:
      - app-network

networks:
  app-network:
    driver: bridge

volumes:
  postgres-data:
  redis-data:
```

### 6. **.dockerignore File**

```
# .dockerignore
node_modules
npm-debug.log
dist
.git
.env
.env.local
*.md
!README.md
.DS_Store
coverage
.vscode
.idea
__pycache__
*.pyc
.pytest_cache
```

## Best Practices

### ✅ DO
- Use official base images
- Implement multi-stage builds
- Run as non-root user
- Use .dockerignore
- Pin specific versions
- Include health checks
- Scan for vulnerabilities
- Minimize layers
- Use build caching effectively

### ❌ DON'T
- Use 'latest' tag in production
- Run as root user
- Include secrets in images
- Create unnecessary layers
- Install unnecessary packages
- Ignore security updates
- Store data in containers

## Examples by Language

### Python (Django/Flask)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

### Java (Spring Boot)
```dockerfile
FROM eclipse-temurin:17-jdk-alpine AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN ./mvnw package -DskipTests

FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
RUN addgroup -S spring && adduser -S spring -G spring
USER spring
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### Go
```dockerfile
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY go.* ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o main .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/main .
CMD ["./main"]
```

## Useful Commands

```bash
# Build image
docker build -t myapp:1.0.0 .

# Build with cache disabled
docker build --no-cache -t myapp:1.0.0 .

# Run container
docker run -d -p 3000:3000 --name myapp myapp:1.0.0

# View logs
docker logs -f myapp

# Execute command in container
docker exec -it myapp sh

# Inspect image layers
docker history myapp:1.0.0

# Check image size
docker images myapp

# Clean up
docker system prune -a
```

## Troubleshooting

**Container exits immediately:**
```bash
docker logs container-name
docker inspect container-name
```

**Build fails:**
```bash
docker build --progress=plain -t myapp .
```

**Permission issues:**
Ensure proper user setup and volume permissions.

**Large image size:**
- Use alpine base images
- Implement multi-stage builds
- Remove unnecessary files
- Use .dockerignore
