#!/usr/bin/env python3
"""
convert_prompts_to_jekyll.py
Converts source prompts from /prompts/**/*.md to Jekyll format in /docs/_prompts/[slug].md
"""

import os
import re
import sys
import yaml
import glob
from pathlib import Path
from datetime import datetime


REPO_ROOT = Path(__file__).parent
PROMPTS_DIR = REPO_ROOT / "prompts"
JEKYLL_PROMPTS_DIR = REPO_ROOT / "docs" / "_prompts"

REQUIRED_HEADERS = {"## Metadata", "## Overview", "## When to Use", "## Prompt"}


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def extract_title(content: str) -> str:
    """Extract title from H1 heading."""
    match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_metadata(content: str) -> dict:
    """Extract metadata fields from ## Metadata section."""
    meta = {}
    section = extract_section(content, "## Metadata", next_h2=True)
    if not section:
        return meta

    field_map = {
        "id": "id",
        "version": "version",
        "category": "category",
        "tags": "tags",
        "complexity": "complexity",
        "interaction": "interaction",
        "models": "compatible_models",
        "compatible_models": "compatible_models",
        "created": "date",
        "updated": "updated",
    }

    for line in section.split("\n"):
        line = line.strip().lstrip("-").strip()
        if "**" in line and ":" in line:
            # Format: **Key**: value
            m = re.match(r"\*\*([^*]+)\*\*\s*:\s*(.+)", line)
            if m:
                key = m.group(1).strip().lower().replace(" ", "_")
                value = m.group(2).strip()
                mapped = field_map.get(key, key)
                meta[mapped] = value
        elif ":" in line and not line.startswith("#"):
            parts = line.split(":", 1)
            if len(parts) == 2:
                key = parts[0].strip().lower().replace(" ", "_").strip("`")
                value = parts[1].strip()
                if key and value:
                    mapped = field_map.get(key, key)
                    meta[mapped] = value

    # Parse tags from comma-separated string or backtick list
    if "tags" in meta and isinstance(meta["tags"], str):
        tags_str = meta["tags"].strip("`")
        tags = [t.strip().strip("`") for t in re.split(r"[,\s]+", tags_str) if t.strip()]
        meta["tags"] = tags

    # Parse compatible_models similarly
    if "compatible_models" in meta and isinstance(meta["compatible_models"], str):
        models_str = meta["compatible_models"]
        models = [m.strip() for m in models_str.split(",") if m.strip()]
        meta["compatible_models"] = models

    return meta


def extract_section(content: str, header: str, next_h2: bool = True) -> str:
    """Extract content of a specific ## section."""
    pattern = re.escape(header)
    start_match = re.search(rf"^{pattern}\s*$", content, re.MULTILINE)
    if not start_match:
        return ""

    start = start_match.end()

    if next_h2:
        end_match = re.search(r"^##\s+", content[start:], re.MULTILINE)
        end = start + end_match.start() if end_match else len(content)
    else:
        end = len(content)

    return content[start:end].strip()


def extract_overview(content: str) -> str:
    """Extract overview description."""
    section = extract_section(content, "## Overview")
    # Remove any sub-headers and take first paragraph
    lines = [l for l in section.split("\n") if l.strip() and not l.startswith("#")]
    return " ".join(lines).strip()


def extract_prompt(content: str) -> str:
    """Extract the prompt from fenced code block in ## Prompt section."""
    section = extract_section(content, "## Prompt")
    if not section:
        return ""

    # Try to find fenced code block (``` ... ```)
    fence_match = re.search(r"```[^\n]*\n(.*?)```", section, re.DOTALL)
    if fence_match:
        return fence_match.group(1).strip()

    # Fall back to full section content
    return section.strip()


def extract_use_cases(content: str) -> list:
    """Extract use cases from ## When to Use section."""
    section = extract_section(content, "## When to Use")
    use_cases = []

    for line in section.split("\n"):
        line = line.strip()
        # Bullet points that are not anti-patterns
        if line.startswith(("-", "*")) and "anti" not in line.lower() and "don't" not in line.lower():
            text = line.lstrip("-* ").strip()
            if text and not text.startswith("**"):
                use_cases.append(text)

    return use_cases[:5]  # Cap at 5 use cases


