# Shell Commands

## Shell Commands

```typescript
// shell-utils.ts
import { exec } from "child_process";
import { promisify } from "util";

const execAsync = promisify(exec);

export class ShellUtils {
  // Execute command with platform-specific handling
  static async execute(command: string): Promise<string> {
    try {
      const { stdout, stderr } = await execAsync(command, {
        shell: this.getShell(),
      });
      if (stderr) console.error(stderr);
      return stdout.trim();
    } catch (error) {
      throw new Error(`Command failed: ${error.message}`);
    }
  }

  // Get platform-specific shell
  static getShell(): string {
    if (process.platform === "win32") {
      return "cmd.exe";
    }
    return process.env.SHELL || "/bin/sh";
  }

  // Platform-specific commands
  static async listFiles(directory: string): Promise<string> {
    if (process.platform === "win32") {
      return this.execute(`dir "${directory}"`);
    }
    return this.execute(`ls -la "${directory}"`);
  }

  static async clearScreen(): Promise<void> {
    if (process.platform === "win32") {
      await this.execute("cls");
    } else {
      await this.execute("clear");
    }
  }

  static async openFile(filepath: string): Promise<void> {
    if (process.platform === "win32") {
      await this.execute(`start "" "${filepath}"`);
    } else if (process.platform === "darwin") {
      await this.execute(`open "${filepath}"`);
    } else {
      await this.execute(`xdg-open "${filepath}"`);
    }
  }
}
```
