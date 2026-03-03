# Accessibility Testing

## Accessibility Testing

```typescript
// jest-axe integration test
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
import { Button } from './Button';

expect.extend(toHaveNoViolations);

describe('Button Accessibility', () => {
  it('should not have accessibility violations', async () => {
    const { container } = render(
      <Button>Click me</Button>
    );

    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  it('should have proper ARIA labels', async () => {
    const { container } = render(
      <Button aria-label="Close dialog">×</Button>
    );

    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });
});

// Accessibility Checker Hook
const useAccessibilityChecker = () => {
  useEffect(() => {
    // Run accessibility checks in development
    if (process.env.NODE_ENV === 'development') {
      import('axe-core').then(axe => {
        axe.run((error, results) => {
          if (results.violations.length > 0) {
            console.warn('Accessibility violations found:', results.violations);
          }
        });
      });
    }
  }, []);
};
```
