---
name: feature-flag-system
description: >
  Implement feature flags (toggles) for controlled feature rollouts, A/B
  testing, canary deployments, and kill switches. Use when deploying new
  features gradually, testing in production, or managing feature lifecycles.
---

# Feature Flag System

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement feature flags to decouple deployment from release, enable gradual rollouts, A/B testing, and provide emergency kill switches.

## When to Use

- Gradual feature rollouts
- A/B testing and experiments
- Canary deployments
- Beta features for specific users
- Emergency kill switches
- Trunk-based development
- Dark launching
- Operational flags (maintenance mode)
- User-specific features

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Feature Flag Service (TypeScript)](references/feature-flag-service-typescript.md) | Feature Flag Service (TypeScript) |
| [React Hook for Feature Flags](references/react-hook-for-feature-flags.md) | React Hook for Feature Flags |
| [Feature Flag with Analytics](references/feature-flag-with-analytics.md) | Feature Flag with Analytics |
| [LaunchDarkly-Style SDK](references/launchdarkly-style-sdk.md) | LaunchDarkly-Style SDK |
| [Admin UI for Feature Flags](references/admin-ui-for-feature-flags.md) | Admin UI for Feature Flags |

## Best Practices

### ✅ DO

- Use descriptive flag names
- Document flag purpose and lifecycle
- Implement gradual rollouts
- Track flag evaluations
- Clean up old flags regularly
- Use feature flags for experiments
- Implement kill switches for critical features
- Test both enabled and disabled states
- Use consistent hashing for stable rollouts
- Provide admin UI for non-technical users

### ❌ DON'T

- Use flags for permanent configuration
- Accumulate technical debt with old flags
- Skip flag cleanup
- Make flags too granular
- Hard-code flag checks everywhere
- Skip analytics and monitoring
