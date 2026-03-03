---
name: release-planning
description: >
  Plan, coordinate, and execute software releases across environments. Manage
  versioning, rollout strategies, rollback procedures, and stakeholder
  communication for smooth deployments.
---

# Release Planning

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Release planning ensures coordinated deployment of features to production with minimal risk, clear communication, and established rollback procedures.

## When to Use

- Planning major feature releases
- Coordinating multi-system deployments
- Managing database migrations
- Rolling out infrastructure changes
- Planning go-live strategies
- Coordinating customer communication
- Preparing for high-traffic periods

## Quick Start

Minimal working example:

```yaml
Release Plan:

Release: v2.5.0 - Customer Portal Redesign
Target Release Date: February 15, 2025
Status: Planning
Owner: Product Manager

---

## Executive Summary

This release delivers the redesigned customer portal with improved
UX, performance, and mobile experience. Includes database optimization
and infrastructure scaling.

Business Impact:
  - 25% improvement in user conversion
  - 40% faster load times
  - Mobile-first experience
  - Estimated $500K revenue impact

---

## Release Contents

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Release Checklist](references/release-checklist.md) | Release Checklist |
| [Versioning Strategy](references/versioning-strategy.md) | Versioning Strategy |
| [Rollout & Monitoring](references/rollout-monitoring.md) | Rollout & Monitoring |

## Best Practices

### ✅ DO

- Plan releases with clear timeline and milestones
- Communicate early and often with stakeholders
- Test thoroughly in staging environment
- Use phased rollout to reduce risk
- Monitor metrics continuously during rollout
- Have clear rollback procedure
- Document all changes and decisions
- Conduct post-release review
- Include support team in planning
- Plan releases during lower-traffic periods

### ❌ DON'T

- Release without adequate testing
- Deploy Friday afternoon
- Release without monitoring in place
- Skip UAT/acceptance testing
- Release all major changes together
- Deploy without rollback plan
- Surprise customers with breaking changes
- Release without support team readiness
- Make unreviewed last-minute changes
- Ignore performance or error metrics
