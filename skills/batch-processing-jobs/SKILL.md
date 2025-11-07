---
name: batch-processing-jobs
description: Implement robust batch processing systems with job queues, schedulers, background tasks, and distributed workers. Use when processing large datasets, scheduled tasks, async operations, or resource-intensive computations.
---

# Batch Processing Jobs

## Overview

Implement scalable batch processing systems for handling large-scale data processing, scheduled tasks, and async operations efficiently.

## When to Use

- Processing large datasets
- Scheduled report generation
- Email/notification campaigns
- Data imports and exports
- Image/video processing
- ETL pipelines
- Cleanup and maintenance tasks
- Long-running computations
- Bulk data updates

## Architecture Patterns

```
┌─────────────┐      ┌─────────────┐      ┌──────────┐
│  Producer   │─────▶│    Queue    │─────▶│  Worker  │
└─────────────┘      └─────────────┘      └──────────┘
                           │                     │
                           │                     ▼
                           │              ┌──────────┐
                           └─────────────▶│  Result  │
                                         │  Storage │
                                         └──────────┘
```

## Implementation Examples

### 1. **Bull Queue (Node.js)**

```typescript
import Queue from 'bull';
import { v4 as uuidv4 } from 'uuid';

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
    this.queue = new Queue('batch-jobs', redisUrl, {
      defaultJobOptions: {
        attempts: 3,
        backoff: {
          type: 'exponential',
          delay: 2000
        },
        removeOnComplete: 1000,
        removeOnFail: 5000,
        timeout: 300000 // 5 minutes
      },
      settings: {
        maxStalledCount: 2,
        stalledInterval: 30000
      }
    });

    // Results queue
    this.resultQueue = new Queue('batch-results', redisUrl);

    this.setupProcessors();
    this.setupEvents();
  }

  private setupProcessors(): void {
    // Data processing job
    this.queue.process('process-data', 10, async (job) => {
      const startTime = Date.now();
      const { payload } = job.data;

      job.log(`Processing ${payload.items?.length || 0} items`);

      try {
        // Update progress
        await job.progress(0);

        const results = await this.processDataBatch(
          payload.items,
          (progress) => job.progress(progress)
        );

        const duration = Date.now() - startTime;

        return {
          success: true,
          data: results,
          processedAt: Date.now(),
          duration
        };
      } catch (error: any) {
        const duration = Date.now() - startTime;
        throw new Error(`Processing failed: ${error.message}`);
      }
    });

    // Report generation job
    this.queue.process('generate-report', 2, async (job) => {
      const { payload } = job.data;

      const report = await this.generateReport(
        payload.type,
        payload.filters,
        payload.format
      );

      return {
        success: true,
        data: {
          reportId: uuidv4(),
          url: report.url,
          size: report.size
        },
        processedAt: Date.now(),
        duration: 0
      };
    });

    // Email batch job
    this.queue.process('send-emails', 5, async (job) => {
      const { payload } = job.data;
      const { recipients, template, data } = payload;

      const results = await this.sendEmailBatch(
        recipients,
        template,
        data
      );

      return {
        success: true,
        data: {
          sent: results.successful,
          failed: results.failed
        },
        processedAt: Date.now(),
        duration: 0
      };
    });
  }

  private setupEvents(): void {
    this.queue.on('completed', (job, result) => {
      console.log(`Job ${job.id} completed:`, result);

      // Store result
      this.resultQueue.add({
        jobId: job.id,
        ...result
      });
    });

    this.queue.on('failed', (job, error) => {
      console.error(`Job ${job?.id} failed:`, error.message);

      // Store failure
      this.resultQueue.add({
        jobId: job?.id,
        success: false,
        error: error.message,
        processedAt: Date.now(),
        duration: 0
      });
    });

    this.queue.on('progress', (job, progress) => {
      console.log(`Job ${job.id} progress: ${progress}%`);
    });

    this.queue.on('stalled', (job) => {
      console.warn(`Job ${job.id} stalled`);
    });
  }

  async addJob(
    type: string,
    payload: any,
    options?: Queue.JobOptions
  ): Promise<Queue.Job<JobData>> {
    const jobData: JobData = {
      id: uuidv4(),
      type,
      payload,
      metadata: {
        createdAt: Date.now()
      }
    };

    return this.queue.add(type, jobData, options);
  }

  async addBulkJobs(
    jobs: Array<{ type: string; payload: any; options?: Queue.JobOptions }>
  ): Promise<Queue.Job<JobData>[]> {
    const bulkData = jobs.map(({ type, payload, options }) => ({
      name: type,
      data: {
        id: uuidv4(),
        type,
        payload,
        metadata: { createdAt: Date.now() }
      },
      opts: options || {}
    }));

    return this.queue.addBulk(bulkData);
  }

  async scheduleJob(
    type: string,
    payload: any,
    cronExpression: string
  ): Promise<Queue.Job<JobData>> {
    return this.addJob(type, payload, {
      repeat: {
        cron: cronExpression
      }
    });
  }

  private async processDataBatch(
    items: any[],
    onProgress: (progress: number) => Promise<void>
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
    await new Promise(resolve => setTimeout(resolve, 100));
    return { ...item, processed: true };
  }

  private async generateReport(
    type: string,
    filters: any,
    format: string
  ): Promise<any> {
    // Simulate report generation
    return {
      url: `https://cdn.example.com/reports/${uuidv4()}.${format}`,
      size: 1024 * 1024
    };
  }

  private async sendEmailBatch(
    recipients: string[],
    template: string,
    data: any
  ): Promise<{ successful: number; failed: number }> {
    // Simulate email sending
    return {
      successful: recipients.length,
      failed: 0
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
      logs: logs.logs
    };
  }

  async getQueueStats(): Promise<any> {
    const [
      waiting,
      active,
      completed,
      failed,
      delayed,
      paused
    ] = await Promise.all([
      this.queue.getWaitingCount(),
      this.queue.getActiveCount(),
      this.queue.getCompletedCount(),
      this.queue.getFailedCount(),
      this.queue.getDelayedCount(),
      this.queue.getPausedCount()
    ]);

    return {
      waiting,
      active,
      completed,
      failed,
      delayed,
      paused
    };
  }

  async pause(): Promise<void> {
    await this.queue.pause();
  }

  async resume(): Promise<void> {
    await this.queue.resume();
  }

  async clean(grace: number = 0): Promise<void> {
    await this.queue.clean(grace, 'completed');
    await this.queue.clean(grace, 'failed');
  }

  async close(): Promise<void> {
    await this.queue.close();
    await this.resultQueue.close();
  }
}

