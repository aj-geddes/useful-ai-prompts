#!/usr/bin/env python3
"""
Fix category assignments in prompt files.
Map invalid categories to valid ones.
"""

import os
import yaml
from pathlib import Path
import re

# Category mapping
CATEGORY_MAPPING = {
    'financial-planning': 'planning',
    'government': 'government-digital',
    'personal-productivity': 'optimization',
    'project-management': 'management-leadership',
    'personal-growth': 'learning-development',
    'content-creation': 'creation',
    'health-wellness': 'healthcare-digital',
    'career-development': 'learning-development',
    'development': 'learning-development',
    'learning-skills': 'learning-development',
    'relationships-communication': 'communication',
    'technical': 'technical-workflows'
}

def get_valid_categories():
    """Get valid categories from _categories directory."""
    categories = set()
    categories_dir = Path('docs/_categories')
    if categories_dir.exists():
        for category_file in categories_dir.glob('*.md'):
            category_name = category_file.stem
            categories.add(category_name)
    return categories

def fix_prompt_category(file_path):
    """Fix category in a single prompt file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---\n'):
            return False, "No YAML front matter"
        
        # Find the end of front matter
        end_marker = content.find('\n---\n', 4)
        if end_marker == -1:
            return False, "Malformed YAML front matter"
        
        front_matter_text = content[4:end_marker]
        body = content[end_marker + 5:]
        
        # Parse YAML
        try:
            front_matter = yaml.safe_load(front_matter_text)
        except yaml.YAMLError as e:
            return False, f"YAML parse error: {e}"
        
        if not isinstance(front_matter, dict):
            return False, "Front matter is not a dictionary"
        
        # Check if category needs fixing
        current_category = front_matter.get('category', '')
        if current_category in CATEGORY_MAPPING:
            new_category = CATEGORY_MAPPING[current_category]
            front_matter['category'] = new_category
            
            # Convert back to YAML
            new_front_matter = yaml.dump(front_matter, default_flow_style=False, sort_keys=True)
            new_content = f"---\n{new_front_matter}---\n{body}"
            
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True, f"Changed category from '{current_category}' to '{new_category}'"
        
        return False, f"Category '{current_category}' is valid or not mapped"
        
    except Exception as e:
        return False, f"Error processing file: {e}"

def main():
    """Fix categories in all prompt files."""
    prompts_dir = Path('docs/_prompts')
    
    if not prompts_dir.exists():
        print("Error: docs/_prompts directory not found")
        return
    
    valid_categories = get_valid_categories()
    print(f"Valid categories: {sorted(valid_categories)}")
    print(f"Category mappings: {CATEGORY_MAPPING}")
    print()
    
    fixed_count = 0
    error_count = 0
    
    for file_path in prompts_dir.glob('*.md'):
        success, message = fix_prompt_category(file_path)
        if success:
            print(f"✅ {file_path.name}: {message}")
            fixed_count += 1
        elif "not mapped" not in message and "is valid" not in message:
            print(f"❌ {file_path.name}: {message}")
            error_count += 1
    
    print(f"\nSummary:")
    print(f"  Fixed: {fixed_count}")
    print(f"  Errors: {error_count}")

if __name__ == "__main__":
    main()