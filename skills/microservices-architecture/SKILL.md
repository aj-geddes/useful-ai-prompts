---
name: microservices-architecture
description: Design and implement microservices architecture including service boundaries, communication patterns, API gateways, service mesh, service discovery, and distributed system patterns. Use when building microservices, distributed systems, or service-oriented architectures.
---

# Microservices Architecture

## Overview

Comprehensive guide to designing, implementing, and maintaining microservices architectures. Covers service decomposition, communication patterns, data management, deployment strategies, and observability for distributed systems.

## When to Use

- Designing new microservices architectures
- Decomposing monolithic applications
- Implementing service-to-service communication
- Setting up API gateways and service mesh
- Implementing service discovery
- Managing distributed transactions
- Designing inter-service data consistency
- Scaling independent services

## Instructions

### 1. **Service Boundary Design**

#### Domain-Driven Design (DDD) Approach
```
Bounded Contexts:
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  Order Service  │  │  User Service   │  │ Payment Service │
│                 │  │                 │  │                 │
│ - Create Order  │  │ - User Profile  │  │ - Process Pay   │
│ - Order Status  │  │ - Auth          │  │ - Refund        │
│ - Order History │  │ - Preferences   │  │ - Transactions  │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

**Decomposition Strategies:**

1. **By Business Capability**
```
E-commerce System:
- Product Catalog Service
- Shopping Cart Service
- Order Management Service
- Payment Service
- Inventory Service
- Shipping Service
- User Account Service
```

2. **By Subdomain**
```
Healthcare System:
- Patient Management (Core Domain)
- Appointment Scheduling (Core Domain)
- Billing (Supporting Domain)
- Notifications (Generic Domain)
- Reporting (Generic Domain)
```

#### Service Design Example
```typescript
// order-service/src/domain/order.ts
export class OrderService {
  constructor(
    private orderRepository: OrderRepository,
    private eventBus: EventBus,
    private paymentClient: PaymentClient,
    private inventoryClient: InventoryClient
  ) {}

  async createOrder(request: CreateOrderRequest): Promise<Order> {
    // 1. Validate order
    const order = Order.create(request);

    // 2. Check inventory (synchronous call)
    const available = await this.inventoryClient.checkAvailability(
      order.items
    );
    if (!available) {
      throw new InsufficientInventoryError();
    }

    // 3. Save order
    await this.orderRepository.save(order);

    // 4. Publish event (asynchronous)
    await this.eventBus.publish(new OrderCreatedEvent(order));

    return order;
  }
}
```

### 2. **Communication Patterns**

#### Synchronous Communication (REST/gRPC)

**REST API Example:**
```typescript
// user-service/src/api/user.controller.ts
import express from 'express';

const router = express.Router();

// Get user profile
router.get('/users/:id', async (req, res) => {
  try {
    const user = await userService.findById(req.params.id);
    res.json(user);
  } catch (error) {
    if (error instanceof UserNotFoundError) {
      res.status(404).json({ error: 'User not found' });
    } else {
      res.status(500).json({ error: 'Internal server error' });
    }
  }
});

// Service-to-service call with circuit breaker
import axios from 'axios';
import CircuitBreaker from 'opossum';

const options = {
  timeout: 3000,
  errorThresholdPercentage: 50,
  resetTimeout: 30000
};

const breaker = new CircuitBreaker(
  async (userId: string) => {
    const response = await axios.get(
      `http://user-service/users/${userId}`,
      { timeout: 2000 }
    );
    return response.data;
  },
  options
);

breaker.fallback(() => ({ id: userId, name: 'Unknown User' }));
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
import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';

const packageDefinition = protoLoader.loadSync('proto/user.proto');
const userProto = grpc.loadPackageDefinition(packageDefinition).user;

// Server
function getUser(call, callback) {
  const userId = call.request.user_id;
  const user = await userService.findById(userId);
  callback(null, user);
}

const server = new grpc.Server();
server.addService(userProto.UserService.service, { getUser });
server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
```

#### Asynchronous Communication (Message Queue)

**Event-Driven with RabbitMQ:**
```typescript
// order-service/src/events/publisher.ts
import amqp from 'amqplib';

export class EventPublisher {
  private connection: amqp.Connection;
  private channel: amqp.Channel;

  async connect() {
    this.connection = await amqp.connect('amqp://localhost');
    this.channel = await this.connection.createChannel();
    await this.channel.assertExchange('orders', 'topic', { durable: true });
  }

  async publishOrderCreated(order: Order) {
    const event = {
      eventType: 'OrderCreated',
      timestamp: new Date(),
      data: order
    };

    this.channel.publish(
      'orders',
      'order.created',
      Buffer.from(JSON.stringify(event)),
      { persistent: true }
    );
  }
}

