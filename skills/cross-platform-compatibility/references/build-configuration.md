# Build Configuration

## Build Configuration

```typescript
// rollup.config.js
export default {
  input: "src/index.ts",
  output: [
    {
      file: "dist/index.js",
      format: "cjs",
    },
    {
      file: "dist/index.esm.js",
      format: "esm",
    },
  ],
  external: [
    // Mark platform-specific modules as external
    "fsevents",
  ],
  plugins: [
    // Replace platform checks at build time for better tree-shaking
    replace({
      "process.platform": JSON.stringify(process.platform),
      preventAssignment: true,
    }),
  ],
};
```