def parse_prompt_file(filepath: Path) -> dict | None:
    """Parse a source prompt file and return structured data."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  ERROR reading {filepath}: {e}", file=sys.stderr)
        return None

    # Skip README files
    if filepath.name.lower() == "readme.md":
        return None

    # Must have at least a title
    title = extract_title(content)
    if not title:
        return None

    slug = slugify(filepath.stem)
    metadata = extract_metadata(content)
    description = extract_overview(content)
    prompt_text = extract_prompt(content)
    use_cases = extract_use_cases(content)

    # Determine category from directory structure or metadata
    category = metadata.get("category", "")
    if not category:
        # Infer from path
        parts = filepath.relative_to(PROMPTS_DIR).parts
        category = parts[0] if parts else "general"
    category = category.lower().strip()

    # Build date
    date = metadata.get("date") or metadata.get("updated") or datetime.now().strftime("%Y-%m-%d")
    # Normalize date format
    date_match = re.match(r"(\d{4}-\d{2}-\d{2})", str(date))
    date = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%d")

    return {
        "title": title,
        "slug": slug,
        "category": category,
        "tags": metadata.get("tags", []),
        "compatible_models": metadata.get("compatible_models", ["Claude 3+", "GPT-4+"]),
        "date": date,
        "description": description or f"{title} - AI prompt for {category}",
        "prompt": prompt_text,
        "use_cases": use_cases,
        "complexity": metadata.get("complexity", "intermediate"),
        "interaction": metadata.get("interaction", "single-shot"),
        "source_file": str(filepath.relative_to(REPO_ROOT)),
    }


class _LiteralBlockDumper(yaml.Dumper):
    """YAML Dumper that uses literal block scalars (|) for multi-line strings.
    This ensures Ruby's Psych parser (used by Jekyll/GitHub Pages) can always
    parse the prompt field correctly, regardless of content (quotes, XML tags, etc.).
    """

    pass


def _literal_str_representer(dumper: yaml.Dumper, data: str) -> yaml.ScalarNode:
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_LiteralBlockDumper.add_representer(str, _literal_str_representer)


def build_jekyll_frontmatter(data: dict) -> str:
    """Build YAML frontmatter for Jekyll output."""
    fm = {
        "title": data["title"],
        "slug": data["slug"],
        "category": data["category"],
        "tags": data["tags"],
        "compatible_models": data["compatible_models"],
        "date": data["date"],
        "description": data["description"],
        "layout": "prompt",
    }
    if data.get("use_cases"):
        fm["use_cases"] = data["use_cases"]
    if data.get("complexity"):
        fm["complexity"] = data["complexity"]
    if data.get("interaction"):
        fm["interaction"] = data["interaction"]
    # Prompt text goes in frontmatter so {{ page.prompt }} renders correctly in code block
    if data.get("prompt"):
        fm["prompt"] = data["prompt"]

    return yaml.dump(fm, Dumper=_LiteralBlockDumper, default_flow_style=False, allow_unicode=True, sort_keys=False)


def build_jekyll_content(data: dict) -> str:
    """Build the full Jekyll prompt file content. Body is empty — prompt is in frontmatter."""
    frontmatter = build_jekyll_frontmatter(data)

    lines = [
        "---",
        frontmatter.rstrip(),
        "---",
        "",
    ]
    return "\n".join(lines)


def convert_all_prompts(dry_run: bool = False) -> tuple[int, int, list]:
    """Convert all source prompts to Jekyll format. Returns (converted, skipped, errors)."""
    JEKYLL_PROMPTS_DIR.mkdir(parents=True, exist_ok=True)

    prompt_files = []
    for pattern in ["**/*.md"]:
        prompt_files.extend(PROMPTS_DIR.glob(pattern))

    prompt_files = sorted(prompt_files)
    converted = 0
    skipped = 0
    errors = []

    for filepath in prompt_files:
        if filepath.name.lower() == "readme.md":
            skipped += 1
            continue

        data = parse_prompt_file(filepath)
        if not data:
            skipped += 1
            continue

        output_path = JEKYLL_PROMPTS_DIR / f"{data['slug']}.md"
        content = build_jekyll_content(data)

        if dry_run:
            print(f"  [DRY RUN] Would write: {output_path.name}")
            converted += 1
            continue

        try:
            output_path.write_text(content, encoding="utf-8")
            converted += 1
        except Exception as e:
            errors.append(f"{filepath}: {e}")
            print(f"  ERROR writing {output_path}: {e}", file=sys.stderr)

    return converted, skipped, errors


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Convert source prompts to Jekyll format")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be converted without writing files")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    print(f"Converting prompts from: {PROMPTS_DIR}")
    print(f"Output directory: {JEKYLL_PROMPTS_DIR}")
    if args.dry_run:
        print("DRY RUN - no files will be written")
    print()

    converted, skipped, errors = convert_all_prompts(dry_run=args.dry_run)

    print(f"\nResults:")
    print(f"  Converted: {converted}")
    print(f"  Skipped:   {skipped}")
    print(f"  Errors:    {len(errors)}")

    if errors:
        print("\nErrors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print("\nDone.")


if __name__ == "__main__":
    main()
