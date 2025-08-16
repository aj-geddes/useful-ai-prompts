#!/usr/bin/env python3
"""
End-to-End Workflow Automation for AI Prompts Repository
Master orchestration system for scaling from 278 to 500+ prompts with full automation
"""

import os
import json
import time
import subprocess
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
import logging
import yaml
import concurrent.futures
from enum import Enum

# Import our custom modules
from cms_automation import PromptCMS
from quality_assurance_pipeline import PromptQualityValidator, QualityReportGenerator
from enhanced_search_system import EnhancedSearchSystem
from bulk_management_tools import BulkContentManager

class WorkflowStage(Enum):
    """Workflow execution stages"""
    PREPARATION = "preparation"
    GENERATION = "generation"
    QUALITY_VALIDATION = "quality_validation"
    JEKYLL_CONVERSION = "jekyll_conversion"
    SEARCH_INDEXING = "search_indexing"
    DEPLOYMENT = "deployment"
    CLEANUP = "cleanup"

@dataclass
class WorkflowStageResult:
    """Result of a workflow stage execution"""
    stage: WorkflowStage
    success: bool
    duration_seconds: float
    output_data: Dict[str, Any]
    errors: List[str]
    warnings: List[str]
    artifacts: List[str]  # File paths created/modified

@dataclass
class WorkflowConfiguration:
    """Complete workflow configuration"""
    # Input configuration
    generation_specs_file: Optional[str] = None
    template_file: Optional[str] = None
    quality_threshold: float = 85.0
    
    # Processing configuration
    enable_parallel_processing: bool = True
    max_workers: int = 4
    batch_size: int = 50
    
    # Quality configuration
    enable_quality_validation: bool = True
    fail_on_critical_issues: bool = True
    auto_fix_minor_issues: bool = True
    
    # Output configuration
    enable_jekyll_conversion: bool = True
    enable_search_indexing: bool = True
    enable_deployment: bool = False
    
    # Backup and safety
    enable_backup: bool = True
    backup_retention_days: int = 30
    
    # Notification configuration
    enable_notifications: bool = False
    notification_webhook: Optional[str] = None
    
    # Git integration
    enable_git_operations: bool = True
    auto_commit: bool = False
    commit_message_template: str = "Automated content update: {summary}"

@dataclass
class WorkflowExecution:
    """Complete workflow execution tracking"""
    execution_id: str
    config: WorkflowConfiguration
    start_time: datetime
    end_time: Optional[datetime] = None
    current_stage: Optional[WorkflowStage] = None
    stages: List[WorkflowStageResult] = None
    overall_success: bool = False
    summary: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.stages is None:
            self.stages = []
        if self.summary is None:
            self.summary = {}

