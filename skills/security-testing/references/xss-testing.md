# XSS Testing

## XSS Testing

```javascript
// tests/security/xss.test.js
describe("XSS Protection", () => {
  const xssPayloads = [
    '<script>alert("XSS")</script>',
    '<img src=x onerror=alert("XSS")>',
    '<svg onload=alert("XSS")>',
    'javascript:alert("XSS")',
    "<iframe src=\"javascript:alert('XSS')\">",
    '<body onload=alert("XSS")>',
  ];

  test("user input should be escaped", async () => {
    const { page } = await browser.newPage();

    for (const payload of xssPayloads) {
      await page.goto("/");

      // Submit comment with XSS payload
      await page.fill('[name="comment"]', payload);
      await page.click('[type="submit"]');

      // Wait for comment to appear
      await page.waitForSelector(".comment");

      // Check that script was not executed
      const dialogAppeared = await page.evaluate(() => {
        return window.xssDetected || false;
      });

      expect(dialogAppeared).toBe(false);

      // Check HTML is escaped
      const commentHTML = await page.$eval(".comment", (el) => el.innerHTML);
      expect(commentHTML).not.toContain("<script>");
      expect(commentHTML).toContain("&lt;script&gt;");
    }
  });

  test("URLs should be validated", async () => {
    const response = await request(app)
      .post("/api/links")
      .send({ url: 'javascript:alert("XSS")' })
      .expect(400);

    expect(response.body.error).toMatch(/invalid url/i);
  });
});
```