// inventory-service/src/events/consumer.ts
export class OrderEventConsumer {
  async subscribe() {
    const connection = await amqp.connect('amqp://localhost');
    const channel = await connection.createChannel();

    await channel.assertExchange('orders', 'topic', { durable: true });
    const q = await channel.assertQueue('inventory-order-events', {
      durable: true
    });

    await channel.bindQueue(q.queue, 'orders', 'order.created');

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
import { Kafka } from 'kafkajs';

const kafka = new Kafka({
  clientId: 'order-service',
  brokers: ['kafka:9092']
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
          'event-type': event.type,
          'correlation-id': event.correlationId
        }
      }
    ]
  });
}

// Consumer
const consumer = kafka.consumer({ groupId: 'inventory-service' });

await consumer.subscribe({ topic: 'order-events', fromBeginning: false });

await consumer.run({
  eachMessage: async ({ topic, partition, message }) => {
    const event = JSON.parse(message.value.toString());
    await eventHandler.handle(event);
  }
});
```

### 3. **API Gateway Pattern**

```typescript
// api-gateway/src/gateway.ts
import express from 'express';
import httpProxy from 'http-proxy-middleware';
import jwt from 'jsonwebtoken';
import rateLimit from 'express-rate-limit';

const app = express();

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100
});

app.use(limiter);

// Authentication middleware
const authenticateToken = (req, res, next) => {
  const token = req.headers['authorization']?.split(' ')[1];
  if (!token) return res.sendStatus(401);

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
};

// Route to services
app.use('/api/users', authenticateToken, httpProxy.createProxyMiddleware({
  target: 'http://user-service:3000',
  changeOrigin: true,
  pathRewrite: { '^/api/users': '/users' }
}));

app.use('/api/orders', authenticateToken, httpProxy.createProxyMiddleware({
  target: 'http://order-service:3000',
  changeOrigin: true,
  pathRewrite: { '^/api/orders': '/orders' }
}));

app.use('/api/products', httpProxy.createProxyMiddleware({
  target: 'http://product-service:3000',
  changeOrigin: true,
  pathRewrite: { '^/api/products': '/products' }
}));

// Aggregation endpoint
app.get('/api/order-details/:orderId', authenticateToken, async (req, res) => {
  const orderId = req.params.orderId;

  // Parallel requests to multiple services
  const [order, user, products] = await Promise.all([
    fetch(`http://order-service:3000/orders/${orderId}`).then(r => r.json()),
    fetch(`http://user-service:3000/users/${req.user.id}`).then(r => r.json()),
    fetch(`http://product-service:3000/products?ids=${order.itemIds}`).then(r => r.json())
  ]);

  res.json({ order, user, products });
});
```

### 4. **Service Discovery**

#### Consul Example
```typescript
// service-registry/consul-client.ts
import Consul from 'consul';

export class ServiceRegistry {
  private consul: Consul.Consul;

  constructor() {
    this.consul = new Consul({
      host: 'consul',
      port: 8500
    });
  }

  // Register service
  async register(serviceName: string, servicePort: number) {
    await this.consul.agent.service.register({
      id: `${serviceName}-${process.env.HOSTNAME}`,
      name: serviceName,
      address: process.env.SERVICE_IP,
      port: servicePort,
      check: {
        http: `http://${process.env.SERVICE_IP}:${servicePort}/health`,
        interval: '10s',
        timeout: '5s'
      }
    });
  }

  // Discover service
  async discover(serviceName: string): Promise<string> {
    const result = await this.consul.health.service({
      service: serviceName,
      passing: true
    });

    if (result.length === 0) {
      throw new Error(`Service ${serviceName} not found`);
    }

    // Simple round-robin
    const service = result[Math.floor(Math.random() * result.length)];
    return `http://${service.Service.Address}:${service.Service.Port}`;
  }

  // Deregister on shutdown
  async deregister(serviceId: string) {
    await this.consul.agent.service.deregister(serviceId);
  }
}
```

#### Kubernetes Service Discovery
```yaml
# user-service-deployment.yaml
apiVersion: v1
kind: Service
metadata:
  name: user-service
spec:
  selector:
    app: user-service
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
  type: ClusterIP
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
    spec:
      containers:
      - name: user-service
        image: user-service:latest
        ports:
        - containerPort: 3000
        env:
        - name: SERVICE_NAME
          value: "user-service"
