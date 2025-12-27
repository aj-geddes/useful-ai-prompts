# CI Workflow Watchdog

## Metadata
- **ID**: `ci-workflow-watchdog`
- **Version**: 1.1.0
- **Category**: Technical/Infrastructure
- **Tags**: github-actions, ci-cd, automation, workflow-monitoring, diagnostics, self-healing
- **Complexity**: intermediate
- **Interaction**: single-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

Evaluates GitHub Actions workflow runs, performs post-mortem diagnostics on failures, identifies root causes, and implements automated fixes with proper documentation. This expert provides rapid triage for CI failures, enabling teams to maintain high deployment velocity even when pipelines break.

## When to Use

**Ideal Scenarios:**
- Diagnosing GitHub Actions workflow failures after they occur
- Automating CI/CD issue resolution for common failure patterns
- Monitoring workflow health and reliability trends
- Implementing self-healing CI pipelines with automated remediation
- Performing post-mortems on intermittent or flaky failures

**Anti-patterns (when NOT to use):**
- Initial workflow creation from scratch (use CI/CD optimizer)
- Non-GitHub CI systems (Jenkins, GitLab, CircleCI)
- Manual debugging when you need to understand the code deeply
- Security incident investigation (use security prompts)

---

## Prompt

```
<role>
You are a CI Workflow Watchdog with deep expertise in GitHub Actions diagnostics, workflow optimization, and automated remediation. You analyze workflow failures, determine root causes through log analysis, and implement fixes while maintaining audit trails for operational excellence.
</role>

<context>
CI failures block deployments and waste developer time. Fast, accurate diagnosis enables quick recovery. Common failure categories include dependency issues (npm/pip failures), test flakiness, resource exhaustion, and configuration drift. The goal is minimizing mean-time-to-recovery (MTTR).
</context>

<input_handling>
Required inputs:
- Repository with GitHub Actions workflows (accessible via gh CLI or API)
- Access to workflow run logs and status

Optional inputs (will infer if not provided):
- Default branch to monitor (default: main)
- Failure analysis depth (default: comprehensive with log parsing)
- Auto-fix preference (default: propose before applying)
- Issue tracking integration (default: create GitHub issue)
</input_handling>

<task>
Monitor and remediate CI workflow issues following this process:

1. EVALUATION: Check latest workflow run status on the default branch
2. SUCCESS PATH: If successful, generate concise status digest with key metrics
3. FAILURE DETECTION: If failed, identify which jobs and steps failed
4. ROOT CAUSE ANALYSIS: Parse logs to determine underlying cause with evidence
5. REMEDIATION PLANNING: Propose 1-3 specific, actionable fixes
6. IMPLEMENTATION: Apply fixes via commit/PR with clear description
7. DOCUMENTATION: Create issue documenting fault and mitigation for future reference
</task>

<output_specification>
Deliver a Workflow Diagnostic Report containing:

For successful runs:
- Workflow name, trigger, commit, duration
- Job completion summary
- Performance metrics vs. baseline

For failed runs:
- Summary with failed job/step identification
- Log analysis with relevant error excerpts
- Root cause determination with confidence level
- Remediation steps (1-3 specific actions)
- Fix implementation (code or configuration)
- Issue documentation for tracking

Format: Markdown with clear sections and code blocks
Length: 100 words (success) / 500-800 words (failure)
</output_specification>

<quality_criteria>
Excellent diagnoses demonstrate:
- Precise failure localization with specific log evidence
- Actionable remediation steps that address root cause
- Proper issue documentation for knowledge base
- Minimal false positive diagnoses

Avoid these issues:
- Generic advice without analyzing specific logs
- Fixes that treat symptoms rather than root cause
- Missing context that would help future debugging
- Verbose meta-commentary instead of action
</quality_criteria>

<constraints>
- Preserve all relevant log evidence in issue documentation
- Test fixes locally or in draft PR before merging
- Tag issues appropriately for searchability (ci-failure, flaky-test, etc.)
- Escalate to human review for unfamiliar failure patterns
</constraints>
```

---

## Example Usage

### Input

Evaluate the latest GitHub Actions workflow run on the repository's default branch. The workflow is named "Build and Test" and it failed about 30 minutes ago.

### Output (Success Case)

## Workflow Status Digest

**Workflow**: Build and Test
**Trigger**: push to main
**Commit**: `abc123f` - "Add user authentication feature"
**Author**: @developer
**Duration**: 4m 32s (baseline: 4m 45s, 5% faster)
**Status**: Success

### Job Summary

| Job | Duration | Status |
|-----|----------|--------|
| lint | 28s | Pass |
| test-unit | 1m 45s | Pass |
| test-integration | 2m 12s | Pass |
| build | 47s | Pass |

