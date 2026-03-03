# Test Selection Strategy

## Test Selection Strategy

```typescript
// scripts/run-affected-tests.ts
import { execSync } from "child_process";
import * as fs from "fs";

class AffectedTestRunner {
  getAffectedFiles(): string[] {
    // Get changed files from git
    const output = execSync("git diff --name-only HEAD~1", {
      encoding: "utf-8",
    });
    return output.split("\n").filter(Boolean);
  }

  getTestsForFiles(files: string[]): Set<string> {
    const tests = new Set<string>();

    for (const file of files) {
      if (file.endsWith(".test.ts") || file.endsWith(".spec.ts")) {
        // File is already a test
        tests.add(file);
      } else if (file.endsWith(".ts")) {
        // Find associated test file
        const testFile = file.replace(".ts", ".test.ts");
        if (fs.existsSync(testFile)) {
          tests.add(testFile);
        }

        // Check for integration tests that import this file
        const integrationTests = execSync(
          `grep -r "from.*${file}" tests/integration/*.test.ts`,
          { encoding: "utf-8" },
        ).split("\n");

        integrationTests.forEach((line) => {
          const match = line.match(/^([^:]+):/);
          if (match) tests.add(match[1]);
        });
      }
    }

    return tests;
  }

  run() {
    const affectedFiles = this.getAffectedFiles();
    console.log("Affected files:", affectedFiles);

    const testsToRun = this.getTestsForFiles(affectedFiles);
    console.log("Tests to run:", testsToRun);

    if (testsToRun.size === 0) {
      console.log("No tests affected");
      return;
    }

    // Run only affected tests
    const testPattern = Array.from(testsToRun).join("|");
    execSync(`npm test -- --testPathPattern="${testPattern}"`, {
      stdio: "inherit",
    });
  }
}

new AffectedTestRunner().run();
```
