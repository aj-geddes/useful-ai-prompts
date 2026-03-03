# Husky Installation and Configuration

## Husky Installation and Configuration

```bash
#!/bin/bash
# setup-husky.sh

# Install Husky
npm install husky --save-dev

# Initialize Husky
npx husky install

# Create pre-commit hook
npx husky add .husky/pre-commit "npm run lint"

# Create commit-msg hook
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"'

# Create pre-push hook
npx husky add .husky/pre-push "npm run test"

# Create post-merge hook
npx husky add .husky/post-merge "npm install"
```
