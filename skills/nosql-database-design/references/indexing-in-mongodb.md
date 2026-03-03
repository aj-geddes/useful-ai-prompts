# Indexing in MongoDB

## Indexing in MongoDB

```javascript
// Single field index
db.users.createIndex({ email: 1 });
db.orders.createIndex({ createdAt: -1 });

// Compound index
db.orders.createIndex({ userId: 1, createdAt: -1 });

// Text index for search
db.products.createIndex({ name: "text", description: "text" });

// Geospatial index
db.stores.createIndex({ location: "2dsphere" });

// TTL index for auto-expiration
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 });

// Sparse index (only documents with field)
db.users.createIndex({ phone: 1 }, { sparse: true });

// Check index usage
db.users.aggregate([{ $indexStats: {} }]);
```
