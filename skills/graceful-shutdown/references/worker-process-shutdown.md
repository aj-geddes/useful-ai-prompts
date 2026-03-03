# Worker Process Shutdown

## Worker Process Shutdown

```typescript
import Queue from "bull";

class WorkerShutdown {
  private queue: Queue.Queue;
  private isProcessing = new Map<string, boolean>();

  constructor(queue: Queue.Queue) {
    this.queue = queue;
    this.setupWorker();
    this.setupShutdownHandlers();
  }

  private setupWorker(): void {
    this.queue.process("task", 5, async (job) => {
      const jobId = job.id!.toString();
      this.isProcessing.set(jobId, true);

      try {
        console.log(`Processing job ${jobId}`);
        await this.processJob(job);
        console.log(`Completed job ${jobId}`);
      } finally {
        this.isProcessing.delete(jobId);
      }
    });
  }

  private async processJob(job: Queue.Job): Promise<void> {
    // Job processing logic
    await new Promise((resolve) => setTimeout(resolve, 5000));
  }

  private setupShutdownHandlers(): void {
    process.on("SIGTERM", () => {
      console.log("SIGTERM received, shutting down worker...");
      this.shutdownWorker();
    });
  }

  private async shutdownWorker(): Promise<void> {
    console.log("Pausing queue...");
    await this.queue.pause(true, true);

    console.log(`Waiting for ${this.isProcessing.size} jobs to complete...`);

    // Wait for current jobs to finish
    const checkInterval = 500;
    const maxWait = 30000;
    let waited = 0;

    while (this.isProcessing.size > 0 && waited < maxWait) {
      await new Promise((resolve) => setTimeout(resolve, checkInterval));
      waited += checkInterval;

      if (waited % 5000 === 0) {
        console.log(`Still processing ${this.isProcessing.size} jobs...`);
      }
    }

    if (this.isProcessing.size > 0) {
      console.warn(
        `Forcing shutdown with ${this.isProcessing.size} jobs remaining`,
      );
    }

    console.log("Closing queue...");
    await this.queue.close();

    console.log("Worker shutdown complete");
    process.exit(0);
  }
}
```
