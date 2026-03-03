# Global Secondary Indexes (GSI)

## Global Secondary Indexes (GSI)

```javascript
// Add GSI for querying by email
const gsiParams = {
  TableName: "users",
  AttributeDefinitions: [{ AttributeName: "email", AttributeType: "S" }],
  GlobalSecondaryIndexes: [
    {
      IndexName: "emailIndex",
      KeySchema: [{ AttributeName: "email", KeyType: "HASH" }],
      Projection: {
        ProjectionType: "ALL", // Return all attributes
      },
      BillingMode: "PAY_PER_REQUEST",
    },
  ],
};

// GSI with composite key for time-based queries
const timeIndexParams = {
  GlobalSecondaryIndexes: [
    {
      IndexName: "userCreatedIndex",
      KeySchema: [
        { AttributeName: "userId", KeyType: "HASH" },
        { AttributeName: "createdAt", KeyType: "RANGE" },
      ],
      Projection: { ProjectionType: "ALL" },
      BillingMode: "PAY_PER_REQUEST",
    },
  ],
};
```
