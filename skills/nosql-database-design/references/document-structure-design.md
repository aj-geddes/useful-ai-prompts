# Document Structure Design

## Document Structure Design

**MongoDB - Embedded Documents:**

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
      orderId: ObjectId("..."),
      date: new Date(),
      total: 89.99,
    },
  ],
});
```

**MongoDB - Referenced Documents:**

```javascript
// Separate collections with references
db.createCollection("users");
db.createCollection("orders");

db.users.insertOne({
  _id: ObjectId("..."),
  email: "john@example.com",
  name: "John Doe",
});

db.orders.insertMany([
  {
    _id: ObjectId("..."),
    userId: ObjectId("..."), // Reference to user
    orderDate: new Date(),
    total: 149.99,
  },
  {
    _id: ObjectId("..."),
    userId: ObjectId("..."),
    orderDate: new Date(),
    total: 89.99,
  },
]);

// Query with $lookup for JOINs
db.orders.aggregate([
  {
    $match: { userId: ObjectId("...") },
  },
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "user",
    },
  },
]);
```
