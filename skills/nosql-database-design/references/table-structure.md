# Table Structure

## Table Structure

```javascript
// DynamoDB table with single primary key
const TableName = "users";
const params = {
  TableName,
  KeySchema: [
    { AttributeName: "userId", KeyType: "HASH" }, // Partition key
  ],
  AttributeDefinitions: [
    { AttributeName: "userId", AttributeType: "S" }, // String
  ],
  BillingMode: "PAY_PER_REQUEST", // On-demand
};

// DynamoDB table with composite primary key
const ordersParams = {
  TableName: "orders",
  KeySchema: [
    { AttributeName: "userId", KeyType: "HASH" }, // Partition key
    { AttributeName: "orderId", KeyType: "RANGE" }, // Sort key
  ],
  AttributeDefinitions: [
    { AttributeName: "userId", AttributeType: "S" },
    { AttributeName: "orderId", AttributeType: "S" },
  ],
  BillingMode: "PAY_PER_REQUEST",
};
```
