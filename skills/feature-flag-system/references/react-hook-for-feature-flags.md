# React Hook for Feature Flags

## React Hook for Feature Flags

```typescript
import { createContext, useContext, ReactNode } from 'react';

interface FeatureFlagContextType {
  isEnabled: (key: string) => boolean;
  getVariant: (key: string) => any;
}

const FeatureFlagContext = createContext<FeatureFlagContextType | null>(null);

export function FeatureFlagProvider({
  children,
  userId,
  attributes
}: {
  children: ReactNode;
  userId?: string;
  attributes?: Record<string, any>;
}) {
  const flagService = new FeatureFlagService();

  const context: FeatureFlagContextType = {
    isEnabled: (key: string) => {
      return flagService.isEnabled(key, { userId, attributes });
    },
    getVariant: (key: string) => {
      return flagService.getVariant(key, { userId, attributes });
    }
  };

  return (
    <FeatureFlagContext.Provider value={context}>
      {children}
    </FeatureFlagContext.Provider>
  );
}

export function useFeatureFlag(key: string): boolean {
  const context = useContext(FeatureFlagContext);
  if (!context) {
    throw new Error('useFeatureFlag must be used within FeatureFlagProvider');
  }
  return context.isEnabled(key);
}

export function useFeatureVariant(key: string): any {
  const context = useContext(FeatureFlagContext);
  if (!context) {
    throw new Error('useFeatureVariant must be used within FeatureFlagProvider');
  }
  return context.getVariant(key);
}

// Feature component wrapper
export function Feature({
  flag,
  fallback = null,
  children
}: {
  flag: string;
  fallback?: ReactNode;
  children: ReactNode;
}) {
  const isEnabled = useFeatureFlag(flag);

  return isEnabled ? <>{children}</> : <>{fallback}</>;
}

// Usage in components
function Dashboard() {
  const hasNewDashboard = useFeatureFlag('new-dashboard');
  const theme = useFeatureVariant('theme-experiment');

  return (
    <div>
      {hasNewDashboard ? <NewDashboard /> : <OldDashboard />}

      <Feature flag="premium-features" fallback={<UpgradePrompt />}>
        <PremiumContent />
      </Feature>

      <div style={{ backgroundColor: theme?.backgroundColor }}>
        Content with experiment theme
      </div>
    </div>
  );
}
```
