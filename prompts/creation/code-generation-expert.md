# Code Generation Expert and Software Architecture Specialist

## Metadata

- **Category**: Creation
- **Tags**: code generation, software development, architecture patterns, clean code, programming
- **Created**: 2025-07-20
- **Version**: 1.0.0
- **Personas**: Senior Code Generation Expert, Software Architecture Specialist
- **Use Cases**: application development, API creation, algorithm implementation, code refactoring, system design
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt combines expert code generation capabilities with software architecture expertise to create robust, scalable, and maintainable code. It employs best practices, design patterns, and modern development principles.

## Prompt Template

```
You are operating as a dual-expertise code generation system combining:

1. **Senior Code Generation Expert** (15+ years experience)
   - Expertise: Multi-language proficiency, algorithms, data structures, performance optimization
   - Strengths: Clean code principles, error handling, security practices, documentation
   - Perspective: Writing code that is both functional and maintainable

2. **Software Architecture Specialist**
   - Expertise: System design, design patterns, scalability, microservices, cloud architecture
   - Strengths: SOLID principles, DDD, event-driven architecture, API design
   - Perspective: Building systems that evolve gracefully with changing requirements

Apply these development frameworks:
- **Clean Architecture**: Separation of concerns and dependency inversion
- **SOLID Principles**: Single responsibility through dependency inversion
- **Design Patterns**: Gang of Four and modern patterns
- **Test-Driven Development**: Red-green-refactor cycle

CODE GENERATION CONTEXT:
- **Project Type**: {{web_app_api_library_cli_service}}
- **Language/Stack**: {{language_framework_runtime}}
- **Architecture Style**: {{monolith_microservices_serverless}}
- **Requirements**: {{functional_nonfunctional_constraints}}
- **Scale Requirements**: {{users_requests_data_volume}}
- **Integration Points**: {{databases_apis_services}}
- **Development Stage**: {{greenfield_refactor_migration}}
- **Team Context**: {{size_experience_practices}}
- **Quality Requirements**: {{performance_security_reliability}}
- **Timeline**: {{prototype_mvp_production}}

CODE GENERATION FOCUS:
{{specific_features_components_problems_to_solve}}

CODE GENERATION FRAMEWORK:

Phase 1: ARCHITECTURE DESIGN
1. Requirements analysis
2. System design
3. Technology selection
4. Pattern identification

Phase 2: IMPLEMENTATION
1. Core structure setup
2. Feature development
3. Integration implementation
4. Error handling

Phase 3: QUALITY ASSURANCE
1. Unit testing
2. Integration testing
3. Performance optimization
4. Security hardening

Phase 4: DOCUMENTATION
1. Code documentation
2. API documentation
3. Deployment guides
4. Maintenance notes

DELIVER YOUR CODE AS:
```

## COMPREHENSIVE CODE SOLUTION

### SYSTEM ARCHITECTURE OVERVIEW

**Project**: E-Commerce Microservices Platform
**Tech Stack**: Node.js/TypeScript, React, PostgreSQL, Redis, Kubernetes
**Architecture**: Event-driven microservices with API Gateway

#### High-Level Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        WEB[Web App]
        MOB[Mobile App]
        API[Public API]
    end

    subgraph "Gateway Layer"
        GW[API Gateway]
        AUTH[Auth Service]
    end

    subgraph "Service Layer"
        PROD[Product Service]
        ORDER[Order Service]
        USER[User Service]
        PAY[Payment Service]
        INV[Inventory Service]
    end

    subgraph "Data Layer"
        PDB[(Product DB)]
        ODB[(Order DB)]
        UDB[(User DB)]
        CACHE[(Redis Cache)]
    end

    subgraph "Infrastructure"
        QUEUE[Message Queue]
        SEARCH[Elasticsearch]
        MONITOR[Monitoring]
    end

    WEB --> GW
    MOB --> GW
    API --> GW

    GW --> AUTH
    GW --> PROD
    GW --> ORDER
    GW --> USER

    ORDER --> QUEUE
    PAY --> QUEUE
    INV --> QUEUE

    PROD --> PDB
    ORDER --> ODB
    USER --> UDB

    PROD --> CACHE
    ORDER --> CACHE
```

### CORE SERVICE IMPLEMENTATION

#### 1. Product Service (TypeScript/Node.js)

**Project Structure**:

```
product-service/
├── src/
│   ├── domain/
│   │   ├── entities/
│   │   │   └── Product.ts
│   │   ├── repositories/
│   │   │   └── IProductRepository.ts
│   │   └── services/
│   │       └── ProductService.ts
│   ├── infrastructure/
│   │   ├── database/
│   │   │   ├── PostgresProductRepository.ts
│   │   │   └── migrations/
│   │   ├── cache/
│   │   │   └── RedisCache.ts
│   │   └── messaging/
│   │       └── EventPublisher.ts
│   ├── application/
│   │   ├── use-cases/
│   │   │   ├── CreateProduct.ts
│   │   │   ├── UpdateProduct.ts
│   │   │   └── SearchProducts.ts
│   │   └── dto/
│   │       └── ProductDTO.ts
│   ├── interfaces/
│   │   ├── http/
│   │   │   ├── controllers/
│   │   │   ├── middleware/
│   │   │   └── routes/
│   │   └── grpc/
│   └── shared/
│       ├── errors/
│       └── utils/
├── tests/
├── docker/
└── k8s/
```

**Domain Entity - Product.ts**:

```typescript
// src/domain/entities/Product.ts
import { Entity, ValueObject } from "@shared/domain";
import { Result } from "@shared/core/Result";
import { Guard } from "@shared/core/Guard";

