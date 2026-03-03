# Dependency Mapping

## Dependency Mapping

```javascript
// Technical dependency management

class RoadmapDependency {
  constructor() {
    this.initiatives = [];
    this.dependencies = [];
  }

  mapDependencies(initiatives) {
    const dependencyMap = {};

    initiatives.forEach((init) => {
      dependencyMap[init.id] = {
        name: init.name,
        dependsOn: init.blockedBy || [],
        enables: init.enables || [],
        criticalPath: init.criticalPath || false,
        startDate: init.plannedStart,
        endDate: init.plannedEnd,
        buffer: init.buffer || "2 weeks",
      };
    });

    return this.validateDependencies(dependencyMap);
  }

  validateDependencies(dependencyMap) {
    const issues = [];

    for (let init in dependencyMap) {
      const current = dependencyMap[init];

      // Check for circular dependencies
      if (this.hasCircularDependency(init, current.dependsOn, dependencyMap)) {
        issues.push({
          type: "Circular Dependency",
          initiative: current.name,
          severity: "Critical",
        });
      }

      // Check for timeline conflicts
      current.dependsOn.forEach((dep) => {
        const depInit = dependencyMap[dep];
        if (depInit && depInit.endDate > current.startDate) {
          issues.push({
            type: "Timeline Conflict",
            initiative: current.name,
            blockedBy: depInit.name,
            gap: this.calculateGap(depInit.endDate, current.startDate),
            severity: "Medium",
          });
        }
      });
    }

    return {
      dependencyMap,
      issues,
      isValid: issues.length === 0,
    };
  }

  hasCircularDependency(node, deps, map, visited = new Set()) {
    if (visited.has(node)) return true;
    visited.add(node);

    for (let dep of deps) {
      if (
        this.hasCircularDependency(dep, map[dep]?.dependsOn || [], map, visited)
      ) {
        return true;
      }
    }

    return false;
  }

  calculateCriticalPath(dependencyMap) {
    // Identify longest dependency chain
    let criticalPath = [];
    let maxDuration = 0;

    for (let init in dependencyMap) {
      const duration = this.calculatePathDuration(init, dependencyMap);
      if (duration > maxDuration) {
        maxDuration = duration;
        criticalPath = this.getPath(init, dependencyMap);
      }
    }

    return {
      path: criticalPath,
      duration: maxDuration,
      initiatives: criticalPath,
      delayImpact: "All dependent initiatives delayed",
    };
  }
}
```
