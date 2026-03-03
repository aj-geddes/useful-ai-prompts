# Security Headers Testing

## Security Headers Testing

```typescript
// tests/security/headers.test.ts
test.describe("Security Headers", () => {
  test("should have required security headers", async () => {
    const response = await request(app).get("/");

    expect(response.headers).toMatchObject({
      "x-frame-options": "DENY",
      "x-content-type-options": "nosniff",
      "x-xss-protection": "1; mode=block",
      "strict-transport-security": expect.stringMatching(/max-age=/),
      "content-security-policy": expect.any(String),
    });
  });

  test("should not expose sensitive headers", async () => {
    const response = await request(app).get("/");

    expect(response.headers["x-powered-by"]).toBeUndefined();
    expect(response.headers["server"]).not.toMatch(/express|nginx|apache/i);
  });

  test("CSP should prevent inline scripts", async ({ page }) => {
    await page.goto("/");

    const cspViolations = [];
    page.on("console", (msg) => {
      if (
        msg.type() === "error" &&
        msg.text().includes("Content Security Policy")
      ) {
        cspViolations.push(msg.text());
      }
    });

    // Try to inject inline script
    await page.evaluate(() => {
      const script = document.createElement("script");
      script.textContent = 'alert("test")';
      document.body.appendChild(script);
    });

    expect(cspViolations.length).toBeGreaterThan(0);
  });
});
```
