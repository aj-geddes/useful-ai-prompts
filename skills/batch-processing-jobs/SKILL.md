---
name: batch-processing-jobs
description: >
  Implement robust batch processing systems with job queues, schedulers,
  background tasks, and distributed workers. Use when processing large datasets,
  scheduled tasks, async operations, or resource-intensive computations.
---

# Batch Processing Jobs

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

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

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Bull Queue (Node.js)](references/bull-queue-nodejs.md) | Bull Queue (Node.js) |
| [Celery-Style Worker (Python)](references/celery-style-worker-python.md) | Celery-Style Worker (Python) |
| [Cron Job Scheduler](references/cron-job-scheduler.md) | Cron Job Scheduler |

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
