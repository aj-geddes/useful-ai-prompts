# Automated Release Workflow

## Automated Release Workflow

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - "v*"

jobs:
  create-release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Generate changelog
        id: changelog
        uses: mikepenz/action-github-changelog-generator@v3
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Create Release
        uses: ncipollo/release-action@v1
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          tag: ${{ github.ref }}
          body: ${{ steps.changelog.outputs.changelog }}
          draft: false

      - name: Publish to npm
        uses: JS-DevTools/npm-publish@v1
        with:
          token: ${{ secrets.NPM_TOKEN }}
```
