# Environment Variables

## Environment Variables

```typescript
// env-utils.ts
export class EnvUtils {
  // Get environment variable with fallback
  static get(key: string, defaultValue?: string): string | undefined {
    return process.env[key] || defaultValue;
  }

  // Get PATH separator (: on Unix, ; on Windows)
  static get pathSeparator(): string {
    return process.platform === "win32" ? ";" : ":";
  }

  // Split PATH into array
  static getPaths(): string[] {
    const pathVar = process.env.PATH || "";
    return pathVar.split(this.pathSeparator);
  }

  // Get common paths
  static get home(): string {
    return process.env.HOME || process.env.USERPROFILE || "";
  }

  static get user(): string {
    return process.env.USER || process.env.USERNAME || "";
  }

  // Check if running in CI
  static get isCI(): boolean {
    return !!(
      process.env.CI ||
      process.env.CONTINUOUS_INTEGRATION ||
      process.env.GITHUB_ACTIONS ||
      process.env.GITLAB_CI
    );
  }
}
```
