#!/usr/bin/env python3
"""
Convert existing prompt markdown files to Jekyll-compatible pages.

This script processes all markdown files in the prompts/ directory and converts them
to Jekyll front matter format in the docs/_prompts/ directory.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
import yaml


class PromptConverter:
    """Convert markdown prompts to Jekyll format."""
    
    # Category mapping from directory structure to Jekyll categories
    CATEGORY_MAPPING = {
        'analysis': 'analysis',
        'creation': 'creation', 
        'planning': 'planning',
        'problem-solving': 'problem-solving',
        'communication': 'communication',
        'learning-development': 'learning-development',
        'decision-making': 'decision-making',
        'creativity-innovation': 'creativity-innovation',
        'evaluation-assessment': 'evaluation-assessment',
        'optimization': 'optimization',
        'research': 'research-workflows',
        'management': 'management-leadership',
        'technical': 'technical-workflows',
        'customer': 'customer-focused',
        'business': 'management-leadership',  # Map business to management
        'administrative': 'management-leadership',  # Map administrative to management
        'academic': 'research-workflows',  # Map academic to research
        'creative': 'creativity-innovation',  # Map creative to creativity-innovation
        'development': 'technical-workflows',  # Map development to technical
        'engineering': 'technical-workflows',  # Map engineering to technical
        'finance': 'analysis',  # Map finance to analysis
        'healthcare': 'technical-workflows',  # Map healthcare to technical
        'human-resources': 'management-leadership',  # Map HR to management
        'operations': 'optimization',  # Map operations to optimization
        'project-management': 'management-leadership',  # Map PM to management
        'security': 'technical-workflows',  # Map security to technical
        'education': 'learning-development',  # Map education to learning
        'customer-service': 'customer-focused',  # Map customer service to customer
    }
    
    def __init__(self, source_dir: str = "prompts", target_dir: str = "docs/_prompts"):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.categories_dir = Path("docs/_categories")
        self.processed_categories = set()
        
    def parse_markdown_file(self, file_path: Path) -> Dict[str, Any]:
        """Parse a markdown file and extract metadata and content."""
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Initialize result
        result = {
            'title': '',
            'description': '',
            'category': '',
            'tags': [],
            'compatible_models': [],
            'use_cases': [],
            'version': '1.0.0',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'prompt': '',
            'examples': [],
            'tips': [],
            'related_prompts': [],
            'personas': [],
            'original_content': content
        }
        
        # Extract title (first # heading)
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if title_match:
            result['title'] = title_match.group(1).strip()
        
        # Extract metadata section
        metadata_match = re.search(r'## Metadata\s*\n(.*?)(?=\n##|\nYou are|\n```|$)', content, re.DOTALL)
        if metadata_match:
            metadata_text = metadata_match.group(1)
            result.update(self._parse_metadata_section(metadata_text))
        
        # Extract description
        desc_match = re.search(r'## Description\s*\n(.*?)(?=\n##|\nYou are|\n```|$)', content, re.DOTALL)
        if desc_match:
            result['description'] = desc_match.group(1).strip()
        
        # Extract prompt content
        prompt_content = self._extract_prompt_content(content)
        if prompt_content:
            result['prompt'] = prompt_content
        
        # Extract examples
        examples = self._extract_examples(content)
        if examples:
            result['examples'] = examples
        
        # Extract tips
        tips = self._extract_tips(content)
        if tips:
            result['tips'] = tips
        
        # Extract related prompts
        related = self._extract_related_prompts(content)
        if related:
            result['related_prompts'] = related
        
        # Determine category from file path
        result['category'] = self._determine_category(file_path)
        
        # Generate slug from filename
        result['slug'] = file_path.stem
        
        return result
    
    def _parse_metadata_section(self, metadata_text: str) -> Dict[str, Any]:
        """Parse the metadata section from markdown."""
        result = {}
        
        # Parse bullet points
        lines = metadata_text.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('- **') and '**:' in line:
                key_match = re.search(r'- \*\*(.+?)\*\*:\s*(.+)', line)
                if key_match:
                    key, value = key_match.groups()
                    key = key.lower().replace(' ', '_')
                    
                    if key == 'category':
                        result['category'] = value.strip()
                    elif key == 'tags':
                        result['tags'] = [tag.strip() for tag in value.split(',')]
                    elif key == 'created':
                        result['date'] = value.strip()
                    elif key == 'version':
                        result['version'] = value.strip()
                    elif key == 'use_cases':
                        result['use_cases'] = [case.strip() for case in value.split(',')]
                    elif key == 'compatible_models':
                        result['compatible_models'] = [model.strip() for model in value.split(',')]
                    elif key == 'personas':
                        result['personas'] = [persona.strip() for persona in value.split(',')]
        
        return result
    
    def _extract_prompt_content(self, content: str) -> str:
        """Extract the main prompt content from the markdown."""
        
        # Look for prompt in code blocks
        prompt_matches = re.findall(r'```(?:\w+)?\s*\n(.*?)\n```', content, re.DOTALL)
        
        # Find the largest code block (likely the main prompt)
        if prompt_matches:
            largest_prompt = max(prompt_matches, key=len)
            return largest_prompt.strip()
        
        # Fallback: look for content after "## Prompt" heading
        prompt_match = re.search(r'## Prompt\s*\n(.*?)(?=\n##|$)', content, re.DOTALL)
        if prompt_match:
            prompt_text = prompt_match.group(1).strip()
            # Remove code block markers if present
            prompt_text = re.sub(r'^```.*?\n', '', prompt_text)
            prompt_text = re.sub(r'\n```$', '', prompt_text)
            return prompt_text.strip()
        
        return ''
    
    def _extract_examples(self, content: str) -> List[Dict[str, str]]:
        """Extract examples from the markdown content."""
        examples = []
        
        # Look for example sections
        example_section_match = re.search(r'## Example Usage.*?\n(.*?)(?=\n##|$)', content, re.DOTALL)
        if not example_section_match:
            example_section_match = re.search(r'## Examples.*?\n(.*?)(?=\n##|$)', content, re.DOTALL)
        
        if example_section_match:
            example_text = example_section_match.group(1)
            
            # Split by example patterns
            example_parts = re.split(r'\*\*(?:User Input|Assistant Output|Example \d+).*?\*\*', example_text)
            
            current_example = {}
            for i, part in enumerate(example_parts):
                if i == 0:  # Skip first empty part
                    continue
                
                part = part.strip()
                if not part:
                    continue
                
                # Check if this looks like input or output
                if '```' in part:
                    code_match = re.search(r'```.*?\n(.*?)\n```', part, re.DOTALL)
                    if code_match:
                        code_content = code_match.group(1).strip()
                        
                        # Determine if this is input or output based on context
                        if i % 2 == 1:  # Odd index likely input
                            current_example['input'] = code_content
                        else:  # Even index likely output
                            current_example['output'] = code_content
                            # Complete example, add to list
                            if 'input' in current_example:
                                examples.append({
                                    'title': f'Example {len(examples) + 1}',
                                    'input': current_example.get('input', ''),
                                    'output': current_example.get('output', '')
                                })
                            current_example = {}
        
        return examples
    
    def _extract_tips(self, content: str) -> List[str]:
        """Extract tips from the markdown content."""
        tips = []
        
        # Look for tips sections
        tips_patterns = [
            r'## Tips.*?\n(.*?)(?=\n##|$)',
            r'## Usage.*?\n(.*?)(?=\n##|$)',
            r'## Instructions.*?\n(.*?)(?=\n##|$)'
        ]
        
        for pattern in tips_patterns:
            tips_match = re.search(pattern, content, re.DOTALL)
            if tips_match:
                tips_text = tips_match.group(1)
                
                # Extract bullet points
                bullet_points = re.findall(r'^[-*]\s+(.+)$', tips_text, re.MULTILINE)
                tips.extend(bullet_points)
                
                # Extract numbered points
                numbered_points = re.findall(r'^\d+\.\s+(.+)$', tips_text, re.MULTILINE)
                tips.extend(numbered_points)
                
                break
        
        return tips
    
    def _extract_related_prompts(self, content: str) -> List[str]:
        """Extract related prompts from the markdown content."""
        related = []
        
        # Look for related prompts section
        related_match = re.search(r'## Related Prompts.*?\n(.*?)(?=\n##|$)', content, re.DOTALL)
        if related_match:
            related_text = related_match.group(1)
            
            # Extract markdown links
            links = re.findall(r'\[([^\]]+)\]\([^)]+/([^/)]+)\.md\)', related_text)
            for title, slug in links:
                related.append(slug)
        
        return related
    
    def _determine_category(self, file_path: Path) -> str:
        """Determine the Jekyll category from the file path."""
        
        # Get the parent directories
        parts = file_path.parts
        
        # Find the first directory after 'prompts'
        if 'prompts' in parts:
            prompts_index = parts.index('prompts')
            if prompts_index + 1 < len(parts):
                category_dir = parts[prompts_index + 1]
                return self.CATEGORY_MAPPING.get(category_dir, category_dir)
        
        return 'miscellaneous'
    
    def create_jekyll_file(self, prompt_data: Dict[str, Any]) -> None:
        """Create a Jekyll-compatible markdown file."""
        
        # Create the target directory if it doesn't exist
        self.target_dir.mkdir(parents=True, exist_ok=True)
        
        # Create the Jekyll front matter
        front_matter = {
            'layout': 'prompt',
            'title': prompt_data['title'],
            'description': prompt_data['description'],
            'category': prompt_data['category'],
            'tags': prompt_data['tags'],
            'date': prompt_data['date'],
            'version': prompt_data['version'],
            'slug': prompt_data['slug']
        }
        
        # Add optional fields if they exist
        if prompt_data.get('compatible_models'):
            front_matter['compatible_models'] = prompt_data['compatible_models']
        if prompt_data.get('use_cases'):
            front_matter['use_cases'] = prompt_data['use_cases']
        if prompt_data.get('personas'):
            front_matter['personas'] = prompt_data['personas']
        if prompt_data.get('examples'):
            front_matter['examples'] = prompt_data['examples']
        if prompt_data.get('tips'):
            front_matter['tips'] = prompt_data['tips']
        if prompt_data.get('related_prompts'):
            front_matter['related_prompts'] = prompt_data['related_prompts']
        
        # Add the prompt content
        front_matter['prompt'] = prompt_data['prompt']
        
        # Create the Jekyll file content
        jekyll_content = "---\n"
        jekyll_content += yaml.dump(front_matter, default_flow_style=False, allow_unicode=True, width=float('inf'))
        jekyll_content += "---\n"
        
        # Write to file
        output_file = self.target_dir / f"{prompt_data['slug']}.md"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(jekyll_content)
        
        print(f"Created: {output_file}")
        
        # Track category for creating category pages
        self.processed_categories.add(prompt_data['category'])
    
    def create_category_pages(self) -> None:
        """Create category pages for Jekyll."""
        
        self.categories_dir.mkdir(parents=True, exist_ok=True)
        
        category_descriptions = {
            'analysis': 'Analytical and research-focused prompts for data analysis, competitive analysis, and strategic evaluation.',
            'creation': 'Content creation prompts for writing, documentation, design, and creative output generation.',
            'planning': 'Strategic planning prompts for project management, roadmaps, and organizational planning.',
            'problem-solving': 'Problem-solving methodologies, troubleshooting guides, and solution development frameworks.',
            'communication': 'Communication enhancement prompts for presentations, meetings, and stakeholder engagement.',
            'learning-development': 'Educational content, training materials, and skill development frameworks.',
            'decision-making': 'Decision support frameworks, evaluation criteria, and choice optimization methods.',
            'creativity-innovation': 'Innovation processes, creative thinking exercises, and idea generation techniques.',
            'evaluation-assessment': 'Performance evaluation, assessment frameworks, and quality measurement tools.',
            'optimization': 'Process improvement, efficiency optimization, and performance enhancement strategies.',
            'research-workflows': 'Research methodologies, investigation frameworks, and knowledge discovery processes.',
            'management-leadership': 'Leadership development, team management, and organizational effectiveness tools.',
            'technical-workflows': 'Technical implementation guides, development workflows, and engineering processes.',
            'customer-focused': 'Customer experience optimization, service delivery, and client relationship management.'
        }
        
        for category in self.processed_categories:
            category_file = self.categories_dir / f"{category}.md"
            
            category_content = f"""---
