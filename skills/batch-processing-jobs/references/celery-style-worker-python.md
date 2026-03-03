# Celery-Style Worker (Python)

## Celery-Style Worker (Python)

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
