---
name: api-pagination
description: >
  Implement efficient pagination strategies for large datasets using
  offset/limit, cursor-based, and keyset pagination. Use when returning
  collections, managing large result sets, or optimizing query performance.
---

# API Pagination

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement scalable pagination strategies for handling large datasets with efficient querying, navigation, and performance optimization.

## When to Use

- Returning large collections of resources
- Implementing search results pagination
- Building infinite scroll interfaces
- Optimizing large dataset queries
- Managing memory in client applications
- Improving API response times

## Quick Start

Minimal working example:

```javascript
// Node.js offset/limit implementation
app.get('/api/users', async (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = Math.min(parseInt(req.query.limit) || 20, 100); // Max 100
  const offset = (page - 1) * limit;

  try {
    const [users, total] = await Promise.all([
      User.find()
        .skip(offset)
        .limit(limit)
        .select('id email firstName lastName createdAt'),
      User.countDocuments()
    ]);

    const totalPages = Math.ceil(total / limit);

    res.json({
      data: users,
      pagination: {
        page,
        limit,
        total,
        totalPages,
        hasNext: page < totalPages,
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Offset/Limit Pagination](references/offsetlimit-pagination.md) | Offset/Limit Pagination |
| [Cursor-Based Pagination](references/cursor-based-pagination.md) | Cursor-Based Pagination |
| [Keyset Pagination](references/keyset-pagination.md) | Keyset Pagination |
| [Search Pagination](references/search-pagination.md) | Search Pagination |
| [Pagination Response Formats](references/pagination-response-formats.md) | Pagination Response Formats |
| [Python Pagination (SQLAlchemy)](references/python-pagination-sqlalchemy.md) | Python Pagination (SQLAlchemy) |

## Best Practices

### ✅ DO

- Use cursor pagination for large datasets
- Set reasonable maximum limits (e.g., 100)
- Include total count when feasible
- Provide navigation links
- Document pagination strategy
- Use indexed fields for sorting
- Cache pagination results when appropriate
- Handle edge cases (empty results)
- Implement consistent pagination formats
- Use keyset for extremely large datasets

### ❌ DON'T

- Use offset with billions of rows
- Allow unlimited page sizes
- Count rows for every request
- Paginate without sorting
- Change sort order mid-pagination
- Use deep pagination without cursor
- Skip pagination for large datasets
- Expose database pagination directly
- Mix pagination strategies
- Ignore performance implications
