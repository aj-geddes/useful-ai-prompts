# Risk Monitoring & Control

## Risk Monitoring & Control

```javascript
// Risk tracking and monitoring dashboard

class RiskMonitoring {
  constructor() {
    this.risks = [];
    this.triggers = [];
    this.escalations = [];
  }

  createRiskRegister(risks) {
    return risks.map((risk, index) => ({
      id: `RK-${String(index + 1).padStart(3, "0")}`,
      description: risk.description,
      category: risk.category,
      probability: risk.probability,
      impact: risk.impact,
      riskScore: risk.probability * risk.impact,
      responseStrategy: risk.strategy,
      owner: risk.owner,
      status: "Active",
      triggers: risk.triggers,
      contingencyPlan: risk.contingency,
      createdDate: new Date(),
      lastReviewDate: new Date(),
      closeDate: null,
    }));
  }

  identifyRiskTriggers(risk) {
    return {
      riskId: risk.id,
      triggers: [
        {
          trigger: "Vendor communication delay >1 week",
          indicator: "No response from vendor",
          escalationAction: "Contact vendor PM, evaluate alternatives",
        },
        {
          trigger: "Team member absence >3 days",
          indicator: "Unplanned time off",
          escalationAction: "Activate cross-training plan",
        },
        {
          trigger: "Performance test fails baseline",
          indicator: "Response time > 500ms",
          escalationAction: "Emergency optimization sprint",
        },
      ],
      reviewFrequency: "Weekly standup",
    };
  }

  monitorRisks(riskRegister) {
    const statusReport = {
      timestamp: new Date(),
      summary: {
        total: riskRegister.length,
        active: riskRegister.filter((r) => r.status === "Active").length,
        mitigated: riskRegister.filter((r) => r.status === "Mitigated").length,
        closed: riskRegister.filter((r) => r.status === "Closed").length,
      },
      criticalRisks: riskRegister.filter((r) => r.riskScore >= 16),
      highRisks: riskRegister.filter(
        (r) => r.riskScore >= 12 && r.riskScore < 16,
      ),
      triggeredRisks: riskRegister.filter((r) => r.triggered === true),
    };

    return statusReport;
  }
}
```