class WorkflowOrchestrator:
    """Master workflow orchestration system"""
    
    def __init__(self, repo_root: str = None, config: WorkflowConfiguration = None):
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.config = config or WorkflowConfiguration()
        
        # Initialize component systems
        self.cms = PromptCMS(str(self.repo_root))
        self.quality_validator = PromptQualityValidator()
        self.quality_reporter = QualityReportGenerator(self.quality_validator)
        self.search_system = EnhancedSearchSystem(str(self.repo_root))
        self.bulk_manager = BulkContentManager(str(self.repo_root))
        
        # Workflow tracking
        self.active_executions = {}
        self.completed_executions = []
        
        # Logging setup
        self.logger = self._setup_logging()
        
        # Artifacts and reports
        self.reports_dir = self.repo_root / "reports"
        self.logs_dir = self.repo_root / "logs"
        self.artifacts_dir = self.repo_root / "artifacts"
        
        # Ensure directories exist
        for directory in [self.reports_dir, self.logs_dir, self.artifacts_dir]:
            directory.mkdir(exist_ok=True)
    
    def _setup_logging(self) -> logging.Logger:
        """Setup workflow logging"""
        logger = logging.getLogger('workflow_orchestrator')
        logger.setLevel(logging.INFO)
        
        # Create file handler
        log_file = self.repo_root / "logs" / "workflow.log"
        log_file.parent.mkdir(exist_ok=True)
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    def execute_full_workflow(self, generation_specs: List[Dict] = None) -> WorkflowExecution:
        """Execute complete end-to-end workflow"""
        execution_id = f"workflow_{int(time.time())}"
        execution = WorkflowExecution(
            execution_id=execution_id,
            config=self.config,
            start_time=datetime.now()
        )
        
        self.active_executions[execution_id] = execution
        self.logger.info(f"Starting workflow execution: {execution_id}")
        
        try:
            # Execute workflow stages
            stages_to_execute = [
                (WorkflowStage.PREPARATION, self._stage_preparation),
                (WorkflowStage.GENERATION, lambda ex: self._stage_generation(ex, generation_specs)),
                (WorkflowStage.QUALITY_VALIDATION, self._stage_quality_validation),
                (WorkflowStage.JEKYLL_CONVERSION, self._stage_jekyll_conversion),
                (WorkflowStage.SEARCH_INDEXING, self._stage_search_indexing),
                (WorkflowStage.DEPLOYMENT, self._stage_deployment),
                (WorkflowStage.CLEANUP, self._stage_cleanup)
            ]
            
            for stage, stage_func in stages_to_execute:
                execution.current_stage = stage
                self.logger.info(f"Executing stage: {stage.value}")
                
                stage_result = self._execute_stage(stage, stage_func, execution)
                execution.stages.append(stage_result)
                
                # Check if stage failed critically
                if not stage_result.success and self._is_critical_stage(stage):
                    self.logger.error(f"Critical stage {stage.value} failed, aborting workflow")
                    execution.overall_success = False
                    break
                
                # Log stage completion
                self.logger.info(f"Stage {stage.value} completed: {'SUCCESS' if stage_result.success else 'FAILED'}")
            
            else:
                # All stages completed
                execution.overall_success = True
            
            # Generate execution summary
            execution.summary = self._generate_execution_summary(execution)
            
        except Exception as e:
            self.logger.error(f"Workflow execution failed with exception: {e}")
            execution.overall_success = False
            execution.summary = {"error": str(e)}
        
        finally:
            execution.end_time = datetime.now()
            execution.current_stage = None
            
            # Move to completed executions
            self.completed_executions.append(execution)
            if execution_id in self.active_executions:
                del self.active_executions[execution_id]
            
            # Generate final report
            self._generate_execution_report(execution)
            
            # Send notifications if enabled
            if self.config.enable_notifications:
                self._send_notification(execution)
            
            self.logger.info(f"Workflow execution completed: {execution_id} ({'SUCCESS' if execution.overall_success else 'FAILED'})")
        
        return execution
    
    def _execute_stage(self, stage: WorkflowStage, stage_func, execution: WorkflowExecution) -> WorkflowStageResult:
        """Execute a single workflow stage with error handling"""
        start_time = time.time()
        errors = []
        warnings = []
        artifacts = []
        output_data = {}
        success = False
        
        try:
            result = stage_func(execution)
            if isinstance(result, dict):
                output_data = result
                success = result.get('success', True)
                errors.extend(result.get('errors', []))
                warnings.extend(result.get('warnings', []))
                artifacts.extend(result.get('artifacts', []))
            else:
                success = bool(result)
            
        except Exception as e:
            errors.append(f"Stage execution failed: {e}")
            self.logger.exception(f"Exception in stage {stage.value}")
        
        duration = time.time() - start_time
        
        return WorkflowStageResult(
            stage=stage,
            success=success,
            duration_seconds=duration,
            output_data=output_data,
            errors=errors,
            warnings=warnings,
            artifacts=artifacts
        )
    
    def _is_critical_stage(self, stage: WorkflowStage) -> bool:
        """Determine if a stage is critical for workflow success"""
        critical_stages = {
            WorkflowStage.PREPARATION,
            WorkflowStage.GENERATION,
            WorkflowStage.QUALITY_VALIDATION
        }
        return stage in critical_stages
    
    def _stage_preparation(self, execution: WorkflowExecution) -> Dict[str, Any]:
        """Preparation stage: validate environment and create backups"""
        self.logger.info("Executing preparation stage")
        
        artifacts = []
        warnings = []
        errors = []
        
        # Validate repository structure
        required_dirs = [self.cms.prompts_dir, self.cms.docs_dir]
        for directory in required_dirs:
            if not directory.exists():
                directory.mkdir(parents=True, exist_ok=True)
                artifacts.append(str(directory))
        
        # Create backup if enabled
        if self.config.enable_backup:
            backup_path = self.bulk_manager.create_backup("workflow_execution")
            if backup_path:
                artifacts.append(backup_path)
        
        # Validate git repository state
        if self.config.enable_git_operations:
            try:
                git_status = subprocess.run(['git', 'status', '--porcelain'], 
                                          capture_output=True, text=True, cwd=self.repo_root)
                if git_status.returncode == 0:
                    if git_status.stdout.strip():
                        warnings.append("Working directory has uncommitted changes")
                else:
                    warnings.append("Not a git repository or git not available")
            except Exception as e:
                warnings.append(f"Git validation failed: {e}")
        
        # Clean up old artifacts
        self._cleanup_old_artifacts()
        
        return {
            'success': True,
            'artifacts': artifacts,
            'warnings': warnings,
            'errors': errors,
            'preparation_data': {
                'backup_enabled': self.config.enable_backup,
                'git_available': len([w for w in warnings if 'git' in w.lower()]) == 0
            }
        }
    
    def _stage_generation(self, execution: WorkflowExecution, generation_specs: List[Dict] = None) -> Dict[str, Any]:
        """Generation stage: create new prompts"""
        self.logger.info("Executing generation stage")
        
        if not generation_specs:
            # Load from file if specified
            if self.config.generation_specs_file and Path(self.config.generation_specs_file).exists():
                with open(self.config.generation_specs_file, 'r') as f:
                    generation_specs = json.load(f)
            else:
                return {
                    'success': True,
                    'warnings': ['No generation specs provided, skipping generation'],
                    'generated_count': 0
                }
        
        # Execute bulk generation
        operation = self.bulk_manager.bulk_generate_prompts(generation_specs, self.config.template_file)
        
        return {
            'success': operation.failed_count == 0,
            'errors': operation.errors,
            'artifacts': operation.results,
            'generated_count': operation.completed_count,
            'failed_count': operation.failed_count,
            'operation_id': operation.operation_id
        }
    
    def _stage_quality_validation(self, execution: WorkflowExecution) -> Dict[str, Any]:
        """Quality validation stage: validate all prompts"""
        self.logger.info("Executing quality validation stage")
        
        reports = []
        total_prompts = 0
        compliant_prompts = 0
        critical_issues = 0
        
        # Validate all prompts in the repository
        for md_file in self.cms.prompts_dir.rglob("*.md"):
            if md_file.name == "README.md":
                continue
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                report = self.quality_validator.validate_prompt(content, str(md_file))
                reports.append(report)
                total_prompts += 1
                
                if report.compliance_status == "COMPLIANT":
                    compliant_prompts += 1
                
                critical_issues += report.critical_issues
                
            except Exception as e:
                self.logger.error(f"Error validating {md_file}: {e}")
        
        # Generate summary report
        summary_report = self.quality_reporter.generate_summary_report(reports)
        report_file = self.reports_dir / f"quality_report_{int(time.time())}.md"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(summary_report)
        
        # Determine if validation passed
        compliance_rate = (compliant_prompts / total_prompts * 100) if total_prompts > 0 else 100
        validation_passed = compliance_rate >= self.config.quality_threshold
        
        if self.config.fail_on_critical_issues and critical_issues > 0:
            validation_passed = False
        
        result = {
            'success': validation_passed,
            'artifacts': [str(report_file)],
            'total_prompts': total_prompts,
            'compliant_prompts': compliant_prompts,
            'compliance_rate': compliance_rate,
            'critical_issues': critical_issues,
            'quality_threshold': self.config.quality_threshold
        }
        
        if not validation_passed:
            result['errors'] = [f"Quality validation failed: {compliance_rate:.1f}% compliance (threshold: {self.config.quality_threshold}%)"]
            if critical_issues > 0:
                result['errors'].append(f"{critical_issues} critical issues found")
        
        return result
    
    def _stage_jekyll_conversion(self, execution: WorkflowExecution) -> Dict[str, Any]:
        """Jekyll conversion stage: convert prompts to Jekyll format"""
        if not self.config.enable_jekyll_conversion:
            return {'success': True, 'warnings': ['Jekyll conversion disabled']}
        
        self.logger.info("Executing Jekyll conversion stage")
        
        # Execute bulk conversion
        operation = self.bulk_manager.bulk_convert_to_jekyll()
        
        return {
            'success': operation.failed_count == 0,
            'errors': operation.errors,
            'artifacts': operation.results,
            'converted_count': operation.completed_count,
            'failed_count': operation.failed_count,
            'operation_id': operation.operation_id
        }
    
    def _stage_search_indexing(self, execution: WorkflowExecution) -> Dict[str, Any]:
        """Search indexing stage: build optimized search index"""
        if not self.config.enable_search_indexing:
            return {'success': True, 'warnings': ['Search indexing disabled']}
        
        self.logger.info("Executing search indexing stage")
        
        try:
            # Build enhanced search index
            search_index = self.search_system.build_enhanced_index()
            
            # Save index
            index_file = self.search_system.assets_dir / "enhanced-search-index.json"
            self.search_system.save_search_index(search_index, str(index_file))
            
            # Also update the main PROMPT-INDEX.json for backward compatibility
            main_index = self.cms.optimize_search_index()
            
            return {
                'success': True,
                'artifacts': [str(index_file), str(self.cms.docs_dir / "assets" / "data" / "search-index.json")],
                'indexed_prompts': search_index.total_prompts,
                'index_size_mb': search_index.performance_metrics.get('index_memory_estimate_mb', 0),
                'build_time_seconds': search_index.performance_metrics.get('build_time_seconds', 0)
            }
            
        except Exception as e:
            return {
                'success': False,
                'errors': [f"Search indexing failed: {e}"]
            }
    
    def _stage_deployment(self, execution: WorkflowExecution) -> Dict[str, Any]:
        """Deployment stage: deploy to production if enabled"""
        if not self.config.enable_deployment:
            return {'success': True, 'warnings': ['Deployment disabled']}
        
        self.logger.info("Executing deployment stage")
        
        artifacts = []
        errors = []
        warnings = []
        
        try:
            # Git operations if enabled
            if self.config.enable_git_operations:
                self._git_add_changes()
                
                if self.config.auto_commit:
                    commit_message = self.config.commit_message_template.format(
                        summary=self._generate_commit_summary(execution)
                    )
                    self._git_commit(commit_message)
                    artifacts.append("Git commit created")
            
            # Additional deployment steps could be added here
            # (e.g., triggering GitHub Pages build, uploading to CDN, etc.)
            
            return {
                'success': True,
                'artifacts': artifacts,
                'warnings': warnings,
                'errors': errors
            }
            
        except Exception as e:
            return {
                'success': False,
                'errors': [f"Deployment failed: {e}"]
            }
    
    def _stage_cleanup(self, execution: WorkflowExecution) -> Dict[str, Any]:
        """Cleanup stage: clean up temporary files and old backups"""
        self.logger.info("Executing cleanup stage")
        
        artifacts = []
        warnings = []
        
        # Clean up old backups
        if self.config.enable_backup:
            cleaned_backups = self._cleanup_old_backups()
            if cleaned_backups:
                artifacts.extend(cleaned_backups)
        
        # Clean up old reports
        cleaned_reports = self._cleanup_old_reports()
        if cleaned_reports:
            artifacts.extend(cleaned_reports)
        
        # Clean up temporary files
        temp_files = list(self.repo_root.glob("*.tmp"))
        for temp_file in temp_files:
            try:
                temp_file.unlink()
                artifacts.append(f"Removed temp file: {temp_file}")
            except Exception as e:
                warnings.append(f"Failed to remove {temp_file}: {e}")
        
        return {
            'success': True,
            'artifacts': artifacts,
            'warnings': warnings,
            'cleanup_items': len(artifacts)
        }
    
    def _cleanup_old_artifacts(self):
        """Clean up old artifacts and temporary files"""
        # Implementation for cleaning up old files
        pass
    
    def _cleanup_old_backups(self) -> List[str]:
        """Clean up backups older than retention period"""
        cleaned = []
        cutoff_time = time.time() - (self.config.backup_retention_days * 24 * 3600)
        
        for backup_dir in self.bulk_manager.backup_dir.iterdir():
            if backup_dir.is_dir():
                try:
                    if backup_dir.stat().st_mtime < cutoff_time:
                        # Remove old backup
                        import shutil
                        shutil.rmtree(backup_dir)
                        cleaned.append(f"Removed old backup: {backup_dir.name}")
                except Exception as e:
                    self.logger.warning(f"Failed to remove old backup {backup_dir}: {e}")
        
        return cleaned
    
    def _cleanup_old_reports(self) -> List[str]:
        """Clean up old reports"""
        cleaned = []
        cutoff_time = time.time() - (7 * 24 * 3600)  # Keep reports for 7 days
        
        for report_file in self.reports_dir.glob("*.md"):
            try:
                if report_file.stat().st_mtime < cutoff_time:
                    report_file.unlink()
                    cleaned.append(f"Removed old report: {report_file.name}")
            except Exception as e:
                self.logger.warning(f"Failed to remove old report {report_file}: {e}")
        
        return cleaned
    
    def _git_add_changes(self):
        """Add changes to git staging area"""
        try:
            subprocess.run(['git', 'add', '.'], check=True, cwd=self.repo_root)
            self.logger.info("Added changes to git staging area")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Git add failed: {e}")
    
    def _git_commit(self, message: str):
        """Create git commit with message"""
        try:
            subprocess.run(['git', 'commit', '-m', message], check=True, cwd=self.repo_root)
            self.logger.info(f"Created git commit: {message}")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Git commit failed: {e}")
    
    def _generate_commit_summary(self, execution: WorkflowExecution) -> str:
        """Generate summary for git commit message"""
        generation_stage = next((s for s in execution.stages if s.stage == WorkflowStage.GENERATION), None)
        if generation_stage and generation_stage.output_data.get('generated_count', 0) > 0:
            return f"Added {generation_stage.output_data['generated_count']} new prompts"
        else:
            return "Automated content maintenance and updates"
    
    def _generate_execution_summary(self, execution: WorkflowExecution) -> Dict[str, Any]:
        """Generate comprehensive execution summary"""
        summary = {
            'execution_id': execution.execution_id,
            'duration_seconds': (execution.end_time - execution.start_time).total_seconds() if execution.end_time else 0,
            'overall_success': execution.overall_success,
            'stages_executed': len(execution.stages),
            'stages_succeeded': len([s for s in execution.stages if s.success]),
            'stages_failed': len([s for s in execution.stages if not s.success]),
            'total_errors': sum(len(s.errors) for s in execution.stages),
            'total_warnings': sum(len(s.warnings) for s in execution.stages),
            'total_artifacts': sum(len(s.artifacts) for s in execution.stages),
            'stage_details': {}
        }
        
        # Add stage-specific details
        for stage_result in execution.stages:
            summary['stage_details'][stage_result.stage.value] = {
                'success': stage_result.success,
                'duration_seconds': stage_result.duration_seconds,
                'output_data': stage_result.output_data,
                'error_count': len(stage_result.errors),
                'warning_count': len(stage_result.warnings),
                'artifact_count': len(stage_result.artifacts)
            }
        
        return summary
    
    def _generate_execution_report(self, execution: WorkflowExecution):
        """Generate detailed execution report"""
        report_file = self.reports_dir / f"workflow_execution_{execution.execution_id}.json"
        
        report_data = {
            'execution': asdict(execution),
            'timestamp': datetime.now().isoformat(),
            'repository_state': {
                'total_prompts': len(list(self.cms.prompts_dir.rglob("*.md"))),
                'jekyll_prompts': len(list(self.cms.jekyll_prompts_dir.glob("*.md"))),
                'categories': len([d for d in self.cms.prompts_dir.iterdir() if d.is_dir()])
            }
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, default=str)
        
        self.logger.info(f"Execution report saved: {report_file}")
    
    def _send_notification(self, execution: WorkflowExecution):
        """Send workflow completion notification"""
        if not self.config.notification_webhook:
            return
        
        # Implementation for sending webhook notifications
        # This would depend on the specific notification system being used
        pass
    
    def get_execution_status(self, execution_id: str) -> Optional[WorkflowExecution]:
        """Get status of workflow execution"""
        if execution_id in self.active_executions:
            return self.active_executions[execution_id]
        
        for execution in self.completed_executions:
            if execution.execution_id == execution_id:
                return execution
        
        return None
    
    def list_executions(self, limit: int = 10) -> List[WorkflowExecution]:
        """List recent workflow executions"""
        all_executions = list(self.active_executions.values()) + self.completed_executions
        all_executions.sort(key=lambda x: x.start_time, reverse=True)
        return all_executions[:limit]
    
    def generate_workflow_analytics(self) -> Dict[str, Any]:
        """Generate workflow performance analytics"""
        all_executions = self.list_executions(limit=100)
        
        if not all_executions:
            return {'message': 'No workflow executions found'}
        
        successful_executions = [e for e in all_executions if e.overall_success]
        failed_executions = [e for e in all_executions if not e.overall_success]
        
        analytics = {
            'timestamp': datetime.now().isoformat(),
            'total_executions': len(all_executions),
            'successful_executions': len(successful_executions),
            'failed_executions': len(failed_executions),
            'success_rate': len(successful_executions) / len(all_executions) * 100,
            'average_duration_seconds': sum((e.end_time - e.start_time).total_seconds() 
                                          for e in all_executions if e.end_time) / len(all_executions),
            'stage_success_rates': {},
            'common_errors': [],
            'performance_trends': {}
        }
        
        # Calculate stage success rates
        stage_stats = {}
        for execution in all_executions:
            for stage_result in execution.stages:
                stage_name = stage_result.stage.value
                if stage_name not in stage_stats:
                    stage_stats[stage_name] = {'total': 0, 'successful': 0}
                stage_stats[stage_name]['total'] += 1
                if stage_result.success:
                    stage_stats[stage_name]['successful'] += 1
        
        for stage_name, stats in stage_stats.items():
            analytics['stage_success_rates'][stage_name] = stats['successful'] / stats['total'] * 100
        
        return analytics

