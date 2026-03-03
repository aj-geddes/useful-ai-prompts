# Browser WebSocket Client

## Browser WebSocket Client

```javascript
class WebSocketClient {
  constructor(url, options = {}) {
    this.url = url;
    this.socket = null;
    this.reconnectAttempts = 0;
    this.maxReconnectAttempts = options.maxReconnectAttempts || 5;
    this.reconnectDelay = options.reconnectDelay || 1000;
    this.listeners = new Map();
    this.messageQueue = [];
    this.isAuthenticated = false;

    this.connect();
  }

  connect() {
    this.socket = io(this.url, {
      reconnection: true,
      reconnectionDelay: this.reconnectDelay,
      reconnectionAttempts: this.maxReconnectAttempts,
    });

    this.socket.on("connect", () => {
      console.log("Connected to server");
      this.reconnectAttempts = 0;
      this.processMessageQueue();
    });

    this.socket.on("disconnect", () => {
      console.log("Disconnected from server");
    });

    this.socket.on("error", (error) => {
      console.error("Socket error:", error);
      this.emit("error", error);
    });

    this.socket.on("connect_error", (error) => {
      console.error("Connection error:", error);
    });
  }

  authenticate(userData) {
    this.socket.emit("auth", userData, (response) => {
      if (response.success) {
        this.isAuthenticated = true;
        this.emit("authenticated");
      }
    });
  }

  on(event, callback) {
    this.socket.on(event, callback);

    if (!this.listeners.has(event)) {
      this.listeners.set(event, []);
    }
    this.listeners.get(event).push(callback);
  }

  emit(event, data, callback) {
    if (!this.socket.connected) {
      this.messageQueue.push({ event, data, callback });
      return;
    }

    this.socket.emit(event, data, callback);
  }

  processMessageQueue() {
    while (this.messageQueue.length > 0) {
      const { event, data, callback } = this.messageQueue.shift();
      this.socket.emit(event, data, callback);
    }
  }

  joinRoom(roomId) {
    this.emit("room:join", roomId);
  }

  leaveRoom(roomId) {
    this.emit("room:leave", roomId);
  }

  sendMessage(roomId, text) {
    this.emit("chat:message", { roomId, text });
  }

  setTypingIndicator(roomId, isTyping) {
    if (isTyping) {
      this.emit("typing:start", roomId);
    } else {
      this.emit("typing:stop", roomId);
    }
  }

  disconnect() {
    this.socket.disconnect();
  }
}

// Usage
const client = new WebSocketClient("http://localhost:3000");

client.on("chat:message", (message) => {
  console.log("Received message:", message);
  displayMessage(message);
});

client.on("typing:indicator", (data) => {
  updateTypingIndicator(data);
});

client.on("user:online", (user) => {
  updateUserStatus(user.userId, "online");
});

client.authenticate({ id: "user123", username: "john" });
client.joinRoom("room1");
client.sendMessage("room1", "Hello everyone!");
```
