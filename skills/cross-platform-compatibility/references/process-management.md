# Process Management

## Process Management

```typescript
// process-utils.ts
import { spawn, ChildProcess } from "child_process";

export class ProcessUtils {
  // Kill process by PID with platform-specific signal
  static kill(pid: number, signal?: string): void {
    if (process.platform === "win32") {
      // Windows doesn't support signals, use taskkill
      spawn("taskkill", ["/pid", pid.toString(), "/f", "/t"]);
    } else {
      process.kill(pid, signal || "SIGTERM");
    }
  }

  // Spawn process with platform-specific handling
  static spawnCommand(command: string, args: string[] = []): ChildProcess {
    if (process.platform === "win32") {
      // Windows requires cmd.exe to run commands
      return spawn("cmd", ["/c", command, ...args], {
        stdio: "inherit",
        shell: true,
      });
    }

    return spawn(command, args, {
      stdio: "inherit",
      shell: true,
    });
  }

  // Find process by name
  static async findProcess(name: string): Promise<number[]> {
    if (process.platform === "win32") {
      const { stdout } = await execAsync(`tasklist /FI "IMAGENAME eq ${name}"`);
      // Parse Windows tasklist output
      const pids: number[] = [];
      const lines = stdout.split("\n");
      for (const line of lines) {
        const match = line.match(/\s+(\d+)\s+/);
        if (match) pids.push(parseInt(match[1]));
      }
      return pids;
    } else {
      const { stdout } = await execAsync(`pgrep ${name}`);
      return stdout.split("\n").filter(Boolean).map(Number);
    }
  }
}
```
