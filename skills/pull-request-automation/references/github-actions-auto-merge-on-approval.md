# GitHub Actions: Auto Merge on Approval

## GitHub Actions: Auto Merge on Approval

```yaml
# .github/workflows/auto-merge.yml
name: Auto Merge PR

on:
  pull_request_review:
    types: [submitted]
  check_suite:
    types: [completed]

jobs:
  auto-merge:
    runs-on: ubuntu-latest
    if: github.event.review.state == 'approved'
    steps:
      - name: Check PR status
        uses: actions/github-script@v7
        with:
          script: |
            const pr = await github.rest.pulls.get({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number
            });

            // Check if all required checks passed
            const checkRuns = await github.rest.checks.listForRef({
              owner: context.repo.owner,
              repo: context.repo.repo,
              ref: pr.data.head.ref
            });

            const allPassed = checkRuns.data.check_runs.every(
              run => run.status === 'completed' && run.conclusion === 'success'
            );

            if (allPassed && pr.data.approved_reviews_count >= 2) {
              // Auto merge with squash strategy
              await github.rest.pulls.merge({
                owner: context.repo.owner,
                repo: context.repo.repo,
                pull_number: context.issue.number,
                merge_method: 'squash'
              });
            }
```
