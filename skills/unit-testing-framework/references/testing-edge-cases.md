# Testing Edge Cases

## Testing Edge Cases

```javascript
describe("Edge Cases", () => {
  it("should handle null input", () => {
    expect(processData(null)).toBeNull();
  });

  it("should handle undefined input", () => {
    expect(processData(undefined)).toBeUndefined();
  });

  it("should handle empty string", () => {
    expect(processData("")).toBe("");
  });

  it("should handle empty array", () => {
    expect(processData([])).toEqual([]);
  });

  it("should handle large numbers", () => {
    expect(calculate(Number.MAX_SAFE_INTEGER)).toBeDefined();
  });

  it("should handle special characters", () => {
    expect(sanitize('<script>alert("xss")</script>')).toBe(
      "&lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt;",
    );
  });
});
```
