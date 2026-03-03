# Distributed Context Propagation

## Distributed Context Propagation

```javascript
// propagation.js
const axios = require("axios");
const { tracer } = require("./tracing");
const opentracing = require("opentracing");

async function callDownstreamService(span, url, data) {
  const headers = {};

  // Inject trace context
  tracer.inject(span, opentracing.FORMAT_HTTP_HEADERS, headers);

  try {
    const response = await axios.post(url, data, { headers });
    span.setTag("downstream.success", true);
    return response.data;
  } catch (error) {
    span.setTag(opentracing.Tags.ERROR, true);
    span.log({
      event: "error",
      message: error.message,
    });
    throw error;
  }
}

module.exports = { callDownstreamService };
```