layout: category
title: {category.replace('-', ' ').title()}
category: {category}
description: {category_descriptions.get(category, f'Prompts in the {category} category.')}
---
"""
            
            with open(category_file, 'w', encoding='utf-8') as f:
                f.write(category_content)
            
            print(f"Created category: {category_file}")
    
    def convert_all_prompts(self) -> None:
        """Convert all prompt files from source to target directory."""
        
        print(f"Converting prompts from {self.source_dir} to {self.target_dir}")
        print(f"Looking for .md files...")
        
        converted_count = 0
        skipped_count = 0
        
        # Find all markdown files in the prompts directory
        for md_file in self.source_dir.rglob("*.md"):
            # Skip README files and other non-prompt files
            if md_file.name.lower() in ['readme.md', 'index.md']:
                print(f"Skipping: {md_file}")
                skipped_count += 1
                continue
            
            try:
                print(f"Processing: {md_file}")
                
                # Parse the markdown file
                prompt_data = self.parse_markdown_file(md_file)
                
                # Skip if no title or prompt content
                if not prompt_data['title'] or not prompt_data['prompt']:
                    print(f"Skipping {md_file}: Missing title or prompt content")
                    skipped_count += 1
                    continue
                
                # Create Jekyll file
                self.create_jekyll_file(prompt_data)
                converted_count += 1
                
            except Exception as e:
                print(f"Error processing {md_file}: {e}")
                skipped_count += 1
        
        # Create category pages
        print("\nCreating category pages...")
        self.create_category_pages()
        
        print(f"\nConversion complete!")
        print(f"Converted: {converted_count} prompts")
        print(f"Skipped: {skipped_count} files")
        print(f"Categories created: {len(self.processed_categories)}")


def main():
    """Main execution function."""
    converter = PromptConverter()
    converter.convert_all_prompts()


if __name__ == "__main__":
    main()