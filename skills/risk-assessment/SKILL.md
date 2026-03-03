---
name: risk-assessment
description: >
  Identify, analyze, and prioritize project risks using qualitative and
  quantitative methods. Develop mitigation strategies to minimize impact and
  maximize project success probability.
---

# Risk Assessment

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Risk assessment is a systematic process of identifying potential threats to project success and developing strategies to mitigate, avoid, or accept them.

## When to Use

- Project initiation and planning phases
- Before major milestones or decisions
- When introducing new technologies
- Third-party dependencies or integration
- Organizational or resource changes
- Budget or timeline constraints
- Regulatory or compliance concerns

## Quick Start

Minimal working example:

```python
# Risk identification framework

class RiskIdentification:
    RISK_CATEGORIES = {
        'Technical': [
            'Technology maturity',
            'Integration complexity',
            'Performance requirements',
            'Security vulnerabilities',
            'Data integrity'
        ],
        'Resource': [
            'Team skill gaps',
            'Staff availability',
            'Budget constraints',
            'Equipment/infrastructure',
            'Vendor availability'
        ],
        'Schedule': [
            'Unrealistic deadlines',
            'Dependency delays',
            'Scope creep',
            'Approval delays',
            'Resource conflicts'
        ],
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Risk Identification Techniques](references/risk-identification-techniques.md) | Risk Identification Techniques |
| [Risk Analysis Matrix](references/risk-analysis-matrix.md) | Risk Analysis Matrix |
| [Risk Response Planning](references/risk-response-planning.md) | Risk Response Planning |
| [Risk Monitoring & Control](references/risk-monitoring-control.md) | Risk Monitoring & Control |

## Best Practices

### ✅ DO

- Identify risks early in project planning
- Involve diverse team members in risk identification
- Quantify risk impact when possible
- Prioritize based on risk score and exposure
- Develop specific mitigation plans
- Assign clear risk ownership
- Monitor triggers regularly
- Review and update risk register monthly
- Document lessons learned from realized risks
- Communicate risks transparently to stakeholders

### ❌ DON'T

- Wait until problems occur to identify risks
- Assume risks will not materialize
- Treat all risks as equal priority
- Plan mitigation without clear trigger conditions
- Ignore early warning signs
- Make risk management a one-time activity
- Skip contingency planning for critical risks
- Hide negative risks from stakeholders
- Eliminate all risk (impossible and uneconomical)
- Blame individuals for realized risks
