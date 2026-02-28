# Test Runner Hook

A PreToolUse hook that automatically runs tests before commits to ensure code quality and prevent breaking changes.

## Features

- Auto-detects test framework (Jest, pytest, RSpec, Go test, etc.)
- Runs relevant tests based on changed files
- Blocks commits if tests fail
- Shows detailed test results and failures
- Supports multiple test frameworks in monorepos
- Configurable test scope (all, changed, affected)
- Parallel test execution support
- Test caching for faster runs
- Customizable test patterns

## Configuration

Add this to your `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "pattern": "^Bash$",
        "command": "/absolute/path/to/hooks/test-runner/hook.sh",
        "description": "Run tests before git commits"
      }
    ]
  }
}
```

## Installation

### 1. Install Test Framework

Ensure your test framework is installed:

```bash
# JavaScript/TypeScript (Jest)
npm install --save-dev jest

# Python (pytest)
pip install pytest pytest-cov

# Ruby (RSpec)
gem install rspec

# Go (built-in)
# No installation needed

# Rust (built-in)
# No installation needed
```

### 2. Set Up the Hook

```bash
# Copy the hook to your project
cp hook.sh /path/to/your/project/.claude/hooks/test-runner.sh
chmod +x /path/to/your/project/.claude/hooks/test-runner.sh

# Update .claude/settings.json with the correct path
```

### 3. Configure Test Scope (Optional)

Create a `.testconfig` file in your project root:

```bash
# .testconfig - Test runner configuration

# Test scope: all, changed, affected
TEST_SCOPE=changed

# Run tests in parallel
PARALLEL_TESTS=true

# Maximum parallel jobs
MAX_PARALLEL=4

# Test timeout (seconds)
TEST_TIMEOUT=300

# Fail fast - stop on first failure
FAIL_FAST=false

# Show verbose output
VERBOSE=false

# Cache test results
CACHE_TESTS=true

# Minimum coverage threshold (percentage)
MIN_COVERAGE=80
```

## Usage

The hook automatically runs before git commits:

```
🧪 Test Runner Starting...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 Detected Test Framework: Jest
📝 Running tests for 5 changed file(s)

Running tests...
  ✓ utils.test.js (4 tests)
  ✓ api.test.js (8 tests)
  ✗ auth.test.js (3 tests, 1 failed)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ TEST FAILURES DETECTED

Test Suite: auth.test.js
  ● Authentication › should validate JWT token

    Expected: true
    Received: false

    at validateToken (src/auth.js:42:10)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Summary:
  Total: 15 tests
  Passed: 14 (93%)
  Failed: 1 (7%)
  Duration: 3.2s

⚠️  COMMIT BLOCKED - Fix failing tests before committing

Next steps:
  1. Review failing test output above
  2. Fix the failing test(s)
  3. Run tests manually: npm test
  4. Try committing again

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Supported Test Frameworks

### JavaScript/TypeScript

- Jest
- Mocha
- Vitest
- Jasmine
- Ava
- Tape

### Python

- pytest
- unittest
- nose2
- doctest

### Ruby

- RSpec
- Minitest
- Test::Unit

### Go

- go test

### Rust

- cargo test

### Java

- JUnit
- TestNG

### PHP

- PHPUnit
- Codeception

## Customization

### Test Scope

Configure which tests to run:

```bash
# In .testconfig or as environment variable

# Run all tests (slowest, most thorough)
TEST_SCOPE=all

# Run tests for changed files only (fast)
TEST_SCOPE=changed

# Run tests affected by changes (smart, recommended)
TEST_SCOPE=affected
```

### Framework-Specific Configuration

#### Jest

```json
// package.json
{
  "scripts": {
    "test": "jest",
    "test:changed": "jest --onlyChanged",
    "test:coverage": "jest --coverage"
  }
}
```

#### pytest

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short --strict-markers
```

#### RSpec

```ruby
# .rspec
--require spec_helper
--format documentation
--color
--fail-fast
```

### Coverage Requirements

Enforce minimum coverage:

```bash
# In .testconfig
MIN_COVERAGE=80

# Framework-specific

# Jest
npx jest --coverage --coverageThreshold='{"global":{"branches":80,"functions":80,"lines":80}}'

# pytest
pytest --cov=src --cov-fail-under=80

# Go
go test -cover -coverprofile=coverage.out
```

### Parallel Execution

Speed up tests with parallel execution:

```bash
# Jest
npm test -- --maxWorkers=4

# pytest
pytest -n 4  # requires pytest-xdist

# Go
go test -parallel 4

# RSpec
parallel_rspec spec/
```

### Selective Testing

Run specific test suites or patterns:

```bash
# In hook.sh, customize the test command

# Jest - specific pattern
npm test -- --testPathPattern=auth

# pytest - specific marker
pytest -m "not slow"

# RSpec - specific tag
rspec --tag ~slow

# Go - specific package
go test ./pkg/auth/...
```

## Best Practices

### 1. Keep Tests Fast

- Use test doubles (mocks, stubs, fakes)
- Avoid network calls in unit tests
- Use in-memory databases
- Run slow tests separately

```javascript
// Jest - separate fast and slow tests
// fast.test.js - runs on every commit
// slow.test.js - runs in CI only
```

### 2. Write Focused Tests

```javascript
// Good - focused, fast
test("validates email format", () => {
  expect(isValidEmail("user@example.com")).toBe(true);
});

// Bad - too broad, slow
test("complete user registration flow", () => {
  // Tests 10 different things...
});
```

### 3. Use Test-Driven Development

1. Write failing test
2. Write minimum code to pass
3. Refactor
4. Commit

### 4. Maintain Test Data

```javascript
// Use factories or fixtures
const user = createTestUser({ role: "admin" });

// Clean up after tests
afterEach(() => {
  cleanupTestDatabase();
});
```

### 5. Monitor Test Performance

```bash
# Jest - show slow tests
npm test -- --verbose

# pytest - show slowest tests
pytest --durations=10

# Track test times over time
# Alert on degradation
```

### 6. Skip Hook When Needed

For work-in-progress commits:

```bash
# Option 1: Disable hook temporarily
export SKIP_TEST_HOOK=1
git commit -m "WIP: implementing feature"

# Option 2: Run tests manually before final commit
npm test
git commit -m "Add feature with tests"
```

### 7. Test Coverage Goals

- Aim for 80%+ coverage
- 100% coverage for critical paths
- Focus on business logic
- Don't obsess over coverage numbers

### 8. Integration with CI/CD

Run comprehensive tests in CI:

```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Tests
        run: npm test -- --coverage
      - name: Upload Coverage
        uses: codecov/codecov-action@v2
```

## Troubleshooting

### Tests Pass Locally But Fail in Hook

Check:

- Environment variables are set
- Dependencies are installed
- Database is initialized
- Ports are available

### Hook Takes Too Long

Optimize:

- Enable test caching
- Use `TEST_SCOPE=changed`
- Run tests in parallel
- Mock external services

### False Failures

If tests are flaky:

- Fix non-deterministic tests
- Add proper teardown
- Increase timeouts for async operations
- Use retry mechanisms

### Hook Not Running

Verify:

- Script is executable: `chmod +x hook.sh`
- Path in settings.json is correct
- Pattern matches: "^Bash$"
- Git repository is initialized

## Advanced Features

### Smart Test Selection

Only run tests affected by code changes:

```bash
# Jest
npm test -- --onlyChanged

# pytest with pytest-testmon
pytest --testmon

# Custom logic
# Map changed files to test files
# Run only relevant tests
```

### Test Result Caching

Cache results for unchanged files:

```bash
# Jest (built-in)
npm test -- --cache

# pytest with pytest-cache
pytest --cache-clear  # Clear when needed
```

### Watch Mode Integration

For continuous testing during development:

```bash
# Jest watch mode
npm test -- --watch

# pytest watch
ptw  # pytest-watch

# Don't enable in hook - use separately
```

## Performance Metrics

Track test execution time:

```bash
# Enable in .testconfig
TRACK_PERFORMANCE=true

# Generates .test-metrics.json
{
  "date": "2025-01-08",
  "duration": 3.2,
  "tests": 15,
  "coverage": 87
}
```

## License

MIT License - Use freely in your projects
