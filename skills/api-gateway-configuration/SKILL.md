---
name: api-gateway-configuration
description: Configure API gateways for routing, authentication, rate limiting, and request/response transformation. Use when deploying microservices, setting up reverse proxies, or managing API traffic.
---

# API Gateway Configuration

## Overview

Design and configure API gateways to handle routing, authentication, rate limiting, and request/response transformation for microservice architectures.

## When to Use

- Setting up reverse proxies for microservices
- Centralizing API authentication
- Implementing request/response transformation
- Managing traffic across backend services
- Rate limiting and quota enforcement
- API versioning and routing

## Instructions

### 1. **Kong Configuration**

```yaml
# kong.yml - Kong Gateway configuration
_format_version: "2.1"
_transform: true

services:
  - name: user-service
    url: http://user-service:3000
    routes:
      - name: user-routes
        paths:
          - /api/users
          - /api/profile
    plugins:
      - name: rate-limiting
        config:
          minute: 100
          policy: local
      - name: jwt
        config:
          secret: your-secret-key
          key_claim_name: "sub"
      - name: cors
        config:
          origins:
            - "http://localhost:3000"
            - "https://example.com"
          methods:
            - GET
            - POST
            - PUT
            - DELETE
          allow_headers:
            - Content-Type
            - Authorization

  - name: product-service
    url: http://product-service:3001
    routes:
      - name: product-routes
        paths:
          - /api/products
    plugins:
      - name: rate-limiting
        config:
          minute: 500
      - name: request-transformer
        config:
          add:
            headers:
              - "X-Service-Name:product-service"

  - name: order-service
    url: http://order-service:3002
    routes:
      - name: order-routes
        paths:
          - /api/orders
    plugins:
      - name: jwt
      - name: request-size-limiting
        config:
          allowed_payload_size: 5

consumers:
  - username: mobile-app
    custom_id: mobile-app-001
    acls:
      - group: api-users

plugins:
  - name: prometheus
    config:
      latency_metrics: true
      upstream_addr_header: X-Upstream-Addr
```

### 2. **Nginx Configuration**

```nginx
# nginx.conf - API Gateway configuration
upstream user_service {
    server user-service:3000;
    keepalive 32;
}

upstream product_service {
    server product-service:3001;
    keepalive 32;
}

upstream order_service {
    server order-service:3002;
    keepalive 32;
}

# Rate limiting
limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
limit_req_zone $http_x_api_key zone=user_limit:10m rate=100r/s;

server {
    listen 80;
    server_name api.example.com;

    # Enable gzip compression
    gzip on;
    gzip_types application/json;
    gzip_min_length 1000;

    # User Service Routes
    location /api/users {
        limit_req zone=api_limit burst=20 nodelay;

        # Authentication check
        access_by_lua_block {
            local token = ngx.var.http_authorization
            if not token then
                return ngx.HTTP_UNAUTHORIZED
            end
        }

        proxy_pass http://user_service;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Request timeout
        proxy_connect_timeout 10s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;
    }

    # Product Service Routes
    location /api/products {
        limit_req zone=api_limit burst=50 nodelay;

        proxy_pass http://product_service;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        # Caching
        proxy_cache api_cache;
        proxy_cache_valid 200 1m;
        proxy_cache_key "$scheme$request_method$host$request_uri";
    }

    # Order Service Routes (requires auth)
    location /api/orders {
        limit_req zone=user_limit burst=10 nodelay;

        auth_request /auth;
        auth_request_set $auth_user $upstream_http_x_user_id;

        proxy_pass http://order_service;
        proxy_http_version 1.1;
        proxy_set_header X-User-ID $auth_user;
    }

    # Health check endpoint
    location /health {
        access_log off;
        return 200 "healthy\n";
        add_header Content-Type text/plain;
    }

    # Metrics endpoint
    location /metrics {
        stub_status on;
        access_log off;
    }
}

# Cache definition
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=api_cache:10m max_size=1g inactive=60m;
```

### 3. **AWS API Gateway Configuration**

