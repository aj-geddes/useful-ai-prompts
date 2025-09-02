# CI/CD Pipeline Optimizer

## Metadata
- **Created**: 2025-07-18

- **Category**: Technical/DevOps
- **Tags**: CI/CD, pipeline optimization, automation, deployment, continuous integration
- **Version**: 2.0.0
- **Use Cases**: pipeline design, build optimization, deployment automation, release management
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you design and optimize CI/CD pipelines that are fast, reliable, and scalable while maintaining security and quality standards.

## Prompt

```
I'll help you optimize your CI/CD pipeline for speed, reliability, and developer experience. Let me understand your current setup:

**Current pipeline:**
1. What's your tech stack? (languages, frameworks, platforms)
2. What CI/CD tools are you using? (Jenkins, GitLab, GitHub Actions, etc.)
3. How long do your builds typically take?
4. What environments do you deploy to? (dev, staging, prod)

**Pain points:**
5. What's the biggest problem with your current pipeline?
6. How often do builds fail? What are common causes?
7. How many deployments per day/week?
8. Any bottlenecks or slow steps?

**Requirements:**
9. What testing do you need? (unit, integration, E2E, security)
10. Any compliance or security requirements?
11. Do you need multi-region or multi-cloud deployments?
12. What's your team size and skill level?

Based on your answers, I'll provide:

**OPTIMIZED PIPELINE DESIGN** - Faster, more reliable architecture
**PARALLELIZATION STRATEGY** - How to speed up builds
**QUALITY GATES** - Automated checks and balances
**DEPLOYMENT STRATEGY** - Safe, fast production releases
**MONITORING & METRICS** - Pipeline observability

Share your pipeline details and let's make it awesome!
```

## Example Usage

**User Input:**
```
1. Node.js microservices (10 services), React frontends (3 apps), PostgreSQL, Redis
2. Currently using Jenkins (considering migration), Docker, Kubernetes on AWS EKS
3. Full pipeline takes 45-60 minutes, individual service builds 15-20 min
4. Dev (auto-deploy), Staging (manual), Production (manual approval + deploy)

5. Too slow - developers waiting too long for feedback, blocks multiple PRs
6. ~20% failure rate, mostly flaky E2E tests and dependency issues
7. 5-10 staging deploys/day, 2-3 production deploys/week
8. Docker builds (no cache), E2E tests (sequential), waiting for environments

9. Unit tests, integration tests, E2E tests (Cypress), Snyk security scanning
10. SOC2 compliance, need approval trails, security scanning, artifact signing
11. Single region now, planning multi-region next quarter
12. 15 developers, mixed DevOps experience, 2 dedicated DevOps engineers
```

**Assistant Output:**

Based on your Node.js/K8s setup, here's an optimized CI/CD pipeline that will cut your build time by 70%:

## OPTIMIZED PIPELINE DESIGN

### Target Architecture
**Current**: 45-60 min → **Target**: 12-15 min

```yaml
# Parallelized Pipeline Structure
┌─────────────────────────────────────────────────────┐
│                    Trigger: PR/Push                  │
└─────────────────┬───────────────────────────────────┘
                  ↓
        ┌─────────┴─────────┐
        │  Pre-flight (30s) │ 
        │  - Lint           │
        │  - Secrets scan   │
        └─────────┬─────────┘
                  ↓
    ┌─────────────┼─────────────┬──────────────┐
    ↓             ↓             ↓              ↓
┌────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│Service1│  │Service2  │  │Frontend1 │  │Frontend2 │
│(3-4min)│  │(3-4min)  │  │(3-4min)  │  │(3-4min)  │
└────┬───┘  └────┬────┘  └────┬────┘  └────┬────┘
     └───────────┴─────────────┴─────────────┘
                           ↓
                  ┌────────────────┐
                  │Integration Tests│
                  │    (3-4 min)    │
                  └────────┬───────┘
                           ↓
                  ┌────────────────┐
                  │  Deploy Stage   │
                  │    (2 min)      │
                  └────────────────┘
```

### Migration from Jenkins to GitHub Actions

**Why GitHub Actions**:
- Native GitHub integration
- Better parallelization
- Cost-effective for your team size
- Built-in secret management

**Migration Strategy**:
1. Start with new services
2. Migrate one service at a time
3. Run both in parallel initially
4. Full cutover in 4-6 weeks

## PARALLELIZATION STRATEGY

### 1. Smart Docker Caching

**Current Problem**: No cache = rebuilding everything
**Solution**: Multi-stage builds with cache mounting

```dockerfile
# Optimized Dockerfile for Node.js
FROM node:18-alpine AS dependencies
WORKDIR /app
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm \
    npm ci --only=production

FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm \
    npm ci
COPY . .
RUN npm run build

FROM node:18-alpine AS runtime
WORKDIR /app
COPY --from=dependencies /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

**GitHub Actions with Cache**:
```yaml
- name → Set up Docker Buildx
  uses: docker/setup-buildx-action@v2

- name → Build and push
  uses: docker/build-push-action@v4
  with:
    context: .
    push: true
    tags: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
    cache-from: type=gha
    cache-to: type=gha,mode=max
    build-args: |
      BUILDKIT_INLINE_CACHE=1
