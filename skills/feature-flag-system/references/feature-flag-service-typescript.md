# Feature Flag Service (TypeScript)

## Feature Flag Service (TypeScript)

```typescript
interface FlagConfig {
  key: string;
  enabled: boolean;
  description: string;
  rules?: FlagRule[];
  variants?: FlagVariant[];
  createdAt: Date;
  updatedAt: Date;
}

interface FlagRule {
  type: "user" | "percentage" | "attribute" | "datetime";
  operator: "in" | "equals" | "contains" | "gt" | "lt" | "between";
  attribute?: string;
  values: any[];
}

interface FlagVariant {
  key: string;
  weight: number;
  value: any;
}

interface EvaluationContext {
  userId?: string;
  email?: string;
  attributes?: Record<string, any>;
  timestamp?: number;
}

class FeatureFlagService {
  private flags: Map<string, FlagConfig> = new Map();

  constructor() {
    this.loadFlags();
  }

  private loadFlags(): void {
    // Load from database or config
    this.flags.set("new-dashboard", {
      key: "new-dashboard",
      enabled: true,
      description: "New dashboard UI",
      rules: [
        {
          type: "percentage",
          operator: "lt",
          values: [25], // 25% rollout
        },
      ],
      createdAt: new Date(),
      updatedAt: new Date(),
    });

    this.flags.set("premium-features", {
      key: "premium-features",
      enabled: true,
      description: "Premium features for paid users",
      rules: [
        {
          type: "attribute",
          operator: "equals",
          attribute: "plan",
          values: ["premium", "enterprise"],
        },
      ],
      createdAt: new Date(),
      updatedAt: new Date(),
    });

    this.flags.set("beta-feature", {
      key: "beta-feature",
      enabled: true,
      description: "Beta feature",
      rules: [
        {
          type: "user",
          operator: "in",
          values: ["user1", "user2", "user3"],
        },
      ],
      createdAt: new Date(),
      updatedAt: new Date(),
    });
  }

  isEnabled(flagKey: string, context: EvaluationContext = {}): boolean {
    const flag = this.flags.get(flagKey);

    if (!flag) {
      console.warn(`Flag not found: ${flagKey}`);
      return false;
    }

    if (!flag.enabled) {
      return false;
    }

    if (!flag.rules || flag.rules.length === 0) {
      return true;
    }

    return this.evaluateRules(flag.rules, context);
  }

  getVariant(flagKey: string, context: EvaluationContext = {}): any {
    const flag = this.flags.get(flagKey);

    if (!flag || !this.isEnabled(flagKey, context)) {
      return null;
    }

    if (!flag.variants || flag.variants.length === 0) {
      return true;
    }

    return this.selectVariant(flag.variants, context);
  }

  private evaluateRules(
    rules: FlagRule[],
    context: EvaluationContext,
  ): boolean {
    return rules.every((rule) => this.evaluateRule(rule, context));
  }

  private evaluateRule(rule: FlagRule, context: EvaluationContext): boolean {
    switch (rule.type) {
      case "user":
        return this.evaluateUserRule(rule, context);

      case "percentage":
        return this.evaluatePercentageRule(rule, context);

      case "attribute":
        return this.evaluateAttributeRule(rule, context);

      case "datetime":
        return this.evaluateDateTimeRule(rule, context);

      default:
        return false;
    }
  }

  private evaluateUserRule(
    rule: FlagRule,
    context: EvaluationContext,
  ): boolean {
    if (!context.userId) return false;

    return rule.values.includes(context.userId);
  }

  private evaluatePercentageRule(
    rule: FlagRule,
    context: EvaluationContext,
  ): boolean {
    const hash = this.hashContext(context);
    const percentage = (hash % 100) + 1;

    return percentage <= rule.values[0];
  }

  private evaluateAttributeRule(
    rule: FlagRule,
    context: EvaluationContext,
  ): boolean {
    if (!rule.attribute || !context.attributes) return false;

    const value = context.attributes[rule.attribute];

    switch (rule.operator) {
      case "equals":
        return rule.values.includes(value);

      case "contains":
        return rule.values.some((v) => String(value).includes(v));

      case "gt":
        return value > rule.values[0];

      case "lt":
        return value < rule.values[0];

      default:
        return false;
    }
  }

  private evaluateDateTimeRule(
    rule: FlagRule,
    context: EvaluationContext,
  ): boolean {
    const now = context.timestamp || Date.now();

    if (rule.operator === "between") {
      return now >= rule.values[0] && now <= rule.values[1];
    }

    return false;
  }

  private selectVariant(
    variants: FlagVariant[],
    context: EvaluationContext,
  ): any {
    const hash = this.hashContext(context);
    const totalWeight = variants.reduce((sum, v) => sum + v.weight, 0);
    const position = hash % totalWeight;

    let cumulative = 0;
    for (const variant of variants) {
      cumulative += variant.weight;
      if (position < cumulative) {
        return variant.value;
      }
    }

    return variants[0].value;
  }

  private hashContext(context: EvaluationContext): number {
    const str = context.userId || context.email || "anonymous";
    let hash = 0;

    for (let i = 0; i < str.length; i++) {
      const char = str.charCodeAt(i);
      hash = (hash << 5) - hash + char;
      hash = hash & hash;
    }

    return Math.abs(hash);
  }

  async createFlag(
    config: Omit<FlagConfig, "createdAt" | "updatedAt">,
  ): Promise<void> {
    this.flags.set(config.key, {
      ...config,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
  }

  async updateFlag(key: string, updates: Partial<FlagConfig>): Promise<void> {
    const flag = this.flags.get(key);
    if (!flag) {
      throw new Error(`Flag not found: ${key}`);
    }

    this.flags.set(key, {
      ...flag,
      ...updates,
      updatedAt: new Date(),
    });
  }

  async deleteFlag(key: string): Promise<void> {
    this.flags.delete(key);
  }

  getAllFlags(): FlagConfig[] {
    return Array.from(this.flags.values());
  }
}

// Usage
const featureFlags = new FeatureFlagService();

// Simple boolean check
if (featureFlags.isEnabled("new-dashboard", { userId: "user123" })) {
  console.log("Show new dashboard");
}

// With user attributes
const hasPremiumFeatures = featureFlags.isEnabled("premium-features", {
  userId: "user123",
  attributes: { plan: "premium" },
});

// Get variant for A/B testing
const buttonColor = featureFlags.getVariant("button-color-test", {
  userId: "user123",
});
```
