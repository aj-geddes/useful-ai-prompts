---
name: api-reference-documentation
description: >
  Create comprehensive API reference documentation with OpenAPI/Swagger specs,
  REST endpoints, authentication, examples, and SDKs. Use when documenting REST
  APIs, GraphQL APIs, endpoint documentation, or OpenAPI specifications.
---

# API Reference Documentation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Generate professional API documentation that developers can use to integrate with your API, including endpoint specifications, authentication, request/response examples, and interactive documentation.

## When to Use

- Documenting REST APIs
- Creating OpenAPI/Swagger specifications
- GraphQL API documentation
- SDK and client library docs
- API authentication guides
- Rate limiting documentation
- Webhook documentation
- API versioning guides

## Quick Start

Minimal working example:

```yaml
openapi: 3.0.3
info:
  title: E-Commerce API
  description: |
    Complete API for managing e-commerce operations including products,
    orders, customers, and payments.

    ## Authentication
    All endpoints require Bearer token authentication. Include your API key
    in the Authorization header: `Authorization: Bearer YOUR_API_KEY`

    ## Rate Limiting
    - 1000 requests per hour for authenticated users
    - 100 requests per hour for unauthenticated requests

    ## Pagination
    List endpoints return paginated results with `page` and `limit` parameters.
  version: 2.0.0
  contact:
    name: API Support
    email: api@example.com
    url: https://example.com/support
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [OpenAPI Specification Example](references/openapi-specification-example.md) | openapi: 3.0.3 |
| [List Products](references/list-products.md) | List Products |

## Best Practices

### ✅ DO

- Use OpenAPI 3.0+ specification
- Include request/response examples for every endpoint
- Document all query parameters and headers
- Provide authentication examples
- Include error response formats
- Document rate limits and pagination
- Use consistent naming conventions
- Include SDK examples in multiple languages
- Document webhook payloads
- Provide interactive API explorer (Swagger UI)
- Version your API documentation
- Include migration guides for breaking changes

### ❌ DON'T

- Skip error response documentation
- Forget to document authentication
- Use inconsistent terminology
- Leave endpoints undocumented
- Ignore deprecation notices
- Skip versioning information
