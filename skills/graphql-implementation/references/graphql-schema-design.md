# GraphQL Schema Design

## GraphQL Schema Design

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
