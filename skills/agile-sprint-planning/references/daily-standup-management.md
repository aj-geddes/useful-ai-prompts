# Daily Standup Management

## Daily Standup Management

```javascript
// Daily standup structure and tracking

class DailyStandup {
  constructor(team) {
    this.team = team;
    this.standups = [];
  }

  conductStandup(date) {
    const standup = {
      date,
      startTime: new Date(),
      participants: [],
      timeboxed: true,
      durationMinutes: 15,
    };

    for (let member of this.team) {
      standup.participants.push({
        name: member.name,
        yesterday: member.getYesterdayWork(),
        today: member.getPlanForToday(),
        blockers: member.getBlockers(),
        helpNeeded: member.getHelpNeeded(),
      });
    }

    return {
      standup,
      followUpActions: this.identifyFollowUps(standup),
      blockerResolutionOwners: this.assignBlockerOwners(standup),
    };
  }

  identifyFollowUps(standup) {
    return standup.participants
      .filter((p) => p.blockers.length > 0)
      .map((p) => ({
        owner: p.name,
        blockers: p.blockers,
        deadline: new Date(Date.now() + 24 * 60 * 60 * 1000),
      }));
  }
}
```
