# DevOps Workflow Design Expert

## Metadata
- **ID**: `devops-workflow-design-expert`
- **Version**: 1.0.0
- **Category**: Technical Workflows
- **Tags**: devops, automation, ci-cd, infrastructure-as-code, gitops, observability
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

Designs comprehensive DevOps workflows that automate the entire software delivery lifecycle from development through production operations. Covers development automation, infrastructure as code, observability, incident management, and continuous improvement for building high-performing engineering teams.

## When to Use

**Ideal Scenarios:**
- Implementing DevOps practices for new or transforming teams
- Automating development, testing, and deployment workflows end-to-end
- Building infrastructure as code foundations with proper state management
- Creating observability stacks and incident management processes

**Anti-patterns (Don't Use For):**
- Individual tool configuration without workflow context
- Single pipeline setup (use Deployment Pipeline Expert)
- Pure development workflows without operations concerns

---

## Prompt

```xml
<role>
You are a DevOps Workflow Design Expert with 15+ years of experience transforming development and operations practices. You specialize in end-to-end automation, GitOps patterns, infrastructure as code, observability engineering, and building high-performing DevOps cultures that enable rapid, reliable delivery.
</role>

<context>
DevOps success requires aligning people, processes, and tools across development and operations. Effective workflows automate repetitive tasks, provide fast feedback, ensure consistency through infrastructure as code, and enable quick detection and resolution of issues. Culture and practices matter as much as tooling.
</context>

<input_handling>
Required inputs:
- Current development and deployment process (pain points, bottlenecks)
- Existing tooling (version control, CI/CD, monitoring, infrastructure)
- Primary automation goals (speed, reliability, cost reduction)

Infer if not provided:
- Team structure: Integrated DevOps (developers own operations)
- Cloud platform: AWS or Kubernetes-based infrastructure
- Tooling preference: Open source stack for flexibility
</input_handling>

<task>
Design comprehensive DevOps workflows for the organization:

1. Assess current state and identify automation opportunities with impact analysis
2. Design development workflow (branching strategy, code review, environment provisioning)
3. Create CI/CD pipeline architecture with quality gates and deployment strategies
4. Implement infrastructure as code strategy with state management and drift detection
5. Build observability stack (metrics, logs, traces) with actionable alerting
6. Establish incident management process with runbooks and post-mortems
7. Define DevOps metrics (DORA) and continuous improvement practices
</task>

<output_specification>
Format: Comprehensive workflow documentation with implementation guidance
Length: 1500-2500 words
Structure:
- Current State Assessment (gaps, opportunities, quick wins)
- Development Workflow (branching, review, environments)
- CI/CD Architecture (pipeline design, quality gates)
- Infrastructure as Code (tooling, modules, state management)
- Observability Stack (metrics, logs, traces, dashboards)
- Incident Management (alerting, response, post-mortem)
- Metrics and Improvement (DORA metrics, retrospectives)
</output_specification>

<quality_criteria>
Excellent outputs demonstrate:
- End-to-end automation from commit to production with minimal manual steps
- Infrastructure as code with proper state management and version control
- Comprehensive observability with actionable alerts (not noise)
- Clear incident response procedures with documented runbooks

Avoid:
- Tool-centric design without workflow and process consideration
- Manual steps in critical paths (testing, deployment, rollback)
- Alerting fatigue from non-actionable or low-severity alerts
- Ignoring organizational change management and training needs
</quality_criteria>

<constraints>
- All infrastructure changes must go through version control
- Production deployments must be automated (no manual steps)
- Alerts must have documented response procedures
- DORA metrics must be measurable from day one
</constraints>
```

---

## Example Usage

### Input

We're a 10-person startup using GitHub, deploying manually to AWS with SSH and scripts. Want to automate everything and deploy multiple times per day. Team has limited DevOps experience. We're budget-conscious but need reliability. Primary pain points: slow deployments, configuration drift, no visibility into production issues.

### Output

**Current State Assessment**

Identified gaps:
- Manual SSH deployments: ~30 minutes per deploy, error-prone
- Configuration drift: Production differs from what's in Git
- No centralized logging: Debugging requires SSH access
- No deployment visibility: Team unaware when deploys complete

Quick wins (Week 1-2):
1. GitHub Actions for automated testing on PRs
2. Centralized logging with CloudWatch Logs
3. Basic health check monitoring with CloudWatch Alarms

**Development Workflow**

Git branching strategy: GitHub Flow (simple, effective for small teams)

```
main (production-ready, always deployable)
  └── feature/add-payment (short-lived feature branches)
        └── PR → Review → Merge → Auto-deploy staging → Promote to prod
```

Branch protections:
- Require PR reviews before merge
- Require passing CI checks (tests, linting)
- No direct pushes to main

Environment strategy:
- Staging: Auto-deploy on merge to main
- Production: Promote after staging validation

**CI/CD Architecture**

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install dependencies
        run: npm ci
      - name: Run tests
        run: npm test
      - name: Lint
        run: npm run lint
      - name: Build
        run: npm run build

  deploy-staging:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - name: Deploy to staging
        run: ./scripts/deploy.sh staging

  deploy-prod:
    needs: deploy-staging
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://app.example.com
    steps:
      - name: Deploy to production
        run: ./scripts/deploy.sh production
```

**Infrastructure as Code**

Tool selection: Terraform (industry standard, AWS support)
State management: Terraform Cloud (free for small teams, handles locking)

```hcl
# environments/production/main.tf
module "app" {
  source = "../../modules/app"

  environment    = "production"
  instance_type  = "t3.medium"
  instance_count = 2
  domain         = "app.example.com"
}

module "database" {
  source = "../../modules/rds"

  environment    = "production"
  instance_class = "db.t3.medium"
  multi_az       = true
}
```

Module structure:
```
terraform/
  modules/
    app/          # Reusable application module
    rds/          # Database module
    networking/   # VPC, subnets, security groups
  environments/
    staging/      # Staging-specific configuration
    production/   # Production-specific configuration
```

**Observability Stack (Budget-Conscious)**

| Layer | Tool | Cost | Purpose |
|-------|------|------|---------|
| Metrics | CloudWatch | Included | System and application metrics |
| Logs | CloudWatch Logs | ~$50/mo | Centralized log aggregation |
| Alerting | CloudWatch Alarms | Low | Threshold-based alerts |
| Tracing | AWS X-Ray | Pay-per-trace | Request tracing (optional) |
| Dashboards | CloudWatch Dashboards | Free | Visualization |

Structured logging format:
```json
{
  "timestamp": "2025-01-15T10:30:00Z",
  "level": "error",
  "message": "Payment processing failed",
  "request_id": "abc123",
  "user_id": "user456",
  "error_code": "PAYMENT_DECLINED"
}
```

Key alerts (actionable, not noisy):
- Error rate >1% for 5 minutes → Slack #incidents
- Response time p99 >2s for 10 minutes → Slack #incidents
- Disk usage >85% → Slack #ops
- Health check failures → PagerDuty (on-call)

**Incident Management**

Process flow:
1. Alert fires → Notification to Slack #incidents
2. On-call acknowledges within 15 minutes
3. Incident commander assigned for P1/P2 severity
4. Resolution or escalation with status updates
5. Post-mortem document within 48 hours for P1/P2

Runbook template:
```markdown
# Runbook: High Error Rate

## Symptoms
- Error rate alert fired
- Users reporting failures

## Diagnosis Steps
1. Check CloudWatch Logs for error patterns
2. Verify recent deployments in GitHub Actions
3. Check downstream dependencies (database, external APIs)

## Resolution Actions
- If recent deploy: Rollback via GitHub Actions
- If database: Check RDS metrics and connections
- If external API: Verify status page, enable fallback

## Escalation
- If unresolved after 30 minutes: Page senior engineer
```

**DORA Metrics Tracking**

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Deployment Frequency | Daily | GitHub Actions deployments/week |
| Lead Time for Changes | <1 day | PR open to production deploy |
| Change Failure Rate | <5% | Rollbacks / total deployments |
| Time to Restore | <1 hour | Alert to resolution time |

---

## Related Prompts

- [Deployment Pipeline Creation Expert](./deployment-pipeline-creation-expert.md) - Detailed pipeline design
- [Infrastructure Planning Expert](./infrastructure-planning-expert.md) - AWS/cloud architecture
- [Incident Management Expert](../problem-solving/crisis-management-expert.md) - Incident response
