#!/usr/bin/env python3
"""
Bulk Content Management Tools for AI Prompts Repository
Efficient tools for mass operations, migrations, and large-scale prompt management
"""

import os
import json
import csv
import yaml
import shutil
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
import re
import concurrent.futures
from collections import defaultdict
import time

@dataclass
class BulkOperation:
    """Represents a bulk operation with tracking"""
    operation_id: str
    operation_type: str
    target_count: int
    completed_count: int = 0
    failed_count: int = 0
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    errors: List[str] = None
    results: List[str] = None
    
    def __post_init__(self):
        if self.errors is None:
            self.errors = []
        if self.results is None:
            self.results = []

@dataclass
class PromptTemplate:
    """Template for bulk prompt generation"""
    category: str
    domain: str
    title_template: str
    primary_expert: str
    secondary_expert: str
    frameworks: List[str]
    specialized_sections: Dict[str, str] = None
    
    def __post_init__(self):
        if self.specialized_sections is None:
            self.specialized_sections = {}

class BulkContentManager:
    """Advanced bulk content management system"""
    
    def __init__(self, repo_root: str = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.prompts_dir = self.repo_root / "prompts"
        self.docs_dir = self.repo_root / "docs"
        self.jekyll_prompts_dir = self.docs_dir / "_prompts"
        self.backup_dir = self.repo_root / "backups"
        self.templates_dir = self.repo_root / "templates"
        self.operations_log = self.repo_root / "bulk_operations.log"
        
        # Ensure directories exist
        for directory in [self.backup_dir, self.templates_dir]:
            directory.mkdir(exist_ok=True)
        
        # Operation tracking
        self.active_operations = {}
        self.completed_operations = []
        
        # Performance settings
        self.max_workers = 4
        self.batch_size = 50
        self.backup_enabled = True
    
    def create_backup(self, operation_type: str) -> str:
        """Create backup before bulk operations"""
        if not self.backup_enabled:
            return ""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{operation_type}_{timestamp}"
        backup_path = self.backup_dir / backup_name
        
        # Create backup directories
        backup_prompts = backup_path / "prompts"
        backup_jekyll = backup_path / "jekyll_prompts"
        
        if self.prompts_dir.exists():
            shutil.copytree(self.prompts_dir, backup_prompts)
        
        if self.jekyll_prompts_dir.exists():
            shutil.copytree(self.jekyll_prompts_dir, backup_jekyll)
        
        # Create backup metadata
        metadata = {
            "timestamp": timestamp,
            "operation_type": operation_type,
            "source_prompt_count": len(list(self.prompts_dir.rglob("*.md"))) if self.prompts_dir.exists() else 0,
            "jekyll_prompt_count": len(list(self.jekyll_prompts_dir.glob("*.md"))) if self.jekyll_prompts_dir.exists() else 0
        }
        
        with open(backup_path / "metadata.json", 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"✓ Backup created: {backup_name}")
        return str(backup_path)
    
    def bulk_generate_prompts(self, generation_specs: List[Dict], 
                             template_file: str = None) -> BulkOperation:
        """Generate multiple prompts from specifications"""
        operation_id = f"bulk_generate_{int(time.time())}"
        operation = BulkOperation(
            operation_id=operation_id,
            operation_type="bulk_generate",
            target_count=len(generation_specs),
            start_time=datetime.now()
        )
        
        self.active_operations[operation_id] = operation
        backup_path = self.create_backup("bulk_generate")
        
        try:
            # Load template if provided
            template_content = None
            if template_file and Path(template_file).exists():
                with open(template_file, 'r', encoding='utf-8') as f:
                    template_content = f.read()
            
            # Process specs in batches
            for i in range(0, len(generation_specs), self.batch_size):
                batch = generation_specs[i:i + self.batch_size]
                self._process_generation_batch(batch, operation, template_content)
                
                # Update progress
                print(f"Processed batch {i//self.batch_size + 1}/{(len(generation_specs) + self.batch_size - 1)//self.batch_size}")
        
        except Exception as e:
            operation.errors.append(f"Bulk generation failed: {e}")
        
        finally:
            operation.end_time = datetime.now()
            self.completed_operations.append(operation)
            del self.active_operations[operation_id]
            self._log_operation(operation)
        
        return operation
    
    def _process_generation_batch(self, batch: List[Dict], operation: BulkOperation,
                                 template_content: str = None):
        """Process a batch of prompt generation specs"""
        
        def generate_single_prompt(spec):
            try:
                content = self._generate_prompt_from_spec(spec, template_content)
                filepath = self._save_generated_prompt(content, spec)
                return True, filepath
            except Exception as e:
                return False, str(e)
        
        # Use thread pool for parallel processing
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(generate_single_prompt, spec) for spec in batch]
            
            for future in concurrent.futures.as_completed(futures):
                success, result = future.result()
                if success:
                    operation.completed_count += 1
                    operation.results.append(result)
                else:
                    operation.failed_count += 1
                    operation.errors.append(result)
    
    def _generate_prompt_from_spec(self, spec: Dict, template_content: str = None) -> str:
        """Generate prompt content from specification"""
        if template_content:
            # Use provided template
            content = template_content
            # Replace placeholders
            replacements = {
                "{{TITLE}}": spec.get('title', ''),
                "{{CATEGORY}}": spec.get('category', ''),
                "{{DOMAIN}}": spec.get('domain', ''),
                "{{PRIMARY_EXPERT}}": spec.get('primary_expert', ''),
                "{{SECONDARY_EXPERT}}": spec.get('secondary_expert', ''),
                "{{FRAMEWORKS}}": json.dumps(spec.get('frameworks', [])),
                "{{DATE}}": datetime.now().strftime("%Y-%m-%d"),
                "{{SLUG}}": self._create_slug(spec.get('title', ''))
            }
            
            for placeholder, value in replacements.items():
                content = content.replace(placeholder, str(value))
            
            return content
        else:
            # Generate using built-in template
            return self._generate_standard_prompt(spec)
    
    def _generate_standard_prompt(self, spec: Dict) -> str:
        """Generate prompt using standard template"""
        title = spec.get('title', '')
        category = spec.get('category', '')
        domain = spec.get('domain', '')
        primary_expert = spec.get('primary_expert', '')
        secondary_expert = spec.get('secondary_expert', '')
        frameworks = spec.get('frameworks', [])
        slug = self._create_slug(title)
        
        frontmatter = {
            'title': title,
            'description': f"Professional prompt combining {primary_expert} and {secondary_expert} expertise for {domain} workflows",
            'category': category,
            'tags': [category.replace('-', ' '), domain.lower()],
            'slug': slug,
            'date': datetime.now().strftime("%Y-%m-%d"),
            'version': "3.0.0",
            'compatible_models': ["claude-3.5-sonnet", "gpt-4", "gemini-pro"],
            'use_cases': [f"{domain} optimization", "professional workflow enhancement"]
        }
        
        frontmatter_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        
        # Generate main content
        main_content = f"""# {title}

You are an expert AI assistant specializing in {domain}. When users need help with {domain.lower()}-related tasks, you adopt the combined expertise of two complementary professionals to provide comprehensive, actionable guidance.

## Your Expert Personas

### Primary Expert: {primary_expert}
You embody a seasoned {primary_expert} with 15+ years of hands-on experience in {domain}. Your expertise includes:
- Deep technical knowledge of {domain} best practices
- Proven track record of successful implementations
- Understanding of industry standards and emerging trends
- Ability to balance theoretical knowledge with practical constraints

### Secondary Expert: {secondary_expert}
You complement this with the perspective of an experienced {secondary_expert} who brings:
- Strategic oversight and stakeholder management skills
- Cross-functional collaboration experience
- Business impact assessment capabilities
- Change management and adoption expertise

## Professional Frameworks Integration

You systematically apply these proven methodologies:

{self._generate_frameworks_section(frameworks)}

## Four-Phase Systematic Approach

### Phase 1: Assessment & Discovery
**Objective**: Thoroughly understand the current state and requirements

**Primary Expert Analysis**:
- Conduct detailed technical assessment of current {domain.lower()} capabilities
- Identify gaps, bottlenecks, and improvement opportunities
- Evaluate existing processes, tools, and methodologies

**Secondary Expert Analysis**:
- Analyze stakeholder requirements and expectations
- Evaluate business impact and strategic alignment
- Assess organizational readiness for change

**Integrated Assessment Deliverables**:
1. Current state analysis with detailed findings
2. Gap analysis between current and desired state
3. Stakeholder impact assessment matrix
4. Risk register with mitigation strategies
5. Success criteria and measurement framework

### Phase 2: Strategic Design & Planning
**Objective**: Design comprehensive solution architecture and implementation roadmap

**Primary Expert Design**:
- Architect optimal {domain.lower()} solution approach
- Design technical implementation strategy
- Define quality standards and validation criteria

**Secondary Expert Design**:
- Develop change management and adoption strategy
- Design stakeholder communication and engagement plan
- Create training and capability development roadmap

**Integrated Design Deliverables**:
1. Comprehensive solution architecture document
2. Detailed implementation roadmap with milestones
3. Resource allocation and timeline planning
4. Change management and communication strategy
5. Training and development framework

### Phase 3: Implementation & Execution
**Objective**: Execute the solution with systematic monitoring and adjustment

**Primary Expert Implementation**:
- Lead technical implementation following best practices
- Establish quality control and validation processes
- Monitor technical performance and system integration

**Secondary Expert Implementation**:
- Orchestrate stakeholder coordination and communication
- Manage change adoption and user acceptance processes
- Monitor business impact and value realization

**Integrated Implementation Deliverables**:
1. Executed solution with validated functionality
2. Comprehensive testing and quality assurance results
3. Stakeholder training completion and adoption metrics
4. Performance monitoring dashboard and reporting
5. Issue resolution log and lessons learned documentation

### Phase 4: Optimization & Sustainability
**Objective**: Continuously improve and ensure long-term success

**Primary Expert Optimization**:
- Analyze performance data and identify optimization opportunities
- Implement technical improvements and efficiency enhancements
- Establish ongoing maintenance and support procedures

**Secondary Expert Optimization**:
- Evaluate business value realization and ROI achievement
- Facilitate continuous improvement culture and processes
- Plan for scaling and future capability expansion

**Integrated Optimization Deliverables**:
1. Performance optimization recommendations and implementations
2. Continuous improvement process framework
3. Long-term sustainability and evolution roadmap
4. Knowledge management and transfer protocols
5. Future capability expansion planning

## Interaction Protocol

When users engage with this prompt:

1. **Initial Assessment**: Ask targeted questions to understand their specific {domain.lower()} challenge
2. **Context Gathering**: Collect relevant details about their environment, constraints, and objectives
3. **Approach Selection**: Choose the most appropriate frameworks and methodologies for their situation
4. **Systematic Execution**: Work through the four phases systematically, adapting depth based on complexity
5. **Deliverable Focus**: Provide concrete, actionable deliverables at each phase

Begin by asking the user about their specific {domain.lower()} challenge and context to initiate the systematic assessment process.
"""
        
        return f"---\n{frontmatter_yaml}---\n\n{main_content}"
    
    def _generate_frameworks_section(self, frameworks: List[str]) -> str:
        """Generate frameworks section for prompt"""
        if not frameworks:
            frameworks = ["Strategic Analysis Framework", "Implementation Planning Framework", "Continuous Improvement Framework"]
        
        sections = []
        for i, framework in enumerate(frameworks, 1):
            sections.append(f"""### Framework {i}: {framework}
- Comprehensive methodology application
- Domain-specific best practices
- Advanced optimization techniques
- Performance measurement and validation""")
        
        return "\n\n".join(sections)
    
    def _create_slug(self, title: str) -> str:
        """Create URL-friendly slug from title"""
        slug = title.lower()
        slug = re.sub(r'[^a-z0-9\s-]', '', slug)
        slug = re.sub(r'\s+', '-', slug)
        slug = re.sub(r'-+', '-', slug)
        return slug.strip('-')
    
    def _save_generated_prompt(self, content: str, spec: Dict) -> str:
        """Save generated prompt to appropriate location"""
        category = spec.get('category', 'general')
        title = spec.get('title', 'untitled')
        slug = self._create_slug(title)
        
        # Create category directory
        category_dir = self.prompts_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)
        
        # Save file
        filename = f"{slug}.md"
        filepath = category_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return str(filepath)
    
    def bulk_convert_to_jekyll(self, source_pattern: str = "prompts/**/*.md") -> BulkOperation:
        """Convert multiple prompts to Jekyll format"""
        operation_id = f"bulk_convert_{int(time.time())}"
        
        # Find source files
        source_files = list(self.repo_root.glob(source_pattern))
        source_files = [f for f in source_files if f.name != "README.md"]
        
        operation = BulkOperation(
            operation_id=operation_id,
            operation_type="bulk_convert_jekyll",
            target_count=len(source_files),
            start_time=datetime.now()
        )
        
        self.active_operations[operation_id] = operation
        backup_path = self.create_backup("bulk_convert")
        
        try:
            # Process files in batches
            for i in range(0, len(source_files), self.batch_size):
                batch = source_files[i:i + self.batch_size]
                self._process_conversion_batch(batch, operation)
                
                print(f"Converted batch {i//self.batch_size + 1}/{(len(source_files) + self.batch_size - 1)//self.batch_size}")
        
        except Exception as e:
            operation.errors.append(f"Bulk conversion failed: {e}")
        
        finally:
            operation.end_time = datetime.now()
            self.completed_operations.append(operation)
            del self.active_operations[operation_id]
            self._log_operation(operation)
        
        return operation
    
    def _process_conversion_batch(self, batch: List[Path], operation: BulkOperation):
        """Process a batch of conversions"""
        
        def convert_single_file(source_file):
            try:
                with open(source_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Convert to Jekyll format
                jekyll_content = self._convert_to_jekyll_format(content, source_file)
                
                # Save to Jekyll directory
                output_file = self.jekyll_prompts_dir / source_file.name
                self.jekyll_prompts_dir.mkdir(parents=True, exist_ok=True)
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(jekyll_content)
                
                return True, str(output_file)
            except Exception as e:
                return False, f"{source_file}: {e}"
        
        # Use thread pool for parallel processing
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(convert_single_file, file) for file in batch]
            
            for future in concurrent.futures.as_completed(futures):
                success, result = future.result()
                if success:
                    operation.completed_count += 1
                    operation.results.append(result)
                else:
                    operation.failed_count += 1
                    operation.errors.append(result)
    
    def _convert_to_jekyll_format(self, content: str, source_file: Path) -> str:
        """Convert prompt to Jekyll format"""
        # If already has frontmatter, return as-is
        if content.startswith('---') and '---' in content[3:]:
            return content
        
        # Extract title from content
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else source_file.stem.replace('-', ' ').title()
        
        # Determine category from file path
        category = source_file.parent.name if source_file.parent.name != "prompts" else "general"
        
        # Generate frontmatter
        frontmatter = {
            'title': title,
            'description': f"Professional prompt for {category} optimization and expert consultation",
            'category': category,
            'tags': [category.replace('-', ' ')],
            'slug': source_file.stem,
            'date': datetime.now().strftime("%Y-%m-%d"),
            'version': "3.0.0",
            'compatible_models': ["claude-3.5-sonnet", "gpt-4", "gemini-pro"],
            'use_cases': [f"{category} optimization", "professional workflow enhancement"]
        }
        
        frontmatter_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        
        return f"---\n{frontmatter_yaml}---\n\n{content}"
    
    def bulk_update_metadata(self, updates: Dict[str, Any], 
                           target_pattern: str = "_prompts/*.md") -> BulkOperation:
        """Update metadata across multiple prompts"""
        operation_id = f"bulk_update_{int(time.time())}"
        
        # Find target files
        target_files = list(self.docs_dir.glob(target_pattern))
        
        operation = BulkOperation(
            operation_id=operation_id,
            operation_type="bulk_update_metadata",
            target_count=len(target_files),
            start_time=datetime.now()
        )
        
        self.active_operations[operation_id] = operation
        backup_path = self.create_backup("bulk_update")
        
        try:
            # Process files in batches
            for i in range(0, len(target_files), self.batch_size):
                batch = target_files[i:i + self.batch_size]
                self._process_update_batch(batch, updates, operation)
                
                print(f"Updated batch {i//self.batch_size + 1}/{(len(target_files) + self.batch_size - 1)//self.batch_size}")
        
        except Exception as e:
            operation.errors.append(f"Bulk update failed: {e}")
        
        finally:
            operation.end_time = datetime.now()
            self.completed_operations.append(operation)
            del self.active_operations[operation_id]
            self._log_operation(operation)
        
        return operation
    
    def _process_update_batch(self, batch: List[Path], updates: Dict[str, Any], 
                             operation: BulkOperation):
        """Process a batch of metadata updates"""
        
        def update_single_file(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update frontmatter
                updated_content = self._update_frontmatter(content, updates)
                
                # Save updated content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                return True, str(file_path)
            except Exception as e:
                return False, f"{file_path}: {e}"
        
        # Use thread pool for parallel processing
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(update_single_file, file) for file in batch]
            
            for future in concurrent.futures.as_completed(futures):
                success, result = future.result()
                if success:
                    operation.completed_count += 1
                    operation.results.append(result)
                else:
                    operation.failed_count += 1
                    operation.errors.append(result)
    
    def _update_frontmatter(self, content: str, updates: Dict[str, Any]) -> str:
        """Update frontmatter in content"""
        if not content.startswith('---'):
            return content
        
        frontmatter_end = content.find('---', 3)
        if frontmatter_end <= 0:
            return content
        
        try:
            frontmatter = yaml.safe_load(content[3:frontmatter_end])
            body_content = content[frontmatter_end + 3:]
            
            # Apply updates
            for key, value in updates.items():
                if key == "tags" and isinstance(value, list) and isinstance(frontmatter.get("tags"), list):
                    # Merge tags instead of replacing
                    existing_tags = set(frontmatter.get("tags", []))
                    new_tags = set(value)
                    frontmatter["tags"] = list(existing_tags.union(new_tags))
                else:
                    frontmatter[key] = value
            
            # Update timestamp
            frontmatter["last_updated"] = datetime.now().strftime("%Y-%m-%d")
            
            # Regenerate content
            frontmatter_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
            return f"---\n{frontmatter_yaml}---{body_content}"
            
        except yaml.YAMLError:
            return content
    
    def migrate_repository_structure(self, migration_plan: Dict) -> BulkOperation:
        """Migrate repository to new structure"""
        operation_id = f"migrate_{int(time.time())}"
        
        operation = BulkOperation(
            operation_id=operation_id,
            operation_type="repository_migration",
            target_count=len(migration_plan.get('operations', [])),
            start_time=datetime.now()
        )
        
        self.active_operations[operation_id] = operation
        backup_path = self.create_backup("repository_migration")
        
        try:
            for step in migration_plan.get('operations', []):
                self._execute_migration_step(step, operation)
                
        except Exception as e:
            operation.errors.append(f"Migration failed: {e}")
        
        finally:
            operation.end_time = datetime.now()
            self.completed_operations.append(operation)
            del self.active_operations[operation_id]
            self._log_operation(operation)
        
        return operation
    
    def _execute_migration_step(self, step: Dict, operation: BulkOperation):
        """Execute a single migration step"""
        step_type = step.get('type')
        
        try:
            if step_type == "move_files":
                self._migrate_move_files(step)
            elif step_type == "rename_categories":
                self._migrate_rename_categories(step)
            elif step_type == "reorganize_structure":
                self._migrate_reorganize_structure(step)
            elif step_type == "update_references":
                self._migrate_update_references(step)
            else:
                raise ValueError(f"Unknown migration step type: {step_type}")
            
            operation.completed_count += 1
            operation.results.append(f"Completed: {step_type}")
            
        except Exception as e:
            operation.failed_count += 1
            operation.errors.append(f"Failed {step_type}: {e}")
    
    def _migrate_move_files(self, step: Dict):
        """Move files as part of migration"""
        source_pattern = step.get('source_pattern')
        target_directory = step.get('target_directory')
        
        source_files = list(self.repo_root.glob(source_pattern))
        target_dir = self.repo_root / target_directory
        target_dir.mkdir(parents=True, exist_ok=True)
        
        for source_file in source_files:
            target_file = target_dir / source_file.name
            shutil.move(str(source_file), str(target_file))
    
    def _migrate_rename_categories(self, step: Dict):
        """Rename categories in frontmatter"""
        category_mapping = step.get('category_mapping', {})
        
        for md_file in self.jekyll_prompts_dir.glob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for old_category, new_category in category_mapping.items():
                content = content.replace(f"category: {old_category}", f"category: {new_category}")
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
    
    def _migrate_reorganize_structure(self, step: Dict):
        """Reorganize directory structure"""
        # Implementation depends on specific reorganization needs
        pass
    
    def _migrate_update_references(self, step: Dict):
        """Update internal references during migration"""
        reference_mapping = step.get('reference_mapping', {})
        
        for md_file in self.repo_root.rglob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            modified = False
            for old_ref, new_ref in reference_mapping.items():
                if old_ref in content:
                    content = content.replace(old_ref, new_ref)
                    modified = True
            
            if modified:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
    
    def export_prompts_csv(self, output_file: str, include_content: bool = False) -> str:
        """Export prompts metadata to CSV"""
        prompts_data = []
        
        for md_file in self.jekyll_prompts_dir.glob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if content.startswith('---'):
                    frontmatter_end = content.find('---', 3)
                    if frontmatter_end > 0:
                        frontmatter = yaml.safe_load(content[3:frontmatter_end])
                        
                        row_data = {
                            'title': frontmatter.get('title', ''),
                            'description': frontmatter.get('description', ''),
                            'category': frontmatter.get('category', ''),
                            'tags': ', '.join(frontmatter.get('tags', [])),
                            'slug': frontmatter.get('slug', ''),
                            'file_path': str(md_file),
                            'word_count': len(content.split()),
                            'version': frontmatter.get('version', ''),
                            'date': frontmatter.get('date', '')
                        }
                        
                        if include_content:
                            body_content = content[frontmatter_end + 3:]
                            row_data['content'] = body_content[:500] + "..." if len(body_content) > 500 else body_content
                        
                        prompts_data.append(row_data)
                        
            except Exception as e:
                print(f"Error processing {md_file}: {e}")
        
        # Write CSV
        if prompts_data:
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = prompts_data[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(prompts_data)
        
        print(f"✓ Exported {len(prompts_data)} prompts to {output_file}")
        return output_file
    
    def import_prompts_csv(self, csv_file: str) -> BulkOperation:
        """Import prompts from CSV file"""
        operation_id = f"import_csv_{int(time.time())}"
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            import_specs = list(reader)
        
        operation = BulkOperation(
            operation_id=operation_id,
            operation_type="import_csv",
            target_count=len(import_specs),
            start_time=datetime.now()
        )
        
        self.active_operations[operation_id] = operation
        
        try:
            for spec in import_specs:
                try:
                    # Convert CSV row to prompt specification
                    prompt_spec = {
                        'title': spec.get('title', ''),
                        'category': spec.get('category', 'general'),
                        'domain': spec.get('domain', spec.get('category', 'general')),
                        'primary_expert': spec.get('primary_expert', 'Senior Consultant'),
                        'secondary_expert': spec.get('secondary_expert', 'Strategy Advisor'),
                        'frameworks': [f.strip() for f in spec.get('frameworks', '').split(',') if f.strip()]
                    }
                    
                    # Generate and save prompt
                    content = self._generate_standard_prompt(prompt_spec)
                    filepath = self._save_generated_prompt(content, prompt_spec)
                    
                    operation.completed_count += 1
                    operation.results.append(filepath)
                    
                except Exception as e:
                    operation.failed_count += 1
                    operation.errors.append(f"Failed to import {spec.get('title', 'Unknown')}: {e}")
        
        finally:
            operation.end_time = datetime.now()
            self.completed_operations.append(operation)
            del self.active_operations[operation_id]
            self._log_operation(operation)
        
        return operation
    
    def _log_operation(self, operation: BulkOperation):
        """Log operation details"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'operation': asdict(operation)
        }
        
        with open(self.operations_log, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry) + '\n')
    
    def get_operation_status(self, operation_id: str) -> Optional[BulkOperation]:
        """Get status of operation"""
        if operation_id in self.active_operations:
            return self.active_operations[operation_id]
        
        for op in self.completed_operations:
            if op.operation_id == operation_id:
                return op
        
        return None
    
    def list_operations(self, operation_type: str = None) -> List[BulkOperation]:
        """List all operations, optionally filtered by type"""
        all_operations = list(self.active_operations.values()) + self.completed_operations
        
        if operation_type:
            return [op for op in all_operations if op.operation_type == operation_type]
        
        return all_operations
    
    def generate_operations_report(self) -> Dict:
        """Generate comprehensive operations report"""
        all_operations = self.list_operations()
        
        stats = {
            'total_operations': len(all_operations),
            'active_operations': len(self.active_operations),
            'completed_operations': len(self.completed_operations),
            'operation_types': defaultdict(int),
            'success_rate': 0,
            'total_processed': 0,
            'total_failed': 0
        }
        
        for op in all_operations:
            stats['operation_types'][op.operation_type] += 1
            stats['total_processed'] += op.completed_count
            stats['total_failed'] += op.failed_count
        
        if stats['total_processed'] + stats['total_failed'] > 0:
            stats['success_rate'] = stats['total_processed'] / (stats['total_processed'] + stats['total_failed']) * 100
        
        return {
            'timestamp': datetime.now().isoformat(),
            'statistics': dict(stats),
            'recent_operations': [asdict(op) for op in all_operations[-10:]],  # Last 10 operations
            'recommendations': self._generate_operations_recommendations(stats)
        }
    
    def _generate_operations_recommendations(self, stats: Dict) -> List[str]:
        """Generate recommendations based on operations statistics"""
        recommendations = []
        
        if stats['success_rate'] < 90:
            recommendations.append("Investigate common failure patterns to improve success rate")
        
        if len(self.active_operations) > 5:
            recommendations.append("Consider reducing concurrent operations to improve performance")
        
        if stats['total_failed'] > stats['total_processed'] * 0.1:
            recommendations.append("High failure rate detected - review error logs and improve validation")
        
        return recommendations

def main():
    """Main CLI interface for bulk management tools"""
    parser = argparse.ArgumentParser(description="Bulk Content Management Tools")
    parser.add_argument("--repo-root", default=".", help="Repository root directory")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Bulk generate prompts")
    gen_parser.add_argument("--specs-file", required=True, help="JSON file with generation specifications")
    gen_parser.add_argument("--template", help="Template file to use")
    
    # Convert command
    conv_parser = subparsers.add_parser("convert", help="Bulk convert to Jekyll format")
    conv_parser.add_argument("--pattern", default="prompts/**/*.md", help="Source file pattern")
    
    # Update command
    update_parser = subparsers.add_parser("update", help="Bulk update metadata")
    update_parser.add_argument("--updates-file", required=True, help="JSON file with metadata updates")
    update_parser.add_argument("--pattern", default="_prompts/*.md", help="Target file pattern")
    
    # Export command
    export_parser = subparsers.add_parser("export", help="Export prompts to CSV")
    export_parser.add_argument("--output", required=True, help="Output CSV file")
    export_parser.add_argument("--include-content", action="store_true", help="Include content in export")
    
    # Import command
    import_parser = subparsers.add_parser("import", help="Import prompts from CSV")
    import_parser.add_argument("--csv-file", required=True, help="CSV file to import")
    
    # Status command
    status_parser = subparsers.add_parser("status", help="Show operation status")
    status_parser.add_argument("--operation-id", help="Specific operation ID")
    
    # Report command
    report_parser = subparsers.add_parser("report", help="Generate operations report")
    
    args = parser.parse_args()
    
    manager = BulkContentManager(args.repo_root)
    
    if args.command == "generate":
        with open(args.specs_file, 'r') as f:
            specs = json.load(f)
        operation = manager.bulk_generate_prompts(specs, args.template)
        print(f"Generation completed. Operation ID: {operation.operation_id}")
        print(f"Success: {operation.completed_count}, Failed: {operation.failed_count}")
        
    elif args.command == "convert":
        operation = manager.bulk_convert_to_jekyll(args.pattern)
        print(f"Conversion completed. Operation ID: {operation.operation_id}")
        print(f"Success: {operation.completed_count}, Failed: {operation.failed_count}")
        
    elif args.command == "update":
        with open(args.updates_file, 'r') as f:
            updates = json.load(f)
        operation = manager.bulk_update_metadata(updates, args.pattern)
        print(f"Update completed. Operation ID: {operation.operation_id}")
        print(f"Success: {operation.completed_count}, Failed: {operation.failed_count}")
        
    elif args.command == "export":
        output_file = manager.export_prompts_csv(args.output, args.include_content)
        print(f"Export completed: {output_file}")
        
    elif args.command == "import":
        operation = manager.import_prompts_csv(args.csv_file)
        print(f"Import completed. Operation ID: {operation.operation_id}")
        print(f"Success: {operation.completed_count}, Failed: {operation.failed_count}")
        
    elif args.command == "status":
        if args.operation_id:
            operation = manager.get_operation_status(args.operation_id)
            if operation:
                print(json.dumps(asdict(operation), indent=2, default=str))
            else:
                print(f"Operation {args.operation_id} not found")
        else:
            operations = manager.list_operations()
            for op in operations[-10:]:  # Show last 10
                print(f"{op.operation_id}: {op.operation_type} - {op.completed_count}/{op.target_count}")
        
    elif args.command == "report":
        report = manager.generate_operations_report()
        print(json.dumps(report, indent=2, default=str))
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()