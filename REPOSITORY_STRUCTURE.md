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
├── docs/                 # Website interface for browsing prompts
│   ├── index.html        # Main website page
│   ├── styles.css        # Website styling
│   ├── app.js           # Website functionality
│   └── README.md        # Website deployment guide
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
    ├── administrative/   # Executive and administrative support
    ├── business/         # Business operations prompts
    ├── creative/         # Creative and design prompts
    ├── customer-service/ # Customer service excellence
    ├── development/      # Development workflow prompts
    ├── education/        # Educational prompts
    ├── engineering/      # Engineering disciplines
    ├── finance/          # Finance and investment
    ├── healthcare/       # Healthcare prompts
    ├── human-resources/  # HR leadership
    ├── operations/       # Operations management
    ├── project-management/ # Project management tools
    ├── research/         # Research and learning prompts
    ├── security/         # Security analysis prompts
    └── technical/        # Technical domain prompts
```

## Prompt Standards

All prompts in this repository follow our interactive question-based format:

### Required Elements

1. **Metadata Section**
   - Category, Tags, Version
   - Compatible Models
   - Use Cases

2. **Interactive Format**
   - "I'll help you..." opening
   - Numbered questions to understand context
   - Clear deliverable sections promised
   - Example usage with realistic scenarios

3. **Structured Output**
   - Professional quality guidance
   - Actionable recommendations
   - Clear implementation steps

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
2. Test interactive question flow
3. Validate output structure
4. Check example usage
5. Review formatting and structure
6. Confirm metadata completeness

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.