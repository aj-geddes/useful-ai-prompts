# Node.js Apollo Server Implementation

## Node.js Apollo Server Implementation

```javascript
const { ApolloServer, gql } = require("apollo-server-express");
const express = require("express");

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
    },
  },

  User: {
    posts: async (user, _, { db }) => {
      return db.posts.findByAuthorId(user.id);
    },
  },

  Post: {
    author: async (post, _, { db }) => {
      return db.users.findById(post.authorId);
    },
  },

  Mutation: {
    createUser: async (_, { email, firstName, lastName }, { db }) => {
      const user = { id: Date.now().toString(), email, firstName, lastName };
      db.users.save(user);
      return user;
    },
    createPost: async (_, { title, content }, { user, db }) => {
      if (!user) throw new Error("Unauthorized");
      const post = {
        id: Date.now().toString(),
        title,
        content,
        authorId: user.id,
      };
      db.posts.save(post);
      return post;
    },
  },
};

const server = new ApolloServer({
  typeDefs,
  resolvers,
  context: ({ req }) => ({
    user: req.user,
    db: require("./database"),
  }),
});

const app = express();
server.start().then(() => {
  server.applyMiddleware({ app });
  app.listen(4000, () => console.log("GraphQL server running on port 4000"));
});
```
