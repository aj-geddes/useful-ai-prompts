---
name: fastapi-development
description: >
  Build high-performance FastAPI applications with async routes, validation,
  dependency injection, security, and automatic API documentation. Use when
  developing modern Python APIs with async support, automatic OpenAPI
  documentation, and high performance requirements.
---

# FastAPI Development

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Create fast, modern Python APIs using FastAPI with async/await support, automatic API documentation, type validation using Pydantic, dependency injection, JWT authentication, and SQLAlchemy ORM integration.

## When to Use

- Building high-performance Python REST APIs
- Creating async API endpoints
- Implementing automatic OpenAPI/Swagger documentation
- Leveraging Python type hints for validation
- Building microservices with async support
- Integrating Pydantic for data validation

## Quick Start

Minimal working example:

```python
# main.py
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI instance
app = FastAPI(
    title="API Service",
    description="A modern FastAPI application",
    version="1.0.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [FastAPI Application Setup](references/fastapi-application-setup.md) | FastAPI Application Setup |
| [Pydantic Models for Validation](references/pydantic-models-for-validation.md) | Pydantic Models for Validation |
| [Async Database Models and Queries](references/async-database-models-and-queries.md) | Async Database Models and Queries |
| [Security and JWT Authentication](references/security-and-jwt-authentication.md) | Security and JWT Authentication |
| [Service Layer for Business Logic](references/service-layer-for-business-logic.md) | Service Layer for Business Logic |
| [API Routes with Async Endpoints](references/api-routes-with-async-endpoints.md) | API Routes with Async Endpoints |

## Best Practices

### ✅ DO

- Use async/await for I/O operations
- Leverage Pydantic for validation
- Use dependency injection for services
- Implement proper error handling with HTTPException
- Use type hints for automatic OpenAPI documentation
- Create service layers for business logic
- Implement authentication on protected routes
- Use environment variables for configuration
- Return appropriate HTTP status codes
- Document endpoints with docstrings and tags

### ❌ DON'T

- Use synchronous database operations
- Trust user input without validation
- Store secrets in code
- Ignore type hints
- Return database models in responses
- Implement authentication in route handlers
- Use mutable default arguments
- Forget to validate query parameters
- Expose stack traces in production
