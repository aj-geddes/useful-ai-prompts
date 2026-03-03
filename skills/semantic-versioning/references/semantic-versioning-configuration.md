# Semantic Versioning Configuration

## Semantic Versioning Configuration

```yaml
# package.json
{
  "name": "my-awesome-package",
  "version": "1.2.3",
  "description": "An awesome package",
  "main": "dist/index.js",
  "repository": { "type": "git", "url": "https://github.com/org/repo.git" },
  "scripts": { "release": "semantic-release" },
  "devDependencies":
    {
      "semantic-release": "^21.0.0",
      "@semantic-release/changelog": "^6.0.0",
      "@semantic-release/git": "^10.0.0",
      "@semantic-release/github": "^9.0.0",
      "conventional-changelog-cli": "^3.0.0",
    },
}
```
