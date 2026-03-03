# Zipkin Integration

## Zipkin Integration

```javascript
// zipkin-setup.js
const CLSContext = require("zipkin-context-cls");
const { Tracer, BatchRecorder, HttpLogger } = require("zipkin");
const zipkinMiddleware =
  require("zipkin-instrumentation-express").expressMiddleware;

const recorder = new BatchRecorder({
  logger: new HttpLogger({
    endpoint: "http://localhost:9411/api/v2/spans",
    headers: { "Content-Type": "application/json" },
  }),
});

const ctxImpl = new CLSContext("zipkin");
const tracer = new Tracer({ recorder, ctxImpl });

module.exports = {
  tracer,
  zipkinMiddleware: zipkinMiddleware({
    tracer,
    serviceName: "api-service",
  }),
};
```


## Trace Analysis

```python
# query-traces.py
import requests

def query_traces(service_name, operation=None, limit=20):
    params = {
        'service': service_name,
        'limit': limit
    }
    if operation:
        params['operation'] = operation

    response = requests.get('http://localhost:16686/api/traces', params=params)
    return response.json()['data']

def find_slow_traces(service_name, min_duration_ms=1000):
    traces = query_traces(service_name, limit=100)
    slow_traces = [
        t for t in traces
        if t['duration'] > min_duration_ms * 1000
    ]
    return sorted(slow_traces, key=lambda t: t['duration'], reverse=True)
```
