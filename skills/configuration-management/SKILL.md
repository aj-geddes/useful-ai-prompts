---
name: configuration-management
description: >
  Manage application configuration including environment variables, settings
  management, configuration hierarchies, secret management, feature flags, and
  12-factor app principles. Use for config, environment setup, or settings
  management.
---

# Configuration Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Comprehensive guide to managing application configuration across environments, including environment variables, configuration files, secrets, feature flags, and following 12-factor app methodology.

## When to Use

- Setting up configuration for different environments
- Managing secrets and credentials
- Implementing feature flags
- Creating configuration hierarchies
- Following 12-factor app principles
- Migrating configuration to cloud services
- Implementing dynamic configuration
- Managing multi-tenant configurations

## Quick Start

Minimal working example:

```bash
# .env.development
NODE_ENV=development
PORT=3000
DATABASE_URL=postgresql://localhost:5432/myapp_dev
REDIS_URL=redis://localhost:6379
LOG_LEVEL=debug
API_KEY=dev-api-key-12345

# .env.production
NODE_ENV=production
PORT=8080
DATABASE_URL=${DATABASE_URL}  # From environment
REDIS_URL=${REDIS_URL}
LOG_LEVEL=info
API_KEY=${API_KEY}  # From secret manager

# .env.test
NODE_ENV=test
DATABASE_URL=postgresql://localhost:5432/myapp_test
LOG_LEVEL=error
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Environment Variables](references/environment-variables.md) | Environment Variables |
| [Configuration Hierarchies](references/configuration-hierarchies.md) | Configuration Hierarchies |
| [Secret Management](references/secret-management.md) | Secret Management |
| [Feature Flags](references/feature-flags.md) | Feature Flags |
| [12-Factor App Configuration](references/12-factor-app-configuration.md) | 12-Factor App Configuration |
| [Configuration Validation](references/configuration-validation.md) | Configuration Validation |
| [Dynamic Configuration (Remote Config)](references/dynamic-configuration-remote-config.md) | Dynamic Configuration (Remote Config) |

## Best Practices

### ✅ DO

- Store configuration in environment variables
- Use different config files per environment
- Validate configuration on startup
- Use secret managers for sensitive data
- Never commit secrets to version control
- Provide sensible defaults
- Document all configuration options
- Use type-safe configuration objects
- Implement configuration hierarchy (base + overrides)
- Use feature flags for gradual rollouts
- Follow 12-factor app principles
- Implement graceful degradation for missing config
- Cache secrets to reduce API calls

### ❌ DON'T

- Hardcode configuration in source code
- Commit .env files with real secrets
- Use different config formats across services
- Store secrets in plain text
- Expose configuration through APIs
- Use production credentials in development
- Ignore configuration validation errors
- Access process.env directly everywhere
- Store configuration in databases (circular dependency)
- Mix configuration with business logic
