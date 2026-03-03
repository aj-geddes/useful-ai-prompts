# Python Flask Health Checks

## Python Flask Health Checks

```python
from flask import Flask, jsonify
from typing import Dict, Any
import psycopg2
import redis
import time

app = Flask(__name__)

class HealthCheck:
    def __init__(self):
        self.start_time = time.time()
        self.db_pool = None  # Initialize your DB pool
        self.redis_client = redis.Redis(host='localhost', port=6379)

    def liveness(self) -> Dict[str, str]:
        """Simple liveness check."""
        return {"status": "alive"}

    def readiness(self) -> Dict[str, Any]:
        """Readiness check with dependencies."""
        checks = {
            "database": self.check_database(),
            "redis": self.check_redis()
        }

        status = "ready" if all(
            c["status"] == "pass" for c in checks.values()
        ) else "not_ready"

        return {
            "status": status,
            "checks": checks,
            "timestamp": time.time()
        }

    def check_database(self) -> Dict[str, Any]:
        """Check database connection."""
        start_time = time.time()

        try:
            conn = psycopg2.connect("dbname=test user=postgres")
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            cursor.close()
            conn.close()

            duration = (time.time() - start_time) * 1000

            return {
                "status": "pass",
                "time": f"{duration:.2f}ms"
            }
        except Exception as e:
            return {
                "status": "fail",
                "error": str(e)
            }

    def check_redis(self) -> Dict[str, Any]:
        """Check Redis connection."""
        start_time = time.time()

        try:
            self.redis_client.ping()
            duration = (time.time() - start_time) * 1000

            return {
                "status": "pass",
                "time": f"{duration:.2f}ms"
            }
        except Exception as e:
            return {
                "status": "fail",
                "error": str(e)
            }

health_checker = HealthCheck()

@app.route('/health/live')
def liveness():
    return jsonify(health_checker.liveness()), 200

@app.route('/health/ready')
def readiness():
    result = health_checker.readiness()
    status_code = 200 if result["status"] == "ready" else 503
    return jsonify(result), status_code

@app.route('/health')
def health():
    result = health_checker.readiness()
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
