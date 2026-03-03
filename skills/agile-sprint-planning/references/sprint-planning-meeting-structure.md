# Sprint Planning Meeting Structure

## Sprint Planning Meeting Structure

```javascript
// Example sprint planning agenda and execution

class SprintPlanner {
  constructor(team, sprintLength = 2) {
    this.team = team;
    this.sprintLength = sprintLength; // weeks
    this.userStories = [];
    this.sprintGoal = "";
    this.capacity = 0;
  }

  calculateTeamCapacity() {
    // Capacity = available hours - meetings - buffer
    const workHours = 40; // per person per week
    const meetingHours = 5; // estimated standups, retros, etc.
    const bufferPercent = 0.2; // 20% buffer for interruptions

    const capacityPerPerson = (workHours - meetingHours) * (1 - bufferPercent);
    this.capacity = capacityPerPerson * this.team.length * this.sprintLength;

    return this.capacity;
  }

  conductPlanningMeeting() {
    return {
      part1: {
        duration: "15 minutes",
        activity: "Product Owner presents sprint goal",
        deliverable: "Team understands business objective",
      },
      part2: {
        duration: "45-60 minutes",
        activity: "Team discusses and estimates user stories",
        deliverable: "Prioritized sprint backlog with story points",
      },
      part3: {
        duration: "15 minutes",
        activity: "Team commits to sprint goal",
        deliverable: "Formal sprint backlog committed",
      },
    };
  }

  createSprintBacklog(stories, capacity) {
    let currentCapacity = capacity;
    const sprintBacklog = [];

    for (let story of stories) {
      if (currentCapacity >= story.points) {
        sprintBacklog.push({
          ...story,
          status: "planned",
          sprint: this.currentSprint,
        });
        currentCapacity -= story.points;
      }
    }

    return {
      goal: this.sprintGoal,
      backlog: sprintBacklog,
      remainingCapacity: currentCapacity,
      utilization:
        (((capacity - currentCapacity) / capacity) * 100).toFixed(1) + "%",
    };
  }
}
```
