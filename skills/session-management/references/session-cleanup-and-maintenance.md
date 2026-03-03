# Session Cleanup and Maintenance

## Session Cleanup and Maintenance

```python
# Scheduled cleanup task with APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

class SessionCleanup:
    def __init__(self, redis_client, cleanup_interval_minutes=60):
        self.redis = redis_client
        self.cleanup_interval = cleanup_interval_minutes
        self.scheduler = BackgroundScheduler()

    def start(self):
        self.scheduler.add_job(
            func=self.cleanup_expired_sessions,
            trigger='interval',
            minutes=self.cleanup_interval,
            id='cleanup_expired_sessions',
            replace_existing=True
        )
        self.scheduler.start()
        atexit.register(lambda: self.scheduler.shutdown())

    def cleanup_expired_sessions(self):
        """Remove expired sessions from Redis"""
        cursor = 0
        removed_count = 0

        while True:
            cursor, keys = self.redis.scan(cursor, match='session:*')
            for key in keys:
                ttl = self.redis.ttl(key)
                if ttl == -2:  # Key doesn't exist
                    removed_count += 1
                elif ttl < 300:  # Less than 5 minutes left
                    self.redis.delete(key)
                    removed_count += 1

            if cursor == 0:
                break

        return removed_count

# Initialize on app startup
cleanup = SessionCleanup(redis_client)
cleanup.start()
```