// Usage
const processor = new BatchProcessor('redis://localhost:6379');

// Add single job
const job = await processor.addJob('process-data', {
  items: [{ id: 1 }, { id: 2 }, { id: 3 }]
});

// Add bulk jobs
await processor.addBulkJobs([
  {
    type: 'process-data',
    payload: { items: [/* ... */] }
  },
  {
    type: 'generate-report',
    payload: { type: 'sales', format: 'pdf' }
  }
]);

// Schedule recurring job
await processor.scheduleJob(
  'generate-report',
  { type: 'daily-summary' },
  '0 0 * * *' // Daily at midnight
);

// Check status
const status = await processor.getJobStatus(job.id!);
console.log('Job status:', status);

// Get queue stats
const stats = await processor.getQueueStats();
console.log('Queue stats:', stats);
```

### 2. **Celery-Style Worker (Python)**

```python
from celery import Celery, Task
from celery.schedules import crontab
from typing import List, Any, Dict
import time
import logging

# Initialize Celery
app = Celery(
    'batch_processor',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1'
)

# Configure Celery
app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=300,  # 5 minutes
    task_soft_time_limit=270,  # 4.5 minutes
    worker_prefetch_multiplier=4,
    worker_max_tasks_per_child=1000,
)

# Periodic tasks
app.conf.beat_schedule = {
    'daily-report': {
        'task': 'tasks.generate_daily_report',
        'schedule': crontab(hour=0, minute=0),
    },
    'cleanup-old-data': {
        'task': 'tasks.cleanup_old_data',
        'schedule': crontab(hour=2, minute=0),
    },
}

logger = logging.getLogger(__name__)


class CallbackTask(Task):
    """Base task with callback support."""

    def on_success(self, retval, task_id, args, kwargs):
        logger.info(f"Task {task_id} succeeded: {retval}")

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error(f"Task {task_id} failed: {exc}")

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        logger.warning(f"Task {task_id} retrying: {exc}")


