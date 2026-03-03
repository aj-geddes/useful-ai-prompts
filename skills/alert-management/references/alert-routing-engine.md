# Alert Routing Engine

## Alert Routing Engine

```javascript
// alert-router.js
class AlertRouter {
  constructor() {
    this.routes = [];
  }

  addRoute(rule) {
    this.routes.push({
      priority: rule.priority || 0,
      condition: rule.condition,
      handler: rule.handler,
      escalation: rule.escalation,
    });
    this.routes.sort((a, b) => b.priority - a.priority);
  }

  async route(alert) {
    for (const route of this.routes) {
      if (route.condition(alert)) {
        return await route.handler(alert, route.escalation);
      }
    }
    return this.defaultHandler(alert);
  }

  async defaultHandler(alert) {
    console.log("Routing to default handler:", alert.name);
    return { routed: true, handler: "default" };
  }
}

// Usage
const router = new AlertRouter();

router.addRoute({
  priority: 100,
  condition: (alert) =>
    alert.severity === "critical" && alert.component === "database",
  handler: async (alert) => {
    console.log("Routing critical database alert to DBA team");
    return { team: "dba", escalation: "immediate" };
  },
});

router.addRoute({
  priority: 90,
  condition: (alert) => alert.component === "payment-service",
  handler: async (alert) => {
    console.log("Routing to payment team");
    return { team: "payment", escalation: "payment-policy" };
  },
});

router.addRoute({
  priority: 10,
  condition: (alert) => alert.severity === "warning",
  handler: async (alert) => {
    console.log("Routing warning to Slack");
    return { handler: "slack-only" };
  },
});

module.exports = router;
```
