# Flask Integration

## Flask Integration

```python
# Flask app
from flask import Flask, request, g
import uuid
import time

app = Flask(__name__)

@app.before_request
def before_request():
    g.start_time = time.time()
    g.request_id = request.headers.get('X-Request-ID', str(uuid.uuid4()))

@app.after_request
def after_request(response):
    duration = time.time() - g.start_time
    logger.info('HTTP Request', extra={
        'method': request.method,
        'path': request.path,
        'status_code': response.status_code,
        'duration_ms': duration * 1000,
        'request_id': g.request_id
    })
    return response

@app.route('/api/orders/<order_id>')
def get_order(order_id):
    logger.info('Order request', extra={
        'order_id': order_id,
        'request_id': g.request_id
    })

    try:
        order = db.query(f'SELECT * FROM orders WHERE id = {order_id}')
        logger.debug('Order retrieved', extra={'order_id': order_id})
        return {'order': order}
    except Exception as e:
        logger.error('Order retrieval failed', extra={
            'order_id': order_id,
            'error': str(e),
            'request_id': g.request_id
        }, exc_info=True)
        return {'error': 'Internal server error'}, 500
```
