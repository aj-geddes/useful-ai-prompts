# Advanced Mocking Patterns

## Advanced Mocking Patterns

```typescript
// Mock timers
describe("Scheduled Tasks", () => {
  beforeEach(() => {
    jest.useFakeTimers();
  });

  afterEach(() => {
    jest.useRealTimers();
  });

  it("should execute task after delay", () => {
    const callback = jest.fn();
    const scheduler = new TaskScheduler();

    scheduler.scheduleTask(callback, 5000);

    expect(callback).not.toHaveBeenCalled();

    jest.advanceTimersByTime(5000);

    expect(callback).toHaveBeenCalledTimes(1);
  });
});

// Partial mocking
describe("UserService with partial mocking", () => {
  it("should use real method for validation, mock for DB", async () => {
    const userService = new UserService();

    // Spy on real object
    const saveSpy = jest
      .spyOn(userService.repository, "save")
      .mockResolvedValue({ id: "123" });

    // Real validation method is used
    await expect(userService.createUser({ email: "invalid" })).rejects.toThrow(
      "Invalid email",
    );

    expect(saveSpy).not.toHaveBeenCalled();

    // Valid data uses mocked save
    await userService.createUser({ email: "valid@example.com" });
    expect(saveSpy).toHaveBeenCalled();
  });
});
```
