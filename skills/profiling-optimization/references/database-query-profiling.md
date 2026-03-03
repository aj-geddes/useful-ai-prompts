# Database Query Profiling

## Database Query Profiling

```typescript
import { Pool } from "pg";

class QueryProfiler {
  constructor(private pool: Pool) {}

  async profileQuery(
    query: string,
    params: any[] = [],
  ): Promise<{
    result: any;
    planningTime: number;
    executionTime: number;
    plan: any;
  }> {
    // Enable timing
    await this.pool.query("SET track_io_timing = ON");

    // Get query plan
    const explainResult = await this.pool.query(
      `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) ${query}`,
      params,
    );

    const plan = explainResult.rows[0]["QUERY PLAN"][0];

    // Execute actual query
    const start = performance.now();
    const result = await this.pool.query(query, params);
    const duration = performance.now() - start;

    return {
      result: result.rows,
      planningTime: plan["Planning Time"],
      executionTime: plan["Execution Time"],
      plan,
    };
  }

  formatPlan(plan: any): string {
    let output = "Query Plan:\n";
    output += `Planning Time: ${plan["Planning Time"]}ms\n`;
    output += `Execution Time: ${plan["Execution Time"]}ms\n\n`;

    const formatNode = (node: any, indent: number = 0) => {
      const prefix = "  ".repeat(indent);
      output += `${prefix}${node["Node Type"]}\n`;
      output += `${prefix}  Cost: ${node["Total Cost"]}\n`;
      output += `${prefix}  Rows: ${node["Actual Rows"]}\n`;
      output += `${prefix}  Time: ${node["Actual Total Time"]}ms\n`;

      if (node.Plans) {
        node.Plans.forEach((child: any) => formatNode(child, indent + 1));
      }
    };

    formatNode(plan.Plan);
    return output;
  }
}

// Usage
const profiler = new QueryProfiler(pool);

const { result, planningTime, executionTime, plan } =
  await profiler.profileQuery("SELECT * FROM users WHERE age > $1", [25]);

console.log(profiler.formatPlan(plan));
```
