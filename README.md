# Useful AI Prompts - The Complete AI Productivity Library

[![Run in Smithery](https://smithery.ai/badge/skills/aj-geddes)](https://smithery.ai/skills?ns=aj-geddes&utm_source=github&utm_medium=badge)


[![GitHub Stars](https://img.shields.io/github/stars/aj-geddes/useful-ai-prompts?style=social)](https://github.com/aj-geddes/useful-ai-prompts)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Prompts](https://img.shields.io/badge/Prompts-557+-green)](prompts/)
[![Skills](https://img.shields.io/badge/Skills-260+-orange)](skills/)
[![Hooks](https://img.shields.io/badge/Hooks-7-purple)](hooks/)

> **The largest open-source collection of production-ready AI prompts, Claude Code skills, and automation hooks for professionals.**

Transform ChatGPT, Claude, and other AI assistants into expert consultants with **820+ curated resources** spanning software development, business strategy, creative work, and emerging technologies.

## What's Inside

| Resource Type | Count | Description |
|--------------|-------|-------------|
| **[AI Prompts](prompts/)** | 557+ | Expert-crafted prompts across 47 categories |
| **[Claude Code Skills](skills/)** | 260+ | Auto-triggering capabilities with code examples |
| **[Automation Hooks](hooks/)** | 7 | Security, testing, formatting, and CI/CD automation |

**Total: 120,000+ lines** of production-ready guidance, code examples, and best practices.

---

## Quick Start

### Using Prompts

1. **Browse** the [prompts directory](prompts/) or [web interface](https://aj-geddes.github.io/useful-ai-prompts/)
2. **Copy** the prompt content
3. **Paste** into ChatGPT, Claude, or your preferred AI assistant
4. **Customize** the `{{variables}}` with your specific context

### Using Claude Code Skills

```bash
# Copy skills to your project
cp -r skills/ /path/to/your/project/.claude/skills/

# Skills auto-trigger based on your requests
# Example: "Help me refactor this legacy code"
# Claude Code automatically applies the refactor-legacy-code skill
```

### Using Automation Hooks

```bash
# Copy hooks to your Claude Code configuration
cp -r hooks/ ~/.claude/hooks/

# Hooks run automatically on events like:
# - Pre-commit: security scanning, linting
# - Session setup: environment configuration
# - Test runner: automated test execution
```

---

## Prompt Categories

### Business & Strategy

| Category | Prompts | Key Use Cases |
|----------|---------|---------------|
| [Business Analysis](prompts/business/) | 45+ | Requirements engineering, process improvement, stakeholder management |
| [Finance](prompts/finance/) | 30+ | Financial modeling, investment analysis, budgeting, forecasting |
| [Marketing](prompts/business/marketing/) | 25+ | Campaign strategy, content marketing, brand development |
| [Operations](prompts/operations/) | 35+ | Process optimization, supply chain, logistics |
| [Project Management](prompts/project-management/) | 40+ | Risk assessment, resource planning, agile methodologies |

### Technology & Engineering

| Category | Prompts | Key Use Cases |
|----------|---------|---------------|
| [Software Engineering](prompts/technical/) | 50+ | Architecture design, code review, full-stack development |
| [DevOps](prompts/technical/devops/) | 25+ | CI/CD pipelines, infrastructure as code, container orchestration |
| [Security](prompts/security/) | 20+ | Threat modeling, vulnerability assessment, incident response |
| [Data Science](prompts/technical/data-science/) | 30+ | ML model development, data analysis, visualization |

### Emerging Technologies (2025 Expansion)

| Category | Prompts | Key Use Cases |
|----------|---------|---------------|
| [Quantum Computing](prompts/quantum-computing/) | 14 | Algorithm development, circuit optimization, quantum ML |
| [Blockchain & Web3](prompts/blockchain/) | 15 | Smart contracts, DeFi protocols, tokenization |
| [Biotechnology](prompts/biotechnology/) | 15 | Drug discovery, bioinformatics, gene editing, clinical trials |
| [Space Economy](prompts/space-economy/) | 24 | Satellite operations, mission planning, commercial spaceflight |
| [Renewable Energy](prompts/renewable-energy/) | 19 | Solar development, energy storage, grid integration |
| [Healthcare Digital](prompts/healthcare-digital/) | 20 | Telehealth, AI diagnostics, patient engagement, EHR systems |
| [Government Digital](prompts/government/) | 8 | Digital transformation, smart cities, citizen services |
| [Supply Chain](prompts/supply-chain/) | 6 | Resilience planning, logistics optimization |

### Creative & Communication

| Category | Prompts | Key Use Cases |
|----------|---------|---------------|
| [Creative](prompts/creative/) | 25+ | Graphic design, UX research, content strategy |
| [Communication](prompts/communication/) | 30+ | Presentations, stakeholder management, technical writing |
| [Learning & Development](prompts/learning-development/) | 20+ | Curriculum design, training programs, skill assessment |

### Specialized Industries

| Category | Prompts | Key Use Cases |
|----------|---------|---------------|
| [Healthcare](prompts/healthcare/) | 15+ | Pharmaceutical R&D, clinical workflows |
| [Engineering](prompts/engineering/) | 10+ | Construction, mechanical design, project delivery |
| [Research](prompts/research/) | 20+ | Academic research, grant writing, literature review |
| [Customer Service](prompts/customer-service/) | 15+ | Support operations, experience optimization |

---

## Claude Code Skills (260+)

Skills are specialized capabilities that Claude Code invokes automatically based on your requests.

### How Skills Work

Unlike prompts, skills:
- **Auto-trigger** when Claude Code detects relevant keywords
- **Provide step-by-step guidance** with multi-language code examples
- **Include industry best practices** and production patterns
- **Range from 200-500+ lines** of detailed instructions

### Skills by Domain

| Domain | Skills | Examples |
|--------|--------|----------|
| **Software Development** | 35 | refactor-legacy-code, code-review-analysis, design-patterns |
| **DevOps & Infrastructure** | 20 | docker-containerization, kubernetes-deployment, terraform-iac |
| **Testing & QA** | 15 | unit-testing-framework, e2e-testing, test-automation |
| **Security** | 15 | vulnerability-scanning, oauth-implementation, data-encryption |
| **API & Integration** | 12 | rest-api-design, graphql-implementation, webhook-development |
| **Database** | 12 | sql-optimization, schema-design, database-indexing |
| **Cloud Platforms** | 15 | aws-lambda, serverless-architecture, cloud-cost-optimization |
| **Frontend** | 12 | react-components, responsive-design, css-architecture |
| **Backend** | 12 | nodejs-express, django-application, background-jobs |
| **Machine Learning** | 10 | ml-model-training, model-deployment, hyperparameter-tuning |
| **Documentation** | 15 | api-documentation, architecture-diagrams, runbook-creation |
| **Data Science** | 20 | exploratory-data-analysis, feature-engineering, ab-testing |
| **Mobile** | 8 | react-native, flutter-development, push-notifications |
| **Monitoring** | 8 | prometheus-monitoring, grafana-dashboards, distributed-tracing |
| **Version Control** | 10 | git-workflow-strategy, github-actions, semantic-versioning |
| **Project Management** | 10 | agile-sprint-planning, risk-assessment, release-planning |
| **Performance** | 8 | web-performance-audit, bundle-optimization, database-tuning |
| **Troubleshooting** | 12 | production-debugging, memory-leak-detection, root-cause-analysis |

See [SKILLS-MATRIX.md](SKILLS-MATRIX.md) for the complete reference with trigger keywords.

---

## Automation Hooks (7)

Hooks execute automatically in response to Claude Code events.

| Hook | Trigger | Purpose |
|------|---------|---------|
| [security-scan](hooks/security-scan/) | Pre-commit | Scan for vulnerabilities and secrets |
| [pre-commit-linting](hooks/pre-commit-linting/) | Pre-commit | Code formatting and style enforcement |
| [test-runner](hooks/test-runner/) | Pre-commit | Automated test execution |
| [dependency-check](hooks/dependency-check/) | Pre-commit | Audit dependencies for vulnerabilities |
| [breaking-change-detection](hooks/breaking-change-detection/) | Pre-commit | Detect API breaking changes |
| [auto-format](hooks/auto-format/) | Post-save | Automatic code formatting |
| [session-setup](hooks/session-setup/) | Session start | Environment initialization |

See [HOOKS-LIBRARY.md](HOOKS-LIBRARY.md) for installation and configuration.

---

## Prompt Architecture

Each prompt follows a consistent structure designed for maximum effectiveness:

```yaml
Metadata:
  - Category: Domain classification
  - Tags: Searchable keywords
  - Use Cases: Applicable scenarios

Structure:
  - Context Questions: Gather user requirements
  - Expert Guidance: Professional methodologies
  - Deliverables: Structured output sections
  - Examples: Real-world usage demonstrations
```

### Output Quality

- **Comprehensive**: 400-800+ lines of structured content
- **Actionable**: Step-by-step implementation guidance
- **Professional**: Industry-standard frameworks and methodologies
- **Customizable**: Variables for context-specific adaptation

---

## Integration

### For AI Agents and Assistants

See [AI-AGENT-GUIDE.md](AI-AGENT-GUIDE.md) for:
- Prompt selection algorithms
- Task classification systems
- API integration patterns
- Variable injection systems

### For Human Users

See [README-HUMANS.md](README-HUMANS.md) for:
- Getting started guide
- Category browsing
- Customization tips
- Real-world examples

### Programmatic Access

```python
# Load prompt index
import json
with open('PROMPT-INDEX.json') as f:
    prompts = json.load(f)

# Select prompt by category
technical_prompts = [p for p in prompts if p['category'] == 'technical']
```

---

## Web Interface

Browse prompts with search and filtering at:
**[https://aj-geddes.github.io/useful-ai-prompts/](https://aj-geddes.github.io/useful-ai-prompts/)**

Features:
- Category-based navigation
- Full-text search
- Responsive design
- Direct copy-to-clipboard

---

## Repository Structure

```
useful-ai-prompts/
├── prompts/           # 557+ AI prompts organized by category
│   ├── technical/     # Software, DevOps, security, data science
│   ├── business/      # Finance, marketing, operations, management
│   ├── creative/      # Design, UX, content strategy
│   ├── blockchain/    # Web3, DeFi, smart contracts
│   ├── quantum-computing/  # Quantum algorithms, circuits
│   └── ...            # 47 total categories
├── skills/            # 260+ Claude Code skills
├── hooks/             # 7 automation hooks
├── docs/              # Jekyll website (GitHub Pages)
├── metadata/          # Framework definitions and guidelines
├── PROMPT-INDEX.json  # Machine-readable prompt catalog
├── SKILLS-MATRIX.md   # Complete skills reference
└── HOOKS-LIBRARY.md   # Hooks documentation
```

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Adding new prompts
- Creating skills
- Building hooks
- Quality standards

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

## Links

- **Website**: [https://aj-geddes.github.io/useful-ai-prompts/](https://aj-geddes.github.io/useful-ai-prompts/)
- **GitHub**: [https://github.com/aj-geddes/useful-ai-prompts](https://github.com/aj-geddes/useful-ai-prompts)
- **Issues**: [Report bugs or request features](https://github.com/aj-geddes/useful-ai-prompts/issues)
- **Discussions**: [Community Q&A](https://github.com/aj-geddes/useful-ai-prompts/discussions)

---

**Keywords**: AI prompts, ChatGPT prompts, Claude prompts, prompt engineering, AI productivity, Claude Code skills, automation hooks, software development prompts, business strategy AI, prompt library, AI assistant, LLM prompts, professional AI tools, AI workflow automation
