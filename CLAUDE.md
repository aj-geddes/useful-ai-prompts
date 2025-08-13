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
Each prompt follows a strict dual-persona architecture:
- **Primary Expert** (10-15+ years domain experience)
- **Secondary Expert** (complementary perspective)
- **Multiple Frameworks** (3-5 professional methodologies)
- **Four-Phase Processing** (Assessment → Design → Implementation → Optimization)
- **Comprehensive Output** (350+ lines minimum)

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
- Follow dual-persona + frameworks structure

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
2. Follow dual-persona architecture requirements
3. Include metadata, frameworks, and 4-phase structure
4. Run conversion scripts to generate Jekyll version
5. Update PROMPT-INDEX.json

### Prompt Quality Standards
- Minimum 350 lines of content
- Dual-persona implementation (Primary + Secondary expert)
- 3-5 professional frameworks integrated
- Four-phase systematic processing
- Executive summary + detailed deliverables
- Implementation roadmap + risk management

### Conversion Process
Old format prompts are converted to new conversational format using:
- Extract key metadata (title, category, tags)
- Transform dual-persona structure
- Maintain framework integration
- Preserve 4-phase processing approach

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

- This repository focuses on **expert-level prompts** for professional workflows
- Each prompt combines multiple perspectives and methodologies
- Prompts are designed for 600+ line outputs with structured deliverables
- The conversion system maintains compatibility between source and Jekyll formats
- Quality standards are strictly enforced (350+ lines, dual-persona, frameworks)