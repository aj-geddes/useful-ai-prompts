# Merge Strategy Script

## Merge Strategy Script

```bash
#!/bin/bash
# merge-with-strategy.sh

BRANCH=$1
STRATEGY=${2:-"squash"}

if [ -z "$BRANCH" ]; then
    echo "Usage: ./merge-with-strategy.sh <branch> [squash|rebase|merge]"
    exit 1
fi

# Update main
git checkout main
git pull origin main

case "$STRATEGY" in
    squash)
        git merge --squash origin/$BRANCH
        git commit -m "Merge $BRANCH"
        ;;
    rebase)
        git rebase origin/$BRANCH
        ;;
    merge)
        git merge --no-ff origin/$BRANCH
        ;;
    *)
        echo "Unknown strategy: $STRATEGY"
        exit 1
        ;;
esac

git push origin main
git push origin -d $BRANCH
```
