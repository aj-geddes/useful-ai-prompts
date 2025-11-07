---
name: nosql-database-design
description: Design NoSQL database schemas for MongoDB and DynamoDB. Use when modeling document structures, designing collections, or planning NoSQL data architectures.
---

# NoSQL Database Design

## Overview

Design scalable NoSQL schemas for MongoDB (document) and DynamoDB (key-value). Covers data modeling patterns, denormalization strategies, and query optimization for NoSQL systems.

## When to Use

- MongoDB collection design
- DynamoDB table and index design
- Document structure modeling
- Embedding vs. referencing decisions
- Query pattern optimization
- NoSQL indexing strategies
- Data denormalization planning

## MongoDB Schema Design

### Document Structure Design

**MongoDB - Embedded Documents:**

```javascript
// Single document with embedded arrays
db.createCollection("users")

db.users.insertOne({
  _id: ObjectId("..."),
  email: "john@example.com",
  name: "John Doe",
  createdAt: new Date(),

  // Embedded address
  address: {
    street: "123 Main St",
    city: "New York",
    state: "NY",
    zipCode: "10001"
  },

  // Embedded array of items
  orders: [
    {
      orderId: ObjectId("..."),
      date: new Date(),
      total: 149.99
    },
    {
      orderId: ObjectId("..."),
      date: new Date(),
      total: 89.99
    }
  ]
})
```

**MongoDB - Referenced Documents:**

```javascript
// Separate collections with references
db.createCollection("users")
db.createCollection("orders")

db.users.insertOne({
  _id: ObjectId("..."),
  email: "john@example.com",
  name: "John Doe"
})

db.orders.insertMany([
  {
    _id: ObjectId("..."),
    userId: ObjectId("..."),  // Reference to user
    orderDate: new Date(),
    total: 149.99
  },
  {
    _id: ObjectId("..."),
    userId: ObjectId("..."),
    orderDate: new Date(),
    total: 89.99
  }
])

// Query with $lookup for JOINs
db.orders.aggregate([
  {
    $match: { userId: ObjectId("...") }
  },
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "user"
    }
  }
])
```

### Indexing in MongoDB

```javascript
// Single field index
db.users.createIndex({ email: 1 })
db.orders.createIndex({ createdAt: -1 })

// Compound index
db.orders.createIndex({ userId: 1, createdAt: -1 })

// Text index for search
db.products.createIndex({ name: "text", description: "text" })

// Geospatial index
db.stores.createIndex({ location: "2dsphere" })

// TTL index for auto-expiration
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 })

// Sparse index (only documents with field)
db.users.createIndex({ phone: 1 }, { sparse: true })

// Check index usage
db.users.aggregate([{ $indexStats: {} }])
```

### Schema Validation

```javascript
// Define collection validation schema
db.createCollection("products", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "price", "category"],
      properties: {
        _id: { bsonType: "objectId" },
        name: {
          bsonType: "string",
          description: "Product name (required)"
        },
        price: {
          bsonType: "decimal",
          minimum: 0,
          description: "Price must be positive"
        },
        category: {
          enum: ["electronics", "clothing", "food"],
          description: "Category must be one of listed values"
        },
        tags: {
          bsonType: "array",
          items: { bsonType: "string" }
        },
        createdAt: {
          bsonType: "date"
        }
      }
    }
  }
})
```

## DynamoDB Schema Design

### Table Structure

```javascript
// DynamoDB table with single primary key
const TableName = "users"
const params = {
  TableName,
  KeySchema: [
    { AttributeName: "userId", KeyType: "HASH" }  // Partition key
  ],
  AttributeDefinitions: [
    { AttributeName: "userId", AttributeType: "S" }  // String
  ],
  BillingMode: "PAY_PER_REQUEST"  // On-demand
}

// DynamoDB table with composite primary key
const ordersParams = {
  TableName: "orders",
  KeySchema: [
    { AttributeName: "userId", KeyType: "HASH" },      // Partition key
    { AttributeName: "orderId", KeyType: "RANGE" }    // Sort key
  ],
  AttributeDefinitions: [
    { AttributeName: "userId", AttributeType: "S" },
    { AttributeName: "orderId", AttributeType: "S" }
  ],
  BillingMode: "PAY_PER_REQUEST"
}
```

### Global Secondary Indexes (GSI)

