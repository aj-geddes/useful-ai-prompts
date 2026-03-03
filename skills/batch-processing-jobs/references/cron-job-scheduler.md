# Cron Job Scheduler

## Cron Job Scheduler

```typescript
import cron from "node-cron";

interface ScheduledJob {
  name: string;
  schedule: string;
  handler: () => Promise<void>;
  enabled: boolean;
  lastRun?: Date;
  nextRun?: Date;
}

class JobScheduler {
  private jobs: Map<string, cron.ScheduledTask> = new Map();
  private jobConfigs: Map<string, ScheduledJob> = new Map();

  register(job: ScheduledJob): void {
    if (this.jobs.has(job.name)) {
      throw new Error(`Job ${job.name} already registered`);
    }

    // Validate cron expression
    if (!cron.validate(job.schedule)) {
      throw new Error(`Invalid cron expression: ${job.schedule}`);
    }

    const task = cron.schedule(job.schedule, async () => {
      if (!job.enabled) return;

      console.log(`Running job: ${job.name}`);
      const startTime = Date.now();

      try {
        await job.handler();

        const duration = Date.now() - startTime;
        console.log(`Job ${job.name} completed in ${duration}ms`);

        job.lastRun = new Date();
      } catch (error) {
        console.error(`Job ${job.name} failed:`, error);
      }
    });

    this.jobs.set(job.name, task);
    this.jobConfigs.set(job.name, job);

    if (job.enabled) {
      task.start();
    }
  }

  start(name: string): void {
    const task = this.jobs.get(name);
    if (!task) {
      throw new Error(`Job ${name} not found`);
    }

    task.start();

    const config = this.jobConfigs.get(name)!;
    config.enabled = true;
  }

  stop(name: string): void {
    const task = this.jobs.get(name);
    if (!task) {
      throw new Error(`Job ${name} not found`);
    }

    task.stop();

    const config = this.jobConfigs.get(name)!;
    config.enabled = false;
  }

  remove(name: string): void {
    const task = this.jobs.get(name);
    if (task) {
      task.destroy();
      this.jobs.delete(name);
      this.jobConfigs.delete(name);
    }
  }

  getJobs(): ScheduledJob[] {
    return Array.from(this.jobConfigs.values());
  }
}

// Usage
const scheduler = new JobScheduler();

// Register jobs
scheduler.register({
  name: "daily-backup",
  schedule: "0 2 * * *", // 2 AM daily
  enabled: true,
  handler: async () => {
    console.log("Running daily backup...");
    // Backup logic
  },
});

scheduler.register({
  name: "hourly-cleanup",
  schedule: "0 * * * *", // Every hour
  enabled: true,
  handler: async () => {
    console.log("Running cleanup...");
    // Cleanup logic
  },
});

scheduler.register({
  name: "weekly-report",
  schedule: "0 9 * * 1", // Monday 9 AM
  enabled: true,
  handler: async () => {
    console.log("Generating weekly report...");
    // Report generation
  },
});
```
