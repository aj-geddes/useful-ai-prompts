# Feature Flag with Analytics

## Feature Flag with Analytics

```typescript
interface FlagEvaluationEvent {
  flagKey: string;
  userId?: string;
  result: boolean;
  variant?: any;
  timestamp: number;
  duration: number;
}

class FeatureFlagServiceWithAnalytics extends FeatureFlagService {
  private analytics: Analytics;

  constructor(analytics: Analytics) {
    super();
    this.analytics = analytics;
  }

  isEnabled(flagKey: string, context: EvaluationContext = {}): boolean {
    const startTime = Date.now();
    const result = super.isEnabled(flagKey, context);
    const duration = Date.now() - startTime;

    this.trackEvaluation({
      flagKey,
      userId: context.userId,
      result,
      timestamp: Date.now(),
      duration,
    });

    return result;
  }

  getVariant(flagKey: string, context: EvaluationContext = {}): any {
    const startTime = Date.now();
    const variant = super.getVariant(flagKey, context);
    const duration = Date.now() - startTime;

    this.trackEvaluation({
      flagKey,
      userId: context.userId,
      result: variant !== null,
      variant,
      timestamp: Date.now(),
      duration,
    });

    return variant;
  }

  private trackEvaluation(event: FlagEvaluationEvent): void {
    this.analytics.track("feature_flag_evaluated", {
      flag_key: event.flagKey,
      user_id: event.userId,
      result: event.result,
      variant: event.variant,
      duration_ms: event.duration,
    });
  }

  async getAnalytics(
    flagKey: string,
    timeRange: { start: Date; end: Date },
  ): Promise<{
    evaluations: number;
    uniqueUsers: number;
    enabledRate: number;
    variantDistribution: Record<string, number>;
  }> {
    return this.analytics.getFlagAnalytics(flagKey, timeRange);
  }
}
```
