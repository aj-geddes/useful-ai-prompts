---
name: jenkins-pipeline
description: >
  Build Jenkins declarative and scripted pipelines with stages, agents,
  parameters, and plugins. Implement multi-branch pipelines and deployment
  automation.
---

# Jenkins Pipeline

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Create enterprise-grade Jenkins pipelines using declarative and scripted approaches to automate building, testing, and deploying with advanced control flow.

## When to Use

- Enterprise CI/CD infrastructure
- Complex multi-stage builds
- On-premise deployment automation
- Parameterized builds

## Quick Start

Minimal working example:

```groovy
pipeline {
    agent { label 'linux-docker' }
    environment {
        REGISTRY = 'docker.io'
        IMAGE_NAME = 'myapp'
    }
    parameters {
        string(name: 'DEPLOY_ENV', defaultValue: 'staging')
    }
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Install') { steps { sh 'npm ci' } }
        stage('Lint') { steps { sh 'npm run lint' } }
        stage('Test') {
            steps {
                sh 'npm run test:coverage'
                junit 'test-results.xml'
            }
        }
        stage('Build') {
            steps {
                sh 'npm run build'
                archiveArtifacts artifacts: 'dist/**/*'
            }
        }
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Declarative Pipeline (Jenkinsfile)](references/declarative-pipeline-jenkinsfile.md) | Declarative Pipeline (Jenkinsfile) |
| [Scripted Pipeline](references/scripted-pipeline.md) | Scripted Pipeline (Groovy), Multi-Branch Pipeline, Parameterized Pipeline, Pipeline with Credentials |

## Best Practices

### ✅ DO

- Use declarative pipelines for clarity
- Use credentials plugin for secrets
- Archive artifacts and reports
- Implement approval gates for production
- Keep pipelines modular and reusable

### ❌ DON'T

- Store credentials in pipeline code
- Ignore pipeline errors
- Skip test coverage reporting
- Use deprecated plugins
