# GraphQL Code Generation

## GraphQL Code Generation

```typescript
// graphql-codegen.config.ts
import type { CodegenConfig } from "@graphql-codegen/cli";

const config: CodegenConfig = {
  schema: "http://localhost:4000/graphql",
  documents: ["src/**/*.tsx", "src/**/*.ts"],
  generates: {
    "./src/generated/graphql.ts": {
      plugins: [
        "typescript",
        "typescript-operations",
        "typescript-react-apollo",
      ],
      config: {
        withHooks: true,
        withComponent: false,
        withHOC: false,
      },
    },
    "./src/generated/introspection.json": {
      plugins: ["introspection"],
    },
  },
};

export default config;
```