@app.task(base=CallbackTask, bind=True, max_retries=3)
def process_batch_data(self, items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Process batch of data items."""
    try:
        results = []
        total = len(items)

        for i, item in enumerate(items):
            # Process item
            result = process_single_item(item)
            results.append(result)

            # Update progress
            progress = int((i + 1) / total * 100)
            self.update_state(
                state='PROGRESS',
                meta={'current': i + 1, 'total': total, 'percent': progress}
            )

        return {
            'processed': len(results),
            'success': True,
            'results': results
        }

    except Exception as exc:
        logger.error(f"Batch processing failed: {exc}")
        raise self.retry(exc=exc, countdown=60)  # Retry after 1 minute


@app.task
def process_single_item(item: Dict[str, Any]) -> Dict[str, Any]:
    """Process single item."""
    # Simulate processing
    time.sleep(0.1)
    return {
        'id': item.get('id'),
        'processed': True,
        'timestamp': time.time()
    }


@app.task(bind=True)
def generate_report(
    self,
    report_type: str,
    filters: Dict[str, Any],
    format: str = 'pdf'
) -> Dict[str, str]:
    """Generate report."""
    logger.info(f"Generating {report_type} report in {format} format")

    self.update_state(state='PROGRESS', meta={'step': 'gathering_data'})
    # Gather data
    time.sleep(2)

    self.update_state(state='PROGRESS', meta={'step': 'processing'})
    # Process data
    time.sleep(2)

    self.update_state(state='PROGRESS', meta={'step': 'generating'})
    # Generate report
    time.sleep(2)

    return {
        'report_id': f"report-{int(time.time())}",
        'url': f"https://cdn.example.com/reports/report.{format}",
        'format': format
    }


@app.task
def send_email_batch(
    recipients: List[str],
    template: str,
    context: Dict[str, Any]
) -> Dict[str, int]:
    """Send batch of emails."""
    successful = 0
    failed = 0

    for recipient in recipients:
        try:
            send_email(recipient, template, context)
            successful += 1
        except Exception as e:
            logger.error(f"Failed to send email to {recipient}: {e}")
            failed += 1

    return {
        'successful': successful,
        'failed': failed,
        'total': len(recipients)
    }


@app.task
def generate_daily_report():
    """Scheduled task: Generate daily report."""
    logger.info("Generating daily report")
    generate_report.delay('daily', {}, 'pdf')


@app.task
def cleanup_old_data():
    """Scheduled task: Clean up old data."""
    logger.info("Cleaning up old data")
    # Cleanup logic here


def send_email(recipient: str, template: str, context: Dict[str, Any]):
    """Send single email."""
    logger.info(f"Sending email to {recipient}")
    # Email sending logic


# Task chaining and grouping
from celery import chain, group, chord

def process_in_chunks(items: List[Any], chunk_size: int = 100):
    """Process items in parallel chunks."""
    chunks = [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

    # Process chunks in parallel
    job = group(process_batch_data.s(chunk) for chunk in chunks)
    result = job.apply_async()

    return result


def process_with_callback(items: List[Any]):
    """Process items and call callback when done."""
    callback = send_notification.s()
    header = group(process_batch_data.s(chunk) for chunk in [items])

    # Use chord to call callback after all tasks complete
    job = chord(header)(callback)
    return job


@app.task
def send_notification(results):
    """Callback task after batch processing."""
    logger.info(f"All tasks completed: {len(results)} results")


# Usage examples
if __name__ == '__main__':
    # Enqueue task
    result = process_batch_data.delay([
        {'id': 1, 'value': 'a'},
        {'id': 2, 'value': 'b'}
    ])

    # Check task status
    print(f"Task ID: {result.id}")
    print(f"Status: {result.status}")

    # Wait for result (blocking)
    final_result = result.get(timeout=10)
    print(f"Result: {final_result}")

    # Process in chunks
    items = [{'id': i} for i in range(1000)]
    chunk_result = process_in_chunks(items, chunk_size=100)

    # Check group result
    print(f"Chunks: {len(chunk_result)}")
```

### 3. **Cron Job Scheduler**

```typescript
import cron from 'node-cron';

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
  name: 'daily-backup',
  schedule: '0 2 * * *', // 2 AM daily
  enabled: true,
  handler: async () => {
    console.log('Running daily backup...');
    // Backup logic
  }
});

scheduler.register({
  name: 'hourly-cleanup',
  schedule: '0 * * * *', // Every hour
  enabled: true,
  handler: async () => {
    console.log('Running cleanup...');
    // Cleanup logic
  }
});

scheduler.register({
  name: 'weekly-report',
  schedule: '0 9 * * 1', // Monday 9 AM
  enabled: true,
  handler: async () => {
    console.log('Generating weekly report...');
    // Report generation
  }
});
```

## Best Practices

### ✅ DO
- Implement idempotency for all jobs
- Use job queues for distributed processing
- Monitor job success/failure rates
- Implement retry logic with exponential backoff
- Set appropriate timeouts
- Log job execution details
- Use dead letter queues for failed jobs
- Implement job priority levels
- Batch similar operations together
- Use connection pooling
- Implement graceful shutdown
- Monitor queue depth and processing time

### ❌ DON'T
- Process jobs synchronously in request handlers
- Ignore failed jobs
- Set unlimited retries
- Skip monitoring and alerting
- Process jobs without timeouts
- Store large payloads in queue
- Forget to clean up completed jobs

## Resources

- [Bull Queue Documentation](https://github.com/OptimalBits/bull)
- [Celery Documentation](https://docs.celeryq.dev/)
- [Cron Expression Guide](https://crontab.guru/)
