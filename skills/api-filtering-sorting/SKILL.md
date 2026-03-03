---
name: api-filtering-sorting
description: >
  Implement advanced filtering and sorting capabilities for APIs with query
  parsing, field validation, and optimization. Use when building search
  features, complex queries, or flexible data retrieval endpoints.
---

# API Filtering & Sorting

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build flexible filtering and sorting systems that handle complex queries efficiently with proper validation, security, and performance optimization.

## When to Use

- Building search and filter interfaces
- Implementing advanced query capabilities
- Creating flexible data retrieval endpoints
- Optimizing query performance
- Validating user input for queries
- Supporting complex filtering logic

## Quick Start

Minimal working example:

```javascript
// Node.js filtering implementation
app.get("/api/products", async (req, res) => {
  const filters = {};
  const sortOptions = {};

  // Parse filtering parameters
  const allowedFilters = [
    "category",
    "minPrice",
    "maxPrice",
    "inStock",
    "rating",
  ];
  for (const key of allowedFilters) {
    if (req.query[key]) {
      filters[key] = req.query[key];
    }
  }

  // Build MongoDB query
  const mongoQuery = {};

  if (filters.category) {
    mongoQuery.category = filters.category;
  }
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Query Parameter Filtering](references/query-parameter-filtering.md) | Query Parameter Filtering |
| [Advanced Filter Parser](references/advanced-filter-parser.md) | Advanced Filter Parser |
| [Filter Builder Pattern](references/filter-builder-pattern.md) | Filter Builder Pattern |
| [Python Filtering (SQLAlchemy)](references/python-filtering-sqlalchemy.md) | Python Filtering (SQLAlchemy) |
| [Elasticsearch Filtering](references/elasticsearch-filtering.md) | Elasticsearch Filtering |
| [Query Validation](references/query-validation.md) | Query Validation |

## Best Practices

### ✅ DO

- Whitelist allowed filter fields
- Validate all input parameters
- Index fields used for filtering
- Support common operators
- Provide faceted navigation
- Cache filter options
- Limit filter complexity
- Document filter syntax
- Use database-native operators
- Optimize queries with indexes

### ❌ DON'T

- Allow arbitrary field filtering
- Support unlimited operators
- Ignore SQL injection risks
- Create complex filter logic
- Expose internal field names
- Filter on unindexed fields
- Allow deeply nested filters
- Skip input validation
- Combine all filters with OR
- Ignore performance impact