```javascript
// Add GSI for querying by email
const gsiParams = {
  TableName: "users",
  AttributeDefinitions: [
    { AttributeName: "email", AttributeType: "S" }
  ],
  GlobalSecondaryIndexes: [
    {
      IndexName: "emailIndex",
      KeySchema: [
        { AttributeName: "email", KeyType: "HASH" }
      ],
      Projection: {
        ProjectionType: "ALL"  // Return all attributes
      },
      BillingMode: "PAY_PER_REQUEST"
    }
  ]
}

// GSI with composite key for time-based queries
const timeIndexParams = {
  GlobalSecondaryIndexes: [
    {
      IndexName: "userCreatedIndex",
      KeySchema: [
        { AttributeName: "userId", KeyType: "HASH" },
        { AttributeName: "createdAt", KeyType: "RANGE" }
      ],
      Projection: { ProjectionType: "ALL" },
      BillingMode: "PAY_PER_REQUEST"
    }
  ]
}
```

### DynamoDB Item Operations

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
        source: { S: "web" }
      }
    }
  }
}

// Query using GSI
const queryParams = {
  TableName: "users",
  IndexName: "emailIndex",
  KeyConditionExpression: "email = :email",
  ExpressionAttributeValues: {
    ":email": { S: "john@example.com" }
  }
}

// Batch get items
const batchGetParams = {
  RequestItems: {
    "users": {
      Keys: [
        { userId: { S: "user-123" } },
        { userId: { S: "user-456" } }
      ]
    }
  }
}
```

## Denormalization Patterns

**MongoDB - Embedding for Performance:**

```javascript
// Embed frequently accessed data to avoid lookups
db.orders.insertOne({
  _id: ObjectId("..."),
  userId: ObjectId("..."),
  userEmail: "john@example.com",      // Denormalized
  userName: "John Doe",                // Denormalized
  createdAt: new Date(),
  items: [
    {
      productId: ObjectId("..."),
      productName: "Laptop",            // Denormalized
      productPrice: 999.99,             // Denormalized
      quantity: 1
    }
  ]
})
```

**DynamoDB - Denormalization with Consistency:**

```javascript
// Store related data in same item to ensure consistency
const params = {
  TableName: "orders",
  Item: {
    userId: { S: "user-123" },
    orderId: { S: "order-456" },
    orderDate: { N: Date.now().toString() },

    // User data snapshot at order time
    userSnapshot: {
      M: {
        email: { S: "john@example.com" },
        address: { S: "123 Main St" }
      }
    },

    // Items with product information
    items: {
      L: [
        {
          M: {
            productId: { S: "prod-789" },
            name: { S: "Laptop" },
            price: { N: "999.99" },
            quantity: { N: "1" }
          }
        }
      ]
    }
  }
}
```

## Design Patterns

**MongoDB - Time-Series Pattern:**

```javascript
// Efficient time-series data storage
db.sensor_data.insertOne({
  _id: ObjectId("..."),
  sensorId: "sensor-123",
  date: ISODate("2024-01-15"),
  measurements: [
    { time: "12:00", temperature: 72.5, humidity: 45 },
    { time: "12:01", temperature: 72.6, humidity: 45.2 },
    { time: "12:02", temperature: 72.4, humidity: 44.8 }
  ]
})

// Index for efficient queries
db.sensor_data.createIndex({ sensorId: 1, date: -1 })
```

**DynamoDB - One-to-Many Relationship:**

```javascript
// Store one-to-many relationships efficiently
// User comments using userId as partition key, commentId as sort key
const commentParams = {
  TableName: "comments",
  Item: {
    userId: { S: "user-123" },           // Partition key
    commentId: { S: "comment-789" },     // Sort key
    postId: { S: "post-456" },
    content: { S: "Great article!" },
    createdAt: { N: Date.now().toString() }
  }
}
```

## Capacity Planning

**MongoDB - Horizontal Scaling:**

```javascript
// Sharding for large collections
sh.shardCollection("ecommerce.orders", { userId: "hashed" })

// Monitor shard distribution
db.orders.aggregate([
  { $group: { _id: "$userId", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
])
```

**DynamoDB - Partition Key Design:**

```javascript
// Good: Distribute across many keys
// Partition key: "USER#123" (spreads across partitions)
// Sort key: "ORDER#2024-01"

// Bad: Hot partition
// Partition key: "ADMIN" (all admin operations hit same partition)

// Solution: Add timestamp or random suffix
// Partition key: "ADMIN#20240115#random"
```

## Migration Considerations

- Plan data migration strategy
- Consider consistency requirements
- Test query patterns before finalizing schema
- Monitor performance after deployment
- Document relationships and access patterns
- Plan for schema evolution

## Resources

- [MongoDB Schema Design Best Practices](https://docs.mongodb.com/manual/core/schema-validation/)
- [DynamoDB Best Practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)
- [MongoDB vs Relational Data Modeling](https://docs.mongodb.com/manual/core/schema-validation/)
