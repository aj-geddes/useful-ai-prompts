# GraphQL Versioning

## GraphQL Versioning

```typescript
// GraphQL handles versioning differently - through schema evolution
// schema-v1.graphql
type User {
  id: ID!
  name: String!
  username: String!
}

// schema-v2.graphql (deprecated fields)
type User {
  id: ID!
  name: String!
  username: String! @deprecated(reason: "Use email instead")
  email: String!
  profile: Profile
}

type Profile {
  avatar: String
  bio: String
}

// Field deprecation in resolver
const resolvers = {
  User: {
    username: (user) => {
      console.warn('username field is deprecated, use email instead');
      return user.email;
    }
  }
};
````