```yaml
# AWS SAM template for API Gateway
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  ApiGateway:
    Type: AWS::Serverless::Api
    Properties:
      StageName: prod
      Auth:
        DefaultAuthorizer: JwtAuthorizer
        Authorizers:
          JwtAuthorizer:
            FunctionArn: !GetAtt AuthorizerFunction.Arn
            Identity:
              Headers:
                - Authorization
      TracingEnabled: true
      MethodSettings:
        - ResourcePath: '/*'
          HttpMethod: '*'
          LoggingLevel: INFO
          DataTraceEnabled: true
          MetricsEnabled: true
          ThrottleSettings:
            BurstLimit: 1000
            RateLimit: 100

  UserServiceFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      Runtime: nodejs18.x
      Environment:
        Variables:
          USER_SERVICE_URL: !Sub 'https://${UserServiceAlb}.elb.amazonaws.com'
      Events:
        GetUsers:
          Type: Api
          Properties:
            RestApiId: !Ref ApiGateway
            Path: /api/users
            Method: GET
            Auth:
              Authorizer: JwtAuthorizer
        CreateUser:
          Type: Api
          Properties:
            RestApiId: !Ref ApiGateway
            Path: /api/users
            Method: POST
            Auth:
              Authorizer: JwtAuthorizer

  ApiUsagePlan:
    Type: AWS::ApiGateway::UsagePlan
    Properties:
      UsagePlanName: StandardPlan
      ApiStages:
        - ApiId: !Ref ApiGateway
          Stage: prod
      Quota:
        Limit: 10000
        Period: DAY
      Throttle:
        RateLimit: 100
        BurstLimit: 1000

  ApiKey:
    Type: AWS::ApiGateway::ApiKey
    Properties:
      Name: StandardKey
      Enabled: true
      UsagePlanId: !Ref ApiUsagePlan
```

### 4. **Traefik Configuration**

```yaml
# traefik.yml - Traefik API Gateway
global:
  checkNewVersion: false
  sendAnonymousUsage: false

entryPoints:
  web:
    address: ":80"
  websecure:
    address: ":443"

api:
  insecure: true
  dashboard: true

providers:
  docker:
    endpoint: "unix:///var/run/docker.sock"
    exposedByDefault: false
  file:
    filename: dynamic.yml

middleware:
  rateLimit:
    rateLimit:
      average: 100
      burst: 50

  authMiddleware:
    basicAuth:
      users:
        - "user:$apr1$r31.....$HqJZimcKQFAMYayBlzkrA/"

routers:
  api-users:
    entrypoints:
      - websecure
    rule: "Path(`/api/users`)"
    service: user-service
    tls:
      certResolver: letsencrypt
    middlewares:
      - rateLimit

  api-products:
    entrypoints:
      - web
    rule: "Path(`/api/products`)"
    service: product-service

services:
  user-service:
    loadBalancer:
      servers:
        - url: "http://user-service:3000"
      healthCheck:
        scheme: http
        path: /health
        interval: 10s
        timeout: 5s

  product-service:
    loadBalancer:
      servers:
        - url: "http://product-service:3001"
```

### 5. **Node.js Gateway Implementation**

```javascript
const express = require('express');
const httpProxy = require('express-http-proxy');
const rateLimit = require('express-rate-limit');
const jwt = require('jsonwebtoken');

const app = express();

// Rate limiting
const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: 100
});

// JWT verification
const verifyJwt = (req, res, next) => {
  const token = req.headers['authorization']?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });

  try {
    jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch (err) {
    res.status(403).json({ error: 'Invalid token' });
  }
};

// Request logging
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} ${req.method} ${req.path}`);
  next();
});

app.use(limiter);

// User service proxy
app.use('/api/users', verifyJwt, httpProxy('http://user-service:3000', {
  proxyReqPathResolver: (req) => `/api/users${req.url}`,
  userResDecorator: (proxyRes, proxyResData, userReq, userRes) => {
    proxyRes.headers['X-Gateway'] = 'true';
    return proxyResData;
  }
}));

// Product service proxy
app.use('/api/products', httpProxy('http://product-service:3001', {
  proxyReqPathResolver: (req) => `/api/products${req.url}`
}));

// Health check
app.get('/health', (req, res) => res.json({ status: 'ok' }));

app.listen(8080, () => console.log('Gateway on port 8080'));
```

## Best Practices

### ✅ DO
- Centralize authentication at gateway level
- Implement rate limiting globally
- Add comprehensive logging
- Use health checks for backends
- Cache responses when appropriate
- Implement circuit breakers
- Monitor gateway metrics
- Use HTTPS in production

### ❌ DON'T
- Expose backend service details
- Skip request validation
- Forget to log API usage
- Use weak authentication
- Over-cache dynamic data
- Ignore backend timeouts
- Skip security headers
- Expose internal IPs

## Monitoring & Observability

```javascript
// Prometheus metrics
const promClient = require('prom-client');

const httpRequestDuration = new promClient.Histogram({
  name: 'gateway_http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status_code']
});

const httpRequests = new promClient.Counter({
  name: 'gateway_http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status_code']
});

app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    httpRequestDuration.labels(req.method, req.path, res.statusCode).observe(duration);
    httpRequests.labels(req.method, req.path, res.statusCode).inc();
  });
  next();
});
```
