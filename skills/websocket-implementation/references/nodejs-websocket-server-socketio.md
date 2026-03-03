# Node.js WebSocket Server (Socket.IO)

## Node.js WebSocket Server (Socket.IO)

```javascript
const express = require("express");
const http = require("http");
const socketIo = require("socket.io");
const redis = require("redis");

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: { origin: "*" },
  transports: ["websocket", "polling"],
  reconnection: true,
  reconnectionDelay: 1000,
  reconnectionDelayMax: 5000,
  reconnectionAttempts: 5,
});

// Redis adapter for horizontal scaling
const redisClient = redis.createClient();
const { createAdapter } = require("@socket.io/redis-adapter");

io.adapter(createAdapter(redisClient, redisClient.duplicate()));

// Connection management
const connectedUsers = new Map();

io.on("connection", (socket) => {
  console.log(`User connected: ${socket.id}`);

  // Store user connection
  socket.on("auth", (userData) => {
    connectedUsers.set(socket.id, {
      userId: userData.id,
      username: userData.username,
      socketId: socket.id,
      connectedAt: new Date(),
    });

    // Join user-specific room
    socket.join(`user:${userData.id}`);
    socket.join("authenticated_users");

    // Notify others user is online
    io.to("authenticated_users").emit("user:online", {
      userId: userData.id,
      username: userData.username,
      timestamp: new Date(),
    });

    console.log(`User authenticated: ${userData.username}`);
  });

  // Chat messaging
  socket.on("chat:message", (message) => {
    const user = connectedUsers.get(socket.id);

    if (!user) {
      socket.emit("error", { message: "Not authenticated" });
      return;
    }

    const chatMessage = {
      id: `msg_${Date.now()}`,
      senderId: user.userId,
      senderName: user.username,
      text: message.text,
      roomId: message.roomId,
      timestamp: new Date(),
      status: "delivered",
    };

    // Save to database
    Message.create(chatMessage);

    // Broadcast to room
    io.to(`room:${message.roomId}`).emit("chat:message", chatMessage);

    // Update message status
    setTimeout(() => {
      socket.emit("chat:message:ack", {
        messageId: chatMessage.id,
        status: "read",
      });
    }, 100);
  });

  // Room management
  socket.on("room:join", (roomId) => {
    socket.join(`room:${roomId}`);

    const user = connectedUsers.get(socket.id);
    io.to(`room:${roomId}`).emit("room:user:joined", {
      userId: user.userId,
      username: user.username,
      timestamp: new Date(),
    });
  });

  socket.on("room:leave", (roomId) => {
    socket.leave(`room:${roomId}`);

    const user = connectedUsers.get(socket.id);
    io.to(`room:${roomId}`).emit("room:user:left", {
      userId: user.userId,
      timestamp: new Date(),
    });
  });

  // Typing indicator
  socket.on("typing:start", (roomId) => {
    const user = connectedUsers.get(socket.id);
    io.to(`room:${roomId}`).emit("typing:indicator", {
      userId: user.userId,
      username: user.username,
      isTyping: true,
    });
  });

  socket.on("typing:stop", (roomId) => {
    const user = connectedUsers.get(socket.id);
    io.to(`room:${roomId}`).emit("typing:indicator", {
      userId: user.userId,
      isTyping: false,
    });
  });

  // Handle disconnection
  socket.on("disconnect", () => {
    const user = connectedUsers.get(socket.id);

    if (user) {
      connectedUsers.delete(socket.id);
      io.to("authenticated_users").emit("user:offline", {
        userId: user.userId,
        timestamp: new Date(),
      });

      console.log(`User disconnected: ${user.username}`);
    }
  });

  // Error handling
  socket.on("error", (error) => {
    console.error(`Socket error: ${error}`);
    socket.emit("error", { message: "An error occurred" });
  });
});

// Server methods
const broadcastUserUpdate = (userId, data) => {
  io.to(`user:${userId}`).emit("user:update", data);
};

const notifyRoom = (roomId, event, data) => {
  io.to(`room:${roomId}`).emit(event, data);
};

const sendDirectMessage = (userId, event, data) => {
  io.to(`user:${userId}`).emit(event, data);
};

server.listen(3000, () => {
  console.log("WebSocket server listening on port 3000");
});
```
