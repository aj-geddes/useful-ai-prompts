# Peer Dependencies

## Peer Dependencies

```json
// library package.json
{
  "name": "my-react-library",
  "peerDependencies": {
    "react": ">=16.8.0",
    "react-dom": ">=16.8.0"
  },
  "peerDependenciesMeta": {
    "react-dom": {
      "optional": true // Makes peer dependency optional
    }
  }
}
```

**When to Use Peer Dependencies:**

- Plugin architecture (webpack plugins, babel plugins)
- React/Vue component libraries
- Framework extensions
- Prevents multiple versions of same package
