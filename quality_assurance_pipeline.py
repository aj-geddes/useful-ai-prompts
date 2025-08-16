#!/usr/bin/env python3
"""
Quality Assurance Pipeline for AI Prompts Repository
Comprehensive validation system ensuring prompt quality and consistency
"""

import os
import re
import json
import yaml
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

@dataclass
class QualityMetric:
    """Quality metric with scoring and recommendations"""
    name: str
    score: float  # 0-100
    max_score: float
    issues: List[str]
    recommendations: List[str]
    critical: bool = False

@dataclass
class QualityReport:
    """Comprehensive quality assessment report"""
    file_path: str
    overall_score: float
    grade: str  # A+, A, B+, B, C+, C, D, F
    metrics: List[QualityMetric]
    word_count: int
    line_count: int
    estimated_output_length: int
    compliance_status: str
    critical_issues: int
    recommendations: List[str]

class PromptQualityValidator:
    """Advanced quality validation system for AI prompts"""
    
    def __init__(self):
        # Quality standards
        self.min_content_lines = 350
        self.min_word_count = 2500
        self.target_output_lines = 600
        
        # Required structural elements
        self.required_sections = {
            "personas": ["Primary Expert", "Secondary Expert"],
            "frameworks": ["Framework 1:", "Framework 2:", "Framework 3:"],
            "phases": ["Phase 1:", "Phase 2:", "Phase 3:", "Phase 4:"],
            "deliverables": ["Deliverables", "deliverables"],
            "interaction": ["Interaction Protocol", "protocol"]
        }
        
        # Content quality patterns
        self.quality_patterns = {
            "actionable_language": [
                r"\b(implement|execute|develop|create|design|analyze|assess|evaluate|optimize)\b",
                r"\b(deliverable|milestone|outcome|result|output)\b",
                r"\b(strategy|framework|methodology|approach|process)\b"
            ],
            "professional_terminology": [
                r"\b(stakeholder|governance|compliance|ROI|KPI|SLA)\b",
                r"\b(best practice|industry standard|proven methodology)\b",
                r"\b(risk assessment|mitigation|optimization)\b"
            ],
            "expertise_indicators": [
                r"\b(\d+\+?\s*years?)\b",
                r"\b(expert|specialist|consultant|advisor|strategist)\b",
                r"\b(proven track record|extensive experience|deep knowledge)\b"
            ],
            "weak_language": [
                r"\b(maybe|perhaps|might|could potentially|possibly)\b",
                r"\b(simple|basic|easy|quick)\b",
                r"\b(help with|assist|support)\b"
            ]
        }
        
        # Grading scale
        self.grade_thresholds = {
            "A+": 95, "A": 90, "B+": 85, "B": 80, 
            "C+": 75, "C": 70, "D": 60, "F": 0
        }
    
    def validate_prompt(self, content: str, file_path: str = "") -> QualityReport:
        """Comprehensive prompt quality validation"""
        
        metrics = []
        
        # Basic metrics
        word_count = len(content.split())
        line_count = len([line for line in content.split('\n') if line.strip()])
        
        # Structural validation
        metrics.append(self._validate_structure(content))
        metrics.append(self._validate_personas(content))
        metrics.append(self._validate_frameworks(content))
        metrics.append(self._validate_phases(content))
        metrics.append(self._validate_deliverables(content))
        
        # Content quality validation
        metrics.append(self._validate_content_length(content, word_count, line_count))
        metrics.append(self._validate_language_quality(content))
        metrics.append(self._validate_actionability(content))
        metrics.append(self._validate_professionalism(content))
        metrics.append(self._validate_expertise_depth(content))
        
        # Technical validation
        metrics.append(self._validate_yaml_frontmatter(content))
        metrics.append(self._validate_markdown_structure(content))
        
        # Calculate overall score
        total_score = sum(metric.score for metric in metrics)
        max_possible = sum(metric.max_score for metric in metrics)
        overall_score = (total_score / max_possible * 100) if max_possible > 0 else 0
        
        # Determine grade
        grade = "F"
        for grade_letter, threshold in self.grade_thresholds.items():
            if overall_score >= threshold:
                grade = grade_letter
                break
        
        # Count critical issues
        critical_issues = sum(1 for metric in metrics if metric.critical and metric.issues)
        
        # Generate recommendations
        recommendations = []
        for metric in metrics:
            recommendations.extend(metric.recommendations)
        
        # Estimate output length
        estimated_output = self._estimate_output_length(content)
        
        # Determine compliance status
        compliance_status = "COMPLIANT" if overall_score >= 85 and critical_issues == 0 else "NON_COMPLIANT"
        
        return QualityReport(
            file_path=file_path,
            overall_score=overall_score,
            grade=grade,
            metrics=metrics,
            word_count=word_count,
            line_count=line_count,
            estimated_output_length=estimated_output,
            compliance_status=compliance_status,
            critical_issues=critical_issues,
            recommendations=list(set(recommendations))  # Remove duplicates
        )
    
    def _validate_structure(self, content: str) -> QualityMetric:
        """Validate overall structural integrity"""
        issues = []
        recommendations = []
        score = 0
        max_score = 15
        
        # Check for YAML frontmatter
        if not content.startswith('---'):
            issues.append("Missing YAML frontmatter")
            recommendations.append("Add proper YAML frontmatter with metadata")
        else:
            score += 3
        
        # Check for main title
        if not re.search(r'^# .+', content, re.MULTILINE):
            issues.append("Missing main title (H1)")
            recommendations.append("Add descriptive main title with # heading")
        else:
            score += 3
        
        # Check for section hierarchy
        h2_count = len(re.findall(r'^## .+', content, re.MULTILINE))
        h3_count = len(re.findall(r'^### .+', content, re.MULTILINE))
        
        if h2_count < 4:
            issues.append(f"Insufficient major sections: {h2_count} (minimum 4)")
            recommendations.append("Add more major sections (H2 headings)")
        else:
            score += 5
        
        if h3_count < 8:
            issues.append(f"Insufficient subsections: {h3_count} (minimum 8)")
            recommendations.append("Add more detailed subsections (H3 headings)")
        else:
            score += 4
        
        return QualityMetric(
            name="Structural Integrity",
            score=score,
            max_score=max_score,
            issues=issues,
            recommendations=recommendations,
            critical=True
        )
    
    def _validate_personas(self, content: str) -> QualityMetric:
        """Validate dual-persona implementation"""
        issues = []
        recommendations = []
        score = 0
        max_score = 20
        
        # Check for primary expert
        if "Primary Expert" not in content:
            issues.append("Missing Primary Expert section")
            recommendations.append("Add detailed Primary Expert persona")
        else:
            score += 8
            
            # Check for expertise depth
            primary_section = self._extract_section(content, "Primary Expert")
            if primary_section:
                if "years" not in primary_section.lower():
                    issues.append("Primary Expert lacks experience timeline")
                    recommendations.append("Specify years of experience for Primary Expert")
                else:
                    score += 2
        
        # Check for secondary expert
        if "Secondary Expert" not in content:
            issues.append("Missing Secondary Expert section")
            recommendations.append("Add complementary Secondary Expert persona")
        else:
            score += 8
            
            # Check for complementary perspective
            secondary_section = self._extract_section(content, "Secondary Expert")
            if secondary_section:
                if len(secondary_section.split()) < 50:
                    issues.append("Secondary Expert description too brief")
                    recommendations.append("Expand Secondary Expert description")
                else:
                    score += 2
        
        # Check for persona integration
        if "Primary Expert" in content and "Secondary Expert" in content:
            if "Integrated" not in content and "Combined" not in content:
                issues.append("Missing persona integration sections")
                recommendations.append("Add sections showing how personas work together")
        
        return QualityMetric(
            name="Dual-Persona Implementation",
            score=score,
            max_score=max_score,
            issues=issues,
            recommendations=recommendations,
            critical=True
        )
    
    def _validate_frameworks(self, content: str) -> QualityMetric:
        """Validate framework integration"""
        issues = []
        recommendations = []
        score = 0
        max_score = 15
        
        framework_matches = re.findall(r'### Framework \d+:', content)
        framework_count = len(framework_matches)
        
        if framework_count < 3:
            issues.append(f"Insufficient frameworks: {framework_count} (minimum 3)")
            recommendations.append("Add at least 3 professional frameworks")
        else:
            score += 10
            
            if framework_count >= 5:
                score += 3  # Bonus for comprehensive framework coverage
        
        # Check framework quality
        for i, match in enumerate(framework_matches[:3], 1):
            framework_section = self._extract_section(content, f"Framework {i}")
            if framework_section:
                if len(framework_section.split()) < 20:
                    issues.append(f"Framework {i} description too brief")
                    recommendations.append(f"Expand Framework {i} with detailed methodology")
                elif len(framework_section.split()) >= 30:
                    score += 1
        
        # Check for framework application
        if "apply" not in content.lower() and "implement" not in content.lower():
            issues.append("Missing framework application guidance")
            recommendations.append("Add sections on how to apply frameworks")
        else:
            score += 1
        
        return QualityMetric(
            name="Framework Integration",
            score=score,
            max_score=max_score,
            issues=issues,
            recommendations=recommendations,
            critical=True
        )
    
    def _validate_phases(self, content: str) -> QualityMetric:
        """Validate four-phase systematic approach"""
        issues = []
        recommendations = []
        score = 0
        max_score = 20
        
        required_phases = ["Assessment", "Design", "Implementation", "Optimization"]
        found_phases = []
        
        for phase in required_phases:
            if f"Phase" in content and phase in content:
                found_phases.append(phase)
                score += 4
            else:
                issues.append(f"Missing {phase} phase")
                recommendations.append(f"Add comprehensive {phase} phase section")
        
        # Check for phase structure
        for phase in found_phases:
            phase_section = self._extract_section(content, f"Phase.*{phase}")
            if phase_section:
                # Check for dual-expert analysis within phase
                if "Primary Expert" in phase_section and "Secondary Expert" in phase_section:
                    score += 1
                else:
                    issues.append(f"{phase} phase missing dual-expert analysis")
                    recommendations.append(f"Add both expert perspectives to {phase} phase")
        
        # Check for deliverables in phases
        phase_deliverables = len(re.findall(r'Deliverables?:', content, re.IGNORECASE))
        if phase_deliverables < 4:
            issues.append(f"Insufficient phase deliverables: {phase_deliverables} (minimum 4)")
            recommendations.append("Add specific deliverables for each phase")
        else:
            score += 4
        
        return QualityMetric(
            name="Four-Phase Approach",
            score=score,
            max_score=max_score,
            issues=issues,
            recommendations=recommendations,
            critical=True
        )
    
    def _validate_deliverables(self, content: str) -> QualityMetric:
        """Validate actionable deliverables"""
        issues = []
        recommendations = []
        score = 0
        max_score = 10
        
        deliverable_matches = re.findall(r'Deliverables?:', content, re.IGNORECASE)
        deliverable_count = len(deliverable_matches)
        
        if deliverable_count < 4:
            issues.append(f"Too few deliverable sections: {deliverable_count} (minimum 4)")
            recommendations.append("Add specific deliverables for each phase")
        else:
            score += 6
        
        # Check for numbered deliverables
        numbered_deliverables = len(re.findall(r'\d+\.\s+\w+', content))
        if numbered_deliverables < 15:
            issues.append(f"Insufficient specific deliverables: {numbered_deliverables} (minimum 15)")
            recommendations.append("Add more specific, numbered deliverables")
        else:
            score += 4
        
        return QualityMetric(
            name="Actionable Deliverables",
            score=score,
            max_score=max_score,
            issues=issues,
            recommendations=recommendations
        )
    
    def _validate_content_length(self, content: str, word_count: int, line_count: int) -> QualityMetric:
        """Validate content length requirements"""
        issues = []
        recommendations = []
        score = 0
        max_score = 10
        
        # Line count validation
        if line_count < self.min_content_lines:
            issues.append(f"Content too short: {line_count} lines (minimum {self.min_content_lines})")
            recommendations.append("Expand content to meet minimum length requirements")
        else:
            score += 5
        
        # Word count validation
        if word_count < self.min_word_count:
            issues.append(f"Word count too low: {word_count} words (minimum {self.min_word_count})")
            recommendations.append("Add more detailed explanations and examples")
        else:
            score += 5
        
        return QualityMetric(
            name="Content Length",
            score=score,
            max_score=max_score,
            issues=issues,
            recommendations=recommendations,
            critical=True
        )
    
    def _validate_language_quality(self, content: str) -> QualityMetric:
        """Validate language quality and professionalism"""
        issues = []
        recommendations = []
        score = 0
        max_score = 10
        
        # Check for weak language
        weak_matches = []
        for pattern in self.quality_patterns["weak_language"]:
            weak_matches.extend(re.findall(pattern, content, re.IGNORECASE))
        
        if len(weak_matches) > 5:
            issues.append(f"Excessive weak language: {len(weak_matches)} instances")
            recommendations.append("Replace weak language with confident, actionable terms")
        else:
            score += 3
        
        # Check for professional terminology
        prof_matches = []
        for pattern in self.quality_patterns["professional_terminology"]:
            prof_matches.extend(re.findall(pattern, content, re.IGNORECASE))
        
        if len(prof_matches) < 10:
            issues.append("Insufficient professional terminology")
            recommendations.append("Add more professional business and technical terms")
        else:
            score += 4
        
        # Check for actionable language
        action_matches = []
        for pattern in self.quality_patterns["actionable_language"]:
            action_matches.extend(re.findall(pattern, content, re.IGNORECASE))
        
        if len(action_matches) < 15:
            issues.append("Insufficient actionable language")
            recommendations.append("Use more action-oriented verbs and terms")
        else:
            score += 3
        
        return QualityMetric(
            name="Language Quality",
            score=score,
            max_score=max_score,
            issues=issues,
            recommendations=recommendations
        )
    
    def _validate_actionability(self, content: str) -> QualityMetric:
        """Validate actionability and implementability"""
        issues = []
        recommendations = []
        score = 0
        max_score = 8
        
        # Check for step-by-step guidance
        step_patterns = [r'\d+\.\s+', r'Step \d+', r'Phase \d+']
        step_count = sum(len(re.findall(pattern, content)) for pattern in step_patterns)
        
        if step_count < 10:
            issues.append("Insufficient step-by-step guidance")
            recommendations.append("Add more numbered steps and sequential instructions")
        else:
            score += 4
        
        # Check for concrete examples
        example_indicators = ["example", "for instance", "such as", "e.g.", "specifically"]
        example_count = sum(content.lower().count(indicator) for indicator in example_indicators)
        
        if example_count < 5:
            issues.append("Insufficient concrete examples")
            recommendations.append("Add more specific examples and use cases")
        else:
            score += 4
        
        return QualityMetric(
            name="Actionability",
            score=score,
            max_score=max_score,
            issues=issues,
            recommendations=recommendations
        )
    
    def _validate_professionalism(self, content: str) -> QualityMetric:
        """Validate professional tone and authority"""
        issues = []
        recommendations = []
        score = 0
        max_score = 7
        
        # Check for expertise indicators
        expertise_matches = []
        for pattern in self.quality_patterns["expertise_indicators"]:
            expertise_matches.extend(re.findall(pattern, content, re.IGNORECASE))
        
        if len(expertise_matches) < 3:
            issues.append("Insufficient expertise indicators")
            recommendations.append("Add more credibility and experience indicators")
        else:
            score += 4
        
        # Check for authority language
        authority_terms = ["proven", "established", "validated", "recognized", "industry-leading"]
        authority_count = sum(content.lower().count(term) for term in authority_terms)
        
        if authority_count < 3:
            issues.append("Lacks authoritative language")
            recommendations.append("Use more authoritative and credible language")
        else:
            score += 3
        
        return QualityMetric(
            name="Professionalism",
            score=score,
            max_score=max_score,
            issues=issues,
            recommendations=recommendations
        )
    
    def _validate_expertise_depth(self, content: str) -> QualityMetric:
        """Validate depth of expertise demonstration"""
        issues = []
        recommendations = []
        score = 0
        max_score = 8
        
        # Check for technical depth
        technical_terms = ["methodology", "framework", "architecture", "optimization", "analysis"]
        tech_count = sum(content.lower().count(term) for term in technical_terms)
        
        if tech_count < 10:
            issues.append("Insufficient technical depth")
            recommendations.append("Add more technical terminology and concepts")
        else:
            score += 4
        
        # Check for industry knowledge
        industry_terms = ["best practice", "industry standard", "compliance", "governance", "stakeholder"]
        industry_count = sum(content.lower().count(term) for term in industry_terms)
        
        if industry_count < 5:
            issues.append("Limited industry knowledge demonstration")
            recommendations.append("Include more industry-specific knowledge and standards")
        else:
            score += 4
        
        return QualityMetric(
            name="Expertise Depth",
            score=score,
            max_score=max_score,
            issues=issues,
            recommendations=recommendations
        )
    
    def _validate_yaml_frontmatter(self, content: str) -> QualityMetric:
        """Validate YAML frontmatter"""
        issues = []
        recommendations = []
        score = 0
        max_score = 5
        
        if not content.startswith('---'):
            issues.append("Missing YAML frontmatter")
            recommendations.append("Add proper YAML frontmatter")
            return QualityMetric("YAML Frontmatter", 0, max_score, issues, recommendations, True)
        
        try:
            frontmatter_end = content.find('---', 3)
            if frontmatter_end > 0:
                frontmatter = content[3:frontmatter_end]
                data = yaml.safe_load(frontmatter)
                
                required_fields = ['title', 'description', 'category', 'tags', 'slug']
                for field in required_fields:
                    if field in data:
                        score += 1
                    else:
                        issues.append(f"Missing required field: {field}")
                        recommendations.append(f"Add {field} to frontmatter")
            else:
                issues.append("Malformed YAML frontmatter")
                recommendations.append("Fix YAML frontmatter structure")
        except yaml.YAMLError:
            issues.append("Invalid YAML syntax")
            recommendations.append("Fix YAML syntax errors")
        
        return QualityMetric(
            name="YAML Frontmatter",
            score=score,
            max_score=max_score,
            issues=issues,
            recommendations=recommendations,
            critical=True
        )
    
    def _validate_markdown_structure(self, content: str) -> QualityMetric:
        """Validate markdown formatting"""
        issues = []
        recommendations = []
        score = 0
        max_score = 5
        
        # Check for proper heading hierarchy
        h1_count = len(re.findall(r'^# ', content, re.MULTILINE))
        h2_count = len(re.findall(r'^## ', content, re.MULTILINE))
        h3_count = len(re.findall(r'^### ', content, re.MULTILINE))
        
        if h1_count != 1:
            issues.append(f"Should have exactly 1 H1 heading, found {h1_count}")
            recommendations.append("Use exactly one H1 heading for the title")
        else:
            score += 2
        
        if h2_count >= 4:
            score += 2
        else:
            issues.append("Insufficient H2 headings for major sections")
            recommendations.append("Add more major sections with H2 headings")
        
        if h3_count >= 8:
            score += 1
        else:
            issues.append("Insufficient H3 headings for subsections")
            recommendations.append("Add more subsections with H3 headings")
        
        return QualityMetric(
            name="Markdown Structure",
            score=score,
            max_score=max_score,
            issues=issues,
            recommendations=recommendations
        )
    
    def _extract_section(self, content: str, section_title: str) -> Optional[str]:
        """Extract content of a specific section"""
        pattern = f"### {section_title}.*?(?=###|##|$)"
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        return match.group(0) if match else None
    
    def _estimate_output_length(self, content: str) -> int:
        """Estimate expected output length from prompt"""
        # Analyze prompt complexity and deliverables
        deliverable_count = len(re.findall(r'\d+\.\s+', content))
        phase_count = len(re.findall(r'Phase \d+', content))
        framework_count = len(re.findall(r'Framework \d+', content))
        
        # Base estimate on complexity
        base_length = 400
        complexity_multiplier = (deliverable_count * 15) + (phase_count * 50) + (framework_count * 30)
        
        return base_length + complexity_multiplier

