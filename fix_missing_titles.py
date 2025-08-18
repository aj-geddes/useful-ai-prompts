#!/usr/bin/env python3
"""
Add missing title fields to prompt files
"""

import os
import yaml
import re
from pathlib import Path

def generate_title_from_slug(slug):
    """Generate a proper title from a slug"""
    # Remove .md extension if present
    if slug.endswith('.md'):
        slug = slug[:-3]
    
    # Replace hyphens with spaces and capitalize each word
    title = slug.replace('-', ' ').title()
    
    # Handle common abbreviations and proper names
    replacements = {
        'Api': 'API',
        'Ai': 'AI',
        'Iot': 'IoT',
        'Crispr': 'CRISPR',
        'Rna': 'RNA',
        'Roi': 'ROI',
        'Kpi': 'KPI',
        'Seo': 'SEO',
        'Ui': 'UI',
        'Ux': 'UX',
        'Hr': 'HR',
        'It': 'IT',
        'Voc': 'VoC',
        'Crm': 'CRM'
    }
    
    for old, new in replacements.items():
        title = title.replace(old, new)
    
    return title

def fix_missing_titles():
    """Add missing title fields to prompt files"""
    docs_dir = Path("docs/_prompts")
    if not docs_dir.exists():
        print("❌ docs/_prompts directory not found")
        return False
    
    missing_title_files = [
        'customer-success-planning-expert.md',
        'customer-feedback-analysis-expert.md',
        'onboarding-experience-expert.md',
        'loyalty-program-design-expert.md',
        'customer-segmentation-expert.md',
        'personalization-framework-expert.md',
        'customer-support-process-expert.md',
        'retention-strategy-expert.md',
        'customer-satisfaction-measurement-expert.md',
        'customer-win-back-strategy-expert.md',
        'customer-journey-mapping-expert.md',
        'voice-of-customer-analysis-expert.md',
        'fresh-repo-readme.md',
        'prioritization-frameworks-expert.md',
        'support-escalation-process-expert.md',
        'stakeholder-impact-analysis-expert.md'
    ]
    
    fixed_files = 0
    
    for filename in missing_title_files:
        prompt_file = docs_dir / filename
        if not prompt_file.exists():
            print(f"❌ {filename}: File not found")
            continue
        
        try:
            with open(prompt_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            if not content.startswith('---'):
                print(f"❌ {filename}: No frontmatter found")
                continue
            
            parts = content.split('---', 2)
            if len(parts) < 3:
                print(f"❌ {filename}: Invalid frontmatter format")
                continue
            
            frontmatter_raw = parts[1]
            body = parts[2]
            
            # Parse frontmatter
            frontmatter = yaml.safe_load(frontmatter_raw)
            if not isinstance(frontmatter, dict):
                print(f"❌ {filename}: Invalid frontmatter")
                continue
            
            # Add title if missing
            if 'title' not in frontmatter:
                # Generate title from filename
                title = generate_title_from_slug(filename[:-3])  # Remove .md
                frontmatter['title'] = title
                
                # Regenerate YAML
                new_frontmatter = yaml.dump(frontmatter, 
                                          default_flow_style=False, 
                                          allow_unicode=True,
                                          width=1000)
                
                # Handle prompt field with literal block style
                if 'prompt' in frontmatter and isinstance(frontmatter['prompt'], str):
                    lines = new_frontmatter.split('\n')
                    new_lines = []
                    
                    for line in lines:
                        if line.startswith('prompt: '):
                            # Convert to literal block style
                            new_lines.append('prompt: |')
                            prompt_content = frontmatter['prompt']
                            for prompt_line in prompt_content.split('\n'):
                                new_lines.append('  ' + prompt_line)
                        elif not line.startswith('  ') or not any(prev_line.startswith('prompt: ') for prev_line in new_lines[-10:]):
                            new_lines.append(line)
                    
                    new_frontmatter = '\n'.join(new_lines)
                
                # Write back
                new_content = f"---\n{new_frontmatter}---{body}"
                
                with open(prompt_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"✅ {filename}: Added title '{title}'")
                fixed_files += 1
            else:
                print(f"ℹ️  {filename}: Title already exists")
                
        except Exception as e:
            print(f"❌ {filename}: Error - {str(e)}")
    
    print(f"\n✅ Fixed {fixed_files} files with missing titles")
    return True

if __name__ == "__main__":
    success = fix_missing_titles()
    exit(0 if success else 1)