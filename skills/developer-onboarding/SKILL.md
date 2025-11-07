---
name: developer-onboarding
description: Create comprehensive developer onboarding documentation including setup guides, README files, contributing guidelines, and getting started tutorials. Use when onboarding new developers or creating setup documentation.
---

# Developer Onboarding

## Overview

Create comprehensive onboarding documentation that helps new developers quickly set up their development environment, understand the codebase, and start contributing effectively.

## When to Use

- New developer onboarding
- README file creation
- Contributing guidelines
- Development environment setup
- Architecture overview docs
- Code style guides
- Git workflow documentation
- Testing guidelines
- Deployment procedures

## Comprehensive README Template

```markdown
# Project Name

Brief project description (1-2 sentences explaining what this project does).

[![Build Status](https://img.shields.io/github/workflow/status/username/repo/CI)](https://github.com/username/repo/actions)
[![Coverage](https://img.shields.io/codecov/c/github/username/repo)](https://codecov.io/gh/username/repo)
[![License](https://img.shields.io/github/license/username/repo)](LICENSE)
[![Version](https://img.shields.io/npm/v/package-name)](https://www.npmjs.com/package/package-name)

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)

## Features

- ✨ Feature 1: Brief description
- 🚀 Feature 2: Brief description
- 🔒 Feature 3: Brief description
- 📊 Feature 4: Brief description

## Quick Start

Get up and running in less than 5 minutes:

```bash
# Clone the repository
git clone https://github.com/username/repo.git
cd repo

# Install dependencies
npm install

# Set up environment
cp .env.example .env

# Run database migrations
npm run db:migrate

# Start development server
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000) to see the app.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** 18.x or higher ([Download](https://nodejs.org/))
- **npm** 9.x or higher (comes with Node.js)
- **PostgreSQL** 14.x or higher ([Download](https://www.postgresql.org/download/))
- **Redis** 7.x or higher ([Download](https://redis.io/download))
- **Docker** (optional, for containerized development)

**Recommended Tools:**
- [VS Code](https://code.visualstudio.com/) with recommended extensions
- [Postman](https://www.postman.com/) for API testing
- [pgAdmin](https://www.pgadmin.org/) for database management

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/username/repo.git
cd repo
```

### 2. Install Dependencies

```bash
# Install all dependencies
npm install

# Or use yarn
yarn install

# Or use pnpm
pnpm install
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and configure the following:

```env
# Application
NODE_ENV=development
PORT=3000
BASE_URL=http://localhost:3000

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Redis
REDIS_URL=redis://localhost:6379

# Authentication
JWT_SECRET=your-secret-key-here
JWT_EXPIRES_IN=7d

# External APIs
STRIPE_SECRET_KEY=sk_test_...
SENDGRID_API_KEY=SG...

# AWS (if applicable)
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
S3_BUCKET_NAME=your-bucket
```

### 4. Database Setup

```bash
# Create database
createdb your_database_name

# Run migrations
npm run db:migrate

# Seed database with sample data (optional)
npm run db:seed
```

### 5. Verify Installation

```bash
# Run tests to verify setup
npm test

# Start development server
npm run dev
```

If everything is set up correctly, you should see:
```
✓ Server running on http://localhost:3000
✓ Database connected
✓ Redis connected
```

## Configuration

### Database Configuration

Edit `config/database.js`:

```javascript
module.exports = {
  development: {
    url: process.env.DATABASE_URL,
    dialect: 'postgres',
    logging: console.log,
  },
  test: {
    url: process.env.TEST_DATABASE_URL,
    dialect: 'postgres',
    logging: false,
  },
  production: {
    url: process.env.DATABASE_URL,
    dialect: 'postgres',
    logging: false,
    pool: {
      max: 20,
      min: 5,
      acquire: 30000,
      idle: 10000,
    },
  },
};
```

### Application Configuration

Main config file: `config/app.js`

```javascript
module.exports = {
  port: process.env.PORT || 3000,
  env: process.env.NODE_ENV || 'development',
  apiVersion: 'v1',
  rateLimit: {
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // limit each IP to 100 requests per windowMs
  },
  cors: {
    origin: process.env.CORS_ORIGIN || '*',
    credentials: true,
  },
};
```

## Development

### Project Structure

```
.
├── src/
│   ├── api/              # API routes
│   │   ├── controllers/  # Route controllers
│   │   ├── middlewares/  # Express middlewares
│   │   └── routes/       # Route definitions
│   ├── config/           # Configuration files
│   ├── models/           # Database models
│   ├── services/         # Business logic
│   ├── utils/            # Utility functions
│   └── app.js            # Express app setup
├── tests/
│   ├── unit/             # Unit tests
│   ├── integration/      # Integration tests
│   └── e2e/              # End-to-end tests
├── scripts/              # Utility scripts
├── docs/                 # Documentation
├── .env.example          # Environment template
├── .eslintrc.js          # ESLint config
├── .prettierrc           # Prettier config
├── package.json
└── README.md
```

### Available Scripts

```bash
# Development
npm run dev              # Start dev server with hot reload
npm run dev:debug        # Start with debugger attached

# Building
npm run build            # Build for production
npm run build:watch      # Build and watch for changes

# Testing
npm test                 # Run all tests
npm run test:unit        # Run unit tests only
npm run test:integration # Run integration tests
npm run test:e2e         # Run e2e tests
npm run test:watch       # Run tests in watch mode
npm run test:coverage    # Generate coverage report

# Linting & Formatting
npm run lint             # Run ESLint
npm run lint:fix         # Fix ESLint errors
npm run format           # Format code with Prettier
npm run format:check     # Check formatting

# Database
npm run db:migrate       # Run migrations
npm run db:migrate:undo  # Undo last migration
npm run db:seed          # Seed database
npm run db:reset         # Reset database (drop, create, migrate, seed)

# Other
npm run clean            # Clean build artifacts
npm start                # Start production server
```

### Code Style

We use ESLint and Prettier for consistent code style:

**ESLint Config:**
```javascript
// .eslintrc.js
module.exports = {
  extends: ['airbnb-base', 'prettier'],
  plugins: ['prettier'],
  rules: {
    'prettier/prettier': 'error',
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
  },
};
```

**Prettier Config:**
```json
{
  "semi": true,
  "singleQuote": true,
  "trailingComma": "es5",
  "printWidth": 100,
  "tabWidth": 2
}
```

### Git Workflow

We follow the [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/) branching model:

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and commit
git add .
git commit -m "feat: add new feature"

# Push to remote
git push origin feature/your-feature-name

# Create pull request on GitHub
```

**Branch Naming Convention:**
- `feature/` - New features
- `bugfix/` - Bug fixes
- `hotfix/` - Urgent production fixes
- `refactor/` - Code refactoring
- `docs/` - Documentation updates

**Commit Message Convention:**

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): subject

body

footer
```

**Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

**Examples:**
```bash
feat(auth): add OAuth2 authentication
fix(api): resolve race condition in order processing
docs(readme): update installation instructions
```

## Testing

### Running Tests

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test file
npm test -- tests/unit/user.test.js

# Run tests matching pattern
npm test -- --grep "User API"
```

### Writing Tests

**Unit Test Example:**

```javascript
// tests/unit/user.service.test.js
const { expect } = require('chai');
const UserService = require('../../src/services/user.service');

describe('UserService', () => {
  describe('createUser', () => {
    it('should create a new user', async () => {
      const userData = {
        email: 'test@example.com',
        password: 'password123',
        name: 'Test User',
      };

      const user = await UserService.createUser(userData);

      expect(user).to.have.property('id');
      expect(user.email).to.equal(userData.email);
      expect(user.password).to.not.equal(userData.password); // Should be hashed
    });

    it('should throw error for duplicate email', async () => {
      const userData = { email: 'existing@example.com' };

      await expect(UserService.createUser(userData)).to.be.rejectedWith(
        'Email already exists'
      );
    });
  });
});
```

**Integration Test Example:**

```javascript
// tests/integration/auth.test.js
const request = require('supertest');
const app = require('../../src/app');

describe('Auth API', () => {
  describe('POST /api/auth/register', () => {
    it('should register a new user', async () => {
      const response = await request(app)
        .post('/api/auth/register')
        .send({
          email: 'newuser@example.com',
          password: 'password123',
          name: 'New User',
        })
        .expect(201);

      expect(response.body).to.have.property('token');
      expect(response.body.user).to.have.property('id');
    });
  });
});
```

## Deployment

### Production Build

```bash
# Build for production
npm run build

# Start production server
NODE_ENV=production npm start
```

### Docker Deployment

```dockerfile
# Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

```bash
# Build Docker image
docker build -t myapp:latest .

# Run container
docker run -p 3000:3000 --env-file .env myapp:latest
```

### Environment Variables

Ensure these are set in production:

```env
NODE_ENV=production
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
JWT_SECRET=strong-random-secret
# ... other production configs
```

## Architecture

### High-Level Overview

```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ API Gateway │
└──────┬──────┘
       │
       ▼
┌─────────────┐     ┌──────────┐
│  Services   │────▶│ Database │
└──────┬──────┘     └──────────┘
       │
       ▼
┌─────────────┐
│    Cache    │
└─────────────┘
```

### Key Components

- **API Layer**: Express.js REST API
- **Service Layer**: Business logic
- **Data Layer**: PostgreSQL + Redis
- **Authentication**: JWT-based auth
- **Caching**: Redis for session and data caching

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Quick Contribution Guide

1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Write/update tests
5. Ensure all tests pass
6. Submit a pull request

### Code Review Process

1. All PRs require at least one approval
2. CI must pass (tests, linting)
3. Code coverage must not decrease
4. Documentation must be updated

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [https://docs.example.com](https://docs.example.com)
- **Issues**: [GitHub Issues](https://github.com/username/repo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/username/repo/discussions)
- **Slack**: [Join our Slack](https://slack.example.com)

## Acknowledgments

- List contributors
- Credit third-party libraries
- Thank sponsors
```

## Best Practices

### ✅ DO
- Start with a clear, concise project description
- Include badges for build status, coverage, etc.
- Provide a quick start section
- Document all prerequisites clearly
- Include troubleshooting section
- Keep README up-to-date
- Use code examples liberally
- Add architecture diagrams
- Document environment variables
- Include contribution guidelines
- Specify code style requirements
- Document testing procedures

### ❌ DON'T
- Assume prior knowledge
- Skip prerequisite documentation
- Forget to update after major changes
- Use overly technical jargon
- Skip example code
- Ignore Windows/Mac/Linux differences
- Forget to document scripts

## Resources

- [Make a README](https://www.makeareadme.com/)
- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [Standard README](https://github.com/RichardLitt/standard-readme)
- [README Template](https://github.com/othneildrew/Best-README-Template)
