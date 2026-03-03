# Communication Patterns

## Communication Patterns

### Synchronous Communication (REST/gRPC)

**REST API Example:**

```typescript
// user-service/src/api/user.controller.ts
import express from "express";

const router = express.Router();

// Get user profile
router.get("/users/:id", async (req, res) => {
  try {
    const user = await userService.findById(req.params.id);
    res.json(user);
  } catch (error) {
    if (error instanceof UserNotFoundError) {
      res.status(404).json({ error: "User not found" });
    } else {
      res.status(500).json({ error: "Internal server error" });
    }
  }
});

// Service-to-service call with circuit breaker
import axios from "axios";
import CircuitBreaker from "opossum";

const options = {
  timeout: 3000,
  errorThresholdPercentage: 50,
  resetTimeout: 30000,
};

const breaker = new CircuitBreaker(async (userId: string) => {
  const response = await axios.get(`http://user-service/users/${userId}`, {
    timeout: 2000,
  });
  return response.data;
}, options);

breaker.fallback(() => ({ id: userId, name: "Unknown User" }));
```

**gRPC Example:**

```protobuf
// proto/user.proto
syntax = "proto3";

package user;

service UserService {
  rpc GetUser (GetUserRequest) returns (UserResponse);
  rpc ListUsers (ListUsersRequest) returns (stream UserResponse);
}

message GetUserRequest {
  string user_id = 1;
}

message UserResponse {
  string user_id = 1;
  string email = 2;
  string name = 3;
}
```

```typescript
// Implementation
import * as grpc from "@grpc/grpc-js";
import * as protoLoader from "@grpc/proto-loader";

const packageDefinition = protoLoader.loadSync("proto/user.proto");
const userProto = grpc.loadPackageDefinition(packageDefinition).user;

// Server
function getUser(call, callback) {
  const userId = call.request.user_id;
  const user = await userService.findById(userId);
  callback(null, user);
}

const server = new grpc.Server();
server.addService(userProto.UserService.service, { getUser });
server.bindAsync("0.0.0.0:50051", grpc.ServerCredentials.createInsecure());
```

### Asynchronous Communication (Message Queue)

**Event-Driven with RabbitMQ:**

```typescript
// order-service/src/events/publisher.ts
import amqp from "amqplib";

export class EventPublisher {
  private connection: amqp.Connection;
  private channel: amqp.Channel;

  async connect() {
    this.connection = await amqp.connect("amqp://localhost");
    this.channel = await this.connection.createChannel();
    await this.channel.assertExchange("orders", "topic", { durable: true });
  }

  async publishOrderCreated(order: Order) {
    const event = {
      eventType: "OrderCreated",
      timestamp: new Date(),
      data: order,
    };

    this.channel.publish(
      "orders",
      "order.created",
      Buffer.from(JSON.stringify(event)),
      { persistent: true },
    );
  }
}

// inventory-service/src/events/consumer.ts
export class OrderEventConsumer {
  async subscribe() {
    const connection = await amqp.connect("amqp://localhost");
    const channel = await connection.createChannel();

    await channel.assertExchange("orders", "topic", { durable: true });
    const q = await channel.assertQueue("inventory-order-events", {
      durable: true,
    });

    await channel.bindQueue(q.queue, "orders", "order.created");

    channel.consume(q.queue, async (msg) => {
      if (msg) {
        const event = JSON.parse(msg.content.toString());
        await this.handleOrderCreated(event.data);
        channel.ack(msg);
      }
    });
  }

  private async handleOrderCreated(order: Order) {
    // Reserve inventory
    await inventoryService.reserveItems(order.items);
  }
}
```

**Kafka Event Streaming:**

```typescript
// event-streaming/kafka-producer.ts
import { Kafka } from "kafkajs";

const kafka = new Kafka({
  clientId: "order-service",
  brokers: ["kafka:9092"],
});

const producer = kafka.producer();

export async function publishEvent(topic: string, event: any) {
  await producer.connect();
  await producer.send({
    topic,
    messages: [
      {
        key: event.aggregateId,
        value: JSON.stringify(event),
        headers: {
          "event-type": event.type,
          "correlation-id": event.correlationId,
        },
      },
    ],
  });
}

// Consumer
const consumer = kafka.consumer({ groupId: "inventory-service" });

await consumer.subscribe({ topic: "order-events", fromBeginning: false });

await consumer.run({
  eachMessage: async ({ topic, partition, message }) => {
    const event = JSON.parse(message.value.toString());
    await eventHandler.handle(event);
  },
});
```
