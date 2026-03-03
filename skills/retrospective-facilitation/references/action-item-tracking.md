# Action Item Tracking

## Action Item Tracking

```javascript
// Converting retrospective insights to action items

class ActionItemManagement {
  createActionItem(feedback, team) {
    return {
      id: `ACTION-${Date.now()}`,
      title: feedback.title,
      description: feedback.description,
      priority: feedback.priority || "Medium",
      owner: feedback.owner,
      dueDate: this.calculateDueDate(feedback),
      successCriteria: [
        `${feedback.title} completed`,
        "Results verified in next sprint",
        "Team confirms improvement",
      ],
      resources: feedback.estimatedHours || 4,
      dependencies: feedback.dependencies || [],
      status: "New",
      createdDate: new Date(),
    };
  }

  calculateDueDate(item) {
    // High priority: before next sprint starts
    // Medium: during next sprint
    // Low: next 2 sprints
    const daysFromNow = {
      High: 7,
      Medium: 14,
      Low: 21,
    };

    const dueDate = new Date();
    dueDate.setDate(dueDate.getDate() + (daysFromNow[item.priority] || 14));
    return dueDate;
  }

  trackActionItems(items) {
    return {
      total: items.length,
      byStatus: {
        new: items.filter((i) => i.status === "New").length,
        inProgress: items.filter((i) => i.status === "In Progress").length,
        completed: items.filter((i) => i.status === "Completed").length,
        blockedPercent: (
          (items.filter((i) => i.status === "Blocked").length / items.length) *
          100
        ).toFixed(1),
      },
      summary: items.map((item) => ({
        id: item.id,
        title: item.title,
        owner: item.owner,
        dueDate: item.dueDate,
        status: item.status,
        completion: item.completion || 0,
      })),
    };
  }

  reviewCompletedItems(previousRetro) {
    return {
      totalCommitted: previousRetro.actionItems.length,
      completed: previousRetro.actionItems.filter(
        (i) => i.status === "Completed",
      ).length,
      completionRate: `${((previousRetro.actionItems.filter((i) => i.status === "Completed").length / previousRetro.actionItems.length) * 100).toFixed(1)}%`,
      celebration: "Celebrate completed items!",
      carryOver: previousRetro.actionItems
        .filter((i) => i.status !== "Completed")
        .map((i) => ({
          ...i,
          reason: "Not completed",
          recommendation: "Revisit in next retrospective",
        })),
    };
  }
}
```
