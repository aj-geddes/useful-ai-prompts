#!/usr/bin/env python3
"""
Validation script for Jekyll prompt conversion.

This script validates the converted Jekyll prompt files to ensure they have proper
structure, required fields, and valid YAML front matter.
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Set
import re


class JekyllValidator:
    """Validate Jekyll prompt files."""
    
    REQUIRED_FIELDS = {
        'layout', 'title', 'description', 'category', 'tags', 
        'date', 'version', 'slug', 'prompt'
    }
    
    VALID_LAYOUTS = {'prompt'}
    
    VALID_CATEGORIES = {
        'analysis', 'communication', 'creation', 'creativity-innovation',
        'customer-focused', 'decision-making', 'evaluation-assessment',
        'learning-development', 'management-leadership', 'optimization',
        'planning', 'problem-solving', 'research-workflows', 'technical-workflows'
    }
    
    def __init__(self, prompts_dir: str = "docs/_prompts", categories_dir: str = "docs/_categories"):
        self.prompts_dir = Path(prompts_dir)
        self.categories_dir = Path(categories_dir)
        self.errors = []
        self.warnings = []
        self.stats = {}
        
    def validate_front_matter(self, file_path: Path, content: str) -> Dict:
        """Validate YAML front matter in a Jekyll file."""
        
        # Extract front matter
        if not content.startswith('---\n'):
            self.errors.append(f"{file_path}: Missing YAML front matter")
            return {}
        
        try:
            # Find the end of front matter
            end_marker = content.find('\n---\n', 4)
            if end_marker == -1:
                self.errors.append(f"{file_path}: Malformed YAML front matter (missing end marker)")
                return {}
            
            front_matter_text = content[4:end_marker]
            front_matter = yaml.safe_load(front_matter_text)
            
            if not isinstance(front_matter, dict):
                self.errors.append(f"{file_path}: Front matter is not a dictionary")
                return {}
            
            return front_matter
            
        except yaml.YAMLError as e:
            self.errors.append(f"{file_path}: Invalid YAML in front matter: {e}")
            return {}
    
    def validate_prompt_file(self, file_path: Path) -> Dict:
        """Validate a single prompt file."""
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"{file_path}: Could not read file: {e}")
            return {}
        
        # Validate front matter
        front_matter = self.validate_front_matter(file_path, content)
        if not front_matter:
            return {}
        
        # Check required fields
        missing_fields = self.REQUIRED_FIELDS - set(front_matter.keys())
        if missing_fields:
            self.errors.append(f"{file_path}: Missing required fields: {missing_fields}")
        
        # Validate layout
        if front_matter.get('layout') not in self.VALID_LAYOUTS:
            self.errors.append(f"{file_path}: Invalid layout '{front_matter.get('layout')}', must be one of {self.VALID_LAYOUTS}")
        
        # Validate category
        if front_matter.get('category') not in self.VALID_CATEGORIES:
            self.errors.append(f"{file_path}: Invalid category '{front_matter.get('category')}', must be one of {self.VALID_CATEGORIES}")
        
        # Validate required string fields
        string_fields = ['title', 'description', 'prompt']
        for field in string_fields:
            if field in front_matter:
                if not isinstance(front_matter[field], str) or not front_matter[field].strip():
                    self.errors.append(f"{file_path}: Field '{field}' must be a non-empty string")
        
        # Validate list fields
        list_fields = ['tags', 'compatible_models', 'use_cases', 'examples', 'tips', 'related_prompts']
        for field in list_fields:
            if field in front_matter:
                if not isinstance(front_matter[field], list):
                    self.errors.append(f"{file_path}: Field '{field}' must be a list")
        
        # Validate slug matches filename
        expected_slug = file_path.stem
        if front_matter.get('slug') != expected_slug:
            self.errors.append(f"{file_path}: Slug '{front_matter.get('slug')}' doesn't match filename '{expected_slug}'")
        
        # Validate date format
        if 'date' in front_matter:
            date_str = front_matter['date']
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(date_str)):
                self.warnings.append(f"{file_path}: Date format should be YYYY-MM-DD, got '{date_str}'")
        
        # Check for empty prompt
        if front_matter.get('prompt', '').strip() == '':
            self.errors.append(f"{file_path}: Prompt content is empty")
        
        return front_matter
    
    def validate_category_file(self, file_path: Path) -> Dict:
        """Validate a category file."""
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"{file_path}: Could not read file: {e}")
            return {}
        
        # Validate front matter
        front_matter = self.validate_front_matter(file_path, content)
        if not front_matter:
            return {}
        
        # Check required fields for categories
        required_category_fields = {'layout', 'title', 'category', 'description'}
        missing_fields = required_category_fields - set(front_matter.keys())
        if missing_fields:
            self.errors.append(f"{file_path}: Missing required category fields: {missing_fields}")
        
        # Validate layout
        if front_matter.get('layout') != 'category':
            self.errors.append(f"{file_path}: Category layout must be 'category', got '{front_matter.get('layout')}'")
        
        # Validate category matches filename
        expected_category = file_path.stem
        if front_matter.get('category') != expected_category:
            self.errors.append(f"{file_path}: Category '{front_matter.get('category')}' doesn't match filename '{expected_category}'")
        
        return front_matter
    
    def validate_all(self) -> None:
        """Validate all Jekyll files."""
        
        print("Validating Jekyll prompt conversion...")
        
        # Reset stats
        self.errors = []
        self.warnings = []
        self.stats = {
            'prompt_files': 0,
            'category_files': 0,
            'categories_used': set(),
            'tags_used': set(),
            'models_supported': set(),
        }
        
        # Validate prompt files
        if self.prompts_dir.exists():
            prompt_files = list(self.prompts_dir.glob('*.md'))
            self.stats['prompt_files'] = len(prompt_files)
            
            print(f"Validating {len(prompt_files)} prompt files...")
            
            for file_path in prompt_files:
                front_matter = self.validate_prompt_file(file_path)
                
                # Collect stats
                if front_matter:
                    if 'category' in front_matter:
                        self.stats['categories_used'].add(front_matter['category'])
                    if 'tags' in front_matter and isinstance(front_matter['tags'], list):
                        self.stats['tags_used'].update(front_matter['tags'])
                    if 'compatible_models' in front_matter and isinstance(front_matter['compatible_models'], list):
                        self.stats['models_supported'].update(front_matter['compatible_models'])
        
        else:
            self.errors.append(f"Prompts directory {self.prompts_dir} does not exist")
        
        # Validate category files  
        if self.categories_dir.exists():
            category_files = list(self.categories_dir.glob('*.md'))
            self.stats['category_files'] = len(category_files)
            
            print(f"Validating {len(category_files)} category files...")
            
            for file_path in category_files:
                self.validate_category_file(file_path)
        else:
            self.errors.append(f"Categories directory {self.categories_dir} does not exist")
        
        # Check category consistency
        defined_categories = set(f.stem for f in self.categories_dir.glob('*.md')) if self.categories_dir.exists() else set()
        used_categories = self.stats['categories_used']
        
        missing_category_files = used_categories - defined_categories
        if missing_category_files:
            self.errors.append(f"Missing category definition files: {missing_category_files}")
        
        unused_category_files = defined_categories - used_categories
        if unused_category_files:
            self.warnings.append(f"Unused category definition files: {unused_category_files}")
    
    def print_report(self) -> None:
        """Print validation report."""
        
        print("\n" + "="*60)
        print("JEKYLL VALIDATION REPORT")
        print("="*60)
        
        # Statistics
        print(f"\nSTATISTICS:")
        print(f"  Prompt files: {self.stats['prompt_files']}")
        print(f"  Category files: {self.stats['category_files']}")
        print(f"  Categories used: {len(self.stats['categories_used'])}")
        print(f"  Unique tags: {len(self.stats['tags_used'])}")
        print(f"  Models supported: {len(self.stats['models_supported'])}")
        
        # Categories
        print(f"\nCATEGORIES USED:")
        for category in sorted(self.stats['categories_used']):
            print(f"  - {category}")
        
        # Models  
        print(f"\nSUPPORTED MODELS:")
        for model in sorted(self.stats['models_supported']):
            print(f"  - {model}")
        
        # Errors
        if self.errors:
            print(f"\nERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  ❌ {error}")
        else:
            print(f"\n✅ NO ERRORS FOUND!")
        
        # Warnings
        if self.warnings:
            print(f"\nWARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  ⚠️  {warning}")
        else:
            print(f"\n✅ NO WARNINGS!")
        
        # Summary
        print(f"\nSUMMARY:")
        if not self.errors:
            print("✅ All Jekyll files are valid and ready for site generation!")
        else:
            print(f"❌ Found {len(self.errors)} errors that need to be fixed.")
        
        if self.warnings:
            print(f"⚠️  Found {len(self.warnings)} warnings to consider.")
    
    def check_related_prompts(self) -> None:
        """Check if related prompt links are valid."""
        
        print("\nValidating related prompt links...")
        
        # Get all slugs
        if not self.prompts_dir.exists():
            return
            
        all_slugs = set(f.stem for f in self.prompts_dir.glob('*.md'))
        
        # Check each prompt's related_prompts
        for file_path in self.prompts_dir.glob('*.md'):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                front_matter = self.validate_front_matter(file_path, content)
                if 'related_prompts' in front_matter:
                    related = front_matter['related_prompts']
                    if isinstance(related, list):
                        for slug in related:
                            if slug not in all_slugs:
                                self.warnings.append(f"{file_path}: Related prompt '{slug}' not found")
            except Exception as e:
                self.errors.append(f"{file_path}: Error checking related prompts: {e}")


def main():
    """Main validation function."""
    validator = JekyllValidator()
    validator.validate_all()
    validator.check_related_prompts()
    validator.print_report()
    
    # Return exit code based on errors
    return 1 if validator.errors else 0


if __name__ == "__main__":
    exit(main())