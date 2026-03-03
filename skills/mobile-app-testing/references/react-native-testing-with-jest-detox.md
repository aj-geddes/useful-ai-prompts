# React Native Testing with Jest & Detox

## React Native Testing with Jest & Detox

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

  test("handles missing user gracefully", () => {
    render(<UserProfile user={null} />);
    expect(screen.getByText(/no user data/i)).toBeTruthy();
  });
});

// E2E Testing with Detox
describe("Login Flow E2E Test", () => {
  beforeAll(async () => {
    await device.launchApp();
  });

  beforeEach(async () => {
    await device.reloadReactNative();
  });

  it("should login successfully with valid credentials", async () => {
    await waitFor(element(by.id("emailInput")))
      .toBeVisible()
      .withTimeout(5000);

    await element(by.id("emailInput")).typeText("user@example.com");
    await element(by.id("passwordInput")).typeText("password123");
    await element(by.id("loginButton")).multiTap();

    await waitFor(element(by.text("Home Feed")))
      .toBeVisible()
      .withTimeout(5000);
  });

  it("should show error with invalid credentials", async () => {
    await element(by.id("emailInput")).typeText("invalid@example.com");
    await element(by.id("passwordInput")).typeText("wrongpass");
    await element(by.id("loginButton")).multiTap();

    await waitFor(element(by.text(/invalid credentials/i)))
      .toBeVisible()
      .withTimeout(5000);
  });

  it("should navigate between tabs", async () => {
    await element(by.id("profileTab")).tap();
    await waitFor(element(by.text("Profile")))
      .toBeVisible()
      .withTimeout(2000);

    await element(by.id("homeTab")).tap();
    await waitFor(element(by.text("Home Feed")))
      .toBeVisible()
      .withTimeout(2000);
  });
});
```
