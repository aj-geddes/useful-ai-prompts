#!/usr/bin/env python3
"""
Script to convert YAML frontmatter to markdown metadata format
"""
import os
import re
import yaml
from pathlib import Path

def convert_yaml_to_metadata(file_path):
    """Convert a file with YAML frontmatter to markdown metadata format"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file starts with YAML frontmatter
    if not content.startswith('---\n'):
        return False, "No YAML frontmatter found"
    
    # Split content at first occurrence of ---\n after the opening
    parts = content.split('---\n', 2)
    if len(parts) < 3:
        return False, "Invalid YAML frontmatter format"
    
    yaml_content = parts[1]
    markdown_content = parts[2]
    
    # Parse YAML
    try:
        yaml_data = yaml.safe_load(yaml_content)
    except yaml.YAMLError as e:
        return False, f"YAML parsing error: {e}"
    
    # Extract title from YAML or markdown
    title = yaml_data.get('title', '')
    if not title:
        # Try to find title from first heading in markdown
        title_match = re.search(r'^# (.+)$', markdown_content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
    
    # Build metadata section
    metadata_lines = [
        f"# {title}",
        "",
        "## Metadata"
    ]
    
    # Map YAML fields to metadata
    if 'category' in yaml_data:
        category = yaml_data['category'].replace('-', ' ').title()
        metadata_lines.append(f"- **Category**: {category}")
    
    if 'tags' in yaml_data:
        if isinstance(yaml_data['tags'], list):
            tags = ', '.join(yaml_data['tags'])
        else:
            tags = yaml_data['tags']
        metadata_lines.append(f"- **Tags**: {tags}")
    
    if 'date' in yaml_data:
        date = str(yaml_data['date']).strip("'")
        metadata_lines.append(f"- **Created**: {date}")
    
    if 'version' in yaml_data:
        metadata_lines.append(f"- **Version**: {yaml_data['version']}")
    
    if 'use_cases' in yaml_data:
        if isinstance(yaml_data['use_cases'], list):
            use_cases = ', '.join(yaml_data['use_cases'])
        else:
            use_cases = yaml_data['use_cases']
        metadata_lines.append(f"- **Use Cases**: {use_cases}")
    
    if 'compatible_models' in yaml_data:
        models = []
        for model in yaml_data['compatible_models']:
            if model == 'claude-3.5-sonnet':
                models.append('Claude 3.5 Sonnet')
            elif model == 'gpt-4':
                models.append('GPT-4')
            elif model == 'gemini-pro':
                models.append('Gemini Pro')
            else:
                models.append(model)
        metadata_lines.append(f"- **Compatible Models**: {', '.join(models)}")
    
    # Add description
    if 'description' in yaml_data:
        metadata_lines.extend([
            "",
            "## Description",
            yaml_data['description']
        ])
    
    # Remove the original title if it exists at the start of markdown content
    if markdown_content.startswith(f"# {title}\n"):
        markdown_content = markdown_content[len(f"# {title}\n"):].lstrip()
    
    # Combine metadata and content
    new_content = '\n'.join(metadata_lines) + '\n\n' + markdown_content
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, "Converted successfully"

def main():
    """Convert all files with YAML frontmatter"""
    target_dirs = [
        'prompts/space-economy',
        'prompts/supply-chain', 
        'prompts/blockchain',
        'prompts/government',
        'prompts/healthcare-digital',
        'prompts/quantum-computing'
    ]
    
    for target_dir in target_dirs:
        dir_path = Path(target_dir)
        if not dir_path.exists():
            print(f"Directory {target_dir} not found")
            continue
            
        for md_file in dir_path.rglob('*.md'):
            success, message = convert_yaml_to_metadata(md_file)
            print(f"{md_file}: {message}")

if __name__ == '__main__':
    main()