# Kong Configuration

## Kong Configuration

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
