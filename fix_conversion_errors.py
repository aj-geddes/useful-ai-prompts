#!/usr/bin/env python3
"""
Fix conversion errors by adding missing descriptions to Jekyll files.
"""

import yaml
from pathlib import Path
from typing import Dict

# Files with missing descriptions and their appropriate descriptions
DESCRIPTION_FIXES = {
    'bandit-security-analysis.md': 'A comprehensive security analysis tool that uses Bandit to identify security vulnerabilities in Python code and provides detailed remediation guidance.',
    'adr-record-generation.md': 'Generate comprehensive Architecture Decision Records (ADRs) to document key architectural decisions with context, consequences, and alternatives.',
    'adr-research-framework.md': 'A structured framework for researching and documenting architectural decisions with comprehensive analysis and decision rationale.',
    'teach-me-beginner.md': 'An interactive learning assistant designed for beginners, providing structured explanations with examples and hands-on exercises.',
    'fastmcp-server-patterns.md': 'Design patterns and best practices for creating efficient FastMCP servers with proper architecture and implementation guidance.',
    'claude-mcp-example.md': 'Practical examples and implementation guides for integrating Claude with MCP (Model Context Protocol) servers.',
    'fresh-repo-readme.md': 'Generate comprehensive README files for new repositories with proper documentation structure and essential project information.',
    'teach-me-journeyman.md': 'An intermediate-level learning assistant that provides in-depth technical explanations with practical applications and advanced concepts.',
    'teach-me-advanced.md': 'An advanced learning assistant focused on expert-level concepts, research insights, and complex technical implementations.',
    'memory-management-patterns.md': 'Best practices and design patterns for efficient memory management in software applications with performance optimization techniques.'
}

def fix_file_description(file_path: Path, new_description: str):
    """Fix a file by adding the missing description."""
    
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse the front matter
        if not content.startswith('---\n'):
            print(f"Skipping {file_path}: No YAML front matter found")
            return
        
        end_marker = content.find('\n---\n', 4)
        if end_marker == -1:
            print(f"Skipping {file_path}: Malformed YAML front matter")
            return
        
        front_matter_text = content[4:end_marker]
        remaining_content = content[end_marker + 5:]  # +5 for '\n---\n'
        
        # Parse YAML
        front_matter = yaml.safe_load(front_matter_text)
        
        # Update description
        if not front_matter.get('description', '').strip():
            front_matter['description'] = new_description
            print(f"Updated description for {file_path}")
        else:
            print(f"Skipping {file_path}: Description already exists")
            return
        
        # Write back to file
        new_content = "---\n"
        new_content += yaml.dump(front_matter, default_flow_style=False, allow_unicode=True, width=float('inf'))
        new_content += "---\n"
        new_content += remaining_content
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")

def main():
    """Fix all files with missing descriptions."""
    
    prompts_dir = Path("docs/_prompts")
    
    print("Fixing files with missing descriptions...")
    
    for filename, description in DESCRIPTION_FIXES.items():
        file_path = prompts_dir / filename
        if file_path.exists():
            fix_file_description(file_path, description)
        else:
            print(f"File not found: {file_path}")
    
    print("Done fixing description errors!")

if __name__ == "__main__":
    main()