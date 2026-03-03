# PR Title Validation Workflow

## PR Title Validation Workflow

```yaml
# .github/workflows/validate-pr-title.yml
name: Validate PR Title

on:
  pull_request:
    types: [opened, reopened, edited]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Validate PR title format
        uses: actions/github-script@v7
        with:
          script: |
            const pr = context.payload.pull_request;
            const title = pr.title;

            // Pattern: type: description
            const pattern = /^(feat|fix|docs|style|refactor|test|chore|perf)(\(.+\))?: .{1,80}$/;

            if (!pattern.test(title)) {
              core.setFailed(
                'PR title must follow: type: description\n' +
                'Types: feat, fix, docs, style, refactor, test, chore, perf'
              );
            }
```