// Value Objects
export class ProductId extends ValueObject<{ value: string }> {
  get value(): string {
    return this.props.value;
  }

  private constructor(props: { value: string }) {
    super(props);
  }

  public static create(id?: string): Result<ProductId> {
    const guardResult = Guard.againstNullOrUndefined(id, "productId");
    if (!guardResult.succeeded) {
      return Result.fail<ProductId>(guardResult.message);
    }
    return Result.ok<ProductId>(new ProductId({ value: id }));
  }
}

export class Price extends ValueObject<{ amount: number; currency: string }> {
  get amount(): number {
    return this.props.amount;
  }

  get currency(): string {
    return this.props.currency;
  }

  private constructor(props: { amount: number; currency: string }) {
    super(props);
  }

  public static create(amount: number, currency: string): Result<Price> {
    const guardResults = Guard.combine([
      Guard.againstNullOrUndefined(amount, "amount"),
      Guard.againstNullOrUndefined(currency, "currency"),
      Guard.greaterThan(0, amount, "amount"),
    ]);

    if (!guardResults.succeeded) {
      return Result.fail<Price>(guardResults.message);
    }

    return Result.ok<Price>(new Price({ amount, currency }));
  }
}

// Aggregate Root
export class Product extends Entity<ProductProps> {
  private constructor(props: ProductProps, id?: string) {
    super(props, id);
  }

  get productId(): ProductId {
    return this.props.productId;
  }

  get name(): string {
    return this.props.name;
  }

  get description(): string {
    return this.props.description;
  }

  get price(): Price {
    return this.props.price;
  }

  get inventory(): number {
    return this.props.inventory;
  }

  get isActive(): boolean {
    return this.props.isActive;
  }

  public static create(
    props: ProductCreateProps,
    id?: string,
  ): Result<Product> {
    const guardResults = Guard.combine([
      Guard.againstNullOrUndefined(props.name, "name"),
      Guard.againstNullOrUndefined(props.price, "price"),
      Guard.inRange(props.inventory, 0, 1000000, "inventory"),
    ]);

    if (!guardResults.succeeded) {
      return Result.fail<Product>(guardResults.message);
    }

    const productId = ProductId.create(id);
    if (productId.isFailure) {
      return Result.fail<Product>(productId.error);
    }

    const product = new Product(
      {
        productId: productId.getValue(),
        name: props.name,
        description: props.description || "",
        price: props.price,
        inventory: props.inventory,
        isActive: props.isActive !== undefined ? props.isActive : true,
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      id,
    );

    return Result.ok<Product>(product);
  }

  public updatePrice(newPrice: Price): Result<void> {
    if (
      newPrice.amount === this.price.amount &&
      newPrice.currency === this.price.currency
    ) {
      return Result.fail<void>("Price is unchanged");
    }

    this.props.price = newPrice;
    this.props.updatedAt = new Date();

    this.addDomainEvent(new ProductPriceUpdatedEvent(this.productId, newPrice));

    return Result.ok<void>();
  }

  public adjustInventory(quantity: number): Result<void> {
    const newInventory = this.props.inventory + quantity;

    if (newInventory < 0) {
      return Result.fail<void>("Insufficient inventory");
    }

    this.props.inventory = newInventory;
    this.props.updatedAt = new Date();

    if (newInventory === 0) {
      this.addDomainEvent(new ProductOutOfStockEvent(this.productId));
    }

    return Result.ok<void>();
  }

  public deactivate(): void {
    this.props.isActive = false;
    this.props.updatedAt = new Date();
    this.addDomainEvent(new ProductDeactivatedEvent(this.productId));
  }
}

interface ProductProps {
  productId: ProductId;
  name: string;
  description: string;
  price: Price;
  inventory: number;
  isActive: boolean;
  createdAt: Date;
  updatedAt: Date;
}

interface ProductCreateProps {
  name: string;
  description?: string;
  price: Price;
  inventory: number;
  isActive?: boolean;
}

// Domain Events
export class ProductPriceUpdatedEvent {
  constructor(
    public readonly productId: ProductId,
    public readonly newPrice: Price,
  ) {}
}

export class ProductOutOfStockEvent {
  constructor(public readonly productId: ProductId) {}
}

export class ProductDeactivatedEvent {
  constructor(public readonly productId: ProductId) {}
}
```

**Repository Implementation**:

```typescript
// src/infrastructure/database/PostgresProductRepository.ts
import { Pool } from "pg";
import { IProductRepository } from "@domain/repositories/IProductRepository";
import { Product, ProductId } from "@domain/entities/Product";
import { Result } from "@shared/core/Result";

export class PostgresProductRepository implements IProductRepository {
  constructor(private pool: Pool) {}

  async findById(id: ProductId): Promise<Result<Product | null>> {
    try {
      const query = `
        SELECT * FROM products 
        WHERE id = $1 AND deleted_at IS NULL
      `;

      const result = await this.pool.query(query, [id.value]);

      if (result.rows.length === 0) {
        return Result.ok<Product | null>(null);
      }

      const product = this.toDomain(result.rows[0]);
      return Result.ok<Product | null>(product);
    } catch (error) {
      return Result.fail<Product | null>(`Database error: ${error.message}`);
    }
  }

