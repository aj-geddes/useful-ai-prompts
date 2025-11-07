---
name: architecture-diagrams
description: Create system architecture diagrams using Mermaid, PlantUML, C4 model, flowcharts, and sequence diagrams. Use when documenting architecture, system design, data flows, or technical workflows.
---

# Architecture Diagrams

## Overview

Create clear, maintainable architecture diagrams using code-based diagramming tools like Mermaid and PlantUML for system design, data flows, and technical documentation.

## When to Use

- System architecture documentation
- C4 model diagrams
- Data flow diagrams
- Sequence diagrams
- Component relationships
- Deployment diagrams
- Infrastructure architecture
- Microservices architecture
- Database schemas (visual)
- Integration patterns

## Mermaid Examples

### 1. **System Architecture Diagram**

```mermaid
graph TB
    subgraph "Client Layer"
        Web[Web App]
        Mobile[Mobile App]
        CLI[CLI Tool]
    end

    subgraph "API Gateway Layer"
        Gateway[API Gateway<br/>Rate Limiting<br/>Authentication]
    end

    subgraph "Service Layer"
        Auth[Auth Service]
        User[User Service]
        Order[Order Service]
        Payment[Payment Service]
        Notification[Notification Service]
    end

    subgraph "Data Layer"
        UserDB[(User DB<br/>PostgreSQL)]
        OrderDB[(Order DB<br/>PostgreSQL)]
        Cache[(Redis Cache)]
        Queue[Message Queue<br/>RabbitMQ]
    end

    subgraph "External Services"
        Stripe[Stripe API]
        SendGrid[SendGrid]
        S3[AWS S3]
    end

    Web --> Gateway
    Mobile --> Gateway
    CLI --> Gateway

    Gateway --> Auth
    Gateway --> User
    Gateway --> Order
    Gateway --> Payment

    Auth --> UserDB
    User --> UserDB
    User --> Cache
    Order --> OrderDB
    Order --> Queue
    Payment --> Stripe
    Queue --> Notification
    Notification --> SendGrid

    Order --> S3
    User --> S3

    style Gateway fill:#ff6b6b
    style Auth fill:#4ecdc4
    style User fill:#4ecdc4
    style Order fill:#4ecdc4
    style Payment fill:#4ecdc4
    style Notification fill:#4ecdc4
```

### 2. **Sequence Diagram**

```mermaid
sequenceDiagram
    actor User
    participant Web as Web App
    participant Gateway as API Gateway
    participant Auth as Auth Service
    participant Order as Order Service
    participant Payment as Payment Service
    participant DB as Database
    participant Queue as Message Queue
    participant Email as Email Service

    User->>Web: Place Order
    Web->>Gateway: POST /orders
    Gateway->>Auth: Validate Token
    Auth-->>Gateway: Token Valid

    Gateway->>Order: Create Order
    Order->>DB: Save Order
    DB-->>Order: Order Saved
    Order->>Payment: Process Payment
    Payment->>Payment: Charge Card
    Payment-->>Order: Payment Success
    Order->>Queue: Publish Order Event
    Queue->>Email: Send Confirmation
    Email->>User: Order Confirmation

    Order-->>Gateway: Order Created
    Gateway-->>Web: 201 Created
    Web-->>User: Order Success

    Note over User,Email: Async email sent via queue
```

### 3. **C4 Context Diagram**

```mermaid
graph TB
    subgraph "E-Commerce System"
        System[E-Commerce Platform<br/>Manages products, orders,<br/>and customer accounts]
    end

    Customer[Customer<br/>Browses and purchases products]
    Admin[Administrator<br/>Manages products and orders]

    Email[Email System<br/>SendGrid]
    Payment[Payment Provider<br/>Stripe]
    Analytics[Analytics Platform<br/>Google Analytics]

    Customer -->|Browses, Orders| System
    Admin -->|Manages| System
    System -->|Sends emails| Email
    System -->|Processes payments| Payment
    System -->|Tracks events| Analytics

    style System fill:#1168bd
    style Customer fill:#08427b
    style Admin fill:#08427b
    style Email fill:#999
    style Payment fill:#999
    style Analytics fill:#999
```

