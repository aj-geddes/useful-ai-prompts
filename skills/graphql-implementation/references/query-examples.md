# Query Examples

## Query Examples

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
