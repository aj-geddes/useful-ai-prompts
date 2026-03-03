# Python Health Checks

## Python Health Checks

```python
from flask import Flask, jsonify
import time

app = Flask(__name__)
startup_time = time.time()

def get_uptime():
    return int(time.time() - startup_time)

@app.route('/health')
def health():
    return jsonify({
        'status': 'ok',
        'uptime_seconds': get_uptime()
    }), 200

@app.route('/health/deep')
def health_deep():
    health_status = {
        'status': 'ok',
        'checks': {
            'database': 'unknown',
            'cache': 'unknown'
        }
    }

    try:
        db.session.execute('SELECT 1')
        health_status['checks']['database'] = 'ok'
    except:
        health_status['checks']['database'] = 'error'
        health_status['status'] = 'degraded'

    try:
        cache.get('_health')
        health_status['checks']['cache'] = 'ok'
    except:
        health_status['checks']['cache'] = 'error'

    status_code = 200 if health_status['status'] == 'ok' else 503
    return jsonify(health_status), status_code

@app.route('/readiness')
def readiness():
    try:
        db.session.execute('SELECT 1')
        return jsonify({'ready': True}), 200
    except:
        return jsonify({'ready': False}), 503
```
