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

### Adding New Prompts
1. Create prompt in appropriate `/prompts/[category]/` directory
2. Follow the conversational format with context questions
3. Include metadata (category, tags, use cases)
4. Run conversion scripts to generate Jekyll version
5. Update PROMPT-INDEX.json

### Prompt Quality Standards
- Clear, conversational tone
- Context-gathering questions to understand the user's needs
- Structured response format with defined deliverables
- Practical, actionable guidance
- Real-world examples demonstrating usage
- Professional expertise without unnecessary complexity

### Conversion Process
Old format prompts are converted to new conversational format using:
- Extract key metadata (title, category, tags)
- Transform to question-based context gathering
- Simplify into user-friendly language
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