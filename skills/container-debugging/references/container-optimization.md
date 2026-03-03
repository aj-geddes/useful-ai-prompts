# Container Optimization

## Container Optimization

```yaml
Resource Limits:

Set in docker-compose:
  version: '3'
  services:
    app:
      image: myapp
      environment:
        - NODE_ENV=production
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M

Limits: Maximum resources
Reservations: Guaranteed resources

---

Multi-Stage Builds:

FROM node:16 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:16-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY package*.json ./
RUN npm install --production
EXPOSE 3000
CMD ["node", "dist/index.js"]

Result: 1GB → 200MB image size
```
