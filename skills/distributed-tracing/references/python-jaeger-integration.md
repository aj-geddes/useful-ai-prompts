# Python Jaeger Integration

## Python Jaeger Integration

```python
# tracing.py
from jaeger_client import Config
from opentracing.propagation import Format

def init_jaeger_tracer(service_name):
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'local_agent': {
                'reporting_host': 'localhost',
                'reporting_port': 6831,
            },
            'logging': True,
        },
        service_name=service_name,
    )
    return config.initialize_tracer()

# Flask integration
from flask import Flask, request

app = Flask(__name__)
tracer = init_jaeger_tracer('api-service')

@app.before_request
def before_request():
    ctx = tracer.extract(Format.HTTP_HEADERS, request.headers)
    request.span = tracer.start_span(
        request.path,
        child_of=ctx,
        tags={
            'http.method': request.method,
            'http.url': request.url,
        }
    )

@app.after_request
def after_request(response):
    request.span.set_tag('http.status_code', response.status_code)
    request.span.finish()
    return response

@app.route('/api/users/<user_id>')
def get_user(user_id):
    with tracer.start_span('fetch-user', child_of=request.span) as span:
        span.set_tag('user.id', user_id)
        # Fetch user from database
        return {'user': {'id': user_id}}
```
