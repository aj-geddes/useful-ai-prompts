# Scaling with Redis

## Scaling with Redis

```javascript
const redis = require("redis");
const { createAdapter } = require("@socket.io/redis-adapter");
const { createClient } = require("redis");

const pubClient = createClient({ host: "redis", port: 6379 });
const subClient = pubClient.duplicate();

io.adapter(createAdapter(pubClient, subClient));

// Publish to multiple servers
io.emit("user:action", { userId: 123, action: "login" });

// Subscribe to events from other servers
redisClient.subscribe("notifications", (message) => {
  const notification = JSON.parse(message);
  io.to(`user:${notification.userId}`).emit("notification", notification);
});
```
