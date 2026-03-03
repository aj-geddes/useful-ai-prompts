---
name: disaster-recovery-testing
description: >
  Execute comprehensive disaster recovery tests, validate recovery procedures,
  and document lessons learned from DR exercises.
---

# Disaster Recovery Testing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement systematic disaster recovery testing to validate recovery procedures, measure RTO/RPO, identify gaps, and ensure team readiness for actual incidents.

## When to Use

- Annual DR exercises
- Infrastructure changes
- New service deployments
- Compliance requirements
- Team training
- Recovery procedure validation
- Cross-region failover testing

## Quick Start

Minimal working example:

```yaml
# dr-test-plan.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: dr-test-procedures
  namespace: operations
data:
  dr-test-plan.md: |
    # Disaster Recovery Test Plan

    ## Test Objectives
    - Validate backup restoration procedures
    - Verify failover mechanisms
    - Test DNS failover
    - Validate data integrity post-recovery
    - Measure RTO and RPO
    - Train incident response team

    ## Pre-Test Checklist
    - [ ] Notify stakeholders
    - [ ] Schedule 4-6 hour window
    - [ ] Disable alerting to prevent noise
    - [ ] Backup production data
    - [ ] Ensure DR environment is isolated
    - [ ] Have rollback plan ready
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [DR Test Plan and Execution](references/dr-test-plan-and-execution.md) | DR Test Plan and Execution |
| [DR Test Script](references/dr-test-script.md) | DR Test Script |
| [DR Test Automation](references/dr-test-automation.md) | DR Test Automation |

## Best Practices

### ✅ DO

- Schedule regular DR tests
- Document procedures in advance
- Test in isolated environments
- Measure actual RTO/RPO
- Involve all teams
- Automate validation
- Record findings
- Update procedures based on results

### ❌ DON'T

- Skip DR testing
- Test during business hours
- Test against production
- Ignore test failures
- Neglect post-test analysis
- Forget to re-enable monitoring
- Use stale backup processes
- Test only once a year
