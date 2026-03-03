# Dashboard Implementation

## Dashboard Implementation

```javascript
// Build dashboard with data integration

class KPIDashboard {
  constructor(config) {
    this.config = config;
    this.widgets = [];
    this.data = {};
    this.alerts = [];
  }

  createWidget(kpi) {
    return {
      id: `widget-${kpi.id}`,
      title: kpi.name,
      metric_value: kpi.current_value,
      target_value: kpi.target_value,
      threshold: this.calculateThreshold(kpi),
      visualization: {
        type: kpi.chart_type, // 'gauge', 'number', 'chart'
        config: this.getVisualizationConfig(kpi),
      },
      drill_down: true,
      refresh_frequency: kpi.refresh_rate || "hourly",
    };
  }

  calculateThreshold(kpi) {
    const range = kpi.target_value - kpi.minimum_value;

    return {
      green: kpi.target_value,
      yellow: kpi.target_value - range * 0.2,
      red: kpi.target_value - range * 0.5,
      status: this.getStatus(kpi),
      trend: this.calculateTrend(kpi),
    };
  }

  getStatus(kpi) {
    const percentOfTarget = kpi.current_value / kpi.target_value;

    if (percentOfTarget >= 1) return "Green";
    if (percentOfTarget >= 0.8) return "Yellow";
    return "Red";
  }

  calculateTrend(kpi) {
    const change = kpi.current_value - kpi.previous_period_value;
    const changePercent = (change / kpi.previous_period_value) * 100;

    return {
      direction: change > 0 ? "Up" : "Down",
      value: Math.abs(changePercent).toFixed(1),
      momentum: this.assessMomentum(change, kpi),
    };
  }

  generateAlerts() {
    return this.widgets
      .filter((w) => w.threshold.status !== "Green")
      .map((w) => ({
        severity: w.threshold.status,
        message: `${w.title} is ${w.threshold.status} (${w.metric_value} vs ${w.target_value} target)`,
        action: "Review and investigate",
        timestamp: new Date(),
      }));
  }

  exportReport() {
    return {
      format: ["PDF", "Excel", "CSV"],
      include: ["Metrics", "Charts", "Trends", "Commentary"],
      schedule: "Weekly, every Monday morning",
    };
  }
}
```
