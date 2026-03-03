# Docker Registry Configuration

## Docker Registry Configuration

```dockerfile
# Dockerfile with multi-stage build for optimization
FROM node:18-alpine AS dependencies
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:18-alpine AS runtime
WORKDIR /app
COPY --from=dependencies /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY package*.json ./

EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
  CMD node healthcheck.js

CMD ["node", "dist/server.js"]

LABEL org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.description="Production application" \
      org.opencontainers.image.authors="DevOps Team"
```
