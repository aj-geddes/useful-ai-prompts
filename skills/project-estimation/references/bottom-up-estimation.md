# Bottom-Up Estimation

## Bottom-Up Estimation

```javascript
// Bottom-up estimation from detailed task breakdown

class BottomUpEstimation {
  constructor(project) {
    this.project = project;
    this.tasks = [];
    this.workBreakdownStructure = {};
  }

  createWBS() {
    // Work Breakdown Structure example
    return {
      level1: "Full Project",
      level2: ["Planning", "Design", "Development", "Testing", "Deployment"],
      level3: {
        Development: [
          "Backend API",
          "Frontend UI",
          "Database Schema",
          "Integration",
        ],
        Testing: [
          "Unit Testing",
          "Integration Testing",
          "UAT",
          "Performance Testing",
        ],
      },
    };
  }

  estimateTasks(tasks) {
    let totalEstimate = 0;
    const estimates = [];

    for (let task of tasks) {
      const taskEstimate = this.estimateSingleTask(task);
      estimates.push({
        name: task.name,
        effort: taskEstimate.effort,
        resources: taskEstimate.resources,
        risk: taskEstimate.risk,
        duration: taskEstimate.duration,
      });
      totalEstimate += taskEstimate.effort;
    }

    return {
      totalEffortHours: totalEstimate,
      totalWorkDays: totalEstimate / 8,
      taskDetails: estimates,
      criticalPath: this.identifyCriticalPath(estimates),
    };
  }

  estimateSingleTask(task) {
    // Base effort
    let effort = task.complexity * task.scope;

    // Adjust for team experience
    const experienceFactor = task.teamExperience / 100; // 0.5 to 1.5
    effort = effort * experienceFactor;

    // Adjust for risk
    const riskFactor = 1 + task.riskLevel * 0.1;
    effort = effort * riskFactor;

    return {
      effort: Math.ceil(effort),
      resources: Math.ceil(effort / 8), // days
      risk: task.riskLevel,
      duration: Math.ceil(effort / (8 * task.teamSize)),
    };
  }

  identifyCriticalPath(estimates) {
    // Return tasks with longest duration
    return estimates.sort((a, b) => b.duration - a.duration).slice(0, 5);
  }
}
```
