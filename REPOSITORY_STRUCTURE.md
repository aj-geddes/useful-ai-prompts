# Repository Structure

This document outlines the organization of the Useful AI Prompts repository.

## Directory Structure

```
useful-ai-prompts/
├── CLAUDE.md              # AI assistant instructions and standards
├── CONTRIBUTING.md        # Contribution guidelines
├── LICENSE               # Repository license
├── README.md             # Main repository documentation
├── REPOSITORY_STRUCTURE.md # This file
├── worklog.md            # Development history and decisions
│
├── metadata/             # Prompt framework metadata and guidelines
│   ├── job-categories.md      # Job role categorization
│   ├── persona-profiles.md    # Persona development guidelines
│   ├── product-strategy.md    # Product development strategy
│   ├── thinking-approaches.md # Analytical frameworks reference
│   └── workflow-categories.md # Workflow categorization
│
└── prompts/              # Main prompt library
    ├── academic/         # Academic and research prompts
    │   └── research/
    │       └── research-excellence-scientist.md
    │
    ├── administrative/   # Executive and administrative support
    │   └── executive-excellence-partner.md
    │
    ├── business/         # Business operations prompts
    │   ├── administrative/     # Admin workflows
    │   ├── business-analysis/  # Business analysis
    │   ├── customer-success/   # Customer retention
    │   ├── finance/           # Financial modeling
    │   ├── human-resources/   # HR and talent
    │   ├── legal/            # Legal and compliance
    │   ├── management/       # Management excellence
    │   ├── marketing/        # Marketing strategy
    │   ├── operations/       # Operations optimization
    │   ├── product-management/ # Product strategy
    │   ├── project-management/ # Project management
    │   └── sales/           # Sales optimization
    │
    ├── creative/         # Creative and design prompts
    │   ├── content-strategy/  # Content planning
    │   ├── design/           # Graphic design
    │   └── ux-design/        # User experience
    │
    ├── customer-service/ # Customer service excellence
    │   └── customer-experience-excellence-leader.md
    │
    ├── development/      # Development workflow prompts
    │   ├── execution-instructions.md
    │   ├── fastmcp-server-patterns.md
    │   ├── mcp-enabler-comprehensive.md
    │   └── python-project-ci-cd.md
    │
    ├── education/        # Educational prompts
    │   └── teaching/
    │       └── lesson-plan-creator.md
    │
    ├── engineering/      # Engineering disciplines
    │   ├── construction-excellence-director.md
    │   └── mechanical/
    │       └── design-review-expert.md
    │
    ├── finance/          # Finance and investment
    │   └── financial-analysis-expert.md
    │
    ├── healthcare/       # Healthcare prompts
    │   ├── administration/
    │   │   └── operations-optimization-expert.md
    │   └── pharmaceutical-research-excellence.md
    │
    ├── human-resources/  # HR leadership
    │   └── hr-excellence-leader.md
    │
    ├── operations/       # Operations management
    │   └── supply-chain-excellence-director.md
    │
    ├── project-management/ # Project management tools
    │   ├── README.md
    │   ├── fresh-repo-readme.md
    │   ├── repo-documentation.md
    │   └── repository-setup-automation.md
    │
    ├── research/         # Research and learning prompts
    │   ├── README.md
    │   ├── adr-record-generation.md
    │   ├── adr-research-framework.md
    │   ├── teach-me-advanced.md
    │   ├── teach-me-beginner.md
    │   └── teach-me-journeyman.md
    │
    ├── security/         # Security analysis prompts
    │   └── bandit-security-analysis.md
    │
    └── technical/        # Technical domain prompts
        ├── ai-engineering/      # AI/ML engineering
        ├── architecture/        # System architecture
        ├── cybersecurity/       # Security operations
        ├── data-engineering/    # Data pipelines
        ├── data-science/        # ML/Data science
        ├── devops/             # DevOps practices
        ├── infrastructure/      # Infrastructure as code
        ├── mcp/                # Model Context Protocol
        ├── quality-assurance/   # QA and testing
        ├── security/           # Security architecture
        └── software-engineering/ # Software development
```

## Prompt Standards

All prompts in this repository follow strict quality standards:

### Required Elements

1. **Metadata Section**
   - Category, Tags, Version
   - Personas (dual-persona architecture)
   - Use Cases and Compatible Models

2. **Dual-Persona Architecture**
   - Primary Expert (10-15+ years domain experience)
   - Secondary Expert (complementary perspective)

3. **Multiple Analytical Frameworks**
   - Core framework + 3-4 supporting frameworks
   - Systems thinking integration
   - First principles approach

4. **Four-Phase Processing**
   - Phase 1: Assessment/Analysis
   - Phase 2: Strategic Design
   - Phase 3: Implementation/Execution
   - Phase 4: Optimization/Control

5. **Comprehensive Output Structure**
   - 350+ lines minimum
   - 8-12 major sections
   - Executive summary
   - Detailed deliverables
   - Implementation roadmap
   - Risk management
   - Performance metrics

6. **Documentation**
   - Clear usage instructions
   - Practical examples
   - Related prompts references
   - Research notes

## File Naming Conventions

- Use kebab-case: `strategic-roadmap-generator.md`
- Be descriptive but concise
- Include role or function in name
- Avoid generic terms

## Commit Guidelines

- One prompt per commit
- Descriptive commit messages: `"Add [prompt-name]: [brief description]"`
- Include category in message when relevant
- Reference issues or PRs when applicable

## Quality Assurance

Before committing a new prompt:

1. Verify all required sections are present
2. Ensure 350+ lines of content
3. Validate dual-persona implementation
4. Check framework integration
5. Test example outputs
6. Review formatting and structure
7. Confirm metadata completeness

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.