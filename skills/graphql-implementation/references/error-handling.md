# Error Handling

## Error Handling

```javascript
const resolvers = {
  Query: {
    user: async (_, { id }) => {
      try {
        const user = await User.findById(id);
        if (!user) {
          throw new GraphQLError("User not found", {
            extensions: {
              code: "NOT_FOUND",
              userId: id,
            },
          });
        }
        return user;
      } catch (error) {
        throw new GraphQLError("Database error", {
          originalError: error,
          extensions: { code: "INTERNAL_ERROR" },
        });
      }
    },
  },
};

server.formatError = (formattedError) => ({
  message: formattedError.message,
  code: formattedError.extensions?.code || "INTERNAL_ERROR",
  timestamp: new Date().toISOString(),
});
```
