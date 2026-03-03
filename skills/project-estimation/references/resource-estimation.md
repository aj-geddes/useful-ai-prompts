# Resource Estimation

## Resource Estimation

```javascript
// Resource allocation and estimation

class ResourceEstimation {
  calculateResourceNeeds(projectDuration, tasks) {
    const resourceMap = {
      "Senior Developer": 0,
      "Mid-Level Developer": 0,
      "Junior Developer": 0,
      "QA Engineer": 0,
      "DevOps Engineer": 0,
      "Project Manager": 0,
    };

    let totalEffort = 0;

    for (let task of tasks) {
      resourceMap[task.requiredRole] += task.effortHours;
      totalEffort += task.effortHours;
    }

    // Calculate FTE (Full Time Equivalent) needed
    const fteMap = {};
    for (let role in resourceMap) {
      fteMap[role] = (resourceMap[role] / (projectDuration * 8 * 5)).toFixed(2);
    }

    return {
      effortByRole: resourceMap,
      fte: fteMap,
      totalEffortHours: totalEffort,
      totalWorkDays: totalEffort / 8,
      costEstimate: this.calculateCost(fteMap),
    };
  }

  calculateCost(fteMap) {
    const dailyRates = {
      "Senior Developer": 1200,
      "Mid-Level Developer": 900,
      "Junior Developer": 600,
      "QA Engineer": 700,
      "DevOps Engineer": 950,
      "Project Manager": 800,
    };

    let totalCost = 0;
    const costByRole = {};

    for (let role in fteMap) {
      const fteDays = fteMap[role] * 250; // 250 working days/year
      costByRole[role] = fteDays * dailyRates[role];
      totalCost += costByRole[role];
    }

    return {
      byRole: costByRole,
      total: totalCost,
      currency: "USD",
    };
  }
}
```
