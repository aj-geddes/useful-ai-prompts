# Risk Analysis Matrix

## Risk Analysis Matrix

```javascript
// Qualitative and quantitative risk analysis

class RiskAnalysis {
  constructor() {
    this.riskMatrix = [];
    this.priorityMap = [];
  }

  // Probability scale 1-5
  static PROBABILITY = {
    1: { name: "Very Low", percentage: 0.1, color: "Green" },
    2: { name: "Low", percentage: 0.3, color: "Green" },
    3: { name: "Medium", percentage: 0.5, color: "Yellow" },
    4: { name: "High", percentage: 0.7, color: "Orange" },
    5: { name: "Very High", percentage: 0.9, color: "Red" },
  };

  // Impact scale 1-5
  static IMPACT = {
    1: { name: "Negligible", value: 1, scope: "Minor inconvenience" },
    2: { name: "Minor", value: 10, scope: "Some delay or cost" },
    3: { name: "Moderate", value: 100, scope: "Significant delay or cost" },
    4: { name: "Major", value: 1000, scope: "Critical failure risk" },
    5: { name: "Catastrophic", value: 10000, scope: "Project cancellation" },
  };

  analyzeRisk(risk) {
    const probability = this.PROBABILITY[risk.probability];
    const impact = this.IMPACT[risk.impact];

    // Risk Score = Probability × Impact
    const riskScore = risk.probability * risk.impact;

    // Risk Exposure = Probability × Financial Impact
    const riskExposure = probability.percentage * impact.value;

    return {
      riskId: risk.id,
      riskScore,
      riskExposure,
      priority: this.calculatePriority(riskScore),
      severity: this.calculateSeverity(riskScore),
      mitigationUrgency: riskExposure > 100 ? "Immediate" : "Planned",
    };
  }

  calculatePriority(riskScore) {
    if (riskScore >= 16) return "Critical";
    if (riskScore >= 12) return "High";
    if (riskScore >= 6) return "Medium";
    if (riskScore >= 2) return "Low";
    return "Very Low";
  }

  calculateSeverity(riskScore) {
    return {
      score: riskScore,
      rating: this.calculatePriority(riskScore),
      responseNeeded: riskScore >= 12,
    };
  }

  // Risk Matrix
  createRiskMatrix(risks) {
    const matrix = {
      critical: [],
      high: [],
      medium: [],
      low: [],
      veryLow: [],
    };

    risks.forEach((risk) => {
      const analysis = this.analyzeRisk(risk);
      const priority = analysis.priority.toLowerCase();

      if (matrix[priority]) {
        matrix[priority].push({
          ...risk,
          ...analysis,
        });
      }
    });

    return matrix;
  }
}
```
