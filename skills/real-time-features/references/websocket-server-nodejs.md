# WebSocket Server (Node.js)

## WebSocket Server (Node.js)

```typescript
// server.ts
import WebSocket, { WebSocketServer } from "ws";
import { createServer } from "http";

interface Message {
  type: "join" | "message" | "leave" | "typing";
  userId: string;
  username: string;
  content?: string;
  timestamp: number;
}

interface Client {
  ws: WebSocket;
  userId: string;
  username: string;
  roomId: string;
}

class ChatServer {
  private wss: WebSocketServer;
  private clients: Map<string, Client> = new Map();
  private rooms: Map<string, Set<string>> = new Map();

  constructor(port: number) {
    const server = createServer();
    this.wss = new WebSocketServer({ server });

    this.wss.on("connection", this.handleConnection.bind(this));

    server.listen(port, () => {
      console.log(`WebSocket server running on port ${port}`);
    });

    // Heartbeat to detect disconnections
    this.startHeartbeat();
  }

  private handleConnection(ws: WebSocket): void {
    const clientId = this.generateId();

    console.log(`New connection: ${clientId}`);

    ws.on("message", (data: string) => {
      try {
        const message: Message = JSON.parse(data.toString());
        this.handleMessage(clientId, message, ws);
      } catch (error) {
        console.error("Invalid message format:", error);
      }
    });

    ws.on("close", () => {
      this.handleDisconnect(clientId);
    });

    ws.on("error", (error) => {
      console.error(`WebSocket error for ${clientId}:`, error);
    });

    // Keep connection alive
    (ws as any).isAlive = true;
    ws.on("pong", () => {
      (ws as any).isAlive = true;
    });
  }

  private handleMessage(
    clientId: string,
    message: Message,
    ws: WebSocket,
  ): void {
    switch (message.type) {
      case "join":
        this.handleJoin(clientId, message, ws);
        break;

      case "message":
        this.broadcastToRoom(clientId, message);
        break;

      case "typing":
        this.broadcastToRoom(clientId, message, [clientId]);
        break;

      case "leave":
        this.handleDisconnect(clientId);
        break;
    }
  }

  private handleJoin(clientId: string, message: Message, ws: WebSocket): void {
    const client: Client = {
      ws,
      userId: message.userId,
      username: message.username,
      roomId: "general", // Could be dynamic
    };

    this.clients.set(clientId, client);

    // Add to room
    if (!this.rooms.has(client.roomId)) {
      this.rooms.set(client.roomId, new Set());
    }
    this.rooms.get(client.roomId)!.add(clientId);

    // Notify room
    this.broadcastToRoom(clientId, {
      type: "join",
      userId: message.userId,
      username: message.username,
      timestamp: Date.now(),
    });

    // Send room state to new user
    this.sendRoomState(clientId);
  }

  private broadcastToRoom(
    senderId: string,
    message: Message,
    exclude: string[] = [],
  ): void {
    const sender = this.clients.get(senderId);
    if (!sender) return;

    const roomClients = this.rooms.get(sender.roomId);
    if (!roomClients) return;

    const payload = JSON.stringify(message);

    roomClients.forEach((clientId) => {
      if (!exclude.includes(clientId)) {
        const client = this.clients.get(clientId);
        if (client && client.ws.readyState === WebSocket.OPEN) {
          client.ws.send(payload);
        }
      }
    });
  }

  private sendRoomState(clientId: string): void {
    const client = this.clients.get(clientId);
    if (!client) return;

    const roomClients = this.rooms.get(client.roomId);
    if (!roomClients) return;

    const users = Array.from(roomClients)
      .map((id) => this.clients.get(id))
      .filter((c) => c && c.userId !== client.userId)
      .map((c) => ({ userId: c!.userId, username: c!.username }));

    client.ws.send(
      JSON.stringify({
        type: "room_state",
        users,
        timestamp: Date.now(),
      }),
    );
  }

  private handleDisconnect(clientId: string): void {
    const client = this.clients.get(clientId);
    if (!client) return;

    // Remove from room
    const roomClients = this.rooms.get(client.roomId);
    if (roomClients) {
      roomClients.delete(clientId);

      // Notify others
      this.broadcastToRoom(clientId, {
        type: "leave",
        userId: client.userId,
        username: client.username,
        timestamp: Date.now(),
      });
    }

    this.clients.delete(clientId);
    console.log(`Client disconnected: ${clientId}`);
  }

  private startHeartbeat(): void {
    setInterval(() => {
      this.wss.clients.forEach((ws: any) => {
        if (ws.isAlive === false) {
          return ws.terminate();
        }
        ws.isAlive = false;
        ws.ping();
      });
    }, 30000);
  }

  private generateId(): string {
    return Math.random().toString(36).substr(2, 9);
  }
}

// Start server
new ChatServer(8080);
```
