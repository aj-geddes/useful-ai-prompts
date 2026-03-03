# GitHub Actions: Auto Review Assignment

## GitHub Actions: Auto Review Assignment

```yaml
# .github/workflows/auto-assign.yml
name: Auto Assign PR

on:
  pull_request:
    types: [opened, reopened]

jobs:
  assign:
    runs-on: ubuntu-latest
    steps:
      - name: Assign reviewers
        uses: actions/github-script@v7
        with:
          script: |
            const pr = context.payload.pull_request;
            const reviewers = ['reviewer1', 'reviewer2', 'reviewer3'];

            // Select random reviewers
            const selected = reviewers.sort(() => 0.5 - Math.random()).slice(0, 2);

            await github.rest.pulls.requestReviewers({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: pr.number,
              reviewers: selected
            });

      - name: Add labels
        uses: actions/github-script@v7
        with:
          script: |
            const pr = context.payload.pull_request;
            const labels = [];

            if (pr.title.startsWith('feat:')) labels.push('feature');
            if (pr.title.startsWith('fix:')) labels.push('bugfix');
            if (pr.title.startsWith('docs:')) labels.push('documentation');

            if (labels.length > 0) {
              await github.rest.issues.addLabels({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: pr.number,
                labels: labels
              });
            }
```
