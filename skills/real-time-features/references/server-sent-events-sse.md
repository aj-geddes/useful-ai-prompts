# Server-Sent Events (SSE)

## Server-Sent Events (SSE)

```typescript
// server.ts - SSE endpoint
import express from "express";

const app = express();

interface Client {
  id: string;
  res: express.Response;
}

class SSEManager {
  private clients: Client[] = [];

  addClient(id: string, res: express.Response): void {
    // Set SSE headers
    res.setHeader("Content-Type", "text/event-stream");
    res.setHeader("Cache-Control", "no-cache");
    res.setHeader("Connection", "keep-alive");
    res.setHeader("Access-Control-Allow-Origin", "*");

    this.clients.push({ id, res });

    // Send initial connection event
    this.sendToClient(id, {
      type: "connected",
      clientId: id,
      timestamp: Date.now(),
    });

    console.log(`Client ${id} connected. Total: ${this.clients.length}`);
  }

  removeClient(id: string): void {
    this.clients = this.clients.filter((client) => client.id !== id);
    console.log(`Client ${id} disconnected. Total: ${this.clients.length}`);
  }

  sendToClient(id: string, data: any): void {
    const client = this.clients.find((c) => c.id === id);
    if (client) {
      client.res.write(`data: ${JSON.stringify(data)}\n\n`);
    }
  }

  broadcast(data: any, excludeId?: string): void {
    const message = `data: ${JSON.stringify(data)}\n\n`;
    this.clients.forEach((client) => {
      if (client.id !== excludeId) {
        client.res.write(message);
      }
    });
  }

  sendEvent(event: string, data: any): void {
    const message = `event: ${event}\ndata: ${JSON.stringify(data)}\n\n`;
    this.clients.forEach((client) => {
      client.res.write(message);
    });
  }
}

const sseManager = new SSEManager();

app.get("/events", (req, res) => {
  const clientId = Math.random().toString(36).substr(2, 9);

  sseManager.addClient(clientId, res);

  req.on("close", () => {
    sseManager.removeClient(clientId);
  });
});

// Simulate real-time updates
setInterval(() => {
  sseManager.broadcast({
    type: "update",
    value: Math.random() * 100,
    timestamp: Date.now(),
  });
}, 5000);

app.listen(3000, () => {
  console.log("SSE server running on port 3000");
});
```

```typescript
// client.ts - SSE client
class SSEClient {
  private eventSource: EventSource | null = null;
  private reconnectAttempts = 0;
  private maxReconnectAttempts = 5;

  connect(
    url: string,
    handlers: {
      onMessage?: (data: any) => void;
      onError?: (error: Event) => void;
      onOpen?: () => void;
    },
  ): void {
    this.eventSource = new EventSource(url);

    this.eventSource.onopen = () => {
      console.log("SSE connected");
      this.reconnectAttempts = 0;
      handlers.onOpen?.();
    };

    this.eventSource.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        handlers.onMessage?.(data);
      } catch (error) {
        console.error("Failed to parse SSE data:", error);
      }
    };

    this.eventSource.onerror = (error) => {
      console.error("SSE error:", error);
      handlers.onError?.(error);

      if (this.reconnectAttempts < this.maxReconnectAttempts) {
        this.reconnectAttempts++;
        setTimeout(() => {
          console.log("Reconnecting to SSE...");
          this.connect(url, handlers);
        }, 3000);
      }
    };

    // Custom event listeners
    this.eventSource.addEventListener("custom-event", (event: any) => {
      console.log("Custom event:", JSON.parse(event.data));
    });
  }

  disconnect(): void {
    this.eventSource?.close();
    this.eventSource = null;
  }
}

// Usage
const client = new SSEClient();
client.connect("http://localhost:3000/events", {
  onMessage: (data) => {
    console.log("Received:", data);
  },
  onOpen: () => {
    console.log("Connected to server");
  },
});
```
