# Python Sentry Integration

## Python Sentry Integration

```python
# sentry_config.py
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
import logging
import os

sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.ERROR
)

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    integrations=[FlaskIntegration(), sentry_logging],
    environment=os.environ.get('ENVIRONMENT', 'development'),
    release=os.environ.get('APP_VERSION', '1.0.0'),
    traces_sample_rate=0.1 if os.environ.get('ENVIRONMENT') == 'production' else 1.0,
    attach_stacktrace=True
)

# Flask integration
from flask import Flask
import sentry_sdk

app = Flask(__name__)

@app.route('/api/orders/<order_id>')
def get_order(order_id):
    try:
        sentry_sdk.set_user({'id': request.user.id})
        sentry_sdk.capture_message(f'Fetching order {order_id}', level='info')

        order = db.query(f'SELECT * FROM orders WHERE id = {order_id}')

        if not order:
            sentry_sdk.capture_exception(ValueError('Order not found'))
            return {'error': 'Order not found'}, 404

        return {'order': order}

    except Exception as e:
        sentry_sdk.capture_exception(e, {
            'tags': { 'endpoint': 'get_order', 'order_id': order_id }
        })
        return {'error': 'Internal server error'}, 500
```
