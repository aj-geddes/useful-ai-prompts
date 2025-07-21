#!/usr/bin/env python3
"""
Update PROMPT-INDEX.json with all converted Jekyll prompts.
"""

import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List

def extract_prompt_metadata(file_path: Path) -> Dict:
    """Extract metadata from a Jekyll prompt file."""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract front matter
        if not content.startswith('---\n'):
            return None
        
        end_marker = content.find('\n---\n', 4)
        if end_marker == -1:
            return None
        
        front_matter_text = content[4:end_marker]
        front_matter = yaml.safe_load(front_matter_text)
        
        if not isinstance(front_matter, dict):
            return None
        
        # Create index entry
        return {
            'title': front_matter.get('title', ''),
            'description': front_matter.get('description', ''),
            'category': front_matter.get('category', ''),
            'tags': front_matter.get('tags', []),
            'slug': front_matter.get('slug', ''),
            'date': front_matter.get('date', ''),
            'version': front_matter.get('version', '1.0.0'),
            'compatible_models': front_matter.get('compatible_models', []),
            'use_cases': front_matter.get('use_cases', []),
            'file_path': f"_prompts/{file_path.name}"
        }
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def update_prompt_index():
    """Update the PROMPT-INDEX.json file with all converted prompts."""
    
    prompts_dir = Path("docs/_prompts")
    index_file = Path("docs/PROMPT-INDEX.json")
    
    if not prompts_dir.exists():
        print(f"Prompts directory {prompts_dir} not found!")
        return
    
    print("Updating PROMPT-INDEX.json...")
    
    # Collect all prompt metadata
    prompts = []
    
    for file_path in sorted(prompts_dir.glob("*.md")):
        metadata = extract_prompt_metadata(file_path)
        if metadata:
            prompts.append(metadata)
    
    # Create index structure
    index_data = {
        'version': '1.0.0',
        'last_updated': datetime.now().isoformat(),
        'total_prompts': len(prompts),
        'categories': list(set(p['category'] for p in prompts)),
        'prompts': prompts
    }
    
    # Write to file
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    
    print(f"Updated {index_file} with {len(prompts)} prompts")
    print(f"Categories: {len(index_data['categories'])}")
    print("Index update complete!")

if __name__ == "__main__":
    update_prompt_index()