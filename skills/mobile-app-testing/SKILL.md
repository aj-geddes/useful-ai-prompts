---
name: mobile-app-testing
description: >
  Comprehensive mobile app testing strategies for iOS and Android. Covers unit
  tests, UI tests, integration tests, performance testing, and test automation
  with Detox, Appium, and XCTest.
---

# Mobile App Testing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive testing strategies for mobile applications including unit tests, UI tests, integration tests, and performance testing.

## When to Use

- Creating reliable mobile applications with test coverage
- Automating UI testing across iOS and Android
- Performance testing and optimization
- Integration testing with backend services
- Regression testing before releases

## Quick Start

Minimal working example:

```javascript
// Unit test with Jest
import { calculate } from "../utils/math";

describe("Math utilities", () => {
  test("should add two numbers", () => {
    expect(calculate.add(2, 3)).toBe(5);
  });

  test("should handle negative numbers", () => {
    expect(calculate.add(-2, 3)).toBe(1);
  });
});

// Component unit test
import React from "react";
import { render, screen } from "@testing-library/react-native";
import { UserProfile } from "../components/UserProfile";

describe("UserProfile Component", () => {
  test("renders user name correctly", () => {
    const mockUser = { id: "1", name: "John Doe", email: "john@example.com" };
    render(<UserProfile user={mockUser} />);

    expect(screen.getByText("John Doe")).toBeTruthy();
  });
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [React Native Testing with Jest & Detox](references/react-native-testing-with-jest-detox.md) | React Native Testing with Jest & Detox |
| [iOS Testing with XCTest](references/ios-testing-with-xctest.md) | iOS Testing with XCTest |
| [Android Testing with Espresso](references/android-testing-with-espresso.md) | Android Testing with Espresso |
| [Performance Testing](references/performance-testing.md) | Performance Testing |

## Best Practices

### ✅ DO

- Write tests for business logic first
- Use dependency injection for testability
- Mock external API calls
- Test both success and failure paths
- Automate UI testing for critical flows
- Run tests on real devices
- Measure performance on target devices
- Keep tests isolated and independent
- Use meaningful test names
- Maintain >80% code coverage

### ❌ DON'T

- Skip testing UI-critical flows
- Use hardcoded test data
- Ignore performance regressions
- Test implementation details
- Make tests flaky or unreliable
- Skip testing on actual devices
- Ignore accessibility testing
- Create interdependent tests
- Test without mocking APIs
- Deploy untested code
