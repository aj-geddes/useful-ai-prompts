#!/usr/bin/env python3
"""
update_prompt_index.py
Scans /prompts/**/*.md and builds PROMPT-INDEX.json at both / and /docs/
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).parent
PROMPTS_DIR = REPO_ROOT / "prompts"
INDEX_PATHS = [
    REPO_ROOT / "PROMPT-INDEX.json",
    REPO_ROOT / "docs" / "PROMPT-INDEX.json",
]


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def extract_title(content: str) -> str:
    match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_section(content: str, header: str) -> str:
    pattern = re.escape(header)
    start_match = re.search(rf"^{pattern}\s*$", content, re.MULTILINE)
    if not start_match:
        return ""
    start = start_match.end()
    end_match = re.search(r"^##\s+", content[start:], re.MULTILINE)
    end = start + end_match.start() if end_match else len(content)
    return content[start:end].strip()


def extract_metadata(content: str) -> dict:
    meta = {}
    section = extract_section(content, "## Metadata")
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

    if "tags" in meta and isinstance(meta["tags"], str):
        tags_str = meta["tags"].strip("`")
        tags = [t.strip().strip("`") for t in re.split(r"[,\s]+", tags_str) if t.strip()]
        meta["tags"] = tags

    if "compatible_models" in meta and isinstance(meta["compatible_models"], str):
        models = [m.strip() for m in meta["compatible_models"].split(",") if m.strip()]
        meta["compatible_models"] = models

    return meta


def extract_overview(content: str) -> str:
    section = extract_section(content, "## Overview")
    lines = [l for l in section.split("\n") if l.strip() and not l.startswith("#")]
    return " ".join(lines).strip()


def parse_prompt_file(filepath: Path) -> dict | None:
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  ERROR reading {filepath}: {e}", file=sys.stderr)
        return None

    if filepath.name.lower() == "readme.md":
        return None

    title = extract_title(content)
    if not title:
        return None

    slug = slugify(filepath.stem)
    metadata = extract_metadata(content)
    description = extract_overview(content)

    category = metadata.get("category", "")
    if not category:
        parts = filepath.relative_to(PROMPTS_DIR).parts
        category = parts[0] if parts else "general"
    category = category.lower().strip()

    date = metadata.get("date") or metadata.get("updated") or datetime.now().strftime("%Y-%m-%d")
    date_match = re.match(r"(\d{4}-\d{2}-\d{2})", str(date))
    date = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%d")

    return {
        "title": title,
        "slug": slug,
        "description": description or f"{title} - AI prompt for {category}",
        "category": category,
        "tags": metadata.get("tags", []),
        "compatible_models": metadata.get("compatible_models", ["Claude 3+", "GPT-4+"]),
        "complexity": metadata.get("complexity", "intermediate"),
        "interaction": metadata.get("interaction", "single-shot"),
        "file_path": str(filepath.relative_to(REPO_ROOT)),
        "date": date,
    }


def build_index() -> dict:
    prompt_files = sorted(PROMPTS_DIR.glob("**/*.md"))

    prompts = []
    categories_set = set()
    skipped = 0

    for filepath in prompt_files:
        if filepath.name.lower() == "readme.md":
            skipped += 1
            continue

        data = parse_prompt_file(filepath)
        if data:
            prompts.append(data)
            categories_set.add(data["category"])
        else:
            skipped += 1

    categories = sorted(categories_set)

    return {
        "version": "2.0.0",
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total_prompts": len(prompts),
        "categories": categories,
        "prompts": prompts,
        "_skipped": skipped,
    }


def write_index(index_data: dict, output_path: Path) -> None:
    # Remove internal keys before writing
    clean_data = {k: v for k, v in index_data.items() if not k.startswith("_")}
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(clean_data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Update PROMPT-INDEX.json from source prompts")
    parser.add_argument("--dry-run", action="store_true", help="Show stats without writing")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    print(f"Scanning prompts in: {PROMPTS_DIR}")
    print()

    index = build_index()

    print(f"Results:")
    print(f"  Total prompts:   {index['total_prompts']}")
    print(f"  Categories:      {len(index['categories'])}")
    print(f"  Skipped files:   {index.get('_skipped', 0)}")
    print(f"  Last updated:    {index['last_updated']}")

    if args.verbose:
        print(f"\nCategories:")
        for cat in index["categories"]:
            count = sum(1 for p in index["prompts"] if p["category"] == cat)
            print(f"  {cat}: {count} prompts")

    if args.dry_run:
        print("\nDRY RUN - no files written")
        return

    for output_path in INDEX_PATHS:
        write_index(index, output_path)
        print(f"\nWritten: {output_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()