  async save(product: Product): Promise<Result<void>> {
    const client = await this.pool.connect();

    try {
      await client.query("BEGIN");

      const query = `
        INSERT INTO products (
          id, name, description, price_amount, price_currency,
          inventory, is_active, created_at, updated_at
        ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
        ON CONFLICT (id) DO UPDATE SET
          name = EXCLUDED.name,
          description = EXCLUDED.description,
          price_amount = EXCLUDED.price_amount,
          price_currency = EXCLUDED.price_currency,
          inventory = EXCLUDED.inventory,
          is_active = EXCLUDED.is_active,
          updated_at = EXCLUDED.updated_at
      `;

      const values = [
        product.productId.value,
        product.name,
        product.description,
        product.price.amount,
        product.price.currency,
        product.inventory,
        product.isActive,
        product.createdAt,
        product.updatedAt,
      ];

      await client.query(query, values);

      // Publish domain events
      const events = product.getUncommittedEvents();
      for (const event of events) {
        await this.publishEvent(event);
      }

      await client.query("COMMIT");
      product.markEventsAsCommitted();

      return Result.ok<void>();
    } catch (error) {
      await client.query("ROLLBACK");
      return Result.fail<void>(`Failed to save product: ${error.message}`);
    } finally {
      client.release();
    }
  }

  async search(criteria: SearchCriteria): Promise<Result<Product[]>> {
    try {
      let query = `
        SELECT * FROM products 
        WHERE deleted_at IS NULL
      `;
      const values: any[] = [];
      let paramCount = 0;

      if (criteria.name) {
        paramCount++;
        query += ` AND name ILIKE $${paramCount}`;
        values.push(`%${criteria.name}%`);
      }

      if (criteria.minPrice !== undefined) {
        paramCount++;
        query += ` AND price_amount >= $${paramCount}`;
        values.push(criteria.minPrice);
      }

      if (criteria.maxPrice !== undefined) {
        paramCount++;
        query += ` AND price_amount <= $${paramCount}`;
        values.push(criteria.maxPrice);
      }

      if (criteria.isActive !== undefined) {
        paramCount++;
        query += ` AND is_active = $${paramCount}`;
        values.push(criteria.isActive);
      }

      query += ` ORDER BY created_at DESC`;

      if (criteria.limit) {
        paramCount++;
        query += ` LIMIT $${paramCount}`;
        values.push(criteria.limit);
      }

      if (criteria.offset) {
        paramCount++;
        query += ` OFFSET $${paramCount}`;
        values.push(criteria.offset);
      }

      const result = await this.pool.query(query, values);
      const products = result.rows.map((row) => this.toDomain(row));

      return Result.ok<Product[]>(products);
    } catch (error) {
      return Result.fail<Product[]>(`Search failed: ${error.message}`);
    }
  }

  private toDomain(raw: any): Product {
    const priceResult = Price.create(raw.price_amount, raw.price_currency);
    if (priceResult.isFailure) {
      throw new Error(`Invalid price data: ${priceResult.error}`);
    }

    const productResult = Product.create(
      {
        name: raw.name,
        description: raw.description,
        price: priceResult.getValue(),
        inventory: raw.inventory,
        isActive: raw.is_active,
      },
      raw.id,
    );

    if (productResult.isFailure) {
      throw new Error(`Invalid product data: ${productResult.error}`);
    }

    return productResult.getValue();
  }

  private async publishEvent(event: any): Promise<void> {
    // Implement event publishing logic
    console.log("Publishing event:", event);
  }
}

interface SearchCriteria {
  name?: string;
  minPrice?: number;
  maxPrice?: number;
  isActive?: boolean;
  limit?: number;
  offset?: number;
}
```

**Use Case Implementation**:

```typescript
// src/application/use-cases/CreateProduct.ts
import { UseCase } from "@shared/application/UseCase";
import { Result } from "@shared/core/Result";
import { IProductRepository } from "@domain/repositories/IProductRepository";
import { Product, Price } from "@domain/entities/Product";
import { CreateProductDTO } from "@application/dto/ProductDTO";

export class CreateProductUseCase
  implements UseCase<CreateProductDTO, Result<Product>>
{
  constructor(
    private productRepository: IProductRepository,
    private eventPublisher: IEventPublisher,
  ) {}

  async execute(dto: CreateProductDTO): Promise<Result<Product>> {
    // Validate input
    const priceResult = Price.create(dto.price, dto.currency);
    if (priceResult.isFailure) {
      return Result.fail<Product>(priceResult.error);
    }

    // Create product entity
    const productResult = Product.create({
      name: dto.name,
      description: dto.description,
      price: priceResult.getValue(),
      inventory: dto.inventory,
      isActive: true,
    });

    if (productResult.isFailure) {
      return Result.fail<Product>(productResult.error);
    }

    const product = productResult.getValue();

    // Save to repository
    const saveResult = await this.productRepository.save(product);
    if (saveResult.isFailure) {
      return Result.fail<Product>(saveResult.error);
    }

    // Publish integration event
    await this.eventPublisher.publish("product.created", {
      productId: product.productId.value,
      name: product.name,
      price: product.price.amount,
      currency: product.price.currency,
      inventory: product.inventory,
    });

    return Result.ok<Product>(product);
  }
}
```

**API Controller**:

```typescript
// src/interfaces/http/controllers/ProductController.ts
import { Request, Response } from "express";
import { CreateProductUseCase } from "@application/use-cases/CreateProduct";
import { BaseController } from "@shared/interfaces/http/BaseController";

export class ProductController extends BaseController {
  constructor(
    private createProductUseCase: CreateProductUseCase,
    private updateProductUseCase: UpdateProductUseCase,
    private searchProductsUseCase: SearchProductsUseCase,
  ) {
    super();
  }

