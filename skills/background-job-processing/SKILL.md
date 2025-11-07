---
name: background-job-processing
description: Implement background job processing systems with task queues, workers, scheduling, and retry mechanisms. Use when handling long-running tasks, sending emails, generating reports, and processing large datasets asynchronously.
---

# Background Job Processing

## Overview

Build robust background job processing systems with distributed task queues, worker pools, job scheduling, error handling, retry policies, and monitoring for efficient asynchronous task execution.

## When to Use

- Handling long-running operations asynchronously
- Sending emails in background
- Generating reports or exports
- Processing large datasets
- Scheduling recurring tasks
- Distributing compute-intensive operations

## Instructions

### 1. **Python with Celery and Redis**

```python
# celery_app.py
from celery import Celery
from kombu import Exchange, Queue
import os

app = Celery('myapp')

# Configuration
app.conf.update(
    broker_url=os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
    result_backend=os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes
    task_soft_time_limit=25 * 60,  # 25 minutes
    broker_connection_retry_on_startup=True,
)

# Queue configuration
default_exchange = Exchange('tasks', type='direct')
app.conf.task_queues = (
    Queue('default', exchange=default_exchange, routing_key='default'),
    Queue('emails', exchange=default_exchange, routing_key='emails'),
    Queue('reports', exchange=default_exchange, routing_key='reports'),
    Queue('batch', exchange=default_exchange, routing_key='batch'),
)

app.conf.task_routes = {
    'tasks.send_email': {'queue': 'emails'},
    'tasks.generate_report': {'queue': 'reports'},
    'tasks.process_batch': {'queue': 'batch'},
}

app.conf.task_default_retry_delay = 60
app.conf.task_max_retries = 3

# Auto-discover tasks
app.autodiscover_tasks(['myapp.tasks'])

# tasks.py
from celery_app import app
from celery import shared_task
from celery.exceptions import SoftTimeLimitExceeded
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_email(self, user_id, email_subject):
    """Send email task with retry logic"""
    try:
        user = User.query.get(user_id)
        if not user:
            logger.error(f"User {user_id} not found")
            return {'status': 'failed', 'reason': 'User not found'}

        # Send email logic
        send_email_helper(user.email, email_subject)

        return {'status': 'success', 'user_id': user_id}

    except Exception as exc:
        logger.error(f"Error sending email: {exc}")
        # Retry with exponential backoff
        raise self.retry(exc=exc, countdown=60 * (2 ** self.request.retries))

@shared_task(bind=True)
def generate_report(self, report_type, filters):
    """Generate report with progress tracking"""
    try:
        self.update_state(
            state='PROGRESS',
            meta={'current': 0, 'total': 100, 'status': 'Initializing...'}
        )

        total_records = count_records(filters)
        processed = 0

        for batch in fetch_records_in_batches(filters, batch_size=1000):
            process_batch(batch, report_type)
            processed += len(batch)

            # Update progress
            progress = int((processed / total_records) * 100)
            self.update_state(
                state='PROGRESS',
                meta={'current': processed, 'total': total_records, 'progress': progress}
            )

        return {'status': 'success', 'total_records': total_records}

    except SoftTimeLimitExceeded:
        logger.error("Report generation exceeded time limit")
        raise Exception("Report generation timed out")

@shared_task(bind=True)
def process_batch(self, batch_data):
    """Process large batch operations"""
    results = []
    for item in batch_data:
        try:
            result = process_item(item)
            results.append(result)
        except Exception as e:
            logger.error(f"Error processing item {item}: {e}")
            results.append({'status': 'failed', 'error': str(e)})

    return {'processed': len(results), 'results': results}

# Periodic tasks with Beat scheduler
from celery.schedules import crontab

app.conf.beat_schedule = {
    'cleanup-expired-sessions': {
        'task': 'tasks.cleanup_expired_sessions',
        'schedule': crontab(minute=0, hour='*/6'),  # Every 6 hours
        'args': ()
    },
    'generate-daily-report': {
        'task': 'tasks.generate_daily_report',
        'schedule': crontab(hour=0, minute=0),  # Daily at midnight
        'args': ()
    },
    'sync-external-data': {
        'task': 'tasks.sync_external_data',
        'schedule': crontab(minute=0),  # Every hour
        'args': ()
    },
}

@shared_task
def cleanup_expired_sessions():
    """Cleanup expired sessions"""
    deleted_count = Session.query.filter(
        Session.expires_at < datetime.utcnow()
    ).delete()
    db.session.commit()
    return {'deleted': deleted_count}

@shared_task
def sync_external_data():
    """Sync data from external API"""
    try:
        data = fetch_from_external_api()
        for item in data:
            update_or_create_record(item)
        return {'status': 'success', 'synced_items': len(data)}
    except Exception as e:
        logger.error(f"Sync failed: {e}")
        raise

# Flask integration
from flask import Blueprint, jsonify

celery_bp = Blueprint('celery', __name__, url_prefix='/api/tasks')

@celery_bp.route('/<task_id>/status', methods=['GET'])
def task_status(task_id):
    """Get task status"""
    result = app.AsyncResult(task_id)
    return jsonify({
        'task_id': task_id,
        'status': result.status,
        'result': result.result if result.ready() else None,
        'progress': result.info if result.state == 'PROGRESS' else None
    })

@celery_bp.route('/send-email', methods=['POST'])
def trigger_email():
    """Trigger email sending task"""
    data = request.json
    task = send_email.delay(data['user_id'], data['subject'])
    return jsonify({'task_id': task.id}), 202
```

