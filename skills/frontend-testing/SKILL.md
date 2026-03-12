---
name: frontend-testing
description: >
  Implement comprehensive frontend testing using Jest, Vitest, React Testing
  Library, and Cypress. Use when building robust test suites for UI and
  integration tests.
---

# Frontend Testing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build comprehensive test suites for frontend applications including unit tests, integration tests, and end-to-end tests with proper coverage and assertions.

## When to Use

- Component testing
- Integration testing
- End-to-end testing
- Regression prevention
- Quality assurance
- Test-driven development

## Quick Start

Minimal working example:

```typescript
// Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Button } from './Button';

describe('Button Component', () => {
  it('renders button with text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button')).toHaveTextContent('Click me');
  });

  it('calls onClick handler when clicked', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click</Button>);

    fireEvent.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('disables button when disabled prop is true', () => {
    render(<Button disabled>Click me</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });

  it('applies variant styles correctly', () => {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Jest Unit Testing (React)](references/jest-unit-testing-react.md) | Jest Unit Testing (React) |
| [React Testing Library Integration Tests](references/react-testing-library-integration-tests.md) | React Testing Library Integration Tests |
| [Vitest for Vue Testing](references/vitest-for-vue-testing.md) | Vitest for Vue Testing |
| [Cypress E2E Testing](references/cypress-e2e-testing.md) | Cypress E2E Testing |
| [Test Coverage Configuration](references/test-coverage-configuration.md) | Test Coverage Configuration |

## Best Practices

### ✅ DO

- Query elements by accessible roles and labels (`getByRole`, `getByLabelText`) rather than CSS selectors or test IDs
- Test user-visible behavior and outcomes, not internal component state or implementation details
- Use `waitFor` and `findBy` queries for async UI updates instead of arbitrary timeouts
- Isolate unit tests with mocked API responses and test integration paths separately with MSW or similar
- Write E2E tests for critical user journeys (login, checkout, form submission) that cover the full stack
- Keep tests deterministic by resetting state between runs and avoiding shared mutable fixtures

### ❌ DON'T

- Snapshot-test large component trees — they produce brittle, low-signal diffs that get blindly updated
- Couple tests to DOM structure (e.g., `div > span:nth-child(2)`) — refactors will break them without any real regression
- Mix unit and E2E concerns in the same test file; keep the test pyramid layers distinct
- Fire events directly on DOM nodes when `userEvent` from Testing Library provides more realistic interaction simulation
