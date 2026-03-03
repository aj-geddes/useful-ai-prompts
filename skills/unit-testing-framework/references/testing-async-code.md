# Testing Async Code

## Testing Async Code

```javascript
// Jest async/await
it("should fetch user data", async () => {
  const user = await fetchUser("123");
  expect(user.id).toBe("123");
});

// Testing promises
it("should resolve with user data", () => {
  return fetchUser("123").then((user) => {
    expect(user.id).toBe("123");
  });
});

// Testing rejection
it("should reject with error for invalid ID", async () => {
  await expect(fetchUser("invalid")).rejects.toThrow("User not found");
});
```


## Test Coverage

```bash
# JavaScript (Jest)
npm test -- --coverage

# Python (pytest with coverage)
pytest --cov=src --cov-report=html

# Java (Maven)
mvn test jacoco:report
```

**Coverage Goals:**

- **Statements**: 80%+ covered
- **Branches**: 75%+ covered
- **Functions**: 85%+ covered
- **Lines**: 80%+ covered
