# File Permissions

## File Permissions

```typescript
// permissions.ts
import fs from "fs";
import path from "path";

export class FilePermissions {
  // Make file executable (Unix only)
  static makeExecutable(filepath: string): void {
    if (process.platform !== "win32") {
      fs.chmodSync(filepath, 0o755);
    }
  }

  // Check if file is executable
  static isExecutable(filepath: string): boolean {
    if (process.platform === "win32") {
      // On Windows, check file extension
      const ext = path.extname(filepath).toLowerCase();
      return [".exe", ".bat", ".cmd", ".com"].includes(ext);
    }

    try {
      fs.accessSync(filepath, fs.constants.X_OK);
      return true;
    } catch {
      return false;
    }
  }

  // Create file with specific permissions (Unix)
  static createWithPermissions(
    filepath: string,
    content: string,
    mode: number = 0o644,
  ): void {
    fs.writeFileSync(filepath, content, { mode });
  }
}
```
