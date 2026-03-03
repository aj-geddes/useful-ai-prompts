# Tiered Rate Limiting

## Tiered Rate Limiting

```typescript
enum PricingTier {
  FREE = "free",
  BASIC = "basic",
  PRO = "pro",
  ENTERPRISE = "enterprise",
}

interface TierLimits {
  requestsPerMinute: number;
  requestsPerHour: number;
  requestsPerDay: number;
  burstLimit: number;
}

const TIER_LIMITS: Record<PricingTier, TierLimits> = {
  [PricingTier.FREE]: {
    requestsPerMinute: 10,
    requestsPerHour: 100,
    requestsPerDay: 1000,
    burstLimit: 20,
  },
  [PricingTier.BASIC]: {
    requestsPerMinute: 60,
    requestsPerHour: 1000,
    requestsPerDay: 10000,
    burstLimit: 100,
  },
  [PricingTier.PRO]: {
    requestsPerMinute: 300,
    requestsPerHour: 10000,
    requestsPerDay: 100000,
    burstLimit: 500,
  },
  [PricingTier.ENTERPRISE]: {
    requestsPerMinute: 1000,
    requestsPerHour: 50000,
    requestsPerDay: 1000000,
    burstLimit: 2000,
  },
};

class TieredRateLimiter {
  constructor(private limiter: RedisRateLimiter) {}

  async checkLimits(
    userId: string,
    tier: PricingTier,
  ): Promise<{
    allowed: boolean;
    limitType?: string;
    retryAfter?: number;
    limits: {
      minuteRemaining: number;
      hourRemaining: number;
      dayRemaining: number;
    };
  }> {
    const limits = TIER_LIMITS[tier];

    // Check minute limit
    const minuteResult = await this.limiter.consume(`${userId}:minute`, {
      points: limits.requestsPerMinute,
      duration: 60,
    });

    // Check hour limit
    const hourResult = await this.limiter.consume(`${userId}:hour`, {
      points: limits.requestsPerHour,
      duration: 3600,
    });

    // Check day limit
    const dayResult = await this.limiter.consume(`${userId}:day`, {
      points: limits.requestsPerDay,
      duration: 86400,
    });

    // Determine if any limit exceeded
    if (!minuteResult.allowed) {
      return {
        allowed: false,
        limitType: "minute",
        retryAfter: minuteResult.retryAfter,
        limits: {
          minuteRemaining: 0,
          hourRemaining: hourResult.remaining,
          dayRemaining: dayResult.remaining,
        },
      };
    }

    if (!hourResult.allowed) {
      return {
        allowed: false,
        limitType: "hour",
        retryAfter: hourResult.retryAfter,
        limits: {
          minuteRemaining: minuteResult.remaining,
          hourRemaining: 0,
          dayRemaining: dayResult.remaining,
        },
      };
    }

    if (!dayResult.allowed) {
      return {
        allowed: false,
        limitType: "day",
        retryAfter: dayResult.retryAfter,
        limits: {
          minuteRemaining: minuteResult.remaining,
          hourRemaining: hourResult.remaining,
          dayRemaining: 0,
        },
      };
    }

    return {
      allowed: true,
      limits: {
        minuteRemaining: minuteResult.remaining,
        hourRemaining: hourResult.remaining,
        dayRemaining: dayResult.remaining,
      },
    };
  }
}
```
