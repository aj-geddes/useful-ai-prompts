# Status Communication Templates

## Status Communication Templates

```javascript
// Status report generation and distribution

class StatusReporting {
  constructor(project) {
    this.project = project;
    this.reportDate = new Date();
  }

  generateExecutiveStatus() {
    return {
      projectName: this.project.name,
      reportDate: this.reportDate,
      status: "Green", // Green/Yellow/Red
      summary: `Project is on track. Completed Phase 1 milestones with 95%
                budget adherence. Minor delay in vendor integration (handled).`,

      keyMetrics: {
        schedulePercentComplete: 45,
        budgetUtilization: 42,
        scope: "On track",
        quality: "All tests passing",
      },

      achievements: [
        "Completed user research and documented requirements",
        "Finalized system architecture and technology stack",
        "Established development pipeline and CI/CD",
        "Delivered Phase 1 prototype to stakeholders",
      ],

      risks: [
        {
          risk: "Third-party API delay",
          impact: "Medium",
          mitigation: "Using mock service, 80% contingency time built in",
        },
      ],

      nextSteps: [
        "Begin Phase 2 development (Week 5)",
        "User acceptance testing planning",
        "Production environment setup",
      ],

      decisionsNeeded: [
        "Approval for enhanced security requirements (+1 week)",
        "Budget for additional load testing tools",
      ],
    };
  }

  generateDetailedStatus() {
    return {
      ...this.generateExecutiveStatus(),

      detailedMetrics: {
        scheduleVariance: "+0.5 weeks (ahead)",
        costVariance: "-$5,000 (under)",
        qualityMetrics: {
          testCoverage: 85,
          defectDensity: "0.2 per 1000 lines",
          codeReviewCompliance: 100,
        },
      },

      phaseBreakdown: [
        {
          phase: "Phase 1: Planning & Design",
          status: "Complete",
          percentComplete: 100,
          owner: "John Smith",
        },
        {
          phase: "Phase 2: Development",
          status: "In Progress",
          percentComplete: 45,
          owner: "Sarah Johnson",
        },
      ],

      issueLog: [
        {
          id: "ISS-001",
          description: "Vendor API documentation incomplete",
          severity: "Medium",
          owner: "Tech Lead",
          targetResolution: "2025-01-15",
        },
      ],
    };
  }

  sendStatusReport(recipients, format = "email") {
    const report = this.generateExecutiveStatus();

    return {
      to: recipients,
      subject: `[${report.status}] ${report.projectName} Status - Week of ${this.reportDate}`,
      body: this.formatReportBody(report),
      attachments: ["detailed_status.pdf"],
      scheduledSend: false,
    };
  }

  formatReportBody(report) {
    return `
Project Status: ${report.status}
Report Date: ${this.reportDate.toISOString().split("T")[0]}

EXECUTIVE SUMMARY
${report.summary}

KEY METRICS
- Schedule: ${report.keyMetrics.schedulePercentComplete}% Complete
- Budget: ${report.keyMetrics.budgetUtilization}% Utilized
- Quality: ${report.keyMetrics.quality}

ACHIEVEMENTS THIS PERIOD
${report.achievements.map((a) => `• ${a}`).join("\n")}

UPCOMING MILESTONES
${report.nextSteps.map((s) => `• ${s}`).join("\n")}

RISKS & ISSUES
${report.risks.map((r) => `• ${r.risk} (${r.impact} Impact): ${r.mitigation}`).join("\n")}

DECISIONS NEEDED
${report.decisionsNeeded.map((d) => `• ${d}`).join("\n")}
    `;
  }
}
```
