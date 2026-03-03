# Python Audit Logging System

## Python Audit Logging System

```python
# audit_logging.py
import logging
import json
from datetime import datetime
from typing import Dict, Any, Optional
import structlog
from elasticsearch import Elasticsearch

class AuditLogger:
    def __init__(self):
        # Configure structured logging
        structlog.configure(
            processors=[
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.processors.JSONRenderer()
            ]
        )

        self.logger = structlog.get_logger()

        # File handler
        file_handler = logging.FileHandler('logs/audit.log')
        file_handler.setLevel(logging.INFO)

        # Elasticsearch for SIEM
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    def _log(self, category: str, event_data: Dict[str, Any]):
        """Internal logging method"""
        log_entry = {
            'category': category,
            'timestamp': datetime.utcnow().isoformat(),
            **event_data
        }

        # Log to file
        self.logger.info(json.dumps(log_entry))

        # Send to Elasticsearch
        try:
            self.es.index(
                index='security-audit',
                document=log_entry
            )
        except Exception as e:
            print(f"Failed to send to Elasticsearch: {e}")

    def log_auth(self, user_id: str, action: str, success: bool,
                  ip: str = None, user_agent: str = None, **kwargs):
        """Log authentication event"""
        self._log('authentication', {
            'user_id': user_id,
            'action': action,
            'success': success,
            'ip': ip,
            'user_agent': user_agent,
            **kwargs
        })

    def log_authorization(self, user_id: str, resource: str, action: str,
                         granted: bool, reason: str = None, **kwargs):
        """Log authorization decision"""
        self._log('authorization', {
            'user_id': user_id,
            'resource': resource,
            'action': action,
            'granted': granted,
            'reason': reason,
            **kwargs
        })

    def log_data_access(self, user_id: str, data_type: str, record_id: str,
                       action: str, **kwargs):
        """Log data access event"""
        self._log('data_access', {
            'user_id': user_id,
            'data_type': data_type,
            'record_id': record_id,
            'action': action,
            **kwargs
        })

    def log_security_event(self, event_type: str, severity: str,
                          description: str, **kwargs):
        """Log security event"""
        self._log('security_event', {
            'event_type': event_type,
            'severity': severity,
            'description': description,
            **kwargs
        })

    def log_config_change(self, user_id: str, setting: str,
                         old_value: Any, new_value: Any, **kwargs):
        """Log configuration change"""
        self._log('configuration_change', {
            'user_id': user_id,
            'setting': setting,
            'old_value': str(old_value),
            'new_value': str(new_value),
            **kwargs
        })

# Flask integration
from flask import Flask, request, g
from functools import wraps

app = Flask(__name__)
audit_logger = AuditLogger()

@app.before_request
def before_request():
    g.request_start_time = datetime.now()

@app.after_request
def after_request(response):
    if hasattr(g, 'request_start_time'):
        duration = (datetime.now() - g.request_start_time).total_seconds() * 1000

        audit_logger._log('api_request', {
            'user_id': getattr(g, 'user_id', 'anonymous'),
            'method': request.method,
            'endpoint': request.path,
            'status_code': response.status_code,
            'duration_ms': duration,
            'ip': request.remote_addr,
            'user_agent': request.user_agent.string
        })

    return response

def audit_data_access(data_type: str):
    """Decorator for data access logging"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            result = f(*args, **kwargs)

            audit_logger.log_data_access(
                user_id=g.user_id,
                data_type=data_type,
                record_id=kwargs.get('id', 'unknown'),
                action=request.method.lower(),
                ip=request.remote_addr
            )

            return result

        return decorated_function
    return decorator

@app.route('/api/users/<user_id>', methods=['GET'])
@audit_data_access('user')
def get_user(user_id):
    # Fetch user
    return jsonify({'id': user_id})

if __name__ == '__main__':
    app.run()
```
