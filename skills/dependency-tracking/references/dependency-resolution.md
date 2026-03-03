# Dependency Resolution

## Dependency Resolution

```javascript
// Handling and resolving dependency issues

class DependencyResolution {
  resolveDependencyConflict(blocker, blocked) {
    return {
      conflict: {
        blocking_task: blocker.name,
        blocked_task: blocked.name,
        reason: "Circular dependency detected",
      },
      resolution_options: [
        {
          option: "Parallelize Work",
          description: "Identify independent portions that can proceed",
          effort: "Medium",
          timeline: "Can save 5 days",
        },
        {
          option: "Remove/Defer Blocker",
          description: "Defer non-critical requirements",
          effort: "Low",
          timeline: "Immediate",
        },
        {
          option: "Create Interim Deliverable",
          description: "Deliver partial results to unblock downstream",
          effort: "High",
          timeline: "Can save 8 days",
        },
      ],
    };
  }

  breakDependency(dependency) {
    return {
      current_state: dependency,
      break_strategies: [
        {
          strategy: "Remove unnecessary dependency",
          action: "Refactor to eliminate requirement",
          risk: "Low if verified",
        },
        {
          strategy: "Mock/Stub external dependency",
          action: "Create temporary implementation",
          risk: "Medium - ensures compatibility",
        },
        {
          strategy: "Parallel development",
          action: "Make assumptions, validate later",
          risk: "Medium - rework possible",
        },
        {
          strategy: "Resource addition",
          action: "Parallelize work streams",
          risk: "Low but costly",
        },
      ],
    };
  }

  handleBlockedTask(task) {
    return {
      task_id: task.id,
      status: "Blocked",
      blocker: task.blocked_by[0],
      time_blocked: task.calculateBlockedDuration(),
      actions: [
        "Notify team of blockage",
        "Escalate if critical path",
        "Identify alternative work",
        "Schedule resolution meeting",
        "Track blocker closure date",
      ],
      escalation: {
        immediate: task.is_critical_path,
        owner: task.program_manager,
        frequency: "Daily standup until resolved",
      },
    };
  }
}
```