class QualityReportGenerator:
    """Generate comprehensive quality reports"""
    
    def __init__(self, validator: PromptQualityValidator):
        self.validator = validator
    
    def generate_detailed_report(self, report: QualityReport) -> str:
        """Generate detailed quality assessment report"""
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        output = f"""
# Quality Assessment Report
**File**: {report.file_path}
**Generated**: {timestamp}
**Overall Score**: {report.overall_score:.1f}/100 (Grade: {report.grade})
**Compliance Status**: {report.compliance_status}

## Summary Statistics
- **Word Count**: {report.word_count:,}
- **Line Count**: {report.line_count:,}
- **Estimated Output Length**: {report.estimated_output_length:,} lines
- **Critical Issues**: {report.critical_issues}

## Quality Metrics Breakdown
"""
        
        for metric in report.metrics:
            critical_indicator = "🚨 CRITICAL" if metric.critical and metric.issues else ""
            output += f"""
### {metric.name} {critical_indicator}
**Score**: {metric.score:.1f}/{metric.max_score} ({metric.score/metric.max_score*100:.1f}%)

"""
            if metric.issues:
                output += "**Issues Found**:\n"
                for issue in metric.issues:
                    output += f"- ❌ {issue}\n"
                output += "\n"
            
            if metric.recommendations:
                output += "**Recommendations**:\n"
                for rec in metric.recommendations:
                    output += f"- ✅ {rec}\n"
                output += "\n"
        
        if report.recommendations:
            output += "## Overall Recommendations\n"
            for i, rec in enumerate(report.recommendations, 1):
                output += f"{i}. {rec}\n"
        
        return output
    
    def generate_summary_report(self, reports: List[QualityReport]) -> str:
        """Generate summary report for multiple prompts"""
        
        if not reports:
            return "No reports to summarize."
        
        # Calculate statistics
        total_prompts = len(reports)
        avg_score = sum(r.overall_score for r in reports) / total_prompts
        compliant_count = sum(1 for r in reports if r.compliance_status == "COMPLIANT")
        total_critical = sum(r.critical_issues for r in reports)
        
        # Grade distribution
        grade_dist = {}
        for report in reports:
            grade_dist[report.grade] = grade_dist.get(report.grade, 0) + 1
        
        # Top issues
        all_issues = []
        for report in reports:
            for metric in report.metrics:
                all_issues.extend(metric.issues)
        
        issue_counts = {}
        for issue in all_issues:
            issue_counts[issue] = issue_counts.get(issue, 0) + 1
        
        top_issues = sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        output = f"""
# Quality Assessment Summary Report
**Generated**: {timestamp}
**Total Prompts Analyzed**: {total_prompts}

## Overall Statistics
- **Average Quality Score**: {avg_score:.1f}/100
- **Compliant Prompts**: {compliant_count}/{total_prompts} ({compliant_count/total_prompts*100:.1f}%)
- **Total Critical Issues**: {total_critical}

## Grade Distribution
"""
        
        for grade, count in sorted(grade_dist.items()):
            percentage = count / total_prompts * 100
            output += f"- **{grade}**: {count} prompts ({percentage:.1f}%)\n"
        
        output += "\n## Most Common Issues\n"
        for issue, count in top_issues:
            output += f"- {issue}: {count} occurrences\n"
        
        output += "\n## Recommendations for Repository\n"
        if avg_score < 85:
            output += "- Focus on improving overall prompt quality to meet compliance standards\n"
        if compliant_count / total_prompts < 0.8:
            output += "- Implement systematic quality checks before publishing prompts\n"
        if total_critical > total_prompts * 0.5:
            output += "- Address critical structural issues across the repository\n"
        
        return output

