# Bull Queue (Node.js)

## Bull Queue (Node.js)

```typescript
import Queue from "bull";
import { v4 as uuidv4 } from "uuid";

interface JobData {
  id: string;
  type: string;
  payload: any;
  userId?: string;
  metadata?: Record<string, any>;
}

interface JobResult {
  success: boolean;
  data?: any;
  error?: string;
  processedAt: number;
  duration: number;
}

class BatchProcessor {
  private queue: Queue.Queue<JobData>;
  private resultQueue: Queue.Queue<JobResult>;

  constructor(redisUrl: string) {
    // Main processing queue
    this.queue = new Queue("batch-jobs", redisUrl, {
      defaultJobOptions: {
        attempts: 3,
        backoff: {
          type: "exponential",
          delay: 2000,
        },
        removeOnComplete: 1000,
        removeOnFail: 5000,
        timeout: 300000, // 5 minutes
      },
      settings: {
        maxStalledCount: 2,
        stalledInterval: 30000,
      },
    });

    // Results queue
    this.resultQueue = new Queue("batch-results", redisUrl);

    this.setupProcessors();
    this.setupEvents();
  }

  private setupProcessors(): void {
    // Data processing job
    this.queue.process("process-data", 10, async (job) => {
      const startTime = Date.now();
      const { payload } = job.data;

      job.log(`Processing ${payload.items?.length || 0} items`);

      try {
        // Update progress
        await job.progress(0);

        const results = await this.processDataBatch(payload.items, (progress) =>
          job.progress(progress),
        );

        const duration = Date.now() - startTime;

        return {
          success: true,
          data: results,
          processedAt: Date.now(),
          duration,
        };
      } catch (error: any) {
        const duration = Date.now() - startTime;
        throw new Error(`Processing failed: ${error.message}`);
      }
    });

    // Report generation job
    this.queue.process("generate-report", 2, async (job) => {
      const { payload } = job.data;

      const report = await this.generateReport(
        payload.type,
        payload.filters,
        payload.format,
      );

      return {
        success: true,
        data: {
          reportId: uuidv4(),
          url: report.url,
          size: report.size,
        },
        processedAt: Date.now(),
        duration: 0,
      };
    });

    // Email batch job
    this.queue.process("send-emails", 5, async (job) => {
      const { payload } = job.data;
      const { recipients, template, data } = payload;

      const results = await this.sendEmailBatch(recipients, template, data);

      return {
        success: true,
        data: {
          sent: results.successful,
          failed: results.failed,
        },
        processedAt: Date.now(),
        duration: 0,
      };
    });
  }

  private setupEvents(): void {
    this.queue.on("completed", (job, result) => {
      console.log(`Job ${job.id} completed:`, result);

      // Store result
      this.resultQueue.add({
        jobId: job.id,
        ...result,
      });
    });

    this.queue.on("failed", (job, error) => {
      console.error(`Job ${job?.id} failed:`, error.message);

      // Store failure
      this.resultQueue.add({
        jobId: job?.id,
        success: false,
        error: error.message,
        processedAt: Date.now(),
        duration: 0,
      });
    });

    this.queue.on("progress", (job, progress) => {
      console.log(`Job ${job.id} progress: ${progress}%`);
    });

    this.queue.on("stalled", (job) => {
      console.warn(`Job ${job.id} stalled`);
    });
  }

  async addJob(
    type: string,
    payload: any,
    options?: Queue.JobOptions,
  ): Promise<Queue.Job<JobData>> {
    const jobData: JobData = {
      id: uuidv4(),
      type,
      payload,
      metadata: {
        createdAt: Date.now(),
      },
    };

    return this.queue.add(type, jobData, options);
  }

  async addBulkJobs(
    jobs: Array<{ type: string; payload: any; options?: Queue.JobOptions }>,
  ): Promise<Queue.Job<JobData>[]> {
    const bulkData = jobs.map(({ type, payload, options }) => ({
      name: type,
      data: {
        id: uuidv4(),
        type,
        payload,
        metadata: { createdAt: Date.now() },
      },
      opts: options || {},
    }));

    return this.queue.addBulk(bulkData);
  }

  async scheduleJob(
    type: string,
    payload: any,
    cronExpression: string,
  ): Promise<Queue.Job<JobData>> {
    return this.addJob(type, payload, {
      repeat: {
        cron: cronExpression,
      },
    });
  }

  private async processDataBatch(
    items: any[],
    onProgress: (progress: number) => Promise<void>,
  ): Promise<any[]> {
    const results = [];
    const total = items.length;

    for (let i = 0; i < total; i++) {
      const result = await this.processItem(items[i]);
      results.push(result);

      // Update progress
      const progress = Math.round(((i + 1) / total) * 100);
      await onProgress(progress);
    }

    return results;
  }

  private async processItem(item: any): Promise<any> {
    // Simulate processing
    await new Promise((resolve) => setTimeout(resolve, 100));
    return { ...item, processed: true };
  }

  private async generateReport(
    type: string,
    filters: any,
    format: string,
  ): Promise<any> {
    // Simulate report generation
    return {
      url: `https://cdn.example.com/reports/${uuidv4()}.${format}`,
      size: 1024 * 1024,
    };
  }

  private async sendEmailBatch(
    recipients: string[],
    template: string,
    data: any,
  ): Promise<{ successful: number; failed: number }> {
    // Simulate email sending
    return {
      successful: recipients.length,
      failed: 0,
    };
  }

  async getJobStatus(jobId: string): Promise<any> {
    const job = await this.queue.getJob(jobId);
    if (!job) return null;

    const state = await job.getState();
    const logs = await this.queue.getJobLogs(jobId);

    return {
      id: job.id,
      name: job.name,
      data: job.data,
      state,
      progress: job.progress(),
      attempts: job.attemptsMade,
      failedReason: job.failedReason,
      finishedOn: job.finishedOn,
      processedOn: job.processedOn,
      logs: logs.logs,
    };
  }

  async getQueueStats(): Promise<any> {
    const [waiting, active, completed, failed, delayed, paused] =
      await Promise.all([
        this.queue.getWaitingCount(),
        this.queue.getActiveCount(),
        this.queue.getCompletedCount(),
        this.queue.getFailedCount(),
        this.queue.getDelayedCount(),
        this.queue.getPausedCount(),
      ]);

    return {
      waiting,
      active,
      completed,
      failed,
      delayed,
      paused,
    };
  }

  async pause(): Promise<void> {
    await this.queue.pause();
  }

  async resume(): Promise<void> {
    await this.queue.resume();
  }

  async clean(grace: number = 0): Promise<void> {
    await this.queue.clean(grace, "completed");
    await this.queue.clean(grace, "failed");
  }

  async close(): Promise<void> {
    await this.queue.close();
    await this.resultQueue.close();
  }
}

// Usage
const processor = new BatchProcessor("redis://localhost:6379");

// Add single job
const job = await processor.addJob("process-data", {
  items: [{ id: 1 }, { id: 2 }, { id: 3 }],
});

// Add bulk jobs
await processor.addBulkJobs([
  {
    type: "process-data",
    payload: {
      items: [
        /* ... */
      ],
    },
  },
  {
    type: "generate-report",
    payload: { type: "sales", format: "pdf" },
  },
]);

// Schedule recurring job
await processor.scheduleJob(
  "generate-report",
  { type: "daily-summary" },
  "0 0 * * *", // Daily at midnight
);

// Check status
const status = await processor.getJobStatus(job.id!);
console.log("Job status:", status);

// Get queue stats
const stats = await processor.getQueueStats();
console.log("Queue stats:", stats);
```
