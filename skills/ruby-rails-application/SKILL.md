---
name: ruby-rails-application
description: >
  Develop Ruby on Rails applications with models, controllers, views, Active
  Record ORM, authentication, and RESTful routes. Use when building Rails
  applications, managing database relationships, and implementing MVC
  architecture.
---

# Ruby Rails Application

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build comprehensive Ruby on Rails applications with proper model associations, RESTful controllers, Active Record queries, authentication systems, middleware chains, and view rendering following Rails conventions.

## When to Use

- Building Rails web applications
- Implementing Active Record models with associations
- Creating RESTful controllers and actions
- Integrating authentication and authorization
- Building complex database relationships
- Implementing Rails middleware and filters

## Quick Start

Minimal working example:

```bash
rails new myapp --api --database=postgresql
cd myapp
rails db:create
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Rails Project Setup](references/rails-project-setup.md) | Rails Project Setup |
| [Models with Active Record](references/models-with-active-record.md) | Models with Active Record |
| [Database Migrations](references/database-migrations.md) | Database Migrations |
| [Controllers with RESTful Actions](references/controllers-with-restful-actions.md) | Controllers with RESTful Actions |
| [Authentication with JWT](references/authentication-with-jwt.md) | Authentication with JWT |
| [Active Record Queries](references/active-record-queries.md) | Active Record Queries |
| [Serializers](references/serializers.md) | Serializers |

## Best Practices

### ✅ DO

- Use conventions over configuration
- Leverage Active Record associations
- Implement proper scopes for queries
- Use strong parameters for security
- Implement authentication in ApplicationController
- Use services for complex business logic
- Implement proper error handling
- Use database migrations for schema changes
- Validate all inputs at model level
- Use before_action filters appropriately

### ❌ DON'T

- Use raw SQL without parameterization
- Implement business logic in controllers
- Trust user input without validation
- Store secrets in code
- Use select \* without specifying columns
- Forget N+1 query problems (use includes/joins)
- Implement authentication in each controller
- Use global variables
- Ignore database constraints
