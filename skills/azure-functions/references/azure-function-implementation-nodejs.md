# Azure Function Implementation (Node.js)

## Azure Function Implementation (Node.js)

```javascript
// HttpTrigger/index.js
module.exports = async function (context, req) {
  context.log("HTTP trigger function processed request.");

  // Extract request data
  const name = req.query.name || (req.body && req.body.name);
  const requestId = context.traceContext.traceparent;

  try {
    // Validate input
    if (!name) {
      return {
        status: 400,
        body: { error: "Name parameter is required" },
      };
    }

    // Business logic
    const response = {
      message: `Hello ${name}!`,
      timestamp: new Date().toISOString(),
      requestId: requestId,
    };

    // Log to Application Insights
    context.log({
      level: "info",
      message: "Request processed successfully",
      name: name,
      requestId: requestId,
    });

    return {
      status: 200,
      headers: {
        "Content-Type": "application/json",
        "X-Request-ID": requestId,
      },
      body: response,
    };
  } catch (error) {
    context.log.error("Error processing request:", error);

    return {
      status: 500,
      body: { error: "Internal server error" },
    };
  }
};

// TimerTrigger/index.js
module.exports = async function (context, myTimer) {
  const timeStamp = new Date().toISOString();

  if (myTimer.isPastDue) {
    context.log("Timer function is running late!");
  }

  // Process scheduled job
  context.log(`Timer trigger function ran at ${timeStamp}`);
  context.log("Processing batch job...");

  // Simulate work
  await new Promise((resolve) => setTimeout(resolve, 1000));

  context.log("Batch job completed");
};

// ServiceBusQueueTrigger/index.js
module.exports = async function (context, mySbMsg) {
  context.log("ServiceBus queue trigger function processed message:", mySbMsg);

  try {
    const messageBody =
      typeof mySbMsg === "string" ? JSON.parse(mySbMsg) : mySbMsg;

    // Process message
    await processMessage(messageBody);

    context.log("Message processed successfully");
  } catch (error) {
    context.log.error("Error processing message:", error);
    throw error; // Re-queue message
  }
};

async function processMessage(messageBody) {
  // Business logic here
  return true;
}
```
