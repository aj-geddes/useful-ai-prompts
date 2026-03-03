# Performance Optimization

## Performance Optimization

### Reduce Bundle Size

```bash
# Analyze bundle size
npm install -g bundle-buddy
npm install --save-dev webpack-bundle-analyzer

# Use production build
npm install --production

# Prune unused dependencies
npm prune

# Find duplicate packages
npm dedupe
npx yarn-deduplicate  # For yarn
```

### package.json Optimization

```json
{
  "dependencies": {
    // ❌ Don't install entire lodash
    "lodash": "^4.17.21",

    // ✅ Install only what you need
    "lodash.debounce": "^4.0.8",
    "lodash.throttle": "^4.1.1"
  }
}
```
