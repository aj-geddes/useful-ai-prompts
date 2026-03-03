# Python/Flask Graceful Shutdown

## Python/Flask Graceful Shutdown

```python
import signal
import sys
import time
from flask import Flask, request, g
from threading import Lock

app = Flask(__name__)

class GracefulShutdown:
    def __init__(self):
        self.is_shutting_down = False
        self.active_requests = 0
        self.lock = Lock()

    def before_request(self):
        """Track active requests."""
        if self.is_shutting_down:
            return {'error': 'Server is shutting down'}, 503

        with self.lock:
            self.active_requests += 1

    def after_request(self, response):
        """Decrement active requests."""
        with self.lock:
            self.active_requests -= 1
        return response

    def shutdown(self, signum, frame):
        """Handle shutdown signal."""
        print(f"Received signal {signum}, starting graceful shutdown...")
        self.is_shutting_down = True

        # Wait for active requests
        max_wait = 30
        waited = 0

        while self.active_requests > 0 and waited < max_wait:
            print(f"Waiting for {self.active_requests} active requests...")
            time.sleep(1)
            waited += 1

        if self.active_requests > 0:
            print(f"Force closing with {self.active_requests} requests remaining")

        print("Graceful shutdown complete")
        sys.exit(0)

# Setup graceful shutdown
shutdown_handler = GracefulShutdown()
app.before_request(shutdown_handler.before_request)
app.after_request(shutdown_handler.after_request)

signal.signal(signal.SIGTERM, shutdown_handler.shutdown)
signal.signal(signal.SIGINT, shutdown_handler.shutdown)

@app.route('/health')
def health():
    if shutdown_handler.is_shutting_down:
        return {'status': 'shutting_down'}, 503
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
