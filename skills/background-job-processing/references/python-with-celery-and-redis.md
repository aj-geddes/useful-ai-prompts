# Python with Celery and Redis

## Python with Celery and Redis

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
