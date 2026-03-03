---
name: error-tracking
description: >
  Implement error tracking with Sentry for automatic exception monitoring,
  release tracking, and performance issues. Use when setting up error
  monitoring, tracking bugs in production, or analyzing application stability.
---

# Error Tracking

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Set up comprehensive error tracking with Sentry to automatically capture, report, and analyze exceptions, performance issues, and application stability.

## When to Use

- Production error monitoring
- Automatic exception capture
- Release tracking
- Performance issue detection
- User impact analysis

## Quick Start

Minimal working example:

```bash
npm install -g @sentry/cli
npm install @sentry/node @sentry/tracing
sentry init -d
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Sentry Setup](references/sentry-setup.md) | Sentry Setup, Node.js Sentry Integration |
| [Express Middleware Integration](references/express-middleware-integration.md) | Express Middleware Integration |
| [Python Sentry Integration](references/python-sentry-integration.md) | Python Sentry Integration |
| [Source Maps and Release Management](references/source-maps-and-release-management.md) | Source Maps and Release Management, CI/CD Release Creation |
| [Custom Error Context](references/custom-error-context.md) | Custom Error Context |
| [Performance Monitoring](references/performance-monitoring.md) | Performance Monitoring |

## Best Practices

### ✅ DO

- Set up source maps for production
- Configure appropriate sample rates
- Track releases and deployments
- Filter sensitive information
- Add meaningful context to errors
- Use breadcrumbs for debugging
- Set user information
- Review error patterns regularly

### ❌ DON'T

- Send 100% of errors in production
- Include passwords in context
- Ignore configuration for environment
- Skip source map uploads
- Log personally identifiable information
- Use without proper filtering
- Disable tracking in production
