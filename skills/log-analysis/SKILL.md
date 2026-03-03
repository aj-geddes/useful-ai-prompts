---
name: log-analysis
description: >
  Analyze application and system logs to identify errors, patterns, and root
  causes. Use log aggregation tools and structured logging for effective
  debugging.
---

# Log Analysis

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Logs are critical for debugging and monitoring. Effective log analysis quickly identifies issues and enables root cause analysis.

## When to Use

- Troubleshooting errors
- Performance investigation
- Security incident analysis
- Auditing user actions
- Monitoring application health

## Quick Start

Minimal working example:

```javascript
// Good: Structured logs (machine-readable)
logger.info({
  level: 'INFO',
  timestamp: '2024-01-15T10:30:00Z',
  service: 'auth-service',
  user_id: '12345',
  action: 'user_login',
  status: 'success',
  duration_ms: 150,
  ip_address: '192.168.1.1'
});

// Bad: Unstructured logs (hard to parse)
console.log('User 12345 logged in successfully in 150ms from 192.168.1.1');

// JSON Format (Elasticsearch friendly)
{
  "@timestamp": "2024-01-15T10:30:00Z",
  "level": "ERROR",
  "service": "api-gateway",
  "trace_id": "abc123",
  "message": "Database connection failed",
  "error": {
    "type": "ConnectionError",
    "code": "ECONNREFUSED"
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Structured Logging](references/structured-logging.md) | Structured Logging |
| [Log Levels & Patterns](references/log-levels-patterns.md) | Log Levels & Patterns |
| [Log Analysis Tools](references/log-analysis-tools.md) | Log Analysis Tools |
| [Common Log Analysis Queries](references/common-log-analysis-queries.md) | Common Log Analysis Queries |

## Best Practices

### ✅ DO

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