### 2. **Node.js with Bull Queue**

```javascript
// queue.js
const Queue = require('bull');
const redis = require('redis');

const redisClient = redis.createClient({
    host: process.env.REDIS_HOST || 'localhost',
    port: process.env.REDIS_PORT || 6379
});

// Create job queues
const emailQueue = new Queue('emails', {
    redis: {
        host: process.env.REDIS_HOST || 'localhost',
        port: process.env.REDIS_PORT || 6379
    }
});

const reportQueue = new Queue('reports', {
    redis: {
        host: process.env.REDIS_HOST || 'localhost',
        port: process.env.REDIS_PORT || 6379
    }
});

const batchQueue = new Queue('batch', {
    redis: {
        host: process.env.REDIS_HOST || 'localhost',
        port: process.env.REDIS_PORT || 6379
    }
});

// Process email jobs
emailQueue.process(5, async (job) => {
    const { userId, subject, body } = job.data;

    try {
        const user = await User.findById(userId);
        if (!user) {
            throw new Error(`User ${userId} not found`);
        }

        await sendEmailHelper(user.email, subject, body);

        return { status: 'success', userId };
    } catch (error) {
        // Retry with exponential backoff
        throw error;
    }
});

// Process report jobs with progress
reportQueue.process(async (job) => {
    const { reportType, filters } = job.data;
    const totalRecords = await countRecords(filters);

    for (let i = 0; i < totalRecords; i += 1000) {
        const batch = await fetchRecordsBatch(filters, i, 1000);
        await processBatch(batch, reportType);

        // Update progress
        job.progress(Math.round((i / totalRecords) * 100));
    }

    return { status: 'success', totalRecords };
});

// Process batch jobs
batchQueue.process(async (job) => {
    const { items } = job.data;
    const results = [];

    for (const item of items) {
        try {
            const result = await processItem(item);
            results.push(result);
        } catch (error) {
            results.push({ status: 'failed', error: error.message });
        }
    }

    return { processed: results.length, results };
});

// Event listeners
emailQueue.on('completed', (job) => {
    console.log(`Email job ${job.id} completed`);
});

emailQueue.on('failed', (job, err) => {
    console.error(`Email job ${job.id} failed:`, err.message);
});

emailQueue.on('progress', (job, progress) => {
    console.log(`Email job ${job.id} ${progress}% complete`);
});

module.exports = {
    emailQueue,
    reportQueue,
    batchQueue
};

// routes.js
const express = require('express');
const { emailQueue, reportQueue } = require('./queue');

const router = express.Router();

// Trigger email job
router.post('/send-email', async (req, res) => {
    const { userId, subject, body } = req.body;

    const job = await emailQueue.add(
        { userId, subject, body },
        {
            attempts: 3,
            backoff: {
                type: 'exponential',
                delay: 2000
            },
            removeOnComplete: true
        }
    );

    res.status(202).json({ jobId: job.id });
});

// Get job status
router.get('/jobs/:jobId/status', async (req, res) => {
    const job = await emailQueue.getJob(req.params.jobId);

    if (!job) {
        return res.status(404).json({ error: 'Job not found' });
    }

    const progress = await job.progress();
    const state = await job.getState();
    const attempts = job.attemptsMade;

    res.json({
        jobId: job.id,
        state,
        progress,
        attempts,
        data: job.data
    });
});

module.exports = router;
```

### 3. **Ruby with Sidekiq**

