# DynamoDB Item Operations

## DynamoDB Item Operations

```javascript
// Put item (insert/update)
const putParams = {
  TableName: "users",
  Item: {
    userId: { S: "user-123" },
    email: { S: "john@example.com" },
    name: { S: "John Doe" },
    createdAt: { N: Date.now().toString() },
    metadata: {
      M: {
        joinDate: { N: Date.now().toString() },
        source: { S: "web" },
      },
    },
  },
};

// Query using GSI
const queryParams = {
  TableName: "users",
  IndexName: "emailIndex",
  KeyConditionExpression: "email = :email",
  ExpressionAttributeValues: {
    ":email": { S: "john@example.com" },
  },
};

// Batch get items
const batchGetParams = {
  RequestItems: {
    users: {
      Keys: [{ userId: { S: "user-123" } }, { userId: { S: "user-456" } }],
    },
  },
};
```
