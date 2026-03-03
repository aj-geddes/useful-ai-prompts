# Pre-commit Hook (Node.js)

## Pre-commit Hook (Node.js)

```bash
#!/usr/bin/env node
# .husky/pre-commit

const { execSync } = require('child_process');
const fs = require('fs');

console.log('🔍 Running pre-commit checks...\n');

try {
  // Get staged files
  const stagedFiles = execSync('git diff --cached --name-only', { encoding: 'utf-8' })
    .split('\n')
    .filter(file => file && (file.endsWith('.js') || file.endsWith('.ts')))
    .join(' ');

  if (!stagedFiles) {
    console.log('✅ No JavaScript/TypeScript files to check');
    process.exit(0);
  }

  // Run linter on staged files
  console.log('📝 Running ESLint...');
  execSync(`npx eslint ${stagedFiles} --fix`, { stdio: 'inherit' });

  // Run Prettier
  console.log('✨ Running Prettier...');
  execSync(`npx prettier --write ${stagedFiles}`, { stdio: 'inherit' });

  // Stage the fixed files
  console.log('📦 Staging fixed files...');
  execSync(`git add ${stagedFiles}`);

  console.log('\n✅ Pre-commit checks passed!');
} catch (error) {
  console.error('❌ Pre-commit checks failed!');
  process.exit(1);
}
```
