# Monitoring and Observability

## Monitoring and Observability

```python
# Monitoring helper
import json
import logging
from aws_lambda_powertools import Logger, Tracer, Metrics
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()
tracer = Tracer()
metrics = Metrics()

@logger.inject_lambda_context
@tracer.capture_lambda_handler
def handler(event: dict, context: LambdaContext) -> dict:
    try:
        logger.info("Processing event", extra={"event": event})

        # Add custom metrics
        metrics.add_metric(
            name="OrderProcessed",
            unit="Count",
            value=1
        )
        metrics.add_metric(
            name="OrderAmount",
            unit="None",
            value=event.get('amount', 0)
        )

        # Business logic
        result = process_order(event)

        logger.info("Order processed successfully", extra={"orderId": result['orderId']})
        return result

    except Exception as e:
        logger.exception("Error processing order")
        metrics.add_metric(
            name="OrderFailed",
            unit="Count",
            value=1
        )
        raise

    finally:
        metrics.flush()

def process_order(event):
    return {"orderId": event.get("id"), "status": "completed"}
```
