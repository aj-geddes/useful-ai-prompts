# Express Tracing Middleware

## Express Tracing Middleware

```javascript
// middleware.js
const { tracer } = require("./tracing");
const opentracing = require("opentracing");

const tracingMiddleware = (req, res, next) => {
  const wireCtx = tracer.extract(opentracing.FORMAT_HTTP_HEADERS, req.headers);

  const span = tracer.startSpan(req.path, {
    childOf: wireCtx,
    tags: {
      [opentracing.Tags.SPAN_KIND]: opentracing.Tags.SPAN_KIND_RPC_SERVER,
      [opentracing.Tags.HTTP_METHOD]: req.method,
      [opentracing.Tags.HTTP_URL]: req.url,
    },
  });

  req.span = span;

  res.on("finish", () => {
    span.setTag(opentracing.Tags.HTTP_STATUS_CODE, res.statusCode);
    span.finish();
  });

  next();
};

module.exports = tracingMiddleware;
```
