---
name: django-application
description: >
  Develop production-grade Django applications with models, views, ORM queries,
  authentication, and admin interfaces. Use when building web applications,
  managing databases with Django ORM, and implementing authentication systems.
---

# Django Application

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build comprehensive Django web applications with proper model design, view hierarchies, database operations, user authentication, and admin functionality following Django conventions and best practices.

## When to Use

- Creating Django web applications
- Designing models and database schemas
- Implementing views and URL routing
- Building authentication systems
- Using Django ORM for database operations
- Creating admin interfaces and dashboards

## Quick Start

Minimal working example:

```bash
django-admin startproject myproject
cd myproject
python manage.py startapp users
python manage.py startapp products
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Django Project Setup](references/django-project-setup.md) | Django Project Setup |
| [Model Design with ORM](references/model-design-with-orm.md) | Model Design with ORM |
| [Views with Class-Based and Function-Based Approaches](references/views-with-class-based-and-function-based-approaches.md) | Views with Class-Based and Function-Based Approaches |
| [Authentication and Permissions](references/authentication-and-permissions.md) | Authentication and Permissions |
| [Database Queries and Optimization](references/database-queries-and-optimization.md) | Database Queries and Optimization |
| [URL Routing](references/url-routing.md) | URL Routing |
| [Admin Interface Customization](references/admin-interface-customization.md) | Admin Interface Customization |

## Best Practices

### ✅ DO

- Use models for database operations
- Implement proper indexes on frequently queried fields
- Use select_related and prefetch_related for query optimization
- Implement authentication and permissions
- Use Django Forms for form validation
- Cache expensive queries
- Use management commands for batch operations
- Implement logging for debugging
- Use middleware for cross-cutting concerns
- Validate user input

### ❌ DON'T

- Use raw SQL without ORM
- N+1 query problems without optimization
- Store secrets in code
- Trust user input directly
- Override **init** in models unnecessarily
- Make synchronous heavy operations in views
- Use inheritance models unless necessary
- Expose stack traces in production
