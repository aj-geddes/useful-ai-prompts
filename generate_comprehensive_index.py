#!/usr/bin/env python3
"""
Generate comprehensive PROMPT-INDEX.json from all source prompts in /prompts directory.
This script processes all 407+ prompts and creates a complete index.
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

def extract_title_from_content(content: str) -> str:
    """Extract title from markdown content."""
    # Look for first H1 heading
    h1_match = re.search(r'^# (.+)', content, re.MULTILINE)
    if h1_match:
        return h1_match.group(1).strip()
    
    # Look for front matter title
    if content.startswith('---'):
        front_matter_end = content.find('\n---\n', 4)
        if front_matter_end != -1:
            front_matter = content[4:front_matter_end]
            title_match = re.search(r'^title:\s*(.+)', front_matter, re.MULTILINE)
            if title_match:
                return title_match.group(1).strip().strip('"\'')
    
    return ""

def extract_description_from_content(content: str) -> str:
    """Extract description from markdown content."""
    # Look for front matter description
    if content.startswith('---'):
        front_matter_end = content.find('\n---\n', 4)
        if front_matter_end != -1:
            front_matter = content[4:front_matter_end]
            desc_match = re.search(r'^description:\s*(.+)', front_matter, re.MULTILINE)
            if desc_match:
                return desc_match.group(1).strip().strip('"\'')
    
    # Look for first paragraph after title
    lines = content.split('\n')
    in_content = False
    for line in lines:
        line = line.strip()
        if line.startswith('# ') and not in_content:
            in_content = True
            continue
        if in_content and line and not line.startswith('#') and not line.startswith('---'):
            # Clean up the line
            if line.startswith('I\'ll help you') or line.startswith('I will help you'):
                return line[:200] + "..." if len(line) > 200 else line
            elif len(line) > 50:  # Substantial description
                return line[:200] + "..." if len(line) > 200 else line
    
    return ""

def categorize_prompt_by_path(file_path: Path) -> str:
    """Determine category based on file path structure."""
    parts = file_path.parts
    prompt_idx = -1
    
    # Find 'prompts' in the path
    for i, part in enumerate(parts):
        if part == 'prompts':
            prompt_idx = i
            break
    
    if prompt_idx == -1 or prompt_idx + 1 >= len(parts):
        return "uncategorized"
    
    primary_category = parts[prompt_idx + 1]
    
    # Map directory names to standardized categories
    category_mapping = {
        'academic': 'research-workflows',
        'administrative': 'management-leadership',
        'analysis': 'analysis',
        'biotechnology': 'biotechnology',
        'blockchain': 'blockchain',
        'business': 'business-workflows',
        'communication': 'communication',
        'creation': 'creation',
        'creative': 'creativity-innovation',
        'creativity-innovation': 'creativity-innovation',
        'customer-focused': 'customer-focused',
        'customer-service': 'customer-focused',
        'decision-making': 'decision-making',
        'development': 'technical-workflows',
        'education': 'learning-development',
        'engineering': 'technical-workflows',
        'evaluation-assessment': 'evaluation-assessment',
        'finance': 'business-workflows',
        'government': 'government-digital',
        'healthcare': 'healthcare-digital',
        'healthcare-digital': 'healthcare-digital',
        'human-resources': 'management-leadership',
        'learning-development': 'learning-development',
        'management-leadership': 'management-leadership',
        'operations': 'business-workflows',
        'optimization': 'optimization',
        'planning': 'planning',
        'problem-solving': 'problem-solving',
        'project-management': 'planning',
        'quantum-computing': 'quantum-computing',
        'renewable-energy': 'renewable-energy',
        'research': 'research-workflows',
        'research-workflows': 'research-workflows',
        'security': 'technical-workflows',
        'space-economy': 'space-economy',
        'supply-chain': 'supply-chain',
        'technical': 'technical-workflows',
        'technical-workflows': 'technical-workflows'
    }
    
    return category_mapping.get(primary_category, primary_category)

def generate_slug_from_filename(filename: str) -> str:
    """Generate slug from filename."""
    return filename.replace('.md', '').replace('_', '-')

def extract_tags_from_path_and_content(file_path: Path, content: str) -> List[str]:
    """Extract relevant tags from file path and content analysis."""
    tags = []
    parts = file_path.parts
    
    # Add subcategory as tag if it exists
    if 'prompts' in parts:
        prompt_idx = parts.index('prompts')
        if prompt_idx + 2 < len(parts):
            subcategory = parts[prompt_idx + 2]
            if subcategory and subcategory != file_path.stem:
                tags.append(subcategory.replace('-', ' ').title())
    
    # Add technology/domain tags based on content
    content_lower = content.lower()
    
    tech_keywords = {
        'ai': ['artificial intelligence', 'machine learning', 'ai', 'ml'],
        'blockchain': ['blockchain', 'cryptocurrency', 'smart contract', 'defi'],
        'cloud': ['cloud', 'aws', 'azure', 'gcp'],
        'data': ['data analysis', 'analytics', 'data science'],
        'project-management': ['project management', 'agile', 'scrum'],
        'strategy': ['strategic', 'strategy', 'roadmap'],
        'security': ['security', 'cybersecurity', 'compliance'],
        'api': ['api', 'rest', 'graphql'],
        'devops': ['devops', 'ci/cd', 'deployment']
    }
    
    for tag, keywords in tech_keywords.items():
        if any(keyword in content_lower for keyword in keywords):
            tags.append(tag.replace('-', ' ').title())
    
    return list(set(tags))  # Remove duplicates

def validate_prompt_format(content: str) -> bool:
    """Validate that prompt follows the strategic-roadmap-generator.md format."""
    content_lower = content.lower()
    
    # Check for conversational/helpful structure (more flexible)
    conversational_indicators = [
        'i\'ll help', 'i will help', 'let me help', 'let me understand',
        'let me guide', 'i\'ll guide', 'i will guide', 'i\'ll assist',
        'i will assist', 'let me assist'
    ]
    
    has_conversational = any(indicator in content_lower for indicator in conversational_indicators)
    
    # Check minimum length (approximately 200+ lines for more inclusive validation)
    line_count = len(content.split('\n'))
    has_sufficient_length = line_count >= 200
    
    # Check for question structure (more patterns)
    question_patterns = [
        r'\d+\.\s+[A-Z].*\?',  # 1. Question?
        r'\*\*\d+\.\s+.*\?\*\*',  # **1. Question?**
        r'###\s+\d+\.\s+.*\?',  # ### 1. Question?
        r'\d+\.\s+What.*\?',  # 1. What...?
        r'\d+\.\s+How.*\?',   # 1. How...?
        r'\d+\.\s+Which.*\?', # 1. Which...?
        r'\d+\.\s+Who.*\?',   # 1. Who...?
        r'\d+\.\s+Where.*\?', # 1. Where...?
        r'\d+\.\s+When.*\?'   # 1. When...?
    ]
    
    question_count = 0
    for pattern in question_patterns:
        question_count += len(re.findall(pattern, content, re.IGNORECASE))
    
    # Check for structured sections (metadata, description, etc.)
    has_structure = any(section in content_lower for section in [
        '## metadata', '## description', '## prompt', '# ', 
        'category:', 'tags:', 'description:'
    ])
    
    # More lenient validation - should have at least 4 questions and some structure
    has_questions = question_count >= 4
    
    # Return true if it has conversational tone OR good structure with questions
    return (has_conversational or has_structure) and has_questions and has_sufficient_length

def process_prompt_file(file_path: Path) -> Optional[Dict]:
    """Process a single prompt file and extract metadata."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip README files
        if file_path.name.lower() == 'readme.md':
            return None
        
        # Extract metadata
        title = extract_title_from_content(content)
        if not title:
            title = file_path.stem.replace('-', ' ').replace('_', ' ').title()
        
        description = extract_description_from_content(content)
        if not description:
            description = f"Professional prompt for {title.lower()} with expert guidance and structured frameworks."
        
        category = categorize_prompt_by_path(file_path)
        slug = generate_slug_from_filename(file_path.name)
        tags = extract_tags_from_path_and_content(file_path, content)
        
        # Validate format
        is_valid_format = validate_prompt_format(content)
        
        # Get relative path from project root
        try:
            relative_path = str(file_path.relative_to(Path.cwd()))
        except ValueError:
            # Handle cases where file is not relative to cwd
            relative_path = str(file_path)
        
        return {
            'title': title,
            'description': description,
            'category': category,
            'tags': tags,
            'slug': slug,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'version': '1.0.0',
            'compatible_models': ['claude-3', 'gpt-4', 'gemini'],
            'use_cases': [],
            'file_path': relative_path,
            'format_validated': is_valid_format,
            'line_count': len(content.split('\n')),
            'word_count': len(content.split())
        }
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def generate_comprehensive_index():
    """Generate comprehensive index from all source prompts."""
    prompts_dir = Path("prompts")
    index_file = Path("docs/PROMPT-INDEX.json")
    
    if not prompts_dir.exists():
        print(f"Prompts directory {prompts_dir} not found!")
        return
    
    print("Generating comprehensive PROMPT-INDEX.json from all source prompts...")
    
    # Collect all prompt files
    prompts = []
    total_files = 0
    processed_files = 0
    
    for file_path in prompts_dir.rglob("*.md"):
        total_files += 1
        metadata = process_prompt_file(file_path)
        if metadata:
            prompts.append(metadata)
            processed_files += 1
            if processed_files % 50 == 0:
                print(f"Processed {processed_files} prompts...")
    
    # Sort prompts by title
    prompts.sort(key=lambda x: x['title'])
    
    # Get unique categories
    categories = sorted(list(set(p['category'] for p in prompts)))
    
    # Calculate statistics
    format_compliant = sum(1 for p in prompts if p.get('format_validated', False))
    total_lines = sum(p.get('line_count', 0) for p in prompts)
    total_words = sum(p.get('word_count', 0) for p in prompts)
    
    # Create comprehensive index structure
    index_data = {
        'version': '2.0.0',
        'last_updated': datetime.now().isoformat(),
        'total_prompts': len(prompts),
        'total_files_scanned': total_files,
        'processed_files': processed_files,
        'format_compliant_prompts': format_compliant,
        'total_content_lines': total_lines,
        'total_content_words': total_words,
        'categories': categories,
        'category_counts': {cat: len([p for p in prompts if p['category'] == cat]) for cat in categories},
        'new_categories': [
            'biotechnology',
            'blockchain', 
            'government-digital',
            'healthcare-digital',
            'quantum-computing',
            'renewable-energy',
            'space-economy',
            'supply-chain'
        ],
        'statistics': {
            'avg_lines_per_prompt': total_lines // len(prompts) if prompts else 0,
            'avg_words_per_prompt': total_words // len(prompts) if prompts else 0,
            'format_compliance_rate': f"{(format_compliant / len(prompts)) * 100:.1f}%" if prompts else "0%"
        },
        'prompts': prompts
    }
    
    # Ensure docs directory exists
    index_file.parent.mkdir(exist_ok=True)
    
    # Write to file
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*50}")
    print(f"Comprehensive Index Generation Complete!")
    print(f"{'='*50}")
    print(f"Total prompts indexed: {len(prompts)}")
    print(f"Categories: {len(categories)}")
    compliance_pct = (format_compliant / len(prompts)) * 100 if prompts else 0
    print(f"Format compliant prompts: {format_compliant} ({compliance_pct:.1f}%)")
    print(f"Average lines per prompt: {total_lines // len(prompts) if prompts else 0}")
    print(f"Average words per prompt: {total_words // len(prompts) if prompts else 0}")
    print(f"\nNew categories added:")
    for cat in index_data['new_categories']:
        count = index_data['category_counts'].get(cat, 0)
        print(f"  - {cat}: {count} prompts")
    print(f"\nIndex saved to: {index_file}")
    print(f"{'='*50}")

if __name__ == "__main__":
    generate_comprehensive_index()