### 4. **Component Diagram**

```mermaid
graph LR
    subgraph "Frontend"
        UI[React UI]
        Store[Redux Store]
        Router[React Router]
    end

    subgraph "API Layer"
        REST[REST API]
        WS[WebSocket]
        GQL[GraphQL]
    end

    subgraph "Business Logic"
        ProductSvc[Product Service]
        OrderSvc[Order Service]
        AuthSvc[Auth Service]
    end

    subgraph "Data Access"
        ProductRepo[Product Repository]
        OrderRepo[Order Repository]
        UserRepo[User Repository]
        Cache[Cache Layer]
    end

    subgraph "Infrastructure"
        DB[(PostgreSQL)]
        Redis[(Redis)]
        S3[AWS S3]
    end

    UI --> Store
    Store --> Router
    UI --> REST
    UI --> WS
    UI --> GQL

    REST --> ProductSvc
    REST --> OrderSvc
    REST --> AuthSvc
    WS --> OrderSvc
    GQL --> ProductSvc

    ProductSvc --> ProductRepo
    OrderSvc --> OrderRepo
    AuthSvc --> UserRepo

    ProductRepo --> DB
    OrderRepo --> DB
    UserRepo --> DB
    ProductRepo --> Cache
    Cache --> Redis
    ProductSvc --> S3
```

### 5. **Deployment Diagram**

```mermaid
graph TB
    subgraph "AWS Cloud"
        subgraph "VPC"
            subgraph "Public Subnet"
                ALB[Application<br/>Load Balancer]
                NAT[NAT Gateway]
            end

            subgraph "Private Subnet 1"
                ECS1[ECS Container<br/>Service Instance 1]
                ECS2[ECS Container<br/>Service Instance 2]
            end

            subgraph "Private Subnet 2"
                RDS1[(RDS Primary)]
                RDS2[(RDS Replica)]
            end

            subgraph "Private Subnet 3"
                ElastiCache[(ElastiCache<br/>Redis Cluster)]
            end
        end

        Route53[Route 53<br/>DNS]
        CloudFront[CloudFront CDN]
        S3[S3 Bucket<br/>Static Assets]
        ECR[ECR<br/>Container Registry]
    end

    Users[Users] --> Route53
    Route53 --> CloudFront
    CloudFront --> ALB
    CloudFront --> S3
    ALB --> ECS1
    ALB --> ECS2
    ECS1 --> RDS1
    ECS2 --> RDS1
    RDS1 --> RDS2
    ECS1 --> ElastiCache
    ECS2 --> ElastiCache
    ECS1 --> S3
    ECS2 --> S3
    ECS1 -.pulls images.-> ECR
    ECS2 -.pulls images.-> ECR

    style ALB fill:#ff6b6b
    style ECS1 fill:#4ecdc4
    style ECS2 fill:#4ecdc4
    style RDS1 fill:#95e1d3
    style RDS2 fill:#95e1d3
```

### 6. **Data Flow Diagram**

```mermaid
graph LR
    User[User Action] --> Frontend[Frontend App]
    Frontend --> Validation{Validation}
    Validation -->|Invalid| Error[Show Error]
    Validation -->|Valid| API[API Request]
    API --> Auth{Authenticated?}
    Auth -->|No| Unauthorized[401 Response]
    Auth -->|Yes| Service[Business Service]
    Service --> Database[(Database)]
    Service --> Cache[(Cache)]
    Cache -->|Hit| Return[Return Cached]
    Cache -->|Miss| Database
    Database --> Transform[Transform Data]
    Transform --> Response[API Response]
    Response --> Frontend
    Frontend --> Render[Render UI]
```

## PlantUML Examples

### 1. **Class Diagram**

