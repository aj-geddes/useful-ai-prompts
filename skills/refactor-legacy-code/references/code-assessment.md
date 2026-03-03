# Code Assessment

## Code Assessment

First, analyze the legacy code to understand:

```bash
# Review the codebase structure
tree -L 3 -I 'node_modules|dist|build'

# Check for outdated dependencies
npm outdated  # or pip list --outdated, composer outdated, etc.

# Identify code complexity hotspots
# Use tools like:
# - SonarQube for code smells
# - eslint for JavaScript
# - pylint for Python
# - RuboCop for Ruby
```

**Assessment Checklist:**

- [ ] Identify deprecated patterns and APIs
- [ ] Locate tightly coupled components
- [ ] Find duplicated code blocks
- [ ] Review test coverage gaps
- [ ] Document current behavior and edge cases
- [ ] Identify performance bottlenecks
