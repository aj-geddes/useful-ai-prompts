# Python Prometheus Integration

## Python Prometheus Integration

```python
from prometheus_client import Counter, Histogram, start_http_server
from flask import Flask, request
import time

app = Flask(__name__)

request_count = Counter('requests_total', 'Total requests', ['method', 'endpoint'])
request_duration = Histogram('request_duration_seconds', 'Request duration', ['method', 'endpoint'])

@app.before_request
def before():
    request.start_time = time.time()

@app.after_request
def after(response):
    duration = time.time() - request.start_time
    request_count.labels(request.method, request.path).inc()
    request_duration.labels(request.method, request.path).observe(duration)
    return response

if __name__ == '__main__':
    start_http_server(8000)
    app.run(port=5000)
```
