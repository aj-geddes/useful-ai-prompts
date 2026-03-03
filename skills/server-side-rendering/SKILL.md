---
name: server-side-rendering
description: >
  Implement server-side rendering with template engines, view layers, and
  dynamic content generation. Use when building server-rendered applications,
  implementing MVC architectures, and generating HTML on the server.
---

# Server-Side Rendering

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build server-side rendered applications using modern template engines, view layers, and data-driven HTML generation with caching, streaming, and performance optimization across Python, Node.js, and Ruby frameworks.

## When to Use

- Building traditional web applications
- Rendering HTML on the server
- Implementing SEO-friendly applications
- Creating real-time updating pages
- Building admin dashboards
- Implementing email templates

## Quick Start

Minimal working example:

```python
# app.py
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Custom Jinja2 filters
@app.template_filter('currency')
def format_currency(value):
    return f"${value:.2f}"

@app.template_filter('date_format')
def format_date(date_obj):
    return date_obj.strftime('%Y-%m-%d %H:%M:%S')

@app.context_processor
def inject_globals():
    """Inject global variables into templates"""
    return {
        'app_name': 'My App',
        'current_year': datetime.now().year,
        'support_email': 'support@example.com'
    }

# routes.py
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Flask with Jinja2 Templates](references/flask-with-jinja2-templates.md) | Flask with Jinja2 Templates |
| [Jinja2 Template Examples](references/jinja2-template-examples.md) | Jinja2 Template Examples |
| [Node.js/Express with EJS Templates](references/nodejsexpress-with-ejs-templates.md) | Node.js/Express with EJS Templates |
| [EJS Template Examples](references/ejs-template-examples.md) | EJS Template Examples |
| [Caching and Performance](references/caching-and-performance.md) | Caching and Performance |
| [Django Template Examples](references/django-template-examples.md) | Django Template Examples |
| [Django Templates](references/django-templates.md) | Django Templates |

## Best Practices

### ✅ DO

- Use template inheritance for DRY code
- Implement caching for frequently rendered pages
- Use template filters for formatting
- Separate concerns between views and templates
- Validate and sanitize all user input
- Use context processors for global variables
- Implement proper pagination
- Use conditional rendering appropriately
- Cache expensive queries
- Optimize template rendering

### ❌ DON'T

- Put business logic in templates
- Use unbounded loops in templates
- Execute database queries in templates
- Trust user input without sanitization
- Over-nest template inheritance
- Use very long template files
- Render sensitive data in templates
- Ignore template caching opportunities
- Use global variables excessively
- Mix multiple concerns in one template
