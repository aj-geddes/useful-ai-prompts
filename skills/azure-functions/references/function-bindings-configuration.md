# Function Bindings Configuration

## Function Bindings Configuration

```json
{
  "scriptFile": "index.js",
  "bindings": [
    {
      "authLevel": "anonymous",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": ["get", "post"],
      "route": "api/{*route}"
    },
    {
      "type": "http",
      "direction": "out",
      "name": "$return"
    },
    {
      "type": "queue",
      "direction": "out",
      "name": "myQueueItem",
      "queueName": "myqueue",
      "connection": "AzureWebJobsStorage"
    },
    {
      "type": "serviceBus",
      "direction": "in",
      "name": "mySbMsg",
      "queueName": "myqueue",
      "connection": "ServiceBusConnection",
      "cardinality": "one"
    },
    {
      "type": "blob",
      "direction": "in",
      "name": "inputBlob",
      "path": "input/{name}",
      "connection": "AzureWebJobsStorage"
    },
    {
      "type": "blob",
      "direction": "out",
      "name": "outputBlob",
      "path": "output/{name}",
      "connection": "AzureWebJobsStorage"
    }
  ]
}
```
