# Jest with jest-axe

## Jest with jest-axe

```typescript
// tests/components/Button.a11y.test.tsx
import React from 'react';
import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
import { Button } from '../Button';

expect.extend(toHaveNoViolations);

describe('Button Accessibility', () => {
  test('should not have accessibility violations', async () => {
    const { container } = render(<Button>Click me</Button>);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  test('icon button should have aria-label', async () => {
    const { container } = render(
      <Button aria-label="Close">
        <CloseIcon />
      </Button>
    );
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  test('disabled button should be accessible', async () => {
    const { container } = render(<Button disabled>Disabled</Button>);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });
});
```
