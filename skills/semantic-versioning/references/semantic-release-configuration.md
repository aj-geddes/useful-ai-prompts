# Semantic Release Configuration

## Semantic Release Configuration

```javascript
// release.config.js
module.exports = {
  branches: ["main", { name: "develop", prerelease: "beta" }],
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/changelog",
    "@semantic-release/git",
    "@semantic-release/github",
    "@semantic-release/npm",
  ],
};
```
