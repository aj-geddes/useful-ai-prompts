# Turborepo Commands

## Turborepo Commands

```bash
# Build all packages with dependency order
turbo run build

# Build with specific filters
turbo run build --filter=web --filter=api

# Build excluding certain packages
turbo run build --filter='!./apps/mobile'

# Run tests with caching
turbo run test --cache-dir=.turbo

# Run in development mode (no cache)
turbo run dev --parallel

# Show execution graph
turbo run build --graph

# Profile build times
turbo run build --profile=profile.json
```
