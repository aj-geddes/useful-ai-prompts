# Python Rate Limiting (Flask)

## Python Rate Limiting (Flask)

```python
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import datetime, timedelta
import redis

app = Flask(__name__)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Custom rate limit based on user plan
redis_client = redis.Redis(host='localhost', port=6379)

def get_rate_limit(user_id):
    plan = redis_client.get(f'user:{user_id}:plan').decode()
    limits = {
        'free': (100, 3600),
        'pro': (10000, 3600),
        'enterprise': (None, None)
    }
    return limits.get(plan, (100, 3600))

@app.route('/api/data', methods=['GET'])
@limiter.limit("30 per minute")
def get_data():
    return jsonify({'data': 'api response'}), 200

@app.route('/api/premium', methods=['GET'])
def get_premium_data():
    user_id = request.user_id
    max_requests, window = get_rate_limit(user_id)

    if max_requests is None:
        return jsonify({'data': 'unlimited data'}), 200

    key = f'ratelimit:{user_id}'
    current = redis_client.incr(key)
    redis_client.expire(key, window)

    if current <= max_requests:
        return jsonify({'data': 'premium data'}), 200
    else:
        return jsonify({'error': 'Rate limit exceeded'}), 429
```
