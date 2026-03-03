# Resource Leveling

## Resource Leveling

```javascript
// Balance workload across team members

class ResourceLeveling {
  levelWorkload(team, tasks) {
    const workloadByPerson = {};

    // Initialize team member workload
    team.forEach((person) => {
      workloadByPerson[person.id] = {
        name: person.name,
        skills: person.skills,
        capacity: person.capacity_hours,
        assigned: [],
        utilization: 0,
      };
    });

    // Assign tasks to balance workload
    const sortedTasks = tasks.sort((a, b) => b.effort - a.effort); // Largest first

    sortedTasks.forEach((task) => {
      const suitable = team.filter(
        (p) =>
          this.hasSufficientSkills(p.skills, task.required_skills) &&
          this.hasCapacity(
            workloadByPerson[p.id].utilization,
            p.capacity_hours,
          ),
      );

      if (suitable.length > 0) {
        const leastUtilized = suitable.reduce((a, b) =>
          workloadByPerson[a.id].utilization <
          workloadByPerson[b.id].utilization
            ? a
            : b,
        );

        workloadByPerson[leastUtilized.id].assigned.push(task);
        workloadByPerson[leastUtilized.id].utilization += task.effort;
      }
    });

    return {
      assignments: workloadByPerson,
      balanceMetrics: this.calculateBalance(workloadByPerson),
      unassignedTasks: tasks.filter(
        (t) =>
          !Object.values(workloadByPerson).some((p) => p.assigned.includes(t)),
      ),
    };
  }

  calculateBalance(workloadByPerson) {
    const utilizations = Object.values(workloadByPerson).map(
      (p) => p.utilization,
    );
    const average = utilizations.reduce((a, b) => a + b) / utilizations.length;
    const variance = Math.sqrt(
      utilizations.reduce((sum, u) => sum + Math.pow(u - average, 2)) /
        utilizations.length,
    );

    return {
      average_utilization: average.toFixed(1),
      std_deviation: variance.toFixed(1),
      balance_score: this.calculateBalanceScore(variance),
      recommendations: this.getBalancingRecommendations(variance),
    };
  }

  calculateBalanceScore(variance) {
    if (variance < 5) return "Excellent";
    if (variance < 10) return "Good";
    if (variance < 15) return "Fair";
    return "Poor - needs rebalancing";
  }
}
```
