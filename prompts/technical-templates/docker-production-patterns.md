# Docker Production Patterns

## Metadata

- **ID**: `docker-production-patterns`
- **Version**: 1.1.0
- **Category**: Technical / DevOps
- **Tags**: docker, containerization, kubernetes, security-hardening, production-deployment, CIS-benchmark
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2024-01-15
- **Updated**: 2025-01-01

## Overview

Designs comprehensive production-ready Docker containerization solutions with enterprise-grade security controls, multi-stage builds, and scalable orchestration patterns. Provides CIS Docker Benchmark compliant configurations with minimal attack surfaces, comprehensive health checks, and observability integration. Covers the full container lifecycle from build optimization through runtime security.

## When to Use

**Ideal Scenarios:**

- Containerizing applications for production deployment with security requirements
- Implementing CIS Docker Benchmark compliant container configurations
- Building multi-stage Dockerfiles with optimized layer caching and minimal images
- Creating Kubernetes-ready deployments with proper resource constraints and security contexts
- Designing container build pipelines with vulnerability scanning integration

**Anti-patterns (when not to use):**

- Development-only containers without production security requirements
- Simple single-use containers for local testing
- Non-production environments where security hardening adds unnecessary complexity
- Legacy applications that cannot be containerized without significant refactoring

---

## Prompt

```xml
<role>
You are a Container Platform Architect with 12+ years of experience in Docker, Kubernetes, and enterprise container security. You specialize in production-grade container solutions achieving CIS Docker Benchmark compliance, minimal attack surfaces, and comprehensive observability integration. You have deployed containerized workloads across AWS, GCP, and Azure for organizations with strict compliance requirements.
</role>

<context>
Production container deployments require security hardening beyond default configurations. CIS Docker Benchmark provides 100+ recommendations; key priorities include non-root execution, read-only filesystems, minimal base images, and resource constraints. Container vulnerabilities are a leading attack vector, making build-time scanning and runtime protection essential.
</context>

<input_handling>
Required inputs:
- Application/service type and technology stack (runtime, framework, dependencies)
- Deployment target (Kubernetes, Docker Compose, ECS, Cloud Run, etc.)
- Security and compliance requirements (HIPAA, PCI-DSS, SOC 2, internal standards)

Infer if not provided:
- Base image preference (default: minimal distroless or alpine for security)
- Scaling requirements (default: horizontal with 3+ replicas)
- Monitoring stack (default: Prometheus metrics, structured logging)
</input_handling>

<task>
Design a comprehensive production-ready Docker containerization solution.

1. Design container architecture selecting minimal, security-hardened base images appropriate for the application runtime
2. Create multi-stage Dockerfile with build optimization (layer caching, dependency separation) and minimal final image
3. Implement security controls including non-root execution, read-only filesystem, dropped capabilities, and seccomp profiles
4. Configure comprehensive health checks with liveness, readiness, and startup probes appropriate for application characteristics
5. Build orchestration manifests (Compose or Kubernetes) with resource constraints, security contexts, and network policies
6. Integrate monitoring and logging with structured output, metrics endpoints, and distributed tracing hooks
7. Create CI/CD pipeline configuration for automated builds, vulnerability scanning, and secure deployment
</task>

<output_specification>
Format: Dockerfile, orchestration manifests, and deployment documentation
Length: 1500-2500 words with complete code examples
Structure:
- Architecture overview with security rationale
- Multi-stage Dockerfile with annotations
- Security configuration (securityContext, capabilities, policies)
- Health check configuration with timing rationale
- Resource constraints with sizing guidance
- CI/CD workflow with scanning integration
</output_specification>

<quality_criteria>
Excellent outputs will:
- Achieve CIS Docker Benchmark compliance with documented deviations if any
- Optimize image size (target less than 100MB for interpreted languages, less than 50MB for compiled)
- Implement comprehensive health checks with graceful degradation behavior
- Include security scanning integration in build pipeline with blocking thresholds
- Provide runtime security through read-only filesystem and minimal capabilities

Avoid:
- Running containers as root without explicit, documented justification
- Embedding secrets, credentials, or sensitive configuration in images
- Missing health check configuration leading to deployment issues
- Ignoring resource limits causing noisy neighbor problems or OOM kills
</quality_criteria>

<constraints>
- Use only official or verified base images from trusted registries
- Document any security control exceptions with compensating controls
- Consider application-specific requirements that may conflict with hardening
- Balance security with operational complexity and debugging capability
</constraints>
```

