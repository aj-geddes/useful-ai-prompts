---
name: graphql-implementation
description: >
  Design and implement GraphQL APIs with schema design, resolvers, queries,
  mutations, subscriptions, and best practices. Use when building GraphQL
  servers, designing schemas, or migrating from REST to GraphQL.
---

# GraphQL Implementation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement GraphQL APIs with proper schema design, resolver patterns, error handling, and performance optimization for flexible client-server communication.

## When to Use

- Designing new GraphQL APIs
- Creating GraphQL schemas and types
- Implementing resolvers and mutations
- Adding subscriptions for real-time data
- Migrating from REST to GraphQL
- Optimizing GraphQL performance

## Quick Start

Minimal working example:

```graphql
type User {
  id: ID!
  email: String!
  firstName: String!
  lastName: String!
  role: UserRole!
  posts: [Post!]!
  createdAt: DateTime!
  updatedAt: DateTime!
}

enum UserRole {
  ADMIN
  USER
  MODERATOR
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
  comments: [Comment!]!
  publishedAt: DateTime
  createdAt: DateTime!
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [GraphQL Schema Design](references/graphql-schema-design.md) | GraphQL Schema Design |
| [Node.js Apollo Server Implementation](references/nodejs-apollo-server-implementation.md) | Node.js Apollo Server Implementation |
| [Python GraphQL Implementation (Graphene)](references/python-graphql-implementation-graphene.md) | Python GraphQL Implementation (Graphene) |
| [Query Examples](references/query-examples.md) | Query Examples |
| [Error Handling](references/error-handling.md) | Error Handling |

## Best Practices

### ✅ DO

- Use clear, descriptive field names
- Design schemas around client needs
- Implement proper error handling
- Use input types for mutations
- Add subscriptions for real-time data
- Cache resolvers efficiently
- Validate input data
- Use federation for scalability

### ❌ DON'T

- Over-nest queries deeply
- Expose internal database IDs
- Return sensitive data without authorization
- Create overly complex schemas
- Forget to handle null values
- Ignore N+1 query problems
- Skip error messages