```plantuml
@startuml
class Order {
  -id: UUID
  -customerId: UUID
  -items: OrderItem[]
  -status: OrderStatus
  -totalAmount: number
  -createdAt: Date
  +calculateTotal(): number
  +addItem(item: OrderItem): void
  +removeItem(itemId: UUID): void
  +updateStatus(status: OrderStatus): void
}

class OrderItem {
  -id: UUID
  -productId: UUID
  -quantity: number
  -price: number
  +getSubtotal(): number
}

class Customer {
  -id: UUID
  -name: string
  -email: string
  -orders: Order[]
  +placeOrder(order: Order): void
  +getOrderHistory(): Order[]
}

enum OrderStatus {
  PENDING
  PROCESSING
  SHIPPED
  DELIVERED
  CANCELLED
}

Customer "1" -- "*" Order: places
Order "1" *-- "*" OrderItem: contains
Order -- OrderStatus: has
@enduml
```

### 2. **Component Diagram**

```plantuml
@startuml
package "Frontend" {
  [Web App]
  [Mobile App]
}

package "API Gateway" {
  [Load Balancer]
  [API Gateway]
}

package "Microservices" {
  [User Service]
  [Product Service]
  [Order Service]
  [Payment Service]
}

package "Data Stores" {
  database "PostgreSQL" {
    [User DB]
    [Product DB]
    [Order DB]
  }
  database "Redis" {
    [Cache]
    [Session Store]
  }
}

[Web App] --> [Load Balancer]
[Mobile App] --> [Load Balancer]
[Load Balancer] --> [API Gateway]
[API Gateway] --> [User Service]
[API Gateway] --> [Product Service]
[API Gateway] --> [Order Service]
[API Gateway] --> [Payment Service]

[User Service] --> [User DB]
[Product Service] --> [Product DB]
[Order Service] --> [Order DB]
[User Service] --> [Cache]
[Product Service] --> [Cache]
[API Gateway] --> [Session Store]
@enduml
```

### 3. **Deployment Diagram**

```plantuml
@startuml
node "CDN (CloudFront)" {
  [Static Assets]
}

node "Load Balancer" {
  [ALB]
}

node "Application Servers" {
  node "Server 1" {
    [App Instance 1]
  }
  node "Server 2" {
    [App Instance 2]
  }
}

node "Database Cluster" {
  database "Primary" {
    [PostgreSQL Primary]
  }
  database "Replica" {
    [PostgreSQL Replica]
  }
}

node "Cache Cluster" {
  [Redis Master]
  [Redis Slave]
}

[Browser] --> [Static Assets]
[Browser] --> [ALB]
[ALB] --> [App Instance 1]
[ALB] --> [App Instance 2]
[App Instance 1] --> [PostgreSQL Primary]
[App Instance 2] --> [PostgreSQL Primary]
[PostgreSQL Primary] ..> [PostgreSQL Replica]: replication
[App Instance 1] --> [Redis Master]
[App Instance 2] --> [Redis Master]
[Redis Master] ..> [Redis Slave]: replication
@enduml
```

## Best Practices

### ✅ DO
- Use consistent notation and symbols
- Include legends for complex diagrams
- Keep diagrams focused on one aspect
- Use color coding meaningfully
- Include titles and descriptions
- Version control your diagrams
- Use text-based formats (Mermaid, PlantUML)
- Show data flow direction clearly
- Include deployment details
- Document diagram conventions
- Keep diagrams up-to-date with code
- Use subgraphs for logical grouping

### ❌ DON'T
- Overcrowd diagrams with details
- Use inconsistent styling
- Skip diagram legends
- Create binary image files only
- Forget to document relationships
- Mix abstraction levels in one diagram
- Use proprietary formats

## Resources

- [Mermaid Documentation](https://mermaid.js.org/)
- [PlantUML Documentation](https://plantuml.com/)
- [C4 Model](https://c4model.com/)
- [Diagrams as Code](https://diagrams.mingrammer.com/)
- [draw.io](https://www.diagrams.net/)
