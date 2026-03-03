# Schema Validation

## Schema Validation

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
          description: "Product name (required)",
        },
        price: {
          bsonType: "decimal",
          minimum: 0,
          description: "Price must be positive",
        },
        category: {
          enum: ["electronics", "clothing", "food"],
          description: "Category must be one of listed values",
        },
        tags: {
          bsonType: "array",
          items: { bsonType: "string" },
        },
        createdAt: {
          bsonType: "date",
        },
      },
    },
  },
});
```
