# Job Retry and Error Handling

## Job Retry and Error Handling

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
