# Chrome DevTools CPU Profile

## Chrome DevTools CPU Profile

```typescript
import inspector from "inspector";
import fs from "fs";

class CPUProfiler {
  private session: inspector.Session | null = null;

  start(): void {
    this.session = new inspector.Session();
    this.session.connect();

    this.session.post("Profiler.enable");
    this.session.post("Profiler.start");

    console.log("CPU profiling started");
  }

  async stop(outputFile: string): Promise<void> {
    if (!this.session) return;

    this.session.post("Profiler.stop", (err, { profile }) => {
      if (err) {
        console.error("Profiling error:", err);
        return;
      }

      fs.writeFileSync(outputFile, JSON.stringify(profile));
      console.log(`Profile saved to ${outputFile}`);

      this.session!.disconnect();
      this.session = null;
    });
  }
}

// Usage
const cpuProfiler = new CPUProfiler();

// Start profiling
cpuProfiler.start();

// Run code to profile
await runExpensiveOperation();

// Stop and save
await cpuProfiler.stop("./profile.cpuprofile");
```