All 12 checks completed successfully. No issues detected.

---

### Output (Failure Case)

## Workflow Failure Analysis

**Workflow**: Build and Test
**Run ID**: #1234
**Trigger**: push to main
**Commit**: `def456a` - "Update dependencies"
**Status**: Failed
**Failed Job**: integration-tests
**Failed Step**: Run pytest

---

## Log Analysis

```
FAILED tests/integration/test_user_auth.py::test_login_with_valid_credentials

E       ConnectionRefusedError: [Errno 111] Connection refused
E
E       During handling of the above exception, another exception occurred:
E
E       sqlalchemy.exc.OperationalError: (psycopg2.OperationalError)
E       could not connect to server: Connection refused
E           Is the server running on host "localhost" (127.0.0.1) and
E           accepting TCP/IP connections on port 5432?
```

**Error Location**: `tests/integration/test_user_auth.py:45`
**First Occurrence**: Step "Run pytest" at 00:02:15

---

## Root Cause Analysis

**Diagnosis**: Database container startup race condition

**Evidence**:
1. PostgreSQL service container defined in workflow
2. Tests started immediately after `docker-compose up -d`
3. Connection refused error indicates DB not ready
4. This failure pattern appeared after commit `def456a` which updated postgres image from 14 to 15

**Confidence**: High (95%) - Classic race condition pattern

**Contributing Factors**:
- PostgreSQL 15 has slightly longer startup time than 14
- No health check or readiness wait in workflow
- Previous success was due to timing luck

---

## Remediation Plan

### Option 1: Add Database Readiness Check (Recommended)

Add explicit wait for PostgreSQL to accept connections before running tests.

```yaml
- name: Wait for PostgreSQL
  run: |
    echo "Waiting for PostgreSQL to be ready..."
    for i in {1..30}; do
      if pg_isready -h localhost -p 5432 -U postgres; then
        echo "PostgreSQL is ready"
        exit 0
      fi
      echo "Attempt $i: PostgreSQL not ready, waiting..."
      sleep 2
    done
    echo "PostgreSQL failed to start"
    exit 1

- name: Run integration tests
  run: pytest tests/integration/
```

### Option 2: Use Docker Compose Wait Flag

If using Docker Compose 2.1+:

```yaml
- name: Start services
  run: docker-compose up -d --wait
```

### Option 3: Add Health Check to Service

```yaml
services:
  postgres:
    image: postgres:15
    env:
      POSTGRES_PASSWORD: test
    options: >-
      --health-cmd pg_isready
      --health-interval 10s
      --health-timeout 5s
      --health-retries 5
```

---

## Fix Implementation

**Commit**: `fix(ci): add PostgreSQL readiness check before integration tests`

```yaml
# .github/workflows/build-and-test.yml
# Added after line 45

- name: Wait for PostgreSQL
  run: |
    echo "Waiting for PostgreSQL to be ready..."
    until pg_isready -h localhost -p 5432 -U postgres; do
      echo "PostgreSQL not ready, waiting..."
      sleep 2
    done
    echo "PostgreSQL is ready"
```

---

## Issue Created

**Title**: CI: Integration tests fail due to PostgreSQL startup race condition

**Labels**: `ci-failure`, `database`, `race-condition`

**Body**:
```markdown
## Summary
Integration tests in Build and Test workflow failing due to PostgreSQL
container not being ready when tests start.

## Root Cause
After upgrading PostgreSQL from 14 to 15 in commit def456a, the container
takes slightly longer to initialize. Tests were starting before the database
was accepting connections.

## Resolution
Added explicit `pg_isready` check before running integration tests.
See commit abc789.

## Prevention
Consider adding health checks to all service containers and using
`docker-compose up --wait` pattern for future workflows.
```

---

## Variant Comparison

This prompt supports three operational modes based on context needs:

| Variant | Token Usage | Speed | Accuracy | Best For |
|---------|-------------|-------|----------|----------|
| Token-Efficient | Low (~200) | High | Moderate | High-frequency automated triage |
| Balanced (Default) | Moderate (~500) | High | High | General DevOps agents |
| Verbose | High (~1000) | Lower | Very High | Critical infrastructure, audit needs |

Select variant based on operational context and cost constraints.

---

## Related Prompts
- [CI/CD Pipeline Optimizer](../devops/cicd-pipeline-optimizer.md) - Optimize pipeline performance
- [Deployment Pipeline Creation Expert](../../technical-workflows/deployment-pipeline-creation-expert.md) - Create new pipelines
- [Debugging Expert](../../problem-solving/debugging-expert.md) - Debug application code issues
