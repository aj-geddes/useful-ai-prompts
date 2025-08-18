#!/usr/bin/env python3
"""
Fix YAML frontmatter issues in prompt files
"""

import os
import yaml
import glob
import re
from pathlib import Path

def fix_prompt_yaml():
    """Fix YAML frontmatter issues in all prompt files"""
    docs_dir = Path("docs/_prompts")
    if not docs_dir.exists():
        print("❌ docs/_prompts directory not found")
        return False
    
    prompt_files = list(docs_dir.glob("*.md"))
    print(f"📋 Found {len(prompt_files)} prompt files")
    
    fixed_files = 0
    
    for prompt_file in prompt_files:
        try:
            with open(prompt_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter and body
            if not content.startswith('---'):
                print(f"❌ {prompt_file.name}: No frontmatter found")
                continue
            
            parts = content.split('---', 2)
            if len(parts) < 3:
                print(f"❌ {prompt_file.name}: Invalid frontmatter format")
                continue
            
            frontmatter_raw = parts[1]
            body = parts[2]
            
            try:
                # Parse existing frontmatter
                frontmatter = yaml.safe_load(frontmatter_raw)
                if not isinstance(frontmatter, dict):
                    print(f"❌ {prompt_file.name}: Frontmatter is not a dictionary")
                    continue
                
                # Fix missing layout field
                if 'layout' not in frontmatter:
                    frontmatter['layout'] = 'prompt'
                    print(f"✅ {prompt_file.name}: Added missing 'layout' field")
                    fixed_files += 1
                
                # Fix prompt field YAML issues
                if 'prompt' in frontmatter:
                    prompt_content = frontmatter['prompt']
                    if isinstance(prompt_content, str):
                        # Use YAML literal block style for multi-line prompts
                        if '\n' in prompt_content or len(prompt_content) > 200:
                            # Store as literal block
                            frontmatter['prompt'] = prompt_content
                
                # Regenerate YAML with proper formatting
                new_frontmatter = yaml.dump(frontmatter, 
                                          default_flow_style=False, 
                                          allow_unicode=True,
                                          width=1000,
                                          default_style='|' if 'prompt' in frontmatter else None)
                
                # Special handling for prompt field - use literal block
                if 'prompt' in frontmatter and isinstance(frontmatter['prompt'], str):
                    lines = new_frontmatter.split('\n')
                    new_lines = []
                    in_prompt = False
                    
                    for line in lines:
                        if line.startswith('prompt: '):
                            # Convert to literal block style
                            new_lines.append('prompt: |')
                            prompt_content = frontmatter['prompt']
                            for prompt_line in prompt_content.split('\n'):
                                new_lines.append('  ' + prompt_line)
                            in_prompt = True
                        elif in_prompt and (line.startswith(' ') or line == ''):
                            # Skip old prompt content lines
                            continue
                        else:
                            in_prompt = False
                            new_lines.append(line)
                    
                    new_frontmatter = '\n'.join(new_lines)
                
                # Write back the corrected file
                new_content = f"---\n{new_frontmatter}---{body}"
                
                with open(prompt_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
            except yaml.YAMLError as e:
                print(f"❌ {prompt_file.name}: YAML syntax error - {str(e)}")
                # Try to fix basic YAML issues
                try:
                    # Fix the quoted scalar issue
                    fixed_frontmatter = re.sub(r"prompt: '([^']*)'([^']*)'", r'prompt: |\n  \1\2', frontmatter_raw)
                    
                    # Write with literal block style for prompt
                    lines = fixed_frontmatter.split('\n')
                    for i, line in enumerate(lines):
                        if line.startswith('prompt: '):
                            prompt_text = line[8:]  # Remove 'prompt: '
                            if prompt_text.startswith("'") and prompt_text.endswith("'"):
                                prompt_text = prompt_text[1:-1]  # Remove quotes
                            
                            # Add missing layout if needed
                            if 'layout:' not in fixed_frontmatter:
                                lines.insert(i, 'layout: prompt')
                            
                            lines[i] = 'prompt: |'
                            lines.insert(i+1, f'  {prompt_text}')
                            break
                    
                    fixed_frontmatter = '\n'.join(lines)
                    new_content = f"---\n{fixed_frontmatter}\n---{body}"
                    
                    with open(prompt_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"✅ {prompt_file.name}: Fixed YAML syntax error")
                    fixed_files += 1
                    
                except Exception as fix_error:
                    print(f"❌ {prompt_file.name}: Could not auto-fix - {str(fix_error)}")
                
        except Exception as e:
            print(f"❌ {prompt_file.name}: File processing error - {str(e)}")
    
    print(f"\n✅ Fixed {fixed_files} files")
    return True

if __name__ == "__main__":
    success = fix_prompt_yaml()
    exit(0 if success else 1)