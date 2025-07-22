#!/usr/bin/env python3
"""
Script to identify and help convert old dual-persona prompts to new conversational format
"""

import os
import re
from pathlib import Path

def find_old_format_prompts(base_path):
    """Find all prompts that use the old dual-persona format"""
    old_format_files = []
    
    patterns = [
        r"You are operating as.*system combining",
        r"dual personas",
        r"Primary Persona.*Secondary Persona",
        r"### 1\. .* \(\d+\+ years",
        r"### 2\. .*",
        r"Phase 1:.*Phase 2:.*Phase 3:.*Phase 4:"
    ]
    
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Check if file matches old format patterns
                for pattern in patterns:
                    if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
                        # Also check if it's over 400 lines (old format characteristic)
                        if len(content.split('\n')) > 400:
                            old_format_files.append(filepath)
                            break
    
    return old_format_files

def analyze_prompt_structure(filepath):
    """Analyze the structure of an old format prompt"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    info = {
        'filepath': filepath,
        'filename': os.path.basename(filepath),
        'line_count': len(lines),
        'has_dual_persona': bool(re.search(r"### 1\.|Primary Persona", content)),
        'has_4_phases': bool(re.search(r"Phase 4:", content)),
        'title': '',
        'category': '',
        'description': ''
    }
    
    # Extract title
    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    if title_match:
        info['title'] = title_match.group(1)
    
    # Extract category
    cat_match = re.search(r"- \*\*Category\*\*: (.+)$", content, re.MULTILINE)
    if cat_match:
        info['category'] = cat_match.group(1)
        
    # Extract description
    desc_match = re.search(r"## Description\s*\n\s*(.+?)(?=\n##|\n###)", content, re.DOTALL)
    if desc_match:
        info['description'] = desc_match.group(1).strip()
    
    return info

def main():
    base_path = "/home/aj-geddes/dev/claude-projects/useful-ai-prompts/prompts"
    
    print("Finding old format prompts...")
    old_prompts = find_old_format_prompts(base_path)
    
    print(f"\nFound {len(old_prompts)} prompts in old format:\n")
    
    # Group by directory
    by_category = {}
    for filepath in sorted(old_prompts):
        rel_path = os.path.relpath(filepath, base_path)
        category = os.path.dirname(rel_path)
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(filepath)
    
    # Print organized list
    for category, files in sorted(by_category.items()):
        print(f"\n{category}:")
        for filepath in files:
            info = analyze_prompt_structure(filepath)
            print(f"  - {info['filename']} ({info['line_count']} lines)")
            if info['title']:
                print(f"    Title: {info['title']}")
    
    print(f"\nTotal categories with old format: {len(by_category)}")
    print(f"Total prompts to convert: {len(old_prompts)}")
    
    # Save list to file for tracking
    with open('old_format_prompts.txt', 'w') as f:
        for filepath in sorted(old_prompts):
            f.write(f"{filepath}\n")
    print("\nList saved to old_format_prompts.txt")

if __name__ == "__main__":
    main()