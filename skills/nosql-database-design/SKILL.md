---
name: nosql-database-design
description: >
  Design NoSQL database schemas for MongoDB and DynamoDB. Use when modeling
  document structures, designing collections, or planning NoSQL data
  architectures.
---

# NoSQL Database Design

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

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

## Quick Start

Minimal working example:

```javascript
// Single document with embedded arrays
db.createCollection("users");

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
    zipCode: "10001",
  },

  // Embedded array of items
  orders: [
    {
      orderId: ObjectId("..."),
      date: new Date(),
      total: 149.99,
    },
    {
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Document Structure Design](references/document-structure-design.md) | Document Structure Design |
| [Indexing in MongoDB](references/indexing-in-mongodb.md) | Indexing in MongoDB |
| [Schema Validation](references/schema-validation.md) | Schema Validation |
| [Table Structure](references/table-structure.md) | Table Structure |
| [Global Secondary Indexes (GSI)](references/global-secondary-indexes-gsi.md) | Global Secondary Indexes (GSI) |
| [DynamoDB Item Operations](references/dynamodb-item-operations.md) | DynamoDB Item Operations |

## Best Practices

### ✅ DO

- Design schemas around query access patterns first — in NoSQL, the data model serves the queries, not the other way around
- Embed related data that is read together into a single document to minimize round-trips (e.g., order with its line items)
- Use compound partition keys and sort keys in DynamoDB to support multiple query patterns on a single table
- Set schema validation rules (MongoDB `$jsonSchema`, DynamoDB attribute constraints) to catch malformed documents at write time
- Plan for document growth — use the bucket pattern or reference pattern when embedded arrays can grow unbounded
- Create indexes that cover your most frequent queries and monitor index usage to remove unused ones

### ❌ DON'T

- Normalize data into many small collections/tables the way you would in a relational database — this forces expensive joins or multiple queries
- Use unbounded arrays in embedded documents — MongoDB has a 16 MB document limit and large arrays degrade write performance
- Design DynamoDB tables with a single hot partition key — distribute writes evenly to avoid throttling
- Skip capacity planning for GSIs in DynamoDB — each GSI consumes its own read/write throughput independently
