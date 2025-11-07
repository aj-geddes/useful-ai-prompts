---
name: dependency-tracking
description: Map, track, and manage project dependencies across teams, systems, and organizations. Identify critical path items and prevent blocking issues through proactive dependency management.
---

# Dependency Tracking

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

## Instructions

### 1. **Dependency Mapping**

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
                'id': task.id,
                'name': task.name,
                'duration': task.duration,
                'owner': task.owner,
                'status': task.status
            })

            for blocker in task.blocked_by:
                dependency_graph['edges'].append({
                    'from': blocker,
                    'to': task.id,
                    'type': 'Finish-to-Start',
                    'lag': 0  # days between tasks
                })

        return dependency_graph

    def analyze_critical_path(self, tasks):
        """Identify longest chain of dependent tasks"""
        paths = self.find_all_paths(tasks)
        critical_path = max(paths, key=len)

        return {
            'critical_items': critical_path,
            'total_duration': sum(t.duration for t in critical_path),
            'slack_available': 0,
            'any_delay_impacts_schedule': True,
            'monitoring_frequency': 'Daily'
        }

    def identify_blocking_dependencies(self, tasks):
        """Find tasks that block other work"""
        blocking_tasks = {}

        for task in tasks:
            blocked_count = sum(1 for t in tasks if task.id in t.blocked_by)
            if blocked_count > 0:
                blocking_tasks[task.id] = {
                    'task': task.name,
                    'blocking_count': blocked_count,
                    'blocked_tasks': [t.id for t in tasks if task.id in t.blocked_by],
                    'status': task.status,
                    'due_date': task.due_date,
                    'risk_level': 'High' if blocked_count > 3 else 'Medium'
                }

        return blocking_tasks

    def find_circular_dependencies(self, tasks):
        """Detect circular dependency chains"""
        cycles = []

        for task in tasks:
            visited = set()
            if self.has_cycle(task, visited, tasks):
                cycles.append({
                    'cycle': visited,
                    'severity': 'Critical',
                    'action': 'Resolve immediately'
                })

        return cycles

    def has_cycle(self, task, visited, tasks):
        visited.add(task.id)

        for blocker_id in task.blocked_by:
            blocker = next(t for t in tasks if t.id == blocker_id)

            if blocker.id in visited:
                return True
            if self.has_cycle(blocker, visited, tasks):
                return True

        visited.remove(task.id)
        return False
```

### 2. **Dependency Management Board**

```yaml
Dependency Tracking Dashboard:

Project: Platform Migration Q1 2025

---

Critical Path (Blocking Progress):

Task: Database Migration
  ID: TASK-101
  Owner: Data Team
  Duration: 20 days
  Status: In Progress (50%)
  Due Date: Feb 28, 2025
  Blocked By: Schema validation (TASK-95) - DUE TODAY
  Blocks: 6 downstream tasks
  Risk Level: HIGH
  Action Items:
    - Daily standup with Data Team
    - Schema validation must complete by EOD
    - Have rollback plan ready

---

Task: API Contract Finalization
  ID: TASK-102
  Owner: Backend Team
  Duration: 10 days
  Status: Pending (Blocked)
  Depends On: Database Migration (TASK-101)
  Blocks: Frontend implementation (TASK-103), Testing (TASK-104)
  Slack Time: 0 days (critical)
  Early Start: Mar 1, 2025
  Action Items:
    - Start draft specifications now
    - Review with Frontend team
    - Have alternative approach ready

---

High-Risk Dependencies:

Dependency: Third-party Integration
  From: Payment Service API (vendor)
  To: Checkout System (TASK-150)
  Type: External/Uncontrollable
  Status: At Risk (Vendor delay reported)
  Mitigation: Mock service implementation, alternative vendor identified
  Escalation Owner: Product Manager

---

By Team Dependencies:

Backend Team:
  - Database migration → API development
  - Schema design → Data layer implementation
  External: Awaiting Payment Gateway API docs

Frontend Team:
  - API contracts → UI implementation
  - Design system → Component development
  Dependency on Backend: API contract specs (scheduled Feb 20)

DevOps Team:
  - Infrastructure provisioning → Testing environment
  - Kubernetes setup → Staging deployment
  External: Cloud provider quota approval
```

### 3. **Dependency Resolution**

```javascript
// Handling and resolving dependency issues

class DependencyResolution {
  resolveDependencyConflict(blocker, blocked) {
    return {
      conflict: {
        blocking_task: blocker.name,
        blocked_task: blocked.name,
        reason: 'Circular dependency detected'
      },
      resolution_options: [
        {
          option: 'Parallelize Work',
          description: 'Identify independent portions that can proceed',
          effort: 'Medium',
          timeline: 'Can save 5 days'
        },
        {
          option: 'Remove/Defer Blocker',
          description: 'Defer non-critical requirements',
          effort: 'Low',
          timeline: 'Immediate'
        },
        {
          option: 'Create Interim Deliverable',
          description: 'Deliver partial results to unblock downstream',
          effort: 'High',
          timeline: 'Can save 8 days'
        }
      ]
    };
  }

  breakDependency(dependency) {
    return {
      current_state: dependency,
      break_strategies: [
        {
          strategy: 'Remove unnecessary dependency',
          action: 'Refactor to eliminate requirement',
          risk: 'Low if verified'
        },
        {
          strategy: 'Mock/Stub external dependency',
          action: 'Create temporary implementation',
          risk: 'Medium - ensures compatibility'
        },
        {
          strategy: 'Parallel development',
          action: 'Make assumptions, validate later',
          risk: 'Medium - rework possible'
        },
        {
          strategy: 'Resource addition',
          action: 'Parallelize work streams',
          risk: 'Low but costly'
        }
      ]
    };
  }

  handleBlockedTask(task) {
    return {
      task_id: task.id,
      status: 'Blocked',
      blocker: task.blocked_by[0],
      time_blocked: task.calculateBlockedDuration(),
      actions: [
        'Notify team of blockage',
        'Escalate if critical path',
        'Identify alternative work',
        'Schedule resolution meeting',
        'Track blocker closure date'
      ],
      escalation: {
        immediate: task.is_critical_path,
        owner: task.program_manager,
        frequency: 'Daily standup until resolved'
      }
    };
  }
}
```

### 4. **Dependency Dashboard Metrics**

```yaml
Key Metrics:

Critical Path Health:
  - Items on Critical Path: 12
  - At-Risk Items: 2 (17%)
  - Completed: 4 (33%)
  - On Track: 6 (50%)
  - Behind: 2 (17%)

Dependency Status:
  - Total Dependencies: 28
  - Resolved: 18
  - Active: 8
  - At Risk: 2
  - Circular: 0 (Good!)

Blocking Impact:
  - Tasks Currently Blocked: 3
  - Team Members Idle: 2
  - Blocked Effort (person-hours): 24
  - Estimated Cost of Blockage: $2,400

Escalations:
  - Open: 1 (Database migration dependency)
  - Resolved This Week: 0
  - Average Resolution Time: 2.3 days
```

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

## Dependency Management Tips

- Color-code by risk level in tracking tools
- Weekly review of blocked/at-risk items
- Maintain updated dependency diagram
- Escalate after 1 day of blockage on critical path
- Build 15-20% buffer for risky dependencies
