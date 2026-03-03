# Python Distributed Tracing

## Python Distributed Tracing

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import Resource
from flask import Flask, request
import requests
import uuid

# Setup tracing
resource = Resource.create({"service.name": "python-service"})
trace.set_tracer_provider(TracerProvider(resource=resource))

jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

# Auto-instrument Flask and requests
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

tracer = trace.get_tracer(__name__)

@app.route('/api/orders/<order_id>')
def get_order(order_id):
    # Current span is automatically created by FlaskInstrumentor

    with tracer.start_as_current_span("fetch_order_details") as span:
        span.set_attribute("order.id", order_id)

        # Fetch from database
        with tracer.start_as_current_span("database_query"):
            order = fetch_order_from_db(order_id)

        # Call another service (automatically traced)
        with tracer.start_as_current_span("fetch_user_details"):
            user = requests.get(
                f"http://user-service/users/{order['user_id']}"
            ).json()

        return {
            "order": order,
            "user": user
        }

def fetch_order_from_db(order_id):
    # Database logic
    return {"id": order_id, "user_id": "user123"}

if __name__ == '__main__':
    app.run(port=5000)
```
