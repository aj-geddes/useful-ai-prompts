# Optimization Techniques

## Optimization Techniques

### Layer Caching

```dockerfile
# ❌ Poor caching - changes in source code invalidate dependency install
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

# ✅ Good caching - dependencies cached separately
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
```

### Minimize Image Size

```dockerfile
# ❌ Large image (~800MB)
FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip

# ✅ Minimal image (~50MB)
FROM python:3.11-alpine
```
