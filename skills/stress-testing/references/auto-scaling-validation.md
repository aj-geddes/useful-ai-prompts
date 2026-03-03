# Auto-Scaling Validation

## Auto-Scaling Validation

```typescript
// test-autoscaling.ts
import { test, expect } from "@playwright/test";
import axios from "axios";

test.describe("Auto-scaling Stress Test", () => {
  test("system should scale up under load", async () => {
    const baseUrl = "http://api.example.com";
    const cloudwatch = new AWS.CloudWatch();

    // Initial instance count
    const initialInstances = await getInstanceCount();
    console.log(`Initial instances: ${initialInstances}`);

    // Generate high load
    const requests = [];
    for (let i = 0; i < 1000; i++) {
      requests.push(
        axios
          .get(`${baseUrl}/api/heavy-operation`)
          .catch((err) => ({ error: err.message })),
      );
    }

    // Wait for auto-scaling trigger
    await Promise.all(requests);
    await new Promise((resolve) => setTimeout(resolve, 120000)); // 2 min

    // Check if scaled up
    const scaledInstances = await getInstanceCount();
    console.log(`Scaled instances: ${scaledInstances}`);

    expect(scaledInstances).toBeGreaterThan(initialInstances);

    // Verify metrics
    const cpuMetrics = await cloudwatch
      .getMetricStatistics({
        Namespace: "AWS/EC2",
        MetricName: "CPUUtilization",
        // ... metric params
      })
      .promise();

    expect(cpuMetrics.Datapoints.some((d) => d.Average > 70)).toBe(true);
  });
});
```
