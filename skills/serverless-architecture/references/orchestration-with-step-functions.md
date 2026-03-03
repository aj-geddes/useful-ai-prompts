# Orchestration with Step Functions

## Orchestration with Step Functions

```json
{
  "Comment": "Order processing workflow",
  "StartAt": "ValidateOrder",
  "States": {
    "ValidateOrder": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:validateOrder",
      "Next": "CheckInventory",
      "Catch": [
        {
          "ErrorEquals": ["InvalidOrder"],
          "Next": "OrderFailed"
        }
      ]
    },
    "CheckInventory": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:checkInventory",
      "Next": "InventoryDecision"
    },
    "InventoryDecision": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.inStock",
          "BooleanEquals": true,
          "Next": "ProcessPayment"
        }
      ],
      "Default": "OutOfStock"
    },
    "ProcessPayment": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:processPayment",
      "Next": "PaymentDecision",
      "Retry": [
        {
          "ErrorEquals": ["PaymentError"],
          "IntervalSeconds": 2,
          "MaxAttempts": 3,
          "BackoffRate": 2.0
        }
      ]
    },
    "PaymentDecision": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.paymentApproved",
          "BooleanEquals": true,
          "Next": "ShipOrder"
        }
      ],
      "Default": "PaymentFailed"
    },
    "ShipOrder": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:shipOrder",
      "Next": "NotifyCustomer"
    },
    "NotifyCustomer": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sns:publish",
      "Parameters": {
        "TopicArn": "arn:aws:sns:region:account:order-updates",
        "Message": {
          "orderId.$": "$.orderId",
          "status": "shipped"
        }
      },
      "Next": "OrderSuccess"
    },
    "OrderSuccess": {
      "Type": "Succeed"
    },
    "OutOfStock": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:notifyOutOfStock",
      "Next": "OrderFailed"
    },
    "PaymentFailed": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:handlePaymentFailure",
      "Next": "OrderFailed"
    },
    "OrderFailed": {
      "Type": "Fail",
      "Error": "OrderFailed",
      "Cause": "Order processing failed"
    }
  }
}
```
