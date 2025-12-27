# Useful AI Prompts - Production-Ready AI Prompt Library

[![Run in Smithery](https://smithery.ai/badge/skills/aj-geddes)](https://smithery.ai/skills?ns=aj-geddes&utm_source=github&utm_medium=badge)
[![GitHub Stars](https://img.shields.io/github/stars/aj-geddes/useful-ai-prompts?style=social)](https://github.com/aj-geddes/useful-ai-prompts)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Prompts](https://img.shields.io/badge/Prompts-488+-green)](prompts/)
[![Skills](https://img.shields.io/badge/Skills-260+-orange)](skills/)
[![Hooks](https://img.shields.io/badge/Hooks-7-purple)](hooks/)

> **488 production-ready AI prompts, all following a standardized template with validated quality gates.**

Transform ChatGPT, Claude, and other AI assistants into expert consultants. Every prompt in this library passes 11 quality validation checks, ensuring consistent structure, clear deliverables, and measurable quality criteria.

---

## What's Inside

| Resource Type | Count | Description |
|--------------|-------|-------------|
| **[AI Prompts](prompts/)** | 488+ | Standardized expert prompts across 47 categories |
| **[Claude Code Skills](skills/)** | 260+ | Auto-triggering capabilities with code examples |
| **[Automation Hooks](hooks/)** | 7 | Security, testing, formatting, and CI/CD automation |

---

## Standardized Prompt Format

Every prompt follows the same validated structure:

```markdown
# [Prompt Name]

## Metadata
- **ID**: `category-prompt-slug`
- **Version**: 1.0.0
- **Category**: Primary category
- **Tags**: searchable, keywords, here
- **Complexity**: simple | intermediate | advanced
- **Interaction**: single-shot | conversational | iterative
- **Models**: Claude 3+, GPT-4+

## Overview
2-3 sentences explaining what the prompt does and who it's for.

## When to Use
- Specific scenario 1
- Specific scenario 2

**Don't use for**: Anti-patterns where this prompt isn't appropriate

---

## Prompt

<role>Expert identity with specific credentials and experience</role>

<context>Situation, success criteria, and key assumptions</context>

<input_handling>
Required: Must-have inputs
Optional: Inferred defaults when not provided
</input_handling>

<task>
Clear steps (3-7) for what to accomplish
</task>

<output_specification>
Format, length, and structure requirements
</output_specification>

<quality_criteria>
Measurable standards for excellent output
</quality_criteria>

<constraints>
Hard boundaries and limitations
</constraints>

---

## Example Usage

### Input
Realistic user request (20-200 words)

### Output
Representative response demonstrating quality (100-600 words)

## Related Prompts
Links to complementary prompts
```

---

## XML Tag Structure

The prompt section uses semantic XML tags for consistent parsing:

| Tag | Purpose | Content |
|-----|---------|---------|
| `<role>` | Expert identity | Specific credentials, experience, reasoning approach |
| `<context>` | Situation framing | When used, success criteria, key assumptions |
| `<input_handling>` | Input specification | Required vs optional inputs with defaults |
| `<task>` | Process steps | 3-7 numbered action steps |
| `<output_specification>` | Deliverable format | Format, length, structure, must-include elements |
| `<quality_criteria>` | Success measures | Objective standards and anti-patterns |
| `<constraints>` | Hard boundaries | Non-negotiable limits on scope/format |

---

## Quality Gates

Every prompt passes these 11 validation checks:

| Gate | Requirement |
|------|-------------|
| `metadata_complete` | All required fields present (ID, Version, Category, Tags, Complexity, Interaction, Models) |
| `overview_concise` | 3 sentences or fewer, no marketing fluff |
| `role_specific` | Concrete expertise defined, not "I'll help you" |
| `inputs_categorized` | Required vs optional distinguished with defaults |
| `task_structured` | 3-7 clear numbered steps |
| `outputs_specified` | Format + length + requirements for each deliverable |
| `criteria_measurable` | Objective quality standards, not vague aspirations |
| `example_realistic` | Input shows real usage (20-200 words) |
| `example_concise` | Output demonstrates pattern (100-600 words) |
| `no_duplication` | No repeated information across sections |
| `copy_paste_ready` | Prompt section is standalone and clearly delimited |

---

## Quick Start

### Using Prompts

1. **Browse** the [prompts directory](prompts/) or [web interface](https://aj-geddes.github.io/useful-ai-prompts/)
2. **Copy** the content within the `## Prompt` section (including XML tags)
3. **Paste** into ChatGPT, Claude, or your preferred AI assistant
4. **Provide** your specific input - the prompt handles the rest

### Example: Competitive Analysis

```text
<role>
You are a competitive intelligence strategist with 12+ years of experience
in market analysis, having led competitive strategy for both startups and
Fortune 500 companies.
</role>

<context>
Businesses need competitive intelligence to make informed strategic decisions.
Success means identifying specific opportunities that inform immediate action.
</context>

<input_handling>
Required: Industry, top competitors, current market position
Infer if not provided: Geographic scope, analysis timeline
</input_handling>

<task>
1. Map competitive landscape with positioning matrix
2. Profile key competitors (strengths, weaknesses, strategies)
3. Identify competitive gaps and white space opportunities
4. Create action recommendations with timelines
</task>

<output_specification>
- Format: Strategic analysis with visual frameworks
- Length: 500-800 words
- Must include: Positioning map, competitor profiles, action plan
</output_specification>
```

---

## Prompt Categories

### Business & Strategy

| Category | Prompts | Key Use Cases |
|----------|---------|---------------|
| [Business Analysis](prompts/business/) | 45+ | Requirements engineering, process improvement |
| [Finance](prompts/finance/) | 30+ | Financial modeling, investment analysis |
| [Marketing](prompts/business/marketing/) | 25+ | Campaign strategy, brand development |
| [Operations](prompts/operations/) | 35+ | Process optimization, supply chain |
| [Project Management](prompts/project-management/) | 40+ | Risk assessment, agile methodologies |

### Technology & Engineering

| Category | Prompts | Key Use Cases |
|----------|---------|---------------|
| [Software Engineering](prompts/technical/) | 50+ | Architecture design, code review |
| [DevOps](prompts/technical/devops/) | 25+ | CI/CD pipelines, infrastructure as code |
| [Security](prompts/security/) | 20+ | Threat modeling, incident response |
| [Data Science](prompts/technical/data-science/) | 30+ | ML development, data analysis |

### Emerging Technologies

| Category | Prompts | Key Use Cases |
|----------|---------|---------------|
| [Quantum Computing](prompts/quantum-computing/) | 14 | Algorithm development, circuit optimization |
| [Blockchain & Web3](prompts/blockchain/) | 15 | Smart contracts, DeFi protocols |
| [Biotechnology](prompts/biotechnology/) | 15 | Drug discovery, bioinformatics |
| [Space Economy](prompts/space-economy/) | 24 | Satellite operations, mission planning |
| [Renewable Energy](prompts/renewable-energy/) | 19 | Solar development, grid integration |
| [Healthcare Digital](prompts/healthcare-digital/) | 20 | Telehealth, AI diagnostics |

### Creative & Communication

| Category | Prompts | Key Use Cases |
|----------|---------|---------------|
| [Creative](prompts/creative/) | 25+ | Graphic design, UX research |
| [Communication](prompts/communication/) | 30+ | Presentations, technical writing |
| [Learning & Development](prompts/learning-development/) | 20+ | Curriculum design, training programs |

---

## Claude Code Skills (260+)

Skills auto-trigger when Claude Code detects relevant keywords:

| Domain | Skills | Examples |
|--------|--------|----------|
| **Software Development** | 35 | refactor-legacy-code, code-review-analysis |
| **DevOps & Infrastructure** | 20 | docker-containerization, kubernetes-deployment |
| **Testing & QA** | 15 | unit-testing-framework, e2e-testing |
| **Security** | 15 | vulnerability-scanning, oauth-implementation |
| **API & Integration** | 12 | rest-api-design, graphql-implementation |
| **Database** | 12 | sql-optimization, schema-design |

See [SKILLS-MATRIX.md](SKILLS-MATRIX.md) for the complete reference.

---

## Automation Hooks (7)

| Hook | Trigger | Purpose |
|------|---------|---------|
| [security-scan](hooks/security-scan/) | Pre-commit | Scan for vulnerabilities and secrets |
| [pre-commit-linting](hooks/pre-commit-linting/) | Pre-commit | Code formatting enforcement |
| [test-runner](hooks/test-runner/) | Pre-commit | Automated test execution |
| [dependency-check](hooks/dependency-check/) | Pre-commit | Dependency vulnerability audit |
| [auto-format](hooks/auto-format/) | Post-save | Automatic code formatting |
| [session-setup](hooks/session-setup/) | Session start | Environment initialization |

See [HOOKS-LIBRARY.md](HOOKS-LIBRARY.md) for installation and configuration.

---

## Repository Structure

```
useful-ai-prompts/
├── prompts/               # 488+ standardized prompts by category
│   ├── analysis/          # Competitive, data, financial analysis
│   ├── technical/         # Software, DevOps, security, data science
│   ├── business/          # Finance, marketing, operations
│   ├── blockchain/        # Web3, DeFi, smart contracts
│   ├── quantum-computing/ # Quantum algorithms, circuits
│   └── ...                # 47 total categories
├── skills/                # 260+ Claude Code skills
├── hooks/                 # 7 automation hooks
├── docs/                  # Jekyll website (GitHub Pages)
├── .claude/skills/        # Prompt refactoring skill
│   └── prompt-refactor/   # Template spec and validation
├── PROMPT-INDEX.json      # Machine-readable prompt catalog
├── SKILLS-MATRIX.md       # Complete skills reference
└── HOOKS-LIBRARY.md       # Hooks documentation
```

---

## Integration

### For AI Agents

```python
import json

# Load prompt index
with open('PROMPT-INDEX.json') as f:
    prompts = json.load(f)

# Select by category
analysis_prompts = [p for p in prompts if p['category'] == 'analysis']
```

See [AI-AGENT-GUIDE.md](AI-AGENT-GUIDE.md) for task classification and API integration patterns.

### For Human Users

See [README-HUMANS.md](README-HUMANS.md) for getting started, customization tips, and real-world examples.

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

## Contributing

We welcome contributions! All new prompts must:

1. Follow the standardized template structure
2. Pass all 11 quality gates
3. Include realistic example usage

Use the prompt-refactor skill for validation:
```bash
./.claude/skills/prompt-refactor/scripts/validate-prompt.sh ./prompts/my-prompt.md
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for complete guidelines.

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

**Keywords**: AI prompts, ChatGPT prompts, Claude prompts, prompt engineering, standardized prompts, AI productivity, Claude Code skills, prompt library, LLM prompts, professional AI tools
