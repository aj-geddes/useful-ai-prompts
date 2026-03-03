---
name: dependency-tracking
description: >
  Map, track, and manage project dependencies across teams, systems, and
  organizations. Identify critical path items and prevent blocking issues
  through proactive dependency management.
---

# Dependency Tracking

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Dependency tracking ensures visibility of task relationships, identifies blocking issues early, and enables better resource planning and risk mitigation.

## When to Use

- Multi-team projects and programs
- Complex technical integrations
- Cross-organizational initiatives
- Identifying critical path items
- Resource allocation planning
- Preventing schedule delays
- Onboarding new team members

## Quick Start

Minimal working example:

```python
# Dependency mapping and tracking

class DependencyTracker:
    DEPENDENCY_TYPES = {
        'Finish-to-Start': 'Task B cannot start until Task A is complete',
        'Start-to-Start': 'Task B cannot start until Task A starts',
        'Finish-to-Finish': 'Task B cannot finish until Task A is complete',
        'Start-to-Finish': 'Task B cannot finish until Task A starts'
    }

    def __init__(self):
        self.tasks = []
        self.dependencies = []
        self.critical_path = []

    def create_dependency_map(self, tasks):
        """Create visual dependency network"""
        dependency_graph = {
            'nodes': [],
            'edges': [],
            'critical_items': []
        }

        for task in tasks:
            dependency_graph['nodes'].append({
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Dependency Mapping](references/dependency-mapping.md) | Dependency Mapping |
| [Dependency Management Board](references/dependency-management-board.md) | Dependency Management Board |
| [Dependency Resolution](references/dependency-resolution.md) | Dependency Resolution |
| [Dependency Dashboard Metrics](references/dependency-dashboard-metrics.md) | Dependency Dashboard Metrics |

## Best Practices

### ✅ DO

- Map dependencies early in planning
- Update dependency tracking weekly
- Identify and monitor critical path items
- Proactively communicate blockers
- Have contingency plans for key dependencies
- Break complex dependencies into smaller pieces
- Track external dependencies separately
- Escalate blocked critical path items immediately
- Remove unnecessary dependencies
- Build in buffer time for risky dependencies

### ❌ DON'T

- Ignore external dependencies
- Leave circular dependencies unresolved
- Assume dependencies will "work out"
- Skip daily monitoring of critical path
- Communicate issues only in status meetings
- Create too many dependencies (couples systems)
- Forget to document dependency rationale
- Avoid escalating blocked critical work
- Plan at 100% utilization (no buffer for dependencies)
- Treat all dependencies as equal priority
