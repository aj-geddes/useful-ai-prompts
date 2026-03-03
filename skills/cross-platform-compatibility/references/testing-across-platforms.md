# Testing Across Platforms

## Testing Across Platforms

### GitHub Actions Matrix

```yaml
# .github/workflows/test.yml
name: Cross-Platform Tests

on: [push, pull_request]

jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node-version: [16, 18, 20]

    runs-on: ${{ matrix.os }}

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

      - name: Platform-specific tests
        if: runner.os == 'Windows'
        run: npm run test:windows

      - name: Platform-specific tests
        if: runner.os == 'macOS'
        run: npm run test:macos

      - name: Platform-specific tests
        if: runner.os == 'Linux'
        run: npm run test:linux
```

### Platform-Specific Tests

```typescript
// tests/platform.test.ts
import { Platform } from "../src/platform-utils";

describe("Platform-specific tests", () => {
  describe("File paths", () => {
    it("should handle paths correctly", () => {
      const configPath = path.join(os.homedir(), "config.json");

      if (Platform.isWindows) {
        expect(configPath).toMatch(/^[A-Z]:\\/);
      } else {
        expect(configPath).toMatch(/^\//);
      }
    });
  });

  describe.skipIf(Platform.isWindows)("Unix-only tests", () => {
    it("should work with symlinks", () => {
      // Symlink tests
    });

    it("should handle file permissions", () => {
      // Permission tests
    });
  });

  describe.skipIf(!Platform.isWindows)("Windows-only tests", () => {
    it("should work with UNC paths", () => {
      // UNC path tests
    });

    it("should handle drive letters", () => {
      // Drive letter tests
    });
  });
});
```
