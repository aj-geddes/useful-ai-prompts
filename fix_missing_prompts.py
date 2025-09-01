#!/usr/bin/env python3
"""
Fix files that are missing the 'prompt' field in their YAML front matter.
These files have content but it's not in the prompt field.
"""

import yaml
from pathlib import Path
import re

def extract_and_fix_prompt(file_path: Path):
    """Extract content and move it to the prompt field in front matter."""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if it starts with front matter
        if not content.startswith('---\n'):
            print(f"Skipping {file_path}: No front matter")
            return False
            
        # Find the end of front matter
        end_marker = content.find('\n---\n', 4)
        if end_marker == -1:
            print(f"Skipping {file_path}: Malformed front matter")
            return False
        
        front_matter_text = content[4:end_marker]
        body_content = content[end_marker + 5:].strip()
        
        # Parse front matter
        front_matter = yaml.safe_load(front_matter_text)
        if not isinstance(front_matter, dict):
            print(f"Skipping {file_path}: Invalid front matter")
            return False
        
        # Check if prompt field is missing or empty
        if 'prompt' not in front_matter or not front_matter['prompt'].strip():
            if body_content:
                # Move body content to prompt field
                front_matter['prompt'] = body_content
                
                # Fix slug if it doesn't match filename
                expected_slug = file_path.stem
                if front_matter.get('slug') != expected_slug:
                    print(f"Fixing slug in {file_path}: {front_matter.get('slug')} -> {expected_slug}")
                    front_matter['slug'] = expected_slug
                
                # Write back to file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('---\n')
                    f.write(yaml.dump(front_matter, default_flow_style=False, allow_unicode=True))
                    f.write('---\n')
                
                print(f"Fixed {file_path}: Moved content to prompt field")
                return True
            else:
                print(f"Skipping {file_path}: No content to move to prompt field")
                return False
        
        return False
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Fix all files missing prompt field."""
    
    prompts_dir = Path("docs/_prompts")
    if not prompts_dir.exists():
        print(f"Prompts directory {prompts_dir} not found!")
        return
    
    files_to_check = [
        'digital-government-transformation-expert.md',
        'quantum-optimization-algorithm-design.md', 
        'repository-setup-automation.md',
        'quantum-hardware-calibration-characterization.md',
        'wind-farm-operations-excellence-director.md',
        'manufacturing-iot-integration-expert.md',
        'protein-structure-prediction-modeling.md',
        'claude-with-mcps.md',
        'synthetic-biology-circuit-design-expert.md',
        'enterprise-blockchain-integration-expert.md'
    ]
    
    fixed_count = 0
    
    for filename in files_to_check:
        file_path = prompts_dir / filename
        if file_path.exists():
            if extract_and_fix_prompt(file_path):
                fixed_count += 1
        else:
            print(f"File not found: {file_path}")
    
    print(f"\nFixed {fixed_count} files")

if __name__ == "__main__":
    main()