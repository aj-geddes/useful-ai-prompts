# Session Storage with Redis

## Session Storage with Redis

```python
# Python/Flask with Redis
import redis
import json
from datetime import timedelta
from functools import wraps

class RedisSessionManager:
    def __init__(self, redis_url='redis://localhost:6379'):
        self.redis = redis.from_url(redis_url, decode_responses=True)
        self.prefix = 'session:'

    def create_session(self, user_id, data, expire_hours=24):
        """Create a session for user"""
        session_data = {
            'user_id': user_id,
            'data': data,
            'created_at': datetime.utcnow().isoformat(),
            'last_activity': datetime.utcnow().isoformat()
        }

        session_id = secrets.token_urlsafe(32)
        key = f'{self.prefix}{session_id}'

        self.redis.setex(
            key,
            timedelta(hours=expire_hours),
            json.dumps(session_data)
        )

        return session_id

    def get_session(self, session_id):
        """Retrieve session data"""
        key = f'{self.prefix}{session_id}'
        data = self.redis.get(key)

        if not data:
            return None

        session_data = json.loads(data)

        # Update last activity
        session_data['last_activity'] = datetime.utcnow().isoformat()
        self.redis.setex(key, timedelta(hours=24), json.dumps(session_data))

        return session_data

    def destroy_session(self, session_id):
        """Destroy a session"""
        key = f'{self.prefix}{session_id}'
        self.redis.delete(key)

    def update_session(self, session_id, updates):
        """Update session data"""
        session_data = self.get_session(session_id)
        if not session_data:
            return False

        session_data['data'].update(updates)
        key = f'{self.prefix}{session_id}'
        self.redis.setex(
            key,
            timedelta(hours=24),
            json.dumps(session_data)
        )
        return True

    def get_user_sessions(self, user_id):
        """Get all sessions for a user"""
        cursor = 0
        sessions = []

        while True:
            cursor, keys = self.redis.scan(cursor, match=f'{self.prefix}*')
            for key in keys:
                data = json.loads(self.redis.get(key))
                if data['user_id'] == user_id:
                    sessions.append({
                        'session_id': key.replace(self.prefix, ''),
                        'created_at': data['created_at'],
                        'last_activity': data['last_activity']
                    })

            if cursor == 0:
                break

        return sessions

    def invalidate_all_user_sessions(self, user_id):
        """Logout user from all devices"""
        sessions = self.get_user_sessions(user_id)
        for session in sessions:
            self.destroy_session(session['session_id'])
```
