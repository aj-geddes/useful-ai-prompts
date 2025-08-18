#!/usr/bin/env python3
"""
Validate YAML frontmatter in all prompt files
"""

import os
import yaml
import glob
from pathlib import Path

def validate_prompt_yaml():
    """Validate YAML frontmatter in all prompt files"""
    docs_dir = Path("docs/_prompts")
    if not docs_dir.exists():
        print("❌ docs/_prompts directory not found")
        return False
    
    prompt_files = list(docs_dir.glob("*.md"))
    print(f"📋 Found {len(prompt_files)} prompt files")
    
    valid_files = 0
    invalid_files = []
    
    for prompt_file in prompt_files:
        try:
            with open(prompt_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            if not content.startswith('---'):
                invalid_files.append((prompt_file.name, "No frontmatter found"))
                continue
            
            parts = content.split('---', 2)
            if len(parts) < 3:
                invalid_files.append((prompt_file.name, "Invalid frontmatter format"))
                continue
            
            frontmatter = parts[1]
            
            # Validate YAML
            try:
                parsed = yaml.safe_load(frontmatter)
                if not isinstance(parsed, dict):
                    invalid_files.append((prompt_file.name, "Frontmatter is not a dictionary"))
                    continue
                
                # Check required fields
                required_fields = ['category', 'title', 'description', 'layout']
                missing_fields = [field for field in required_fields if field not in parsed]
                if missing_fields:
                    invalid_files.append((prompt_file.name, f"Missing fields: {', '.join(missing_fields)}"))
                    continue
                
                valid_files += 1
                
            except yaml.YAMLError as e:
                invalid_files.append((prompt_file.name, f"YAML syntax error: {str(e)}"))
                continue
                
        except Exception as e:
            invalid_files.append((prompt_file.name, f"File read error: {str(e)}"))
    
    print(f"\n✅ Valid files: {valid_files}")
    print(f"❌ Invalid files: {len(invalid_files)}")
    
    if invalid_files:
        print("\n📋 Issues found:")
        for filename, error in invalid_files:
            print(f"  • {filename}: {error}")
        return False
    
    print("✅ All prompt files have valid YAML frontmatter!")
    return True

if __name__ == "__main__":
    success = validate_prompt_yaml()
    exit(0 if success else 1)