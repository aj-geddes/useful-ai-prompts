#!/usr/bin/env python3
"""
Convert skills and hooks to Jekyll format.
Creates individual pages for each skill and hook in the docs directory.
"""

import os
import re
import yaml
from pathlib import Path

# Directories
SKILLS_SOURCE = Path("skills")
HOOKS_SOURCE = Path("hooks")
DOCS_DIR = Path("docs")
SKILLS_OUTPUT = DOCS_DIR / "_skills"
HOOKS_OUTPUT = DOCS_DIR / "_hooks"

# Skill category mapping based on skill names
SKILL_CATEGORIES = {
    "software-development": [
        "refactor", "design-pattern", "code-review", "microservices", "clean-code",
        "architecture", "solid", "dependency-injection", "event-driven", "modular"
    ],
    "devops-infrastructure": [
        "docker", "kubernetes", "terraform", "ci-cd", "ansible", "jenkins",
        "infrastructure", "deployment", "container", "orchestration"
    ],
    "api-integration": [
        "rest-api", "graphql", "grpc", "webhook", "api-gateway", "oauth",
        "api-authentication", "api-versioning", "api-rate-limiting"
    ],
    "testing-qa": [
        "unit-test", "integration-test", "e2e-test", "test-automation",
        "mocking", "fixture", "coverage", "tdd", "bdd"
    ],
    "database-storage": [
        "sql", "nosql", "database", "migration", "indexing", "schema",
        "postgres", "mysql", "mongodb", "redis"
    ],
    "security-compliance": [
        "security", "vulnerability", "encryption", "audit", "compliance",
        "penetration", "secure-coding", "authentication"
    ],
    "data-analytics": [
        "data-analysis", "exploratory", "feature-engineering", "ab-test",
        "statistical", "visualization", "pandas", "etl", "data-pipeline"
    ],
    "frontend-development": [
        "react", "vue", "angular", "css", "responsive", "accessibility",
        "frontend", "ui", "ux", "component"
    ],
    "cloud-platforms": [
        "aws", "azure", "gcp", "serverless", "lambda", "cloud-function",
        "s3", "ec2", "cloud-cost"
    ],
    "machine-learning": [
        "ml-model", "machine-learning", "deep-learning", "neural",
        "training", "hyperparameter", "model-deployment"
    ],
    "monitoring-observability": [
        "prometheus", "grafana", "logging", "tracing", "alerting",
        "monitoring", "observability", "metrics"
    ],
    "troubleshooting": [
        "debugging", "root-cause", "memory-leak", "performance-profiling",
        "troubleshooting", "diagnostics"
    ],
    "documentation": [
        "documentation", "readme", "api-doc", "changelog", "comment",
        "docstring", "markdown"
    ],
    "backend-development": [
        "backend", "server", "middleware", "session", "caching",
        "queue", "websocket"
    ],
    "mobile-development": [
        "mobile", "ios", "android", "react-native", "flutter", "swift", "kotlin"
    ],
    "version-control": [
        "git", "branch", "merge", "rebase", "commit", "version-control"
    ],
    "project-management": [
        "agile", "scrum", "kanban", "sprint", "backlog", "estimation"
    ],
    "performance": [
        "performance", "optimization", "caching", "lazy-loading", "profiling"
    ]
}


def categorize_skill(skill_name):
    """Determine category based on skill name."""
    skill_lower = skill_name.lower()

    for category, keywords in SKILL_CATEGORIES.items():
        for keyword in keywords:
            if keyword in skill_lower:
                return category

    return "software-development"  # Default category


def extract_skill_tags(skill_name, description):
    """Extract tags from skill name and description."""
    tags = []

    # Common technology tags
    tech_keywords = [
        "python", "javascript", "typescript", "java", "go", "rust", "ruby",
        "react", "vue", "angular", "node", "django", "flask", "fastapi",
        "docker", "kubernetes", "aws", "azure", "gcp", "terraform",
        "postgres", "mysql", "mongodb", "redis", "elasticsearch",
        "git", "ci/cd", "jenkins", "github", "gitlab"
    ]

    combined = f"{skill_name} {description}".lower()

    for tech in tech_keywords:
        if tech in combined:
            tags.append(tech)

    # Add skill type tags
    if "test" in combined:
        tags.append("testing")
    if "api" in combined:
        tags.append("api")
    if "security" in combined:
        tags.append("security")
    if "data" in combined:
        tags.append("data")
    if "deploy" in combined:
        tags.append("deployment")

    return tags[:5] if tags else ["development"]


