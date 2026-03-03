# Jaeger Setup

## Jaeger Setup

```yaml
# docker-compose.yml
version: "3.8"
services:
  jaeger:
    image: jaegertracing/all-in-one:latest
    ports:
      - "5775:5775/udp"
      - "6831:6831/udp"
      - "16686:16686"
      - "14268:14268"
    networks:
      - tracing

networks:
  tracing:
```


## Node.js Jaeger Instrumentation

```javascript
// tracing.js
const initTracer = require("jaeger-client").initTracer;
const opentracing = require("opentracing");

const initJaegerTracer = (serviceName) => {
  const config = {
    serviceName: serviceName,
    sampler: {
      type: "const",
      param: 1,
    },
    reporter: {
      logSpans: true,
      agentHost: process.env.JAEGER_AGENT_HOST || "localhost",
      agentPort: process.env.JAEGER_AGENT_PORT || 6831,
    },
  };

  return initTracer(config, {});
};

const tracer = initJaegerTracer("api-service");
module.exports = { tracer };
```
