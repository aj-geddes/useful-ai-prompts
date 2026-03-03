# Test Structure (AAA Pattern)

## Test Structure (AAA Pattern)

```javascript
// Jest/JavaScript example
describe("UserService", () => {
  describe("createUser", () => {
    it("should create user with valid data", async () => {
      // Arrange - Set up test data and dependencies
      const userData = {
        email: "john@example.com",
        firstName: "John",
        lastName: "Doe",
      };
      const mockDatabase = createMockDatabase();
      const service = new UserService(mockDatabase);

      // Act - Execute the function being tested
      const result = await service.createUser(userData);

      // Assert - Verify the outcome
      expect(result.id).toBeDefined();
      expect(result.email).toBe("john@example.com");
      expect(mockDatabase.save).toHaveBeenCalledWith(
        expect.objectContaining(userData),
      );
    });
  });
});
```