def convert_skills():
    """Convert all skills to Jekyll format."""
    # Create output directory
    SKILLS_OUTPUT.mkdir(parents=True, exist_ok=True)

    converted = 0
    errors = []

    for skill_dir in sorted(SKILLS_SOURCE.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue

        try:
            content = skill_file.read_text(encoding='utf-8')

            # Parse YAML frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    body = parts[2].strip()
                else:
                    frontmatter = {}
                    body = content
            else:
                frontmatter = {}
                body = content

            # Extract metadata
            name = frontmatter.get('name', skill_dir.name.replace('-', ' ').title())
            description = frontmatter.get('description', '')

            # Generate slug
            slug = skill_dir.name

            # Determine category and tags
            category = categorize_skill(slug)
            tags = extract_skill_tags(slug, description)

            # Create Jekyll frontmatter
            jekyll_frontmatter = {
                'title': name,
                'description': description,
                'slug': slug,
                'category': category,
                'tags': tags,
                'date': '2025-01-01',
                'layout': 'skill'
            }

            # Write Jekyll file
            output_file = SKILLS_OUTPUT / f"{slug}.md"

            jekyll_content = "---\n"
            jekyll_content += yaml.dump(jekyll_frontmatter, default_flow_style=False, allow_unicode=True)
            jekyll_content += "---\n\n"
            jekyll_content += body

            output_file.write_text(jekyll_content, encoding='utf-8')
            converted += 1

        except Exception as e:
            errors.append(f"{skill_dir.name}: {str(e)}")

    print(f"Skills converted: {converted}")
    if errors:
        print(f"Errors: {len(errors)}")
        for error in errors[:5]:
            print(f"  - {error}")

    return converted


def convert_hooks():
    """Convert all hooks to Jekyll format."""
    # Create output directory
    HOOKS_OUTPUT.mkdir(parents=True, exist_ok=True)

    # Hook metadata
    hook_metadata = {
        "security-scan": {
            "event_type": "PreToolUse",
            "matcher": "Bash",
            "icon": "fa-shield-alt",
            "icon_class": "security",
            "lines_of_code": 450,
            "features": [
                "AWS key detection",
                "API token scanning",
                "Private key detection",
                "15+ secret patterns",
                "Whitelist support",
                "JSON output for CI/CD"
            ]
        },
        "test-runner": {
            "event_type": "PreToolUse",
            "matcher": "Bash",
            "icon": "fa-check-circle",
            "icon_class": "testing",
            "lines_of_code": 520,
            "features": [
                "Jest support",
                "pytest support",
                "RSpec support",
                "Go test support",
                "Auto framework detection",
                "Failure prevention"
            ]
        },
        "session-setup": {
            "event_type": "SessionStart",
            "matcher": "",
            "icon": "fa-rocket",
            "icon_class": "setup",
            "lines_of_code": 580,
            "features": [
                ".env file loading",
                "Dependency checking",
                "Database verification",
                "Service status",
                "Environment validation"
            ]
        },
        "auto-format": {
            "event_type": "PostToolUse",
            "matcher": "Edit|Write",
            "icon": "fa-magic",
            "icon_class": "format",
            "lines_of_code": 565,
            "features": [
                "Prettier support",
                "Black (Python)",
                "gofmt (Go)",
                "rustfmt (Rust)",
                "8+ language formatters",
                "Auto-detection"
            ]
        },
        "breaking-change-detection": {
            "event_type": "PreToolUse",
            "matcher": "Bash",
            "icon": "fa-exclamation-triangle",
            "icon_class": "warning",
            "lines_of_code": 540,
            "features": [
                "API signature comparison",
                "Export tracking",
                "Parameter change detection",
                "SemVer integration",
                "Warning system"
            ]
        },
        "dependency-check": {
            "event_type": "PreToolUse",
            "matcher": "Bash",
            "icon": "fa-box",
            "icon_class": "dependencies",
            "lines_of_code": 600,
            "features": [
                "npm audit",
                "pip-audit",
                "bundle audit",
                "Severity-based blocking",
                "5+ package managers"
            ]
        }
    }

    converted = 0
    errors = []

    for hook_dir in sorted(HOOKS_SOURCE.iterdir()):
        if not hook_dir.is_dir():
            continue

        readme_file = hook_dir / "README.md"
        if not readme_file.exists():
            continue

        hook_name = hook_dir.name

        try:
            content = readme_file.read_text(encoding='utf-8')

            # Get metadata
            metadata = hook_metadata.get(hook_name, {
                "event_type": "PreToolUse",
                "matcher": "Bash",
                "icon": "fa-code",
                "icon_class": "default",
                "lines_of_code": 300,
                "features": []
            })

            # Extract first paragraph as description
            lines = content.split('\n')
            description = ""
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    description = line
                    break

            # Create Jekyll frontmatter
            jekyll_frontmatter = {
                'title': hook_name,
                'description': description,
                'slug': hook_name,
                'event_type': metadata['event_type'],
                'matcher': metadata['matcher'],
                'icon': metadata['icon'],
                'icon_class': metadata['icon_class'],
                'lines_of_code': metadata['lines_of_code'],
                'features': metadata['features'],
                'date': '2025-01-01',
                'layout': 'hook'
            }

            # Remove first heading from content (it's the title)
            body = content
            if body.startswith('# '):
                body = '\n'.join(body.split('\n')[1:]).strip()

            # Write Jekyll file
            output_file = HOOKS_OUTPUT / f"{hook_name}.md"

            jekyll_content = "---\n"
            jekyll_content += yaml.dump(jekyll_frontmatter, default_flow_style=False, allow_unicode=True)
            jekyll_content += "---\n\n"
            jekyll_content += body

            output_file.write_text(jekyll_content, encoding='utf-8')
            converted += 1

        except Exception as e:
            errors.append(f"{hook_name}: {str(e)}")

    print(f"Hooks converted: {converted}")
    if errors:
        print(f"Errors: {len(errors)}")
        for error in errors:
            print(f"  - {error}")

    return converted


def main():
    """Main conversion function."""
    print("=" * 50)
    print("Converting Skills and Hooks to Jekyll Format")
    print("=" * 50)
    print()

    # Convert skills
    print("Converting skills...")
    skills_count = convert_skills()
    print()

    # Convert hooks
    print("Converting hooks...")
    hooks_count = convert_hooks()
    print()

    print("=" * 50)
    print(f"Total converted: {skills_count} skills, {hooks_count} hooks")
    print("=" * 50)


if __name__ == "__main__":
    main()
