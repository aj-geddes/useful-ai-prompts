---
name: developer-onboarding
description: >
  Create comprehensive developer onboarding documentation including setup
  guides, README files, contributing guidelines, and getting started tutorials.
  Use when onboarding new developers or creating setup documentation.
---

# Developer Onboarding

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

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

## Quick Start

Minimal working example:

````markdown
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

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Clone the Repository](references/clone-the-repository.md) | Clone the Repository, Install Dependencies |
| [Set Up Environment Variables](references/set-up-environment-variables.md) | Set Up Environment Variables |
| [Database Setup](references/database-setup.md) | Database Setup, Verify Installation |
| [Project Structure](references/project-structure.md) | Project Structure |
| [Available Scripts](references/available-scripts.md) | Available Scripts |
| [Code Style](references/code-style.md) | Code Style |
| [Git Workflow](references/git-workflow.md) | Git Workflow |
| [Running Tests](references/running-tests.md) | Running Tests |
| [Writing Tests](references/writing-tests.md) | Writing Tests |

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
