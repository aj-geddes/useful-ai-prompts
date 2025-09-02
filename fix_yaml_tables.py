#!/usr/bin/env python3
"""
Fix YAML front matter issues caused by markdown tables.
"""

import os
import re
from pathlib import Path

# Files that need fixing based on error output
BROKEN_FILES = [
    'prioritization-frameworks-expert.md',
    'retention-strategy-expert.md',
    'customer-segmentation-expert.md',
    'customer-feedback-analysis-expert.md',
    'loyalty-program-design-expert.md',
    'customer-support-process-expert.md',
    'customer-win-back-strategy-expert.md',
    'retention-optimization-expert.md',
    'support-escalation-process-expert.md',
    'personalization-framework-expert.md',
    'stakeholder-impact-analysis-expert.md',
    'fresh-repo-readme.md',
    'customer-satisfaction-measurement-expert.md',
    'customer-journey-mapping-expert.md',
    'voice-of-customer-analysis-expert.md',
    'onboarding-experience-expert.md'
]

def fix_yaml_file(file_path):
    """Fix YAML issues in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file starts with YAML front matter
        if not content.startswith('---\n'):
            return False, "No YAML front matter found"
        
        # Find the end of YAML front matter
        end_marker_pos = content.find('\n---\n', 4)
        if end_marker_pos == -1:
            return False, "No end marker found"
        
        yaml_section = content[4:end_marker_pos]
        body = content[end_marker_pos + 5:]
        
        # Common issues to fix:
        
        # 1. Remove markdown tables from YAML section
        lines = yaml_section.split('\n')
        fixed_lines = []
        in_prompt = False
        for line in lines:
            if line.startswith('prompt:'):
                in_prompt = True
                fixed_lines.append(line)
            elif in_prompt and line.startswith('  ') and '|' in line:
                # This is likely a table in the prompt, keep it
                fixed_lines.append(line)
            elif in_prompt and not line.startswith(' ') and ':' in line:
                # End of prompt section
                in_prompt = False
                fixed_lines.append(line)
            elif '|---' in line or '----' in line:
                # Skip table separator lines
                continue
            elif line.strip().startswith('|') and line.strip().endswith('|'):
                # Skip table rows outside prompt
                continue
            else:
                fixed_lines.append(line)
        
        # 2. Fix common YAML syntax issues
        fixed_yaml = '\n'.join(fixed_lines)
        
        # 3. Fix percent signs that aren't quoted
        fixed_yaml = re.sub(r'([^\'"])(%\s+[A-Za-z])', r'\1"\2"', fixed_yaml)
        
        # Write back
        new_content = f"---\n{fixed_yaml}\n---\n{body}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, "Fixed YAML issues"
        
    except Exception as e:
        return False, f"Error: {e}"

def main():
    """Fix YAML issues in problematic files."""
    prompts_dir = Path('docs/_prompts')
    
    if not prompts_dir.exists():
        print("Error: docs/_prompts directory not found")
        return
    
    fixed_count = 0
    error_count = 0
    
    for filename in BROKEN_FILES:
        file_path = prompts_dir / filename
        if file_path.exists():
            success, message = fix_yaml_file(file_path)
            if success:
                print(f"✅ {filename}: {message}")
                fixed_count += 1
            else:
                print(f"❌ {filename}: {message}")
                error_count += 1
        else:
            print(f"⚠️  {filename}: File not found")
    
    print(f"\nSummary:")
    print(f"  Fixed: {fixed_count}")
    print(f"  Errors: {error_count}")

if __name__ == "__main__":
    main()