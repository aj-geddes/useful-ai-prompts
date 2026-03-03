# Feature Flags

## Feature Flags

### Simple Feature Flag Implementation

```typescript
// feature-flags/feature-flag.ts
export interface FeatureFlag {
  enabled: boolean;
  rolloutPercentage?: number;
  allowedUsers?: string[];
  allowedEnvironments?: string[];
}

export class FeatureFlagManager {
  private flags: Map<string, FeatureFlag>;

  constructor(flags: Record<string, FeatureFlag>) {
    this.flags = new Map(Object.entries(flags));
  }

  isEnabled(
    flagName: string,
    context?: { userId?: string; environment?: string },
  ): boolean {
    const flag = this.flags.get(flagName);
    if (!flag) return false;

    // Check if disabled globally
    if (!flag.enabled) return false;

    // Check environment restriction
    if (flag.allowedEnvironments && context?.environment) {
      if (!flag.allowedEnvironments.includes(context.environment)) {
        return false;
      }
    }

    // Check user whitelist
    if (flag.allowedUsers && context?.userId) {
      if (flag.allowedUsers.includes(context.userId)) {
        return true;
      }
    }

    // Check rollout percentage
    if (flag.rolloutPercentage !== undefined && context?.userId) {
      const hash = this.hashUserId(context.userId);
      return hash % 100 < flag.rolloutPercentage;
    }

    return true;
  }

  private hashUserId(userId: string): number {
    let hash = 0;
    for (let i = 0; i < userId.length; i++) {
      hash = (hash << 5) - hash + userId.charCodeAt(i);
      hash |= 0;
    }
    return Math.abs(hash);
  }
}

// Configuration
const featureFlags = {
  "new-dashboard": {
    enabled: true,
    rolloutPercentage: 50, // 50% of users
  },
  "experimental-feature": {
    enabled: true,
    allowedUsers: ["user-123", "user-456"],
    allowedEnvironments: ["development", "staging"],
  },
  "beta-api": {
    enabled: true,
    rolloutPercentage: 10,
  },
};

const flagManager = new FeatureFlagManager(featureFlags);

// Usage
app.get("/api/dashboard", (req, res) => {
  if (
    flagManager.isEnabled("new-dashboard", {
      userId: req.user.id,
      environment: process.env.NODE_ENV,
    })
  ) {
    return res.json(getNewDashboard());
  }

  return res.json(getOldDashboard());
});
```

### LaunchDarkly Integration

```typescript
// feature-flags/launchdarkly.ts
import LaunchDarkly from "launchdarkly-node-server-sdk";

export class LaunchDarklyClient {
  private client: LaunchDarkly.LDClient;

  async initialize() {
    this.client = LaunchDarkly.init(process.env.LAUNCHDARKLY_SDK_KEY!);
    await this.client.waitForInitialization();
  }

  async isEnabled(
    flagKey: string,
    user: LaunchDarkly.LDUser,
  ): Promise<boolean> {
    return this.client.variation(flagKey, user, false);
  }

  async getVariation<T>(
    flagKey: string,
    user: LaunchDarkly.LDUser,
    defaultValue: T,
  ): Promise<T> {
    return this.client.variation(flagKey, user, defaultValue);
  }

  close() {
    this.client.close();
  }
}

// Usage
const ldClient = new LaunchDarklyClient();
await ldClient.initialize();

app.get("/api/dashboard", async (req, res) => {
  const user = {
    key: req.user.id,
    email: req.user.email,
    custom: {
      groups: req.user.groups,
    },
  };

  const showNewDashboard = await ldClient.isEnabled("new-dashboard", user);

  if (showNewDashboard) {
    return res.json(getNewDashboard());
  }

  return res.json(getOldDashboard());
});
```