  async createProduct(req: Request, res: Response): Promise<Response> {
    try {
      const dto = req.body;

      const result = await this.createProductUseCase.execute(dto);

      if (result.isFailure) {
        return this.fail(res, result.error);
      }

      const product = result.getValue();

      return this.created(res, {
        id: product.productId.value,
        name: product.name,
        description: product.description,
        price: product.price.amount,
        currency: product.price.currency,
        inventory: product.inventory,
        isActive: product.isActive,
      });
    } catch (error) {
      return this.fail(res, error.message || "Unexpected error");
    }
  }

  async searchProducts(req: Request, res: Response): Promise<Response> {
    try {
      const criteria = {
        name: req.query.name as string,
        minPrice: req.query.minPrice
          ? parseFloat(req.query.minPrice as string)
          : undefined,
        maxPrice: req.query.maxPrice
          ? parseFloat(req.query.maxPrice as string)
          : undefined,
        isActive:
          req.query.isActive !== undefined
            ? req.query.isActive === "true"
            : undefined,
        limit: req.query.limit ? parseInt(req.query.limit as string) : 20,
        offset: req.query.offset ? parseInt(req.query.offset as string) : 0,
      };

      const result = await this.searchProductsUseCase.execute(criteria);

      if (result.isFailure) {
        return this.fail(res, result.error);
      }

      const products = result.getValue();

      return this.ok(res, {
        data: products.map((p) => ({
          id: p.productId.value,
          name: p.name,
          description: p.description,
          price: p.price.amount,
          currency: p.price.currency,
          inventory: p.inventory,
          isActive: p.isActive,
        })),
        pagination: {
          limit: criteria.limit,
          offset: criteria.offset,
          total: products.length,
        },
      });
    } catch (error) {
      return this.fail(res, error.message || "Unexpected error");
    }
  }
}
```

### INFRASTRUCTURE CODE

#### Docker Configuration

**Dockerfile**:

```dockerfile
# Multi-stage build for production optimization
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./
COPY tsconfig*.json ./

# Install dependencies
RUN npm ci --only=production && \
    npm cache clean --force

# Copy source code
COPY src ./src

# Build TypeScript
RUN npm run build

# Production stage
FROM node:18-alpine

# Install dumb-init for proper signal handling
RUN apk add --no-cache dumb-init

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

WORKDIR /app

# Copy built application
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/package*.json ./

# Switch to non-root user
USER nodejs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node healthcheck.js || exit 1

# Use dumb-init to handle signals properly
ENTRYPOINT ["dumb-init", "--"]

# Start application
CMD ["node", "dist/main.js"]
```

**Docker Compose**:

```yaml
version: "3.8"

services:
  product-service:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      NODE_ENV: production
      DATABASE_URL: postgresql://user:password@postgres:5432/products
      REDIS_URL: redis://redis:6379
      RABBITMQ_URL: amqp://user:password@rabbitmq:5672
    ports:
      - "3001:3000"
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
      rabbitmq:
        condition: service_healthy
    networks:
      - microservices-network
    restart: unless-stopped

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: products
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - microservices-network

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - microservices-network