```

### 2. Parallel Testing Strategy

**Test Execution Matrix**:
```yaml
jobs:
  test:
    strategy:
      matrix:
        service: [service1, service2, service3]
        test-suite: [unit, integration]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run ${{ matrix.test-suite }} tests for ${{ matrix.service }}
        run: |
          cd services/${{ matrix.service }}
          npm run test:${{ matrix.test-suite }}
```

### 3. Dynamic Environment Provisioning

```yaml
# Ephemeral environments for each PR
- name → Deploy Preview Environment
  run: |
    kubectl create namespace pr-${{ github.event.number }} || true
    helm upgrade --install pr-${{ github.event.number }} \
      ./charts/app \
      --namespace pr-${{ github.event.number }} \
      --set image.tag=${{ github.sha }} \
      --wait --timeout 5m
```

## QUALITY GATES

### Automated Quality Checks

```yaml
quality-gates:
  runs-on: ubuntu-latest
  steps:
    # Code Quality
    - name: SonarQube Scan
      env:
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
      run: |
        sonar-scanner \
          -Dsonar.qualitygate.wait=true \
          -Dsonar.projectKey=${{ github.repository }}

    # Security Scanning
    - name: Snyk Security Scan
      run: |
        snyk test --severity-threshold=high
        snyk container test $IMAGE --severity-threshold=high

    # License Compliance
    - name: License Check
      run: npx license-checker --onlyAllow 'MIT;Apache-2.0;BSD'

    # Performance Regression
    - name: Lighthouse CI
      uses: treosh/lighthouse-ci-action@v9
      with:
        budgetPath: ./lighthouse-budget.json
```

### E2E Test Optimization

**Parallel Cypress Execution**:
```yaml
e2e-tests:
  strategy:
    matrix:
      containers: [1, 2, 3, 4]
  runs-on: ubuntu-latest
  steps:
    - name: Cypress parallel run
      uses: cypress-io/github-action@v5
      with:
        record: true
        parallel: true
        group: 'E2E Tests'
        ci-build-id: ${{ github.sha }}
      env:
        CYPRESS_RECORD_KEY: ${{ secrets.CYPRESS_RECORD_KEY }}
```

## DEPLOYMENT STRATEGY

### Progressive Delivery with Flagger

```yaml
# Canary deployment configuration
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: api-service
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api-service
  progressDeadlineSeconds: 60
  service:
    port: 80
  analysis:
    interval: 30s
    threshold: 5
    maxWeight: 50
    stepWeight: 10
    metrics:
    - name: request-success-rate
      thresholdRange:
        min: 99
      interval: 1m
    - name: request-duration
      thresholdRange:
        max: 500
      interval: 30s
```

### Multi-Region Deployment Pipeline

```yaml
deploy-production:
  needs: [quality-gates, e2e-tests]
  strategy:
    matrix:
      region: [us-east-1, eu-west-1, ap-southeast-1]
  steps:
    - name: Deploy to ${{ matrix.region }}
      run: |
        aws eks update-kubeconfig --region ${{ matrix.region }}
        helm upgrade --install production ./charts/app \
          --set image.tag=${{ github.sha }} \
          --set region=${{ matrix.region }} \
          --atomic --timeout 10m
```

## MONITORING & METRICS

### Pipeline Observability

```yaml
# Datadog CI Visibility
- name → Datadog CI
  uses: datadog/datadog-ci-action@v1
  with:
    api-key: ${{ secrets.DD_API_KEY }}
    service: 'ci-pipeline'
    env: 'ci'

# Custom metrics tracking
- name → Track Pipeline Metrics
  run: |
    cat << EOF | curl -X POST $METRICS_ENDPOINT
    {
      "pipeline_duration": ${{ steps.timer.outputs.duration }},
      "build_size": $(du -sh dist | cut -f1),
      "test_count": $(npm test -- --json | jq '.numTotalTests'),
      "coverage": $(npm run coverage -- --json | jq '.total.lines.pct')
    }
    EOF
```

### Key Metrics Dashboard

```
Pipeline KPIs:
├── Lead Time: 12 min (was 50 min)
├── Deployment Frequency: 10/day (was 3/day)
├── MTTR: <5 min (was 30 min)
├── Change Failure Rate: <2% (was 20%)
└── Pipeline Success Rate: >95% (was 80%)
```

### Cost Optimization

**GitHub Actions Cost Reduction**:
- Use larger runners for critical path: 4x faster, 2x cost = 50% savings
- Self-hosted runners for heavy workloads
- Aggressive caching reduces compute by 60%

**Monthly Estimate**:
- Current (Jenkins): ~$3000 (infrastructure + maintenance)
- Optimized (GitHub Actions): ~$800
- Savings: $2200/month

### Implementation Roadmap

**Week 1-2**: 
- Set up GitHub Actions for one service
- Implement Docker caching
- Create reusable workflows

**Week 3-4**:
- Migrate 50% of services
- Set up parallel testing
- Implement quality gates

**Week 5-6**:
- Complete migration
- Set up Flagger for canary
- Full monitoring implementation

**Week 7-8**:
- Team training
- Documentation
- Decommission Jenkins

This optimized pipeline will transform your deployment velocity while improving quality and reducing costs.

## Related Prompts

- [Infrastructure as Code Expert](../../creation/code-generation-expert.md)
- [Kubernetes Optimization Specialist](../../renewable-energy/solar-project-development-optimization-expert.md)
- [DevOps Security Expert](../../problem-solving/security-vulnerability-mitigation-expert.md)
