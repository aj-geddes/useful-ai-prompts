# Security Best Practices

## Security Best Practices

```dockerfile
FROM node:18-alpine

# Update packages for security patches
RUN apk update && apk upgrade

# Don't run as root
RUN addgroup -g 1001 appgroup && adduser -S -u 1001 -G appgroup appuser
USER appuser

# Use specific versions, not 'latest'
WORKDIR /app

# Scan for vulnerabilities
# Run: docker scan your-image:tag
```


## Environment Configuration

```dockerfile
# Use build arguments for flexibility
ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s \
  CMD node healthcheck.js || exit 1

# Labels for metadata
LABEL maintainer="team@example.com" \
      version="1.0.0" \
      description="Production API service"
```
