#!/usr/bin/env python3
"""
Force convert all source prompts to Jekyll format
"""

import os
import yaml
from pathlib import Path
from datetime import datetime
import re

def create_slug(title):
    """Create URL-friendly slug from title"""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')

def extract_title_from_content(content):
    """Extract title from markdown content"""
    # Look for first # heading
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if title_match:
        return title_match.group(1).strip()
    
    # Look for title in frontmatter
    if content.startswith('---'):
        frontmatter_end = content.find('---', 3)
        if frontmatter_end > 0:
            try:
                frontmatter = yaml.safe_load(content[3:frontmatter_end])
                if 'title' in frontmatter:
                    return frontmatter['title']
            except:
                pass
    
    return None

def create_frontmatter(title, category, source_file):
    """Create frontmatter for Jekyll"""
    slug = create_slug(title)
    
    frontmatter = {
        'title': title,
        'description': f"Professional prompt for {category} optimization and expert consultation",
        'category': category,
        'tags': [category.replace('-', ' ')],
        'slug': slug,
        'date': datetime.now().strftime("%Y-%m-%d"),
        'version': "3.0.0",
        'compatible_models': ["claude-3.5-sonnet", "gpt-4", "gemini-pro"],
        'use_cases': [f"{category} optimization", "professional workflow enhancement"]
    }
    
    return frontmatter

def convert_prompt_to_jekyll(source_file, docs_dir):
    """Convert a single prompt to Jekyll format"""
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has proper frontmatter
        if content.startswith('---') and content.count('---') >= 2:
            frontmatter_end = content.find('---', 3)
            if frontmatter_end > 0:
                try:
                    frontmatter = yaml.safe_load(content[3:frontmatter_end])
                    if 'title' in frontmatter and 'category' in frontmatter:
                        # Already properly formatted, just copy
                        output_file = docs_dir / source_file.name
                        with open(output_file, 'w', encoding='utf-8') as f:
                            f.write(content)
                        return str(output_file)
                except:
                    pass
        
        # Extract title
        title = extract_title_from_content(content)
        if not title:
            # Create title from filename
            title = source_file.stem.replace('-', ' ').title()
        
        # Determine category from file path
        path_parts = source_file.parts
        if 'prompts' in path_parts:
            prompts_index = path_parts.index('prompts')
            if prompts_index + 1 < len(path_parts):
                category = path_parts[prompts_index + 1]
            else:
                category = 'general'
        else:
            category = 'general'
        
        # Create frontmatter
        frontmatter = create_frontmatter(title, category, source_file)
        
        # Remove existing frontmatter if present
        if content.startswith('---'):
            frontmatter_end = content.find('---', 3)
            if frontmatter_end > 0:
                content = content[frontmatter_end + 3:].strip()
        
        # Format frontmatter
        frontmatter_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        
        # Create final content
        final_content = f"---\n{frontmatter_yaml}---\n\n{content}"
        
        # Save to Jekyll directory
        output_file = docs_dir / source_file.name
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        return str(output_file)
        
    except Exception as e:
        print(f"Error converting {source_file}: {e}")
        return None

def main():
    repo_root = Path.cwd()
    prompts_dir = repo_root / "prompts"
    jekyll_dir = repo_root / "docs" / "_prompts"
    
    # Ensure Jekyll directory exists
    jekyll_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all markdown files in prompts directory
    md_files = list(prompts_dir.rglob("*.md"))
    md_files = [f for f in md_files if f.name != "README.md"]
    
    print(f"Found {len(md_files)} source prompts")
    
    converted = 0
    skipped = 0
    failed = 0
    
    for md_file in md_files:
        result = convert_prompt_to_jekyll(md_file, jekyll_dir)
        if result:
            converted += 1
            print(f"✓ Converted: {md_file.name}")
        else:
            failed += 1
            print(f"✗ Failed: {md_file.name}")
    
    print(f"\nConversion complete:")
    print(f"✓ Converted: {converted}")
    print(f"✗ Failed: {failed}")
    
    # Update final count
    final_count = len(list(jekyll_dir.glob("*.md")))
    print(f"Total Jekyll prompts: {final_count}")

if __name__ == "__main__":
    main()