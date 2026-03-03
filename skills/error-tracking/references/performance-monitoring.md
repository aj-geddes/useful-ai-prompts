# Performance Monitoring

## Performance Monitoring

```javascript
// performance.js
const Sentry = require("@sentry/node");

const transaction = Sentry.startTransaction({
  name: "process_order",
  op: "task",
  data: { orderId: "12345" },
});

const dbSpan = transaction.startChild({
  op: "db",
  description: "Save order to database",
});
saveOrderToDb(order);
dbSpan.finish();

const paymentSpan = transaction.startChild({
  op: "http.client",
  description: "Process payment",
});
processPayment(order);
paymentSpan.finish();

transaction.setStatus("ok");
transaction.finish();
```
