# Establish Safety Net

## Establish Safety Net

Before refactoring, ensure you have comprehensive tests:

```javascript
// Add characterization tests to lock in current behavior
describe("LegacyFeature", () => {
  it("should preserve existing behavior during refactoring", () => {
    // Test current implementation behavior
    const input = {
      /* realistic test data */
    };
    const result = legacyFunction(input);

    // Document expected output
    expect(result).toEqual({
      /* current actual output */
    });
  });
});
```

**Testing Strategy:**

- Add unit tests for critical paths
- Create integration tests for component interactions
- Document edge cases and error scenarios
- Set up test coverage monitoring
- Run tests before each refactoring step