def main():
    """Main CLI interface for workflow orchestration"""
    parser = argparse.ArgumentParser(description="Workflow Orchestration System")
    parser.add_argument("--repo-root", default=".", help="Repository root directory")
    parser.add_argument("--config-file", help="Workflow configuration file")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Execute workflow command
    exec_parser = subparsers.add_parser("execute", help="Execute full workflow")
    exec_parser.add_argument("--specs-file", help="Generation specifications file")
    exec_parser.add_argument("--template", help="Template file for generation")
    exec_parser.add_argument("--quality-threshold", type=float, default=85.0, help="Quality threshold")
    exec_parser.add_argument("--enable-deployment", action="store_true", help="Enable deployment stage")
    exec_parser.add_argument("--auto-commit", action="store_true", help="Auto-commit changes")
    
    # Status command
    status_parser = subparsers.add_parser("status", help="Check execution status")
    status_parser.add_argument("--execution-id", help="Specific execution ID")
    
    # Analytics command
    analytics_parser = subparsers.add_parser("analytics", help="Generate workflow analytics")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List recent executions")
    list_parser.add_argument("--limit", type=int, default=10, help="Number of executions to show")
    
    args = parser.parse_args()
    
    # Load configuration
    config = WorkflowConfiguration()
    if args.config_file and Path(args.config_file).exists():
        with open(args.config_file, 'r') as f:
            config_data = yaml.safe_load(f)
            for key, value in config_data.items():
                if hasattr(config, key):
                    setattr(config, key, value)
    
    # Override config with command line arguments
    if hasattr(args, 'quality_threshold'):
        config.quality_threshold = args.quality_threshold
    if hasattr(args, 'enable_deployment'):
        config.enable_deployment = args.enable_deployment
    if hasattr(args, 'auto_commit'):
        config.auto_commit = args.auto_commit
    
    orchestrator = WorkflowOrchestrator(args.repo_root, config)
    
    if args.command == "execute":
        # Load generation specs if provided
        generation_specs = None
        if args.specs_file and Path(args.specs_file).exists():
            with open(args.specs_file, 'r') as f:
                generation_specs = json.load(f)
        
        # Set template file
        if args.template:
            config.template_file = args.template
        
        # Execute workflow
        print("Starting workflow execution...")
        execution = orchestrator.execute_full_workflow(generation_specs)
        
        print(f"Workflow completed: {'SUCCESS' if execution.overall_success else 'FAILED'}")
        print(f"Execution ID: {execution.execution_id}")
        print(f"Duration: {(execution.end_time - execution.start_time).total_seconds():.2f} seconds")
        
        # Print stage summary
        for stage_result in execution.stages:
            status = "✓" if stage_result.success else "✗"
            print(f"  {status} {stage_result.stage.value}: {stage_result.duration_seconds:.2f}s")
            if stage_result.errors:
                for error in stage_result.errors[:3]:  # Show first 3 errors
                    print(f"    Error: {error}")
        
    elif args.command == "status":
        if args.execution_id:
            execution = orchestrator.get_execution_status(args.execution_id)
            if execution:
                print(json.dumps(asdict(execution), indent=2, default=str))
            else:
                print(f"Execution {args.execution_id} not found")
        else:
            # Show active executions
            active = list(orchestrator.active_executions.values())
            if active:
                print("Active executions:")
                for execution in active:
                    print(f"  {execution.execution_id}: {execution.current_stage.value if execution.current_stage else 'Unknown'}")
            else:
                print("No active executions")
    
    elif args.command == "analytics":
        analytics = orchestrator.generate_workflow_analytics()
        print(json.dumps(analytics, indent=2, default=str))
    
    elif args.command == "list":
        executions = orchestrator.list_executions(args.limit)
        print(f"Recent workflow executions (last {len(executions)}):")
        for execution in executions:
            status = "✓" if execution.overall_success else "✗"
            duration = (execution.end_time - execution.start_time).total_seconds() if execution.end_time else 0
            print(f"  {status} {execution.execution_id}: {execution.start_time.strftime('%Y-%m-%d %H:%M:%S')} ({duration:.1f}s)")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()