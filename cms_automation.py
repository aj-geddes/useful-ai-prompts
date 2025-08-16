#!/usr/bin/env python3
"""
Content Management System for Useful AI Prompts Repository
Automated pipeline for scaling from 278 to 500+ prompts with quality assurance
"""

import os
import json
import re
import yaml
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import argparse
import subprocess

class PromptCMS:
    """Comprehensive Content Management System for AI Prompts Repository"""
    
    def __init__(self, repo_root: str = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.prompts_dir = self.repo_root / "prompts"
        self.docs_dir = self.repo_root / "docs"
        self.jekyll_prompts_dir = self.docs_dir / "_prompts"
        self.metadata_dir = self.repo_root / "metadata"
        self.research_dir = self.repo_root / "research"
        
        # Quality standards
        self.min_content_lines = 350
        self.required_sections = [
            "Primary Expert", "Secondary Expert", "Frameworks", 
            "Assessment Phase", "Design Phase", "Implementation Phase", "Optimization Phase"
        ]
        
        # Performance tracking
        self.stats = {
            "prompts_created": 0,
            "prompts_validated": 0,
            "prompts_converted": 0,
            "quality_issues": 0,
            "processing_time": 0
        }
    
    def generate_prompt_template(self, category: str, domain: str, title: str, 
                               primary_expert: str, secondary_expert: str,
                               frameworks: List[str]) -> str:
        """Generate a new prompt using standardized template"""
        
        slug = self._create_slug(title)
        date = datetime.now().strftime("%Y-%m-%d")
        
        template = f"""---
title: "{title}"
description: "Professional prompt combining {primary_expert} and {secondary_expert} expertise for {domain} workflows"
category: {category}
tags: [{', '.join([f'"{f.lower()}"' for f in frameworks[:3]])}]
slug: {slug}
date: {date}
version: "3.0.0"
compatible_models: ["claude-3.5-sonnet", "gpt-4", "gemini-pro"]
use_cases: ["{domain} optimization", "professional workflow enhancement", "expert consultation"]
---

# {title}

You are an expert AI assistant specializing in {domain}. When users need help with {domain.lower()}-related tasks, you adopt the combined expertise of two complementary professionals to provide comprehensive, actionable guidance.

## Your Expert Personas

### Primary Expert: {primary_expert}
You embody a seasoned {primary_expert} with 15+ years of hands-on experience in {domain}. Your expertise includes:
- Deep technical knowledge of {domain} best practices
- Proven track record of successful implementations
- Understanding of industry standards and emerging trends
- Ability to balance theoretical knowledge with practical constraints
- Experience mentoring teams and driving organizational change

### Secondary Expert: {secondary_expert}
You complement this with the perspective of an experienced {secondary_expert} who brings:
- Strategic oversight and stakeholder management skills
- Cross-functional collaboration experience
- Business impact assessment capabilities
- Change management and adoption expertise
- Long-term planning and sustainability focus

## Professional Frameworks Integration

You systematically apply these proven methodologies:

### Framework 1: {frameworks[0] if len(frameworks) > 0 else "Strategic Analysis Framework"}
- Comprehensive situation assessment
- Stakeholder impact analysis
- Risk and opportunity evaluation
- Success metrics definition

### Framework 2: {frameworks[1] if len(frameworks) > 1 else "Implementation Planning Framework"}
- Resource requirement analysis
- Timeline and milestone planning
- Change management strategy
- Quality assurance protocols

### Framework 3: {frameworks[2] if len(frameworks) > 2 else "Continuous Improvement Framework"}
- Performance monitoring setup
- Feedback loop implementation
- Optimization opportunity identification
- Knowledge transfer planning

{self._generate_additional_frameworks(frameworks[3:] if len(frameworks) > 3 else [])}

## Four-Phase Systematic Approach

### Phase 1: Assessment & Discovery
**Objective**: Thoroughly understand the current state and requirements

**Primary Expert Analysis**:
- Conduct detailed technical assessment of current {domain.lower()} capabilities
- Identify gaps, bottlenecks, and improvement opportunities
- Evaluate existing processes, tools, and methodologies
- Assess team skills and resource availability

**Secondary Expert Analysis**:
- Analyze stakeholder requirements and expectations
- Evaluate business impact and strategic alignment
- Assess organizational readiness for change
- Identify potential resistance points and mitigation strategies

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
- Create detailed process workflows and procedures

**Secondary Expert Design**:
- Develop change management and adoption strategy
- Design stakeholder communication and engagement plan
- Create training and capability development roadmap
- Establish governance and oversight framework

**Integrated Design Deliverables**:
1. Comprehensive solution architecture document
2. Detailed implementation roadmap with milestones
3. Resource allocation and timeline planning
4. Change management and communication strategy
5. Training and development framework
6. Quality assurance and validation protocols

### Phase 3: Implementation & Execution
**Objective**: Execute the solution with systematic monitoring and adjustment

**Primary Expert Implementation**:
- Lead technical implementation following best practices
- Establish quality control and validation processes
- Monitor technical performance and system integration
- Provide hands-on guidance and troubleshooting support

**Secondary Expert Implementation**:
- Orchestrate stakeholder coordination and communication
- Manage change adoption and user acceptance processes
- Monitor business impact and value realization
- Facilitate feedback collection and issue resolution

**Integrated Implementation Deliverables**:
1. Executed solution with validated functionality
2. Comprehensive testing and quality assurance results
3. Stakeholder training completion and adoption metrics
4. Performance monitoring dashboard and reporting
5. Issue resolution log and lessons learned documentation
6. Change management impact assessment

### Phase 4: Optimization & Sustainability
**Objective**: Continuously improve and ensure long-term success

**Primary Expert Optimization**:
- Analyze performance data and identify optimization opportunities
- Implement technical improvements and efficiency enhancements
- Establish ongoing maintenance and support procedures
- Create knowledge transfer and documentation framework

**Secondary Expert Optimization**:
- Evaluate business value realization and ROI achievement
- Facilitate continuous improvement culture and processes
- Plan for scaling and future capability expansion
- Establish long-term sustainability and evolution strategy

**Integrated Optimization Deliverables**:
1. Performance optimization recommendations and implementations
2. Continuous improvement process framework
3. Long-term sustainability and evolution roadmap
4. Knowledge management and transfer protocols
5. Future capability expansion planning
6. ROI analysis and value realization report

## Interaction Protocol

When users engage with this prompt:

1. **Initial Assessment**: Ask targeted questions to understand their specific {domain.lower()} challenge
2. **Context Gathering**: Collect relevant details about their environment, constraints, and objectives
3. **Approach Selection**: Choose the most appropriate frameworks and methodologies for their situation
4. **Systematic Execution**: Work through the four phases systematically, adapting depth based on complexity
5. **Deliverable Focus**: Provide concrete, actionable deliverables at each phase
6. **Continuous Validation**: Regularly check understanding and adjust approach based on feedback

## Quality Standards

All outputs must meet these professional standards:
- **Comprehensiveness**: Address all aspects of the challenge systematically
- **Actionability**: Provide specific, implementable recommendations
- **Evidence-Based**: Ground advice in proven frameworks and best practices
- **Stakeholder-Aware**: Consider all relevant perspectives and impacts
- **Future-Focused**: Include sustainability and evolution considerations
- **Risk-Conscious**: Identify and address potential challenges proactively

Begin by asking the user about their specific {domain.lower()} challenge and context to initiate the systematic assessment process.
"""
        return template
    
    def _generate_additional_frameworks(self, additional_frameworks: List[str]) -> str:
        """Generate additional framework sections if provided"""
        if not additional_frameworks:
            return ""
        
        sections = []
        for i, framework in enumerate(additional_frameworks, 4):
            sections.append(f"""
### Framework {i}: {framework}
- Specialized methodology application
- Domain-specific best practices
- Advanced optimization techniques
- Innovation and improvement focus""")
        
        return "\n".join(sections)
    
    def _create_slug(self, title: str) -> str:
        """Create URL-friendly slug from title"""
        slug = title.lower()
        slug = re.sub(r'[^a-z0-9\s-]', '', slug)
        slug = re.sub(r'\s+', '-', slug)
        slug = re.sub(r'-+', '-', slug)
        return slug.strip('-')
    
    def validate_prompt_quality(self, content: str, filepath: str = None) -> Tuple[bool, List[str]]:
        """Comprehensive quality validation for prompts"""
        issues = []
        
        # Check minimum content length
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        if len(lines) < self.min_content_lines:
            issues.append(f"Content too short: {len(lines)} lines (minimum {self.min_content_lines})")
        
        # Check for required sections
        for section in self.required_sections:
            if section not in content:
                issues.append(f"Missing required section: {section}")
        
        # Check for dual-persona structure
        if "Primary Expert" not in content:
            issues.append("Missing Primary Expert section")
        if "Secondary Expert" not in content:
            issues.append("Missing Secondary Expert section")
        
        # Check for framework integration
        framework_count = len(re.findall(r'### Framework \d+:', content))
        if framework_count < 3:
            issues.append(f"Insufficient frameworks: {framework_count} (minimum 3)")
        
        # Check for four-phase structure
        phases = ["Assessment", "Design", "Implementation", "Optimization"]
        missing_phases = [phase for phase in phases if f"Phase" not in content or phase not in content]
        if missing_phases:
            issues.append(f"Missing phases: {', '.join(missing_phases)}")
        
        # Check for actionable deliverables
        deliverables_count = len(re.findall(r'Deliverables?:', content, re.IGNORECASE))
        if deliverables_count < 4:
            issues.append(f"Insufficient deliverables sections: {deliverables_count} (minimum 4)")
        
        # Check YAML frontmatter
        if content.startswith('---'):
            try:
                frontmatter_end = content.find('---', 3)
                if frontmatter_end > 0:
                    frontmatter = content[3:frontmatter_end]
                    yaml.safe_load(frontmatter)
            except yaml.YAMLError:
                issues.append("Invalid YAML frontmatter")
        else:
            issues.append("Missing YAML frontmatter")
        
        self.stats["quality_issues"] += len(issues)
        self.stats["prompts_validated"] += 1
        
        return len(issues) == 0, issues
    
    def batch_create_prompts(self, prompt_specs: List[Dict]) -> List[str]:
        """Create multiple prompts from specifications"""
        created_files = []
        start_time = time.time()
        
        for spec in prompt_specs:
            try:
                # Generate prompt content
                content = self.generate_prompt_template(
                    category=spec['category'],
                    domain=spec['domain'],
                    title=spec['title'],
                    primary_expert=spec['primary_expert'],
                    secondary_expert=spec['secondary_expert'],
                    frameworks=spec['frameworks']
                )
                
                # Validate quality
                is_valid, issues = self.validate_prompt_quality(content)
                if not is_valid:
                    print(f"Quality issues in {spec['title']}: {', '.join(issues)}")
                    continue
                
                # Save to appropriate directory
                category_dir = self.prompts_dir / spec['category']
                category_dir.mkdir(parents=True, exist_ok=True)
                
                filename = f"{self._create_slug(spec['title'])}.md"
                filepath = category_dir / filename
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                created_files.append(str(filepath))
                self.stats["prompts_created"] += 1
                
                print(f"✓ Created: {spec['title']}")
                
            except Exception as e:
                print(f"✗ Failed to create {spec.get('title', 'Unknown')}: {e}")
        
        self.stats["processing_time"] += time.time() - start_time
        return created_files
    
    def optimize_search_index(self) -> Dict:
        """Generate optimized search index for 500+ prompts"""
        start_time = time.time()
        
        # Collect all prompts
        all_prompts = []
        
        for prompt_file in self.jekyll_prompts_dir.glob("*.md"):
            try:
                with open(prompt_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract frontmatter
                if content.startswith('---'):
                    frontmatter_end = content.find('---', 3)
                    if frontmatter_end > 0:
                        frontmatter = yaml.safe_load(content[3:frontmatter_end])
                        
                        # Extract searchable content
                        body_content = content[frontmatter_end + 3:]
                        searchable_text = self._extract_searchable_text(body_content)
                        
                        prompt_data = {
                            "title": frontmatter.get('title', ''),
                            "description": frontmatter.get('description', ''),
                            "category": frontmatter.get('category', ''),
                            "tags": frontmatter.get('tags', []),
                            "slug": frontmatter.get('slug', ''),
                            "use_cases": frontmatter.get('use_cases', []),
                            "searchable_content": searchable_text[:500],  # Limit for performance
                            "file_path": f"_prompts/{prompt_file.name}",
                            "word_count": len(body_content.split()),
                            "frameworks": self._extract_frameworks(body_content)
                        }
                        
                        all_prompts.append(prompt_data)
                        
            except Exception as e:
                print(f"Error processing {prompt_file}: {e}")
        
        # Create optimized index structure
        search_index = {
            "version": "2.0.0",
            "last_updated": datetime.now().isoformat(),
            "total_prompts": len(all_prompts),
            "categories": list(set(p['category'] for p in all_prompts)),
            "all_tags": list(set(tag for p in all_prompts for tag in p['tags'])),
            "prompts": all_prompts,
            "category_counts": self._calculate_category_counts(all_prompts),
            "performance_metrics": {
                "index_size_kb": 0,  # Will be calculated after writing
                "build_time_seconds": time.time() - start_time,
                "average_prompt_length": sum(p['word_count'] for p in all_prompts) / len(all_prompts) if all_prompts else 0
            }
        }
        
        # Save optimized index
        index_path = self.docs_dir / "assets" / "data" / "search-index.json"
        index_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(search_index, f, indent=2, ensure_ascii=False)
        
        # Calculate file size
        search_index["performance_metrics"]["index_size_kb"] = round(index_path.stat().st_size / 1024, 2)
        
        # Update main index
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(search_index, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Optimized search index created with {len(all_prompts)} prompts")
        print(f"  File size: {search_index['performance_metrics']['index_size_kb']} KB")
        print(f"  Build time: {search_index['performance_metrics']['build_time_seconds']:.2f} seconds")
        
        return search_index
    
    def _extract_searchable_text(self, content: str) -> str:
        """Extract key searchable text from prompt content"""
        # Remove markdown formatting
        text = re.sub(r'[#*_`]', '', content)
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        # Extract key phrases (deliverables, objectives, etc.)
        key_sections = re.findall(r'(?:Objective|Deliverable|Framework|Phase).*?(?=\n|$)', text, re.IGNORECASE)
        return ' '.join(key_sections[:10])  # Limit to top 10 key phrases
    
    def _extract_frameworks(self, content: str) -> List[str]:
        """Extract framework names from content"""
        frameworks = re.findall(r'### Framework \d+: (.+)', content)
        return [f.strip() for f in frameworks]
    
    def _calculate_category_counts(self, prompts: List[Dict]) -> Dict[str, int]:
        """Calculate prompt counts per category"""
        counts = {}
        for prompt in prompts:
            category = prompt['category']
            counts[category] = counts.get(category, 0) + 1
        return counts
    
    def convert_to_jekyll_batch(self, source_dir: str = None) -> List[str]:
        """Batch convert prompts to Jekyll format"""
        if source_dir is None:
            source_dir = self.prompts_dir
        
        converted_files = []
        start_time = time.time()
        
        # Recursively find all markdown files
        for md_file in Path(source_dir).rglob("*.md"):
            if md_file.name == "README.md":
                continue
                
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Skip if already in Jekyll format
                if content.startswith('---') and '---' in content[3:]:
                    continue
                
                # Convert to Jekyll format
                jekyll_content = self._convert_to_jekyll_format(content, md_file)
                
                # Validate quality
                is_valid, issues = self.validate_prompt_quality(jekyll_content)
                if not is_valid:
                    print(f"Quality issues in {md_file.name}: {', '.join(issues[:3])}...")
                    continue
                
                # Save to Jekyll directory
                output_file = self.jekyll_prompts_dir / md_file.name
                self.jekyll_prompts_dir.mkdir(parents=True, exist_ok=True)
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(jekyll_content)
                
                converted_files.append(str(output_file))
                self.stats["prompts_converted"] += 1
                
                print(f"✓ Converted: {md_file.name}")
                
            except Exception as e:
                print(f"✗ Failed to convert {md_file}: {e}")
        
        self.stats["processing_time"] += time.time() - start_time
        return converted_files
    
    def _convert_to_jekyll_format(self, content: str, source_file: Path) -> str:
        """Convert prompt to Jekyll format with frontmatter"""
        # Extract title
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else source_file.stem.replace('-', ' ').title()
        
        # Determine category from file path
        category = source_file.parent.name
        
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
        
        # Format frontmatter
        frontmatter_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        
        return f"---\n{frontmatter_yaml}---\n\n{content}"
    
    def generate_cms_report(self) -> Dict:
        """Generate comprehensive CMS status report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "repository_status": {
                "total_source_prompts": len(list(self.prompts_dir.rglob("*.md"))),
                "total_jekyll_prompts": len(list(self.jekyll_prompts_dir.glob("*.md"))),
                "categories": len([d for d in self.prompts_dir.iterdir() if d.is_dir()]),
                "target_prompts": 500
            },
            "processing_statistics": self.stats,
            "quality_metrics": {
                "validation_rate": (self.stats["prompts_validated"] - self.stats["quality_issues"]) / max(self.stats["prompts_validated"], 1) * 100,
                "conversion_success_rate": self.stats["prompts_converted"] / max(self.stats["prompts_validated"], 1) * 100,
                "average_processing_time": self.stats["processing_time"] / max(self.stats["prompts_created"] + self.stats["prompts_converted"], 1)
            },
            "recommendations": []
        }
        
        # Add recommendations based on metrics
        if report["quality_metrics"]["validation_rate"] < 90:
            report["recommendations"].append("Improve prompt quality standards compliance")
        
        if report["repository_status"]["total_source_prompts"] < 400:
            remaining = 500 - report["repository_status"]["total_source_prompts"]
            report["recommendations"].append(f"Create {remaining} additional prompts to reach 500 target")
        
        if self.stats["processing_time"] > 60:
            report["recommendations"].append("Optimize processing pipeline for better performance")
        
        return report

def main():
    """Main CLI interface for the CMS"""
    parser = argparse.ArgumentParser(description="Useful AI Prompts CMS")
    parser.add_argument("--repo-root", default=".", help="Repository root directory")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate new prompts")
    gen_parser.add_argument("--spec-file", required=True, help="JSON file with prompt specifications")
    
    # Validate command
    val_parser = subparsers.add_parser("validate", help="Validate prompt quality")
    val_parser.add_argument("--path", default="prompts", help="Path to validate")
    
    # Convert command
    conv_parser = subparsers.add_parser("convert", help="Convert prompts to Jekyll format")
    conv_parser.add_argument("--source", default="prompts", help="Source directory")
    
    # Index command
    idx_parser = subparsers.add_parser("index", help="Generate search index")
    
    # Report command
    rep_parser = subparsers.add_parser("report", help="Generate CMS report")
    
    args = parser.parse_args()
    
    cms = PromptCMS(args.repo_root)
    
    if args.command == "generate":
        with open(args.spec_file, 'r') as f:
            specs = json.load(f)
        created = cms.batch_create_prompts(specs)
        print(f"Created {len(created)} prompts")
        
    elif args.command == "validate":
        # Validate all prompts in path
        issues_found = 0
        for md_file in Path(args.path).rglob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            is_valid, issues = cms.validate_prompt_quality(content, str(md_file))
            if not is_valid:
                print(f"Issues in {md_file}: {', '.join(issues)}")
                issues_found += len(issues)
        print(f"Validation complete. {issues_found} issues found.")
        
    elif args.command == "convert":
        converted = cms.convert_to_jekyll_batch(args.source)
        print(f"Converted {len(converted)} prompts")
        
    elif args.command == "index":
        index = cms.optimize_search_index()
        print(f"Generated index with {index['total_prompts']} prompts")
        
    elif args.command == "report":
        report = cms.generate_cms_report()
        print(json.dumps(report, indent=2))
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()