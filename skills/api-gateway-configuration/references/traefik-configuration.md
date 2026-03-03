# Traefik Configuration

## Traefik Configuration

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
