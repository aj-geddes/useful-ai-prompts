# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **Useful AI Prompts** repository - a comprehensive library of specialized prompts designed for AI assistants to adopt expert personas when completing tasks. The repository contains 259+ prompts organized across 14 categories, combining multiple expert perspectives with professional frameworks.

## Key Commands

### Development Commands
```bash
# Install dependencies
npm install

# Code formatting
npx prettier --write .

# Validation scripts
python validate_jekyll_conversion.py
python update_prompt_index.py
```

### Jekyll Website (docs/ directory)
```bash
cd docs/
bundle install           # Install Ruby dependencies
bundle exec jekyll build # Build the site
bundle exec jekyll serve # Serve locally (http://localhost:4000)
```

### Prompt Management
```bash
# Convert old format prompts to new conversational format
python batch_convert_prompts.py

# Fix conversion errors
python fix_conversion_errors.py

# Update the prompt index
python update_prompt_index.py
```

## Architecture Overview

### Directory Structure
- **`/prompts/`** - Main prompt library organized by domain (technical, business, creative, specialized)
- **`/docs/`** - Jekyll website for browsing prompts (GitHub Pages deployment)
- **`/metadata/`** - Framework definitions and guidelines
- **`/_prompts/`** (in docs) - Jekyll collection of converted prompts for website
- **Python scripts** - Conversion, validation, and maintenance utilities

### Prompt Architecture
Each prompt follows a conversational, user-friendly format:
- **Clear metadata** (category, tags, use cases)
- **Helpful description** explaining the prompt's purpose
- **Interactive questions** to understand user's context
- **Structured deliverables** based on user's needs
- **Practical examples** showing usage

### Data Flow
1. Source prompts in `/prompts/` directories
2. Conversion scripts transform to Jekyll format in `/docs/_prompts/`
3. Jekyll builds website from `/docs/` directory
4. PROMPT-INDEX.json provides machine-readable catalog

## File Organization Patterns

### Prompt Files
- Located in categorized subdirectories under `/prompts/`
- Use kebab-case naming: `strategic-roadmap-generator.md`
- Include role/function in filename
- Follow conversational format with clear structure

### Jekyll Collections
- `_prompts/` - Individual prompt pages
- `_categories/` - Category index pages
- Uses frontmatter for metadata (title, category, tags, etc.)

### Python Utilities
- `batch_convert_prompts.py` - Converts old format to new conversational format
- `convert_prompts_to_jekyll.py` - Jekyll format conversion
- `validate_jekyll_conversion.py` - Validation and error checking
- `update_prompt_index.py` - Generates/updates PROMPT-INDEX.json

## Working with Prompts

### Required Skill: prompt-refactor

**IMPORTANT**: When creating, editing, refactoring, or improving any prompts in this repository, you MUST use the `prompt-refactor` skill located at `.claude/skills/prompt-refactor/`.

The skill provides:
- Standardized template structure for all prompts
- 11 quality gates for validation
- Batch processing support for multiple prompts
- Consistent metadata and formatting

**How to use:**
```bash
# Single prompt refactoring
claude "Using prompt-refactor skill, refactor this prompt: [paste or path]"

# Batch processing
./.claude/skills/prompt-refactor/scripts/orchestrate-refactor.sh ./prompts ./output 4

# Validate a refactored prompt
./.claude/skills/prompt-refactor/scripts/validate-prompt.sh ./prompts/my-prompt.md
```

**Skill triggers** (auto-activated on these phrases):
- "refactor prompt"
- "improve prompt"
- "standardize prompts"
- "prompt template"
- "apply prompt template"

See `.claude/skills/prompt-refactor/SKILL.md` for full template specification and quality gates.

### Adding New Prompts
1. Create prompt in appropriate `/prompts/[category]/` directory
2. **Use the prompt-refactor skill** to ensure proper structure
3. Follow the standardized template with metadata, role, task, output specification
4. Validate with the validation script
5. Run conversion scripts to generate Jekyll version
6. Update PROMPT-INDEX.json

### Prompt Quality Standards (enforced by prompt-refactor skill)
- Complete metadata (ID, version, category, tags, complexity, interaction, models)
- Concise overview (≤3 sentences)
- Specific role definition with concrete expertise
- Categorized inputs (required vs optional)
- Structured task (3-7 clear steps)
- Specified outputs (format + length + requirements)
- Measurable quality criteria
- Realistic examples (input: 20-200 words, output: 100-600 words)
- Copy-paste ready prompt section

### Conversion Process
Old format prompts are converted to new standardized format using:
- Extract key metadata (title, category, tags)
- Transform to structured XML tags (role, input_handling, task, output_specification, etc.)
- Apply quality gates validation
- Add practical examples and clear deliverables

## Website Deployment

The Jekyll website is automatically deployed to GitHub Pages from the `/docs/` directory:
- Base URL: `/useful-ai-prompts`
- Collections: prompts and categories
- Search functionality enabled
- Responsive design with category browsing

## Integration Guidelines

For AI agents working with this repository:
1. Parse task requirements to identify appropriate prompt category
2. Match to prompt taxonomy using `/prompts/[category]/[subcategory]/`
3. Load and customize selected prompt with task-specific variables
4. Execute using the standard 4-phase framework
5. Reference PROMPT-INDEX.json for programmatic selection

## Important Notes

- This repository focuses on **helpful prompts** for professional workflows
- Each prompt provides expert guidance in a conversational format
- Prompts gather context through questions and provide structured deliverables
- The conversion system maintains compatibility between source and Jekyll formats
- Quality standards focus on clarity, usability, and practical value