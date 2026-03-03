---
name: websocket-implementation
description: >
  Implement real-time bidirectional communication with WebSockets including
  connection management, message routing, and scaling. Use when building
  real-time features, chat systems, live notifications, or collaborative
  applications.
---

# WebSocket Implementation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build scalable WebSocket systems for real-time communication with proper connection management, message routing, error handling, and horizontal scaling support.

## When to Use

- Building real-time chat and messaging
- Implementing live notifications
- Creating collaborative editing tools
- Broadcasting live data updates
- Building real-time dashboards
- Streaming events to clients
- Live multiplayer games

## Quick Start

Minimal working example:

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

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Node.js WebSocket Server (Socket.IO)](references/nodejs-websocket-server-socketio.md) | Node.js WebSocket Server (Socket.IO) |
| [Browser WebSocket Client](references/browser-websocket-client.md) | Browser WebSocket Client |
| [Python WebSocket Server (aiohttp)](references/python-websocket-server-aiohttp.md) | Python WebSocket Server (aiohttp) |
| [Message Types and Protocols](references/message-types-and-protocols.md) | Message Types and Protocols |
| [Scaling with Redis](references/scaling-with-redis.md) | Scaling with Redis |

## Best Practices

### ✅ DO

- Implement proper authentication
- Handle reconnection gracefully
- Manage rooms/channels effectively
- Persist messages appropriately
- Monitor active connections
- Implement presence features
- Use Redis for scaling
- Add message acknowledgment
- Implement rate limiting
- Handle errors properly

### ❌ DON'T

- Send unencrypted sensitive data
- Keep unlimited message history in memory
- Allow arbitrary room/channel creation
- Forget to clean up disconnected connections
- Send large messages frequently
- Ignore network failures
- Store passwords in messages
- Skip authentication/authorization
- Create unbounded growth of connections
- Ignore scalability from day one