def main():
    """Main CLI interface for quality validation"""
    parser = argparse.ArgumentParser(description="AI Prompt Quality Assurance Pipeline")
    parser.add_argument("path", help="Path to prompt file or directory")
    parser.add_argument("--output", "-o", help="Output file for report")
    parser.add_argument("--format", choices=["detailed", "summary"], default="detailed")
    parser.add_argument("--min-score", type=float, default=85.0, help="Minimum acceptable score")
    parser.add_argument("--fail-on-critical", action="store_true", help="Fail if critical issues found")
    
    args = parser.parse_args()
    
    validator = PromptQualityValidator()
    report_generator = QualityReportGenerator(validator)
    
    path = Path(args.path)
    reports = []
    
    if path.is_file():
        # Single file validation
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        report = validator.validate_prompt(content, str(path))
        reports.append(report)
        
        if args.format == "detailed":
            output = report_generator.generate_detailed_report(report)
        else:
            output = report_generator.generate_summary_report([report])
            
    elif path.is_dir():
        # Directory validation
        for md_file in path.rglob("*.md"):
            if md_file.name == "README.md":
                continue
                
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                report = validator.validate_prompt(content, str(md_file))
                reports.append(report)
                print(f"Analyzed: {md_file.name} (Score: {report.overall_score:.1f}, Grade: {report.grade})")
            except Exception as e:
                print(f"Error analyzing {md_file}: {e}")
        
        output = report_generator.generate_summary_report(reports)
    
    else:
        print(f"Error: {path} is not a valid file or directory")
        return 1
    
    # Output results
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Report saved to: {args.output}")
    else:
        print(output)
    
    # Check exit conditions
    if reports:
        avg_score = sum(r.overall_score for r in reports) / len(reports)
        critical_issues = sum(r.critical_issues for r in reports)
        
        if avg_score < args.min_score:
            print(f"FAILED: Average score {avg_score:.1f} below minimum {args.min_score}")
            return 1
        
        if args.fail_on_critical and critical_issues > 0:
            print(f"FAILED: {critical_issues} critical issues found")
            return 1
    
    print("Quality validation completed successfully!")
    return 0

if __name__ == "__main__":
    exit(main())