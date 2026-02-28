---
date: "2025-01-01"
description:
  A SessionStart hook that automatically initializes your development environment
  when starting a Claude Code session.
event_type: SessionStart
features:
  - .env file loading
  - Dependency checking
  - Database verification
  - Service status
  - Environment validation
icon: fa-rocket
icon_class: setup
layout: hook
lines_of_code: 580
matcher: ""
slug: session-setup
title: session-setup
---

A SessionStart hook that automatically initializes your development environment when starting a Claude Code session.

## Features

- Loads environment variables from .env files
- Checks for required dependencies
- Verifies runtime versions (Node.js, Python, Ruby, etc.)
- Sets up development database connections
- Displays project status and reminders
- Shows git branch and uncommitted changes
- Lists available npm/yarn scripts
- Provides custom welcome messages
- Validates configuration files
- Auto-starts development services (optional)

## Configuration

Add this to your `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "command": "/absolute/path/to/hooks/session-setup/hook.sh",
        "description": "Initialize development environment on session start"
      }
    ]
  }
}
```

## Installation

### 1. Copy the Hook

```bash
# Copy the hook to your project
cp hook.sh /path/to/your/project/.claude/hooks/session-setup.sh
chmod +x /path/to/your/project/.claude/hooks/session-setup.sh

# Update .claude/settings.json with the correct path
```

### 2. Configure Environment (Optional)

Create a `.session-config` file in your project root:

```bash
# .session-config - Session setup configuration

# Environment file to load
ENV_FILE=.env

# Check for required dependencies
CHECK_DEPENDENCIES=true

# Required commands (comma-separated)
REQUIRED_COMMANDS="node,npm,git"

# Minimum versions (optional)
MIN_NODE_VERSION=18.0.0
MIN_NPM_VERSION=9.0.0
MIN_PYTHON_VERSION=3.9.0

# Database connection check
CHECK_DATABASE=false
DATABASE_URL=${DATABASE_URL}

# Show git status
SHOW_GIT_STATUS=true

# Show available scripts
SHOW_SCRIPTS=true

# Auto-start services
AUTO_START_SERVICES=false
SERVICES="redis,postgresql"

# Custom welcome message
WELCOME_MESSAGE="Welcome to MyProject! Happy coding!"

# Display TODO reminders
SHOW_TODOS=true
TODO_FILE=TODO.md
```

### 3. Create .env File

Create a `.env` file for your environment variables:

```bash
# .env - Environment variables

# API Keys
API_KEY=your-api-key-here
SECRET_KEY=your-secret-key

# Database
DATABASE_URL=postgresql://localhost:5432/mydb
REDIS_URL=redis://localhost:6379

# Application
NODE_ENV=development
PORT=3000
LOG_LEVEL=debug
```

Ensure `.env` is in your `.gitignore`:

```bash
echo ".env" >> .gitignore
```

## Usage

The hook runs automatically when you start a Claude Code session:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 Session Setup - MyProject
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Environment Variables Loaded
   Loaded 8 variables from .env

✅ Dependencies Check
   ✓ node (v20.10.0)
   ✓ npm (v10.2.3)
   ✓ git (v2.39.0)

✅ Database Connection
   ✓ PostgreSQL connected (localhost:5432/mydb)
   ✓ Redis connected (localhost:6379)

📊 Git Status
   Branch: feature/new-feature
   Status: 3 files changed, 2 files staged
   Commits ahead: 2

📝 Available Scripts
   npm start         - Start development server
   npm test          - Run tests
   npm run build     - Build for production
   npm run lint      - Run linter

📌 TODO Reminders (3 items)
   - Implement user authentication
   - Add error handling to API
   - Update documentation

💡 Welcome to MyProject! Happy coding!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ Session initialized successfully!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Customization

### Custom Environment Files

Load different environment files based on context:

```bash
# In .session-config
ENV_FILE=.env.development  # Development
# ENV_FILE=.env.test       # Testing
# ENV_FILE=.env.production # Production
```

### Required Dependencies

Specify which commands must be available:

```bash
# In .session-config
REQUIRED_COMMANDS="node,npm,git,docker,kubectl"

# With version requirements
MIN_NODE_VERSION=18.0.0
MIN_DOCKER_VERSION=20.0.0
```

### Database Health Checks

Verify database connectivity:

```bash
# In .session-config
CHECK_DATABASE=true
DATABASE_URL=postgresql://localhost:5432/mydb

# Multiple databases
CHECK_POSTGRES=true
CHECK_REDIS=true
CHECK_MONGODB=true
```

### Custom Welcome Messages

Personalize the session welcome:

```bash
# In .session-config
WELCOME_MESSAGE="🎉 Welcome back, $(whoami)! Let's build something great!"

# Or use a file
WELCOME_FILE=.welcome.txt
```

### Auto-Start Services

Automatically start required services:

```bash
# In .session-config
AUTO_START_SERVICES=true
SERVICES="postgresql,redis,elasticsearch"

# Uses Docker Compose if available
# Or falls back to system services
```

### Custom Checks

Add custom initialization logic to `hook.sh`:

```bash
# Custom function in hook.sh
custom_checks() {
    # Check if ports are available
    if lsof -i :3000 > /dev/null 2>&1; then
        echo "⚠️  Port 3000 is already in use"
    fi

    # Verify configuration files
    if [[ ! -f "config/app.yml" ]]; then
        echo "⚠️  Missing config/app.yml"
    fi

    # Check disk space
    local available=$(df -h . | awk 'NR==2 {print $4}')
    echo "💾 Available disk space: $available"
}
```

## Best Practices

### 1. Keep .env Secure

Never commit .env files:

```bash
# .gitignore
.env
.env.*
!.env.example
```

Provide an example file:

```bash
# .env.example
API_KEY=your-api-key-here
DATABASE_URL=postgresql://localhost:5432/mydb
```

### 2. Document Requirements

Keep a README with environment setup:

```markdown
# Development Setup

## Prerequisites

- Node.js 18+
- PostgreSQL 14+
- Redis 7+

## Environment Variables

Copy `.env.example` to `.env` and fill in values.

## Database Setup

npm run db:setup
```

### 3. Graceful Degradation

Don't fail if optional checks don't pass:

```bash
# In hook.sh
if ! check_redis_connection; then
    echo "⚠️  Redis not available (optional)"
    # Continue anyway
fi
```

### 4. Quick Feedback

Show the most important information first:

```bash
# Priority order:
# 1. Critical errors (missing dependencies)
# 2. Environment status
# 3. Git status
# 4. Nice-to-have info (todos, tips)
```

### 5. Performance

Keep the hook fast:

```bash
# Parallelize checks where possible
check_node_version &
check_database_connection &
load_git_status &
wait

# Cache expensive operations
# Timeout long-running checks
```

### 6. Team Consistency

Share configuration across team:

```bash
# Commit .session-config to repository
git add .session-config
git commit -m "Add session setup configuration"

# Team members get same environment checks
```

### 7. Environment-Specific Setup

Use different configs per environment:

```bash
# Development
.session-config

# CI/CD
.session-config.ci

# In hook.sh, detect environment
if [[ -n "$CI" ]]; then
    source .session-config.ci
else
    source .session-config
fi
```

### 8. Health Monitoring

Track session initialization:

```bash
# Log session starts
echo "$(date): Session started by $(whoami)" >> .session.log

# Track failures
if ! initialize_environment; then
    echo "$(date): Initialization failed" >> .session.log
    notify_team
fi
```

## Advanced Features

### Multi-Environment Support

Automatically detect and load the right environment:

```bash
# In hook.sh
detect_environment() {
    if [[ -n "$CI" ]]; then
        echo "ci"
    elif [[ -f ".env.development" ]]; then
        echo "development"
    else
        echo "local"
    fi
}

ENV=$(detect_environment)
load_env_file ".env.$ENV"
```

### Service Dependencies

Check if required services are running:

```bash
check_services() {
    local services=("postgresql" "redis" "elasticsearch")

    for service in "${services[@]}"; do
        if systemctl is-active "$service" > /dev/null 2>&1; then
            echo "✓ $service is running"
        else
            echo "✗ $service is not running"
            echo "  Start with: systemctl start $service"
        fi
    done
}
```

### Git Workflow Reminders

Show relevant git information:

```bash
show_git_reminders() {
    # Check for uncommitted changes
    if ! git diff-index --quiet HEAD --; then
        echo "⚠️  You have uncommitted changes"
    fi

    # Check for unpushed commits
    local unpushed=$(git log origin/main..HEAD --oneline | wc -l)
    if [[ $unpushed -gt 0 ]]; then
        echo "⚠️  You have $unpushed unpushed commit(s)"
    fi

    # Check for pull request
    if command -v gh &>/dev/null; then
        local prs=$(gh pr list --author "@me" --json number --jq length)
        echo "📝 You have $prs open PR(s)"
    fi
}
```

### Dependency Updates

Check for outdated dependencies:

```bash
check_updates() {
    if [[ -f "package.json" ]]; then
        local outdated=$(npm outdated --json 2>/dev/null | jq 'length')
        if [[ $outdated -gt 0 ]]; then
            echo "📦 $outdated package(s) have updates available"
            echo "   Run: npm outdated"
        fi
    fi
}
```

### Project Metrics

Display project statistics:

```bash
show_metrics() {
    echo "📊 Project Metrics"

    # Line count
    local lines=$(find . -name "*.js" -o -name "*.ts" | xargs wc -l | tail -1)
    echo "   Lines of code: $lines"

    # File count
    local files=$(find . -type f | wc -l)
    echo "   Total files: $files"

    # Contributors
    local contributors=$(git log --format='%an' | sort -u | wc -l)
    echo "   Contributors: $contributors"
}
```

### Interactive Setup

Prompt for missing configuration:

```bash
interactive_setup() {
    if [[ ! -f ".env" ]]; then
        echo "No .env file found. Would you like to create one? (y/n)"
        read -r response
        if [[ "$response" == "y" ]]; then
            cp .env.example .env
            echo "Created .env from .env.example"
            echo "Please update .env with your values"
        fi
    fi
}
```

## Troubleshooting

### Hook Not Running

Check:

1. Hook is in SessionStart section of settings.json
2. Script is executable: `chmod +x hook.sh`
3. Path is absolute and correct
4. No syntax errors: `bash -n hook.sh`

### Environment Variables Not Loading

Verify:

1. .env file exists and has correct format
2. ENV_FILE path is correct in .session-config
3. No syntax errors in .env (no spaces around =)

### Slow Initialization

Optimize by:

1. Disabling optional checks
2. Caching results
3. Running checks in parallel
4. Setting timeouts

### Database Connection Fails

Check:

1. Database is running
2. DATABASE_URL is correct
3. Network connectivity
4. Credentials are valid

## Example Configurations

### Minimal Setup

```bash
# .session-config
ENV_FILE=.env
SHOW_GIT_STATUS=true
WELCOME_MESSAGE="Ready to code!"
```

### Full-Featured Setup

```bash
# .session-config
ENV_FILE=.env
CHECK_DEPENDENCIES=true
REQUIRED_COMMANDS="node,npm,git,docker"
MIN_NODE_VERSION=18.0.0
CHECK_DATABASE=true
DATABASE_URL=${DATABASE_URL}
SHOW_GIT_STATUS=true
SHOW_SCRIPTS=true
SHOW_TODOS=true
AUTO_START_SERVICES=false
WELCOME_MESSAGE="🚀 Let's build something awesome!"
```

### CI/CD Setup

```bash
# .session-config.ci
ENV_FILE=.env.ci
CHECK_DEPENDENCIES=true
REQUIRED_COMMANDS="node,npm,git"
CHECK_DATABASE=false
SHOW_GIT_STATUS=false
SHOW_SCRIPTS=false
AUTO_START_SERVICES=false
```

## License

MIT License - Use freely in your projects
