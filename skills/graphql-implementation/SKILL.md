---
name: graphql-implementation
description: Design and implement GraphQL APIs with schema design, resolvers, queries, mutations, subscriptions, and best practices. Use when building GraphQL servers, designing schemas, or migrating from REST to GraphQL.
---

# GraphQL Implementation

## Overview

Implement GraphQL APIs with proper schema design, resolver patterns, error handling, and performance optimization for flexible client-server communication.

## When to Use

- Designing new GraphQL APIs
- Creating GraphQL schemas and types
- Implementing resolvers and mutations
- Adding subscriptions for real-time data
- Migrating from REST to GraphQL
- Optimizing GraphQL performance

## Instructions

### 1. **GraphQL Schema Design**

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
}

type Comment {
  id: ID!
  text: String!
  author: User!
  post: Post!
  createdAt: DateTime!
}

type Query {
  user(id: ID!): User
  users(limit: Int, offset: Int): [User!]!
  post(id: ID!): Post
  posts(authorId: ID, limit: Int, offset: Int): [Post!]!
  search(query: String!): [SearchResult!]!
}

union SearchResult = User | Post | Comment

type Mutation {
  createUser(input: CreateUserInput!): User!
  updateUser(id: ID!, input: UpdateUserInput!): User!
  deleteUser(id: ID!): Boolean!
  createPost(input: CreatePostInput!): Post!
  updatePost(id: ID!, input: UpdatePostInput!): Post!
  deletePost(id: ID!): Boolean!
  createComment(postId: ID!, text: String!): Comment!
}

input CreateUserInput {
  email: String!
  firstName: String!
  lastName: String!
  role: UserRole!
}

input UpdateUserInput {
  email: String
  firstName: String
  lastName: String
  role: UserRole
}

input CreatePostInput {
  title: String!
  content: String!
}

input UpdatePostInput {
  title: String
  content: String
  publishedAt: DateTime
}

type Subscription {
  userCreated: User!
  postPublished: Post!
  commentAdded(postId: ID!): Comment!
}

scalar DateTime
```

### 2. **Node.js Apollo Server Implementation**

```javascript
const { ApolloServer, gql } = require('apollo-server-express');
const express = require('express');

const typeDefs = gql`
  type Query {
    user(id: ID!): User
    users: [User!]!
  }

  type User {
    id: ID!
    email: String!
    firstName: String!
    lastName: String!
    posts: [Post!]!
  }

  type Post {
    id: ID!
    title: String!
    content: String!
    author: User!
  }

  type Mutation {
    createUser(email: String!, firstName: String!, lastName: String!): User!
    createPost(title: String!, content: String!): Post!
  }
`;

const resolvers = {
  Query: {
    user: async (_, { id }, { db }) => {
      return db.users.findById(id);
    },
    users: async (_, __, { db }) => {
      return db.users.findAll();
    }
  },

  User: {
    posts: async (user, _, { db }) => {
      return db.posts.findByAuthorId(user.id);
    }
  },

  Post: {
    author: async (post, _, { db }) => {
      return db.users.findById(post.authorId);
    }
  },

  Mutation: {
    createUser: async (_, { email, firstName, lastName }, { db }) => {
      const user = { id: Date.now().toString(), email, firstName, lastName };
      db.users.save(user);
      return user;
    },
    createPost: async (_, { title, content }, { user, db }) => {
      if (!user) throw new Error('Unauthorized');
      const post = { id: Date.now().toString(), title, content, authorId: user.id };
      db.posts.save(post);
      return post;
    }
  }
};

const server = new ApolloServer({
  typeDefs,
  resolvers,
  context: ({ req }) => ({
    user: req.user,
    db: require('./database')
  })
});

const app = express();
server.start().then(() => {
  server.applyMiddleware({ app });
  app.listen(4000, () => console.log('GraphQL server running on port 4000'));
});
```

### 3. **Python GraphQL Implementation (Graphene)**

```python
import graphene
from datetime import datetime
from typing import List

class UserType(graphene.ObjectType):
    id = graphene.ID(required=True)
    email = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    posts = graphene.List(lambda: PostType)

class PostType(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    content = graphene.String(required=True)
    author = graphene.Field(UserType)
    created_at = graphene.DateTime(required=True)

class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.ID(required=True))
    users = graphene.List(UserType)
    posts = graphene.List(PostType, author_id=graphene.ID())

    def resolve_user(self, info, id):
        return User.objects.get(pk=id)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_posts(self, info, author_id=None):
        if author_id:
            return Post.objects.filter(author_id=author_id)
        return Post.objects.all()

class CreateUserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    user = graphene.Field(UserType)
    success = graphene.Boolean()

    def mutate(self, info, email, first_name, last_name):
        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        return CreateUserMutation(user=user, success=True)

class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
```

### 4. **Query Examples**

```graphql
# Get user with posts
query GetUserWithPosts {
  user(id: "123") {
    id
    email
    firstName
    posts {
      id
      title
      createdAt
    }
  }
}

# Paginated users query
query GetUsers($limit: Int, $offset: Int) {
  users(limit: $limit, offset: $offset) {
    id
    email
    firstName
  }
}

# Search across types
query Search($query: String!) {
  search(query: $query) {
    ... on User {
      id
      email
    }
    ... on Post {
      id
      title
    }
  }
}

# Create user mutation
mutation CreateUser($input: CreateUserInput!) {
  createUser(input: $input) {
    id
    email
    firstName
  }
}

# Subscribe to new comments
subscription OnCommentAdded($postId: ID!) {
  commentAdded(postId: $postId) {
    id
    text
    author {
      firstName
    }
  }
}
```

### 5. **Error Handling**

```javascript
const resolvers = {
  Query: {
    user: async (_, { id }) => {
      try {
        const user = await User.findById(id);
        if (!user) {
          throw new GraphQLError('User not found', {
            extensions: {
              code: 'NOT_FOUND',
              userId: id
            }
          });
        }
        return user;
      } catch (error) {
        throw new GraphQLError('Database error', {
          originalError: error,
          extensions: { code: 'INTERNAL_ERROR' }
        });
      }
    }
  }
};

server.formatError = (formattedError) => ({
  message: formattedError.message,
  code: formattedError.extensions?.code || 'INTERNAL_ERROR',
  timestamp: new Date().toISOString()
});
```

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

## Performance Tips

- Use DataLoader to batch database queries
- Implement query complexity analysis
- Cache at resolver level
- Use connection patterns for pagination
- Monitor query execution time