```

```typescript
// Service call in Kubernetes
const userServiceUrl = process.env.USER_SERVICE_URL || 'http://user-service';
const response = await fetch(`${userServiceUrl}/users/${userId}`);
```

### 5. **Data Consistency Patterns**

#### Saga Pattern (Orchestration)
```typescript
// order-saga-orchestrator.ts
export class OrderSagaOrchestrator {
  async createOrder(orderData: CreateOrderRequest) {
    const sagaId = uuidv4();
    const saga = new SagaInstance(sagaId);

    try {
      // Step 1: Create order
      const order = await this.orderService.createOrder(orderData);
      saga.addCompensation(() => this.orderService.cancelOrder(order.id));

      // Step 2: Reserve inventory
      await this.inventoryService.reserveItems(order.items);
      saga.addCompensation(() =>
        this.inventoryService.releaseReservation(order.id)
      );

      // Step 3: Process payment
      const payment = await this.paymentService.charge(order.total);
      saga.addCompensation(() =>
        this.paymentService.refund(payment.id)
      );

      // Step 4: Confirm order
      await this.orderService.confirmOrder(order.id);

      return order;
    } catch (error) {
      // Compensate in reverse order
      await saga.compensate();
      throw error;
    }
  }
}
```

#### Event Sourcing Pattern
```typescript
// order-aggregate.ts
export class OrderAggregate {
  private id: string;
  private status: OrderStatus;
  private items: OrderItem[];
  private events: DomainEvent[] = [];

  // Command handler
  createOrder(command: CreateOrderCommand) {
    // Validation
    if (this.id) throw new Error('Order already exists');

    // Apply event
    this.apply(new OrderCreatedEvent({
      orderId: command.orderId,
      userId: command.userId,
      items: command.items
    }));
  }

  // Event handler
  private apply(event: DomainEvent) {
    switch (event.type) {
      case 'OrderCreated':
        this.id = event.orderId;
        this.items = event.items;
        this.status = OrderStatus.PENDING;
        break;
      case 'OrderConfirmed':
        this.status = OrderStatus.CONFIRMED;
        break;
    }
    this.events.push(event);
  }

  getUncommittedEvents(): DomainEvent[] {
    return this.events;
  }
}
```

### 6. **Service Mesh (Istio)**

```yaml
# istio-config.yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: order-service
spec:
  hosts:
  - order-service
  http:
  - match:
    - headers:
        user-type:
          exact: premium
    route:
    - destination:
        host: order-service
        subset: v2
      weight: 100
  - route:
    - destination:
        host: order-service
        subset: v1
      weight: 90
    - destination:
        host: order-service
        subset: v2
      weight: 10
---
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: order-service
spec:
  host: order-service
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        http1MaxPendingRequests: 50
        maxRequestsPerConnection: 2
    outlierDetection:
      consecutiveErrors: 5
      interval: 30s
      baseEjectionTime: 30s
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
```

## Best Practices

### ✅ DO
- Design services around business capabilities
- Use asynchronous communication where possible
- Implement circuit breakers for resilience
- Use API gateway for cross-cutting concerns
- Implement distributed tracing
- Use service mesh for service-to-service communication
- Design for failure (chaos engineering)
- Implement health checks for all services
- Use correlation IDs for request tracking
- Version your APIs
- Implement proper monitoring and alerting
- Use event-driven architecture for loose coupling
- Implement idempotent operations
- Use database per service pattern

### ❌ DON'T
- Share databases between services
- Create overly granular services (nanoservices)
- Use distributed transactions (two-phase commit)
- Ignore network latency and failures
- Share domain models between services
- Deploy all services as one unit
- Hardcode service URLs
- Forget to implement authentication/authorization
- Use synchronous calls for long-running operations
- Ignore backward compatibility
- Skip monitoring and logging
- Create circular dependencies between services

## Common Patterns

### Pattern 1: Backend for Frontend (BFF)
```typescript
// mobile-bff/src/api.ts - Optimized for mobile
app.get('/api/home', async (req, res) => {
  const [featured, recommendations] = await Promise.all([
    productService.getFeatured(5),
    recommendationService.getForUser(req.user.id, 10)
  ]);
  res.json({ featured, recommendations });
});

// web-bff/src/api.ts - More data for web
app.get('/api/home', async (req, res) => {
  const [featured, recommendations, categories, promotions] = await Promise.all([
    productService.getFeatured(20),
    recommendationService.getForUser(req.user.id, 50),
    categoryService.getAll(),
    promotionService.getActive()
  ]);
  res.json({ featured, recommendations, categories, promotions });
});
```

### Pattern 2: Sidecar Pattern
```yaml
# Pod with sidecar
apiVersion: v1
kind: Pod
metadata:
  name: app-with-sidecar
spec:
  containers:
  - name: app
    image: my-app:latest
  - name: logging-sidecar
    image: fluentd:latest
    volumeMounts:
    - name: logs
      mountPath: /logs
  volumes:
  - name: logs
    emptyDir: {}
```

## Tools & Resources

- **Service Mesh**: Istio, Linkerd, Consul Connect
- **API Gateway**: Kong, Apigee, AWS API Gateway
- **Service Discovery**: Consul, Eureka, Zookeeper
- **Message Queue**: RabbitMQ, Apache Kafka, AWS SQS
- **Orchestration**: Kubernetes, Docker Swarm, Nomad
- **Monitoring**: Prometheus, Grafana, Datadog
- **Tracing**: Jaeger, Zipkin, AWS X-Ray
- **Circuit Breaker**: Hystrix, Resilience4j, Polly
