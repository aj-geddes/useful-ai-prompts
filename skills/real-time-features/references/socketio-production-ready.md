# Socket.IO (Production-Ready)

## Socket.IO (Production-Ready)

```typescript
// server.ts
import { Server } from "socket.io";
import { createServer } from "http";

const httpServer = createServer();
const io = new Server(httpServer, {
  cors: {
    origin: process.env.CLIENT_URL || "http://localhost:3000",
    methods: ["GET", "POST"],
  },
  pingTimeout: 60000,
  pingInterval: 25000,
});

// Middleware
io.use((socket, next) => {
  const token = socket.handshake.auth.token;
  if (isValidToken(token)) {
    next();
  } else {
    next(new Error("Authentication error"));
  }
});

io.on("connection", (socket) => {
  console.log(`User connected: ${socket.id}`);

  // Join room
  socket.on("join-room", (roomId: string) => {
    socket.join(roomId);
    socket.to(roomId).emit("user-joined", {
      userId: socket.id,
      timestamp: Date.now(),
    });
  });

  // Handle messages
  socket.on("message", (data) => {
    const roomId = Array.from(socket.rooms)[1]; // First is own ID
    io.to(roomId).emit("message", {
      ...data,
      userId: socket.id,
      timestamp: Date.now(),
    });
  });

  // Typing indicator
  socket.on("typing", (isTyping: boolean) => {
    const roomId = Array.from(socket.rooms)[1];
    socket.to(roomId).emit("user-typing", {
      userId: socket.id,
      isTyping,
    });
  });

  socket.on("disconnect", () => {
    console.log(`User disconnected: ${socket.id}`);
  });
});

httpServer.listen(3001);

function isValidToken(token: string): boolean {
  // Implement token validation
  return true;
}
```