```ruby
# Gemfile
gem 'sidekiq', '~> 7.0'
gem 'redis'
gem 'sidekiq-scheduler'

# config/sidekiq.yml
---
:redis:
  :url: redis://localhost:6379/0
:concurrency: 5
:timeout: 25
:max_retries: 3
:dead_letter_queue:
  :enabled: true
  :queue_name: dead_letter_queue

# app/workers/email_worker.rb
class EmailWorker
  include Sidekiq::Worker
  sidekiq_options queue: 'emails', retry: 3, lock: :until_executed

  def perform(user_id, subject)
    user = User.find(user_id)
    UserMailer.send_email(user, subject).deliver_now

    logger.info "Email sent to user #{user_id}"
  rescue StandardError => e
    logger.error "Failed to send email: #{e.message}"
    raise
  end
end

# app/workers/report_worker.rb
class ReportWorker
  include Sidekiq::Worker
  sidekiq_options queue: 'reports', retry: 2

  def perform(report_type, filters)
    total_records = Record.filter_by(filters).count
    processed = 0

    Record.filter_by(filters).find_in_batches(batch_size: 1000) do |batch|
      process_batch(batch, report_type)
      processed += batch.size

      # Update progress
      Sidekiq.redis { |conn|
        conn.hset("job:#{jid}", 'progress', (processed.to_f / total_records * 100).round(2))
      }
    end

    logger.info "Report #{report_type} generated"
    { status: 'success', total_records: total_records }
  end
end

# app/controllers/tasks_controller.rb
class TasksController < ApplicationController
  def send_email
    user_id = params[:user_id]
    subject = params[:subject]

    job_id = EmailWorker.perform_async(user_id, subject)
    render json: { job_id: job_id }, status: :accepted
  end

  def job_status
    job_id = params[:job_id]
    status = Sidekiq::Status.get(job_id)

    render json: {
      job_id: job_id,
      status: status || 'not_found'
    }
  end
end

# Scheduled jobs (lib/tasks/scheduler.rake or config/sidekiq.yml)
sidekiq_scheduler:
  cleanup_expired_sessions:
    cron: '0 */6 * * *'
    class: CleanupSessionsWorker
  generate_daily_report:
    cron: '0 0 * * *'
    class: DailyReportWorker
```

### 4. **Job Retry and Error Handling**

```python
# Retry strategies
from celery import shared_task
from celery.exceptions import MaxRetriesExceededError
import logging
import random

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=5, autoretry_for=(Exception,))
def resilient_task(self, data):
    """Task with advanced retry logic"""
    try:
        # Attempt task
        result = perform_operation(data)
        return result

    except TemporaryError as exc:
        # Retry with exponential backoff
        retry_delay = min(2 ** self.request.retries * 60, 3600)
        raise self.retry(exc=exc, countdown=retry_delay)

    except PermanentError as exc:
        logger.error(f"Permanent error in task {self.request.id}: {exc}")
        # Don't retry, just log and fail
        return {'status': 'failed', 'error': str(exc)}

    except Exception as exc:
        if self.request.retries < self.max_retries:
            logger.warning(f"Retrying task {self.request.id}, attempt {self.request.retries + 1}")
            # Add jitter to prevent thundering herd
            jitter = random.uniform(0, 10)
            raise self.retry(exc=exc, countdown=60 + jitter)
        else:
            raise MaxRetriesExceededError(f"Task {self.request.id} failed after {self.max_retries} retries")
```

### 5. **Monitoring and Observability**

```python
# monitoring.py
from prometheus_client import Counter, Histogram, Gauge
import time

# Metrics
task_counter = Counter('celery_task_total', 'Total tasks', ['task_name', 'status'])
task_duration = Histogram('celery_task_duration_seconds', 'Task duration', ['task_name'])
task_queue_size = Gauge('celery_queue_size', 'Queue size', ['queue_name'])

def track_task_metrics(task_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                task_counter.labels(task_name=task_name, status='success').inc()
                return result
            except Exception as e:
                task_counter.labels(task_name=task_name, status='failed').inc()
                raise
            finally:
                duration = time.time() - start_time
                task_duration.labels(task_name=task_name).observe(duration)
        return wrapper
    return decorator

@shared_task
@track_task_metrics('send_email')
def send_email_tracked(user_id, subject):
    # Task implementation
    pass
```

## Best Practices

### ✅ DO
- Use task timeouts to prevent hanging jobs
- Implement retry logic with exponential backoff
- Make tasks idempotent
- Use job priorities for critical tasks
- Monitor queue depths and job failures
- Log job execution details
- Clean up completed jobs
- Set appropriate batch sizes for memory efficiency
- Use dead-letter queues for failed jobs
- Test jobs independently

### ❌ DON'T
- Use synchronous operations in async tasks
- Ignore job failures
- Make tasks dependent on external state
- Use unbounded retries
- Store large objects in job data
- Forget to handle timeouts
- Run jobs without monitoring
- Use blocking operations in queues
- Forget to track job progress
- Mix unrelated operations in one job

## Complete Example

```python
from celery import shared_task
from celery_app import app

@shared_task
def simple_task(x, y):
    return x + y

# Trigger task
result = simple_task.delay(4, 6)
print(result.get())  # 10
```
