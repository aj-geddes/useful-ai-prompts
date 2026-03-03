---
name: real-time-features
description: >
  Implement real-time functionality using WebSockets, Server-Sent Events (SSE),
  or long polling. Use when building chat applications, live dashboards,
  collaborative editing, notifications, or any feature requiring instant
  updates.
---

# Real-Time Features

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement real-time bidirectional communication between clients and servers for instant data synchronization and live updates.

## When to Use

- Chat and messaging applications
- Live dashboards and analytics
- Collaborative editing (Google Docs-style)
- Real-time notifications
- Live sports scores or stock tickers
- Multiplayer games
- Live auctions or bidding systems
- IoT device monitoring
- Real-time location tracking

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [WebSocket Server (Node.js)](references/websocket-server-nodejs.md) | WebSocket Server (Node.js) |
| [WebSocket Client (React)](references/websocket-client-react.md) | WebSocket Client (React) |
| [Server-Sent Events (SSE)](references/server-sent-events-sse.md) | Server-Sent Events (SSE) |
| [Socket.IO (Production-Ready)](references/socketio-production-ready.md) | Socket.IO (Production-Ready) |

## Best Practices

### ✅ DO

- Implement reconnection logic with exponential backoff
- Use heartbeat/ping-pong to detect dead connections
- Validate and sanitize all messages
- Implement authentication and authorization
- Handle connection limits and rate limiting
- Use compression for large payloads
- Implement proper error handling
- Monitor connection health
- Use rooms/channels for targeted messaging
- Implement graceful shutdown

### ❌ DON'T

- Send sensitive data without encryption
- Keep connections open indefinitely without cleanup
- Broadcast to all users when targeted messaging suffices
- Ignore connection state management
- Send large payloads frequently
- Skip message validation
- Forget about mobile/unstable connections
- Ignore scaling considerations