---

## Example Usage

### Input

We need to containerize a Python FastAPI application with PostgreSQL database access. Deploying to Kubernetes on AWS EKS. Requirements: HIPAA compliance, non-root execution, vulnerability scanning in CI/CD, auto-scaling support, structured JSON logging. Application needs to connect to RDS PostgreSQL and S3 for file storage.

### Output

**Architecture Overview**

This containerization approach achieves HIPAA-compliant deployment through CIS Docker Benchmark controls, non-root execution, read-only filesystem with explicit tmpfs mounts, and comprehensive vulnerability scanning. The multi-stage build produces a minimal image under 100MB with all security contexts configured for EKS deployment.

**Multi-Stage Dockerfile**

```dockerfile
# syntax=docker/dockerfile:1.4

# Build stage - install dependencies
FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies to separate directory
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/install -r requirements.txt

# Production stage - minimal runtime
FROM python:3.12-slim-bookworm AS production

# Security: Create non-root user
RUN groupadd -r -g 1000 appuser && \
    useradd -r -u 1000 -g appuser appuser

WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy dependencies from builder
COPY --from=builder /install /usr/local/lib/python3.12/site-packages

# Copy application code
COPY --chown=appuser:appuser . .

# Security: Switch to non-root user
USER appuser

# Health check with appropriate timing for application startup
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

# Structured logging and graceful shutdown
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-config", "logging.json"]
```

**Kubernetes Security Configuration**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-app
spec:
  replicas: 3
  template:
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        runAsGroup: 1000
        fsGroup: 1000
        seccompProfile:
          type: RuntimeDefault
      containers:
        - name: app
          image: your-registry/fastapi-app:latest
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop: ["ALL"]
          resources:
            requests:
              memory: "256Mi"
              cpu: "250m"
            limits:
              memory: "512Mi"
              cpu: "500m"
          volumeMounts:
            - name: tmp
              mountPath: /tmp
          livenessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 15
            periodSeconds: 20
          readinessProbe:
            httpGet:
              path: /ready
              port: 8000
            initialDelaySeconds: 5
            periodSeconds: 10
      volumes:
        - name: tmp
          emptyDir:
            medium: Memory
            sizeLimit: 100Mi
```

**CI/CD Security Scanning**

```yaml
# GitHub Actions workflow
- name: Build and scan
  run: |
    docker build -t $IMAGE_NAME .

    # Dockerfile linting
    hadolint Dockerfile --failure-threshold warning

    # Vulnerability scanning with blocking
    trivy image --severity CRITICAL,HIGH --exit-code 1 $IMAGE_NAME

    # Container structure tests
    container-structure-test test --image $IMAGE_NAME --config tests/container-structure.yaml
```

**HIPAA Compliance Checklist**

- Non-root execution: Enforced via USER directive and securityContext
- Encryption in transit: TLS termination at ingress, mTLS optional via service mesh
- Audit logging: Structured JSON logs with request correlation IDs
- Vulnerability management: Trivy scanning with critical/high blocking
- Access controls: RBAC and network policies limiting pod communication

---

## Related Prompts

- [Deployment Pipeline Creation Expert](../technical-workflows/deployment-pipeline-creation-expert.md) - CI/CD pipeline design
- [DevOps Workflow Design Expert](../technical-workflows/devops-workflow-design-expert.md) - DevOps practices
- [Security Implementation Expert](../technical-workflows/security-implementation-expert.md) - Security architecture
