# Monitoring and Observability

## Monitoring and Observability

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
