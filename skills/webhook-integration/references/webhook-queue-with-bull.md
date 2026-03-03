# Webhook Queue with Bull

## Webhook Queue with Bull

```typescript
import Queue from "bull";
import axios from "axios";

interface WebhookJob {
  endpoint: WebhookEndpoint;
  event: WebhookEvent;
}

class WebhookQueue {
  private queue: Queue.Queue<WebhookJob>;

  constructor(redisUrl: string) {
    this.queue = new Queue("webhooks", redisUrl, {
      defaultJobOptions: {
        attempts: 3,
        backoff: {
          type: "exponential",
          delay: 2000,
        },
        removeOnComplete: 100,
        removeOnFail: 1000,
      },
    });

    this.setupProcessors();
    this.setupEventHandlers();
  }

  private setupProcessors(): void {
    // Process webhook deliveries
    this.queue.process("delivery", 5, async (job) => {
      const { endpoint, event } = job.data;

      job.log(`Delivering webhook to ${endpoint.url}`);

      const sender = new WebhookSender();
      const attempts = await sender.send(endpoint, event);

      return {
        endpoint: endpoint.url,
        attempts,
        success: true,
      };
    });
  }

  private setupEventHandlers(): void {
    this.queue.on("completed", (job, result) => {
      console.log(`Webhook delivered: ${job.id}`, result);
    });

    this.queue.on("failed", (job, err) => {
      console.error(`Webhook delivery failed: ${job?.id}`, err);
    });

    this.queue.on("stalled", (job) => {
      console.warn(`Webhook delivery stalled: ${job.id}`);
    });
  }

  async enqueue(
    endpoint: WebhookEndpoint,
    event: WebhookEvent,
    options?: Queue.JobOptions,
  ): Promise<Queue.Job<WebhookJob>> {
    return this.queue.add(
      "delivery",
      { endpoint, event },
      {
        jobId: `${event.id}-${endpoint.url}`,
        ...options,
      },
    );
  }

  async enqueueBatch(
    endpoints: WebhookEndpoint[],
    event: WebhookEvent,
  ): Promise<Queue.Job<WebhookJob>[]> {
    const jobs = endpoints.map((endpoint) => ({
      name: "delivery",
      data: { endpoint, event },
      opts: {
        jobId: `${event.id}-${endpoint.url}`,
      },
    }));

    return this.queue.addBulk(jobs);
  }

  async getJobStatus(jobId: string): Promise<any> {
    const job = await this.queue.getJob(jobId);
    if (!job) return null;

    return {
      id: job.id,
      state: await job.getState(),
      progress: job.progress(),
      attempts: job.attemptsMade,
      failedReason: job.failedReason,
      finishedOn: job.finishedOn,
      processedOn: job.processedOn,
    };
  }

  async retryFailed(jobId: string): Promise<void> {
    const job = await this.queue.getJob(jobId);
    if (!job) {
      throw new Error("Job not found");
    }

    await job.retry();
  }

  async pause(): Promise<void> {
    await this.queue.pause();
  }

  async resume(): Promise<void> {
    await this.queue.resume();
  }

  async close(): Promise<void> {
    await this.queue.close();
  }
}

// Usage
const webhookQueue = new WebhookQueue("redis://localhost:6379");

// Enqueue single webhook
await webhookQueue.enqueue(endpoint, event, {
  delay: 1000, // Delay 1 second
  priority: 1,
});

// Enqueue to multiple endpoints
await webhookQueue.enqueueBatch(endpoints, event);

// Check job status
const status = await webhookQueue.getJobStatus("job-id");
console.log("Job status:", status);
```
