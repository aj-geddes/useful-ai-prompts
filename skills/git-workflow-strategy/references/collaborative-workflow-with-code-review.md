# Collaborative Workflow with Code Review

## Collaborative Workflow with Code Review

```bash
# Developer creates feature
git checkout -b feature/search-optimization
# Make changes
git add .
git commit -m "perf: optimize search algorithm"
git push origin feature/search-optimization

# Create pull request with detailed description
# Reviewer reviews and suggests changes

# Developer makes requested changes
git add .
git commit -m "refactor: improve search efficiency per review"
git push origin feature/search-optimization

# After approval
git checkout main
git pull origin main
git merge feature/search-optimization
git push origin main

# Cleanup
git branch -d feature/search-optimization
git push origin -d feature/search-optimization
```