  rabbitmq:
    image: rabbitmq:3-management-alpine
    environment:
      RABBITMQ_DEFAULT_USER: user
      RABBITMQ_DEFAULT_PASS: password
    ports:
      - "15672:15672" # Management UI
    volumes:
      - rabbitmq-data:/var/lib/rabbitmq
    healthcheck:
      test: ["CMD", "rabbitmq-diagnostics", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - microservices-network

volumes:
  postgres-data:
  redis-data:
  rabbitmq-data:

networks:
  microservices-network:
    driver: bridge
```

#### Kubernetes Deployment

**deployment.yaml**:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: product-service
  namespace: ecommerce
  labels:
    app: product-service
    version: v1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: product-service
  template:
    metadata:
      labels:
        app: product-service
        version: v1
    spec:
      serviceAccountName: product-service
      containers:
        - name: product-service
          image: myregistry.com/product-service:1.0.0
          ports:
            - containerPort: 3000
              name: http
          env:
            - name: NODE_ENV
              value: "production"
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: product-service-secrets
                  key: database-url
            - name: REDIS_URL
              valueFrom:
                secretKeyRef:
                  name: product-service-secrets
                  key: redis-url
          resources:
            requests:
              memory: "256Mi"
              cpu: "250m"
            limits:
              memory: "512Mi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 5
          securityContext:
            runAsNonRoot: true
            runAsUser: 1001
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL
---
apiVersion: v1
kind: Service
metadata:
  name: product-service
  namespace: ecommerce
spec:
  selector:
    app: product-service
  ports:
    - port: 80
      targetPort: 3000
      protocol: TCP
  type: ClusterIP
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: product-service-hpa
  namespace: ecommerce
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: product-service
  minReplicas: 3
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
```

### TESTING IMPLEMENTATION

#### Unit Tests

```typescript
// tests/unit/domain/entities/Product.test.ts
import { Product, Price, ProductId } from "@domain/entities/Product";

describe("Product Entity", () => {
  describe("create", () => {
    it("should create a valid product", () => {
      // Arrange
      const priceResult = Price.create(99.99, "USD");
      expect(priceResult.isSuccess).toBe(true);

      const props = {
        name: "Test Product",
        description: "Test Description",
        price: priceResult.getValue(),
        inventory: 100,
      };

      // Act
      const productResult = Product.create(props);

      // Assert
      expect(productResult.isSuccess).toBe(true);
      const product = productResult.getValue();
      expect(product.name).toBe(props.name);
      expect(product.description).toBe(props.description);
      expect(product.price.amount).toBe(99.99);
      expect(product.inventory).toBe(100);
      expect(product.isActive).toBe(true);
    });

    it("should fail with invalid price", () => {
      const priceResult = Price.create(-10, "USD");
      expect(priceResult.isFailure).toBe(true);
      expect(priceResult.error).toContain("greater than 0");
    });

    it("should fail with missing name", () => {
      const priceResult = Price.create(99.99, "USD");
      const productResult = Product.create({
        name: null,
        price: priceResult.getValue(),
        inventory: 100,
      });

      expect(productResult.isFailure).toBe(true);
      expect(productResult.error).toContain("name");
    });
  });

  describe("updatePrice", () => {
    it("should update price and emit event", () => {
      // Arrange
      const product = createTestProduct();
      const newPrice = Price.create(149.99, "USD").getValue();

      // Act
      const result = product.updatePrice(newPrice);

      // Assert
      expect(result.isSuccess).toBe(true);
      expect(product.price.amount).toBe(149.99);

      const events = product.getUncommittedEvents();
      expect(events).toHaveLength(1);
      expect(events[0]).toBeInstanceOf(ProductPriceUpdatedEvent);
    });
  });

  describe("adjustInventory", () => {
    it("should increase inventory", () => {
      const product = createTestProduct({ inventory: 50 });
      const result = product.adjustInventory(25);

      expect(result.isSuccess).toBe(true);
      expect(product.inventory).toBe(75);
    });

    it("should decrease inventory", () => {
      const product = createTestProduct({ inventory: 50 });
      const result = product.adjustInventory(-20);

      expect(result.isSuccess).toBe(true);
      expect(product.inventory).toBe(30);
    });

    it("should fail when inventory goes negative", () => {
      const product = createTestProduct({ inventory: 10 });
      const result = product.adjustInventory(-15);

      expect(result.isFailure).toBe(true);
      expect(result.error).toContain("Insufficient inventory");
      expect(product.inventory).toBe(10); // Unchanged
    });

    it("should emit out of stock event when inventory reaches zero", () => {
      const product = createTestProduct({ inventory: 5 });
      product.adjustInventory(-5);

      const events = product.getUncommittedEvents();
      expect(events).toHaveLength(1);
      expect(events[0]).toBeInstanceOf(ProductOutOfStockEvent);
    });
  });
});

function createTestProduct(overrides = {}): Product {
  const price = Price.create(99.99, "USD").getValue();
  const defaultProps = {
    name: "Test Product",
    description: "Test Description",
    price,
    inventory: 100,
    ...overrides,
  };

  return Product.create(defaultProps).getValue();
}
```

#### Integration Tests

```typescript
// tests/integration/ProductService.integration.test.ts
import { PostgresProductRepository } from "@infrastructure/database/PostgresProductRepository";
import { CreateProductUseCase } from "@application/use-cases/CreateProduct";
import { Pool } from "pg";
import { TestDatabaseHelper } from "../helpers/TestDatabaseHelper";

describe("Product Service Integration Tests", () => {
  let pool: Pool;
  let repository: PostgresProductRepository;
  let createProductUseCase: CreateProductUseCase;
  let dbHelper: TestDatabaseHelper;

  beforeAll(async () => {
    dbHelper = new TestDatabaseHelper();
    pool = await dbHelper.createTestDatabase();
    repository = new PostgresProductRepository(pool);
    createProductUseCase = new CreateProductUseCase(
      repository,
      mockEventPublisher,
    );
  });

  afterAll(async () => {
    await dbHelper.dropTestDatabase();
    await pool.end();
  });

  beforeEach(async () => {
    await dbHelper.cleanDatabase();
  });

  describe("CreateProduct Use Case", () => {
    it("should create and persist a product", async () => {
      // Arrange
      const dto = {
        name: "Integration Test Product",
        description: "Test Description",
        price: 99.99,
        currency: "USD",
        inventory: 100,
      };

      // Act
      const result = await createProductUseCase.execute(dto);

      // Assert
      expect(result.isSuccess).toBe(true);
      const product = result.getValue();

      // Verify persistence
      const savedProduct = await repository.findById(product.productId);
      expect(savedProduct.isSuccess).toBe(true);
      expect(savedProduct.getValue()).toBeDefined();
      expect(savedProduct.getValue().name).toBe(dto.name);
    });

    it("should handle concurrent product creation", async () => {
      // Arrange
      const createPromises = Array(10)
        .fill(null)
        .map((_, i) =>
          createProductUseCase.execute({
            name: `Concurrent Product ${i}`,
            description: "Test",
            price: 99.99,
            currency: "USD",
            inventory: 100,
          }),
        );

      // Act
      const results = await Promise.all(createPromises);

      // Assert
      results.forEach((result) => {
        expect(result.isSuccess).toBe(true);
      });

      const searchResult = await repository.search({ limit: 20 });
      expect(searchResult.getValue()).toHaveLength(10);
    });
  });

  describe("Product Search", () => {
    beforeEach(async () => {
      // Seed test data
      const products = [
        { name: "Laptop Pro", price: 1299.99, inventory: 50 },
        { name: "Laptop Air", price: 999.99, inventory: 30 },
        { name: "Desktop Ultra", price: 1999.99, inventory: 20 },
        { name: "Tablet Mini", price: 499.99, inventory: 100 },
      ];

      for (const p of products) {
        await createProductUseCase.execute({
          ...p,
          currency: "USD",
          description: "Test product",
        });
      }
    });

    it("should search products by name", async () => {
      const result = await repository.search({ name: "Laptop" });

      expect(result.isSuccess).toBe(true);
      expect(result.getValue()).toHaveLength(2);
      expect(result.getValue().every((p) => p.name.includes("Laptop"))).toBe(
        true,
      );
    });

    it("should search products by price range", async () => {
      const result = await repository.search({
        minPrice: 500,
        maxPrice: 1500,
      });

      expect(result.isSuccess).toBe(true);
      expect(result.getValue()).toHaveLength(3);
    });
  });
});
```

### API DOCUMENTATION

#### OpenAPI Specification

```yaml
openapi: 3.0.0
info:
  title: Product Service API
  version: 1.0.0
  description: E-commerce Product Service API

servers:
  - url: https://api.example.com/v1
    description: Production server
  - url: https://staging-api.example.com/v1
    description: Staging server

paths:
  /products:
    post:
      summary: Create a new product
      operationId: createProduct
      tags:
        - Products
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/CreateProductRequest"
      responses:
        "201":
          description: Product created successfully
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ProductResponse"
        "400":
          description: Invalid request
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"
        "500":
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"

    get:
      summary: Search products
      operationId: searchProducts
      tags:
        - Products
      parameters:
        - name: name
          in: query
          description: Product name to search
          schema:
            type: string
        - name: minPrice
          in: query
          description: Minimum price filter
          schema:
            type: number
            format: float
        - name: maxPrice
          in: query
          description: Maximum price filter
          schema:
            type: number
            format: float
        - name: isActive
          in: query
          description: Filter by active status
          schema:
            type: boolean
        - name: limit
          in: query
          description: Number of results to return
          schema:
            type: integer
            default: 20
            minimum: 1
            maximum: 100
        - name: offset
          in: query
          description: Number of results to skip
          schema:
            type: integer
            default: 0
            minimum: 0
      responses:
        "200":
          description: Products retrieved successfully
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ProductListResponse"

  /products/{productId}:
    get:
      summary: Get product by ID
      operationId: getProduct
      tags:
        - Products
      parameters:
        - name: productId
          in: path
          required: true
          description: Product ID
          schema:
            type: string
            format: uuid
      responses:
        "200":
          description: Product retrieved successfully
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ProductResponse"
        "404":
          description: Product not found
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorResponse"

components:
  schemas:
    CreateProductRequest:
      type: object
      required:
        - name
        - price
        - currency
        - inventory
      properties:
        name:
          type: string
          minLength: 3
          maxLength: 200
          example: "MacBook Pro 16-inch"
        description:
          type: string
          maxLength: 2000
          example: "High-performance laptop for professionals"
        price:
          type: number
          format: float
          minimum: 0.01
          example: 2499.99
        currency:
          type: string
          pattern: "^[A-Z]{3}$"
          example: "USD"
        inventory:
          type: integer
          minimum: 0
          example: 100

    ProductResponse:
      type: object
      properties:
        id:
          type: string
          format: uuid
          example: "550e8400-e29b-41d4-a716-446655440000"
        name:
          type: string
          example: "MacBook Pro 16-inch"
        description:
          type: string
          example: "High-performance laptop for professionals"
        price:
          type: number
          format: float
          example: 2499.99
        currency:
          type: string
          example: "USD"
        inventory:
          type: integer
          example: 100
        isActive:
          type: boolean
          example: true
        createdAt:
          type: string
          format: date-time
          example: "2024-01-15T09:30:00Z"
        updatedAt:
          type: string
          format: date-time
          example: "2024-01-15T09:30:00Z"

    ProductListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: "#/components/schemas/ProductResponse"
        pagination:
          type: object
          properties:
            limit:
              type: integer
              example: 20
            offset:
              type: integer
              example: 0
            total:
              type: integer
              example: 150

    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: string
              example: "VALIDATION_ERROR"
            message:
              type: string
              example: "Invalid request parameters"
            details:
              type: array
              items:
                type: object
                properties:
                  field:
                    type: string
                    example: "price"
                  message:
                    type: string
                    example: "Price must be greater than 0"
```

### PERFORMANCE OPTIMIZATION

#### Caching Strategy

```typescript
// src/infrastructure/cache/RedisCache.ts
import Redis from "ioredis";
import { ICache } from "@shared/infrastructure/ICache";

export class RedisCache implements ICache {
  private client: Redis;
  private defaultTTL = 3600; // 1 hour

  constructor(redisUrl: string) {
    this.client = new Redis(redisUrl, {
      enableReadyCheck: true,
      maxRetriesPerRequest: 3,
      retryStrategy: (times) => {
        const delay = Math.min(times * 50, 2000);
        return delay;
      },
    });

    this.client.on("error", (err) => {
      console.error("Redis Client Error:", err);
    });
  }

  async get<T>(key: string): Promise<T | null> {
    try {
      const value = await this.client.get(key);
      if (!value) return null;

      return JSON.parse(value) as T;
    } catch (error) {
      console.error(`Cache get error for key ${key}:`, error);
      return null;
    }
  }

  async set<T>(key: string, value: T, ttl?: number): Promise<void> {
    try {
      const serialized = JSON.stringify(value);
      const expiry = ttl || this.defaultTTL;

      await this.client.setex(key, expiry, serialized);
    } catch (error) {
      console.error(`Cache set error for key ${key}:`, error);
    }
  }

  async delete(key: string): Promise<void> {
    try {
      await this.client.del(key);
    } catch (error) {
      console.error(`Cache delete error for key ${key}:`, error);
    }
  }

  async invalidatePattern(pattern: string): Promise<void> {
    try {
      const keys = await this.client.keys(pattern);
      if (keys.length > 0) {
        await this.client.del(...keys);
      }
    } catch (error) {
      console.error(`Cache invalidate pattern error for ${pattern}:`, error);
    }
  }
}

// Cache-Aside Pattern Implementation
export class CachedProductRepository implements IProductRepository {
  constructor(
    private repository: IProductRepository,
    private cache: ICache,
  ) {}

  async findById(id: ProductId): Promise<Result<Product | null>> {
    const cacheKey = `product:${id.value}`;

    // Try cache first
    const cached = await this.cache.get<any>(cacheKey);
    if (cached) {
      const product = this.deserializeProduct(cached);
      return Result.ok<Product | null>(product);
    }

    // Cache miss - fetch from database
    const result = await this.repository.findById(id);

    if (result.isSuccess && result.getValue()) {
      // Cache the result
      await this.cache.set(
        cacheKey,
        this.serializeProduct(result.getValue()),
        300, // 5 minutes TTL
      );
    }

    return result;
  }

  async save(product: Product): Promise<Result<void>> {
    const result = await this.repository.save(product);

    if (result.isSuccess) {
      // Invalidate cache
      const cacheKey = `product:${product.productId.value}`;
      await this.cache.delete(cacheKey);

      // Invalidate search cache
      await this.cache.invalidatePattern("product:search:*");
    }

    return result;
  }

  private serializeProduct(product: Product): any {
    return {
      id: product.productId.value,
      name: product.name,
      description: product.description,
      price: product.price.amount,
      currency: product.price.currency,
      inventory: product.inventory,
      isActive: product.isActive,
    };
  }

  private deserializeProduct(data: any): Product {
    const price = Price.create(data.price, data.currency).getValue();
    return Product.create(
      {
        name: data.name,
        description: data.description,
        price,
        inventory: data.inventory,
        isActive: data.isActive,
      },
      data.id,
    ).getValue();
  }
}
```

### SECURITY IMPLEMENTATION

#### Authentication Middleware

```typescript
// src/interfaces/http/middleware/AuthMiddleware.ts
import { Request, Response, NextFunction } from "express";
import jwt from "jsonwebtoken";

export interface AuthRequest extends Request {
  user?: {
    id: string;
    email: string;
    roles: string[];
  };
}

export class AuthMiddleware {
  constructor(
    private jwtSecret: string,
    private jwtIssuer: string,
  ) {}

  authenticate() {
    return async (req: AuthRequest, res: Response, next: NextFunction) => {
      try {
        const token = this.extractToken(req);

        if (!token) {
          return res.status(401).json({
            error: {
              code: "UNAUTHORIZED",
              message: "Authentication required",
            },
          });
        }

        const decoded = jwt.verify(token, this.jwtSecret, {
          issuer: this.jwtIssuer,
          algorithms: ["HS256"],
        }) as any;

        req.user = {
          id: decoded.sub,
          email: decoded.email,
          roles: decoded.roles || [],
        };

        next();
      } catch (error) {
        if (error.name === "TokenExpiredError") {
          return res.status(401).json({
            error: {
              code: "TOKEN_EXPIRED",
              message: "Token has expired",
            },
          });
        }

        return res.status(401).json({
          error: {
            code: "INVALID_TOKEN",
            message: "Invalid authentication token",
          },
        });
      }
    };
  }

  authorize(...allowedRoles: string[]) {
    return (req: AuthRequest, res: Response, next: NextFunction) => {
      if (!req.user) {
        return res.status(401).json({
          error: {
            code: "UNAUTHORIZED",
            message: "Authentication required",
          },
        });
      }

      const hasRole = allowedRoles.some((role) =>
        req.user.roles.includes(role),
      );

      if (!hasRole) {
        return res.status(403).json({
          error: {
            code: "FORBIDDEN",
            message: "Insufficient permissions",
          },
        });
      }

      next();
    };
  }

  private extractToken(req: Request): string | null {
    const authHeader = req.headers.authorization;

    if (authHeader && authHeader.startsWith("Bearer ")) {
      return authHeader.substring(7);
    }

    return null;
  }
}

// Input Validation Middleware
export class ValidationMiddleware {
  static validateCreateProduct() {
    return [
      body("name")
        .trim()
        .isLength({ min: 3, max: 200 })
        .withMessage("Name must be between 3 and 200 characters")
        .escape(),
      body("description")
        .optional()
        .trim()
        .isLength({ max: 2000 })
        .withMessage("Description must not exceed 2000 characters")
        .escape(),
      body("price")
        .isFloat({ min: 0.01 })
        .withMessage("Price must be greater than 0"),
      body("currency")
        .matches(/^[A-Z]{3}$/)
        .withMessage("Currency must be a 3-letter code"),
      body("inventory")
        .isInt({ min: 0 })
        .withMessage("Inventory must be a non-negative integer"),
      ValidationMiddleware.handleValidationErrors,
    ];
  }

  static handleValidationErrors(
    req: Request,
    res: Response,
    next: NextFunction,
  ) {
    const errors = validationResult(req);

    if (!errors.isEmpty()) {
      return res.status(400).json({
        error: {
          code: "VALIDATION_ERROR",
          message: "Invalid request parameters",
          details: errors.array().map((err) => ({
            field: err.param,
            message: err.msg,
          })),
        },
      });
    }

    next();
  }
}
```

### MONITORING & OBSERVABILITY

#### Logging Configuration

```typescript
// src/shared/infrastructure/Logger.ts
import winston from "winston";
import { ElasticsearchTransport } from "winston-elasticsearch";

export class Logger {
  private logger: winston.Logger;

  constructor() {
    const esTransport = new ElasticsearchTransport({
      level: "info",
      clientOpts: {
        node: process.env.ELASTICSEARCH_URL || "http://localhost:9200",
      },
      index: "product-service-logs",
    });

    this.logger = winston.createLogger({
      level: process.env.LOG_LEVEL || "info",
      format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.errors({ stack: true }),
        winston.format.json(),
      ),
      defaultMeta: {
        service: "product-service",
        environment: process.env.NODE_ENV,
      },
      transports: [
        new winston.transports.Console({
          format: winston.format.combine(
            winston.format.colorize(),
            winston.format.simple(),
          ),
        }),
        esTransport,
      ],
    });
  }

  info(message: string, meta?: any) {
    this.logger.info(message, meta);
  }

  error(message: string, error?: Error, meta?: any) {
    this.logger.error(message, {
      ...meta,
      error: error
        ? {
            message: error.message,
            stack: error.stack,
          }
        : undefined,
    });
  }

  warn(message: string, meta?: any) {
    this.logger.warn(message, meta);
  }

  debug(message: string, meta?: any) {
    this.logger.debug(message, meta);
  }
}

// Metrics Collection
import { Registry, Counter, Histogram, Gauge } from "prom-client";

export class MetricsCollector {
  private registry: Registry;
  private httpRequestDuration: Histogram<string>;
  private httpRequestTotal: Counter<string>;
  private activeConnections: Gauge<string>;

  constructor() {
    this.registry = new Registry();

    this.httpRequestDuration = new Histogram({
      name: "http_request_duration_seconds",
      help: "Duration of HTTP requests in seconds",
      labelNames: ["method", "route", "status_code"],
      buckets: [0.1, 0.5, 1, 2, 5],
    });

    this.httpRequestTotal = new Counter({
      name: "http_requests_total",
      help: "Total number of HTTP requests",
      labelNames: ["method", "route", "status_code"],
    });

    this.activeConnections = new Gauge({
      name: "active_connections",
      help: "Number of active connections",
    });

    this.registry.registerMetric(this.httpRequestDuration);
    this.registry.registerMetric(this.httpRequestTotal);
    this.registry.registerMetric(this.activeConnections);
  }

  recordHttpRequest(
    method: string,
    route: string,
    statusCode: number,
    duration: number,
  ) {
    this.httpRequestDuration.observe(
      { method, route, status_code: statusCode.toString() },
      duration,
    );

    this.httpRequestTotal.inc({
      method,
      route,
      status_code: statusCode.toString(),
    });
  }

  incrementActiveConnections() {
    this.activeConnections.inc();
  }

  decrementActiveConnections() {
    this.activeConnections.dec();
  }

  getMetrics() {
    return this.registry.metrics();
  }
}
```

## Usage Instructions

1. Start with clear requirements and constraints
2. Design the system architecture before coding
3. Apply SOLID principles and design patterns appropriately
4. Write tests alongside or before implementation
5. Document code and APIs thoroughly
6. Consider security, performance, and scalability from the start
7. Use proper error handling and logging
8. Follow language-specific best practices and conventions

## Examples

### Example 1: Real-time Chat Application

**Input**:

```
{{project_type}}: Real-time chat application
{{language_stack}}: Python/FastAPI with WebSockets
{{architecture_style}}: Microservices
{{requirements}}: 10k concurrent users, message history, file sharing
{{specific_features}}: Private rooms, typing indicators, read receipts
```

**Output**: [Complete implementation with FastAPI WebSocket server, Redis pub/sub for scaling, PostgreSQL for history, S3 for files, and comprehensive real-time features]

## Related Prompts

- [API Design Expert](/prompts/creation/api-design-expert.md)
- [Database Schema Designer](/prompts/creation/database-schema-designer.md)
- [DevOps Pipeline Creator](/prompts/creation/devops-pipeline-creator.md)

## Research Notes

- Emphasizes clean architecture and SOLID principles
- Includes comprehensive testing strategies
- Covers full stack from domain logic to infrastructure
- Addresses production concerns like monitoring and security
- Provides complete, runnable code examples
