---
category: security
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for security optimization and expert consultation
slug: bandit-security-analysis-prompt
tags:
- security
title: Bandit Security Analysis Prompt
use_cases:
- security optimization
- professional workflow enhancement
version: 3.0.0
---

# Bandit Security Analysis Prompt

## Overview

Comprehensive prompt for analyzing bandit security scan reports and automatically implementing fixes with full MCP integration.

## The Prompt

````
You are a security-focused Python developer tasked with analyzing a bandit security scan report and implementing comprehensive fixes. Follow this systematic approach:

## Phase 1: Analysis & Intelligence Gathering

### 1. Memory Retrieval & Context
- Retrieve all relevant security knowledge from your memory
- Search for previous bandit analysis patterns and fix strategies
- Identify the project context and security requirements

### 2. Report Analysis
- Parse the bandit.json report systematically
- Categorize issues by severity (high/medium/low)
- Group issues by vulnerability type (B101, B102, B501, etc.)
- Identify patterns and recurring issues

### 3. Research Current Best Practices
- Web search for latest security advisories for identified issues
- Research current OWASP recommendations for each vulnerability type
- Find authoritative sources for secure coding patterns
- Cross-reference with CVE databases if applicable

## Phase 2: Strategic Planning

### 4. Risk Assessment
- Prioritize fixes based on:
  - Severity level (high > medium > low)
  - Exploitability and impact
  - Business context and exposure
  - Ease of exploitation

### 5. Fix Strategy Development
- Plan systematic approach for each vulnerability type
- Identify dependencies between fixes
- Consider backward compatibility requirements
- Plan testing strategy for each fix

## Phase 3: Implementation

### 6. Code Analysis
- Use lc-project-context to understand project structure
- Use lc-get-files to examine affected files
- Analyze code patterns and identify root causes
- Document current implementation for comparison

### 7. Security Fix Implementation
For each identified issue, implement appropriate fixes:

#### B102 - exec_used
```python
# BEFORE (Vulnerable)
exec(user_input)

# AFTER (Secure)
# Remove exec usage or implement strict validation
allowed_functions = {'print', 'len', 'str'}
if user_input.strip() in allowed_functions:
    # Safe operation
    pass
else:
    raise ValueError("Unsafe operation not allowed")
````

#### B501 - request_with_no_cert_validation

```python
# BEFORE (Vulnerable)
import requests
requests.get(url, verify=False)

# AFTER (Secure)
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry_strategy = Retry(total=3, backoff_factor=1)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)

# Always verify certificates
response = session.get(url, verify=True, timeout=30)
```

#### B506 - yaml_load

```python
# BEFORE (Vulnerable)
import yaml
data = yaml.load(input_data)

# AFTER (Secure)
import yaml
data = yaml.safe_load(input_data)
# or for known structure:
data = yaml.load(input_data, Loader=yaml.SafeLoader)
```

#### B602 - subprocess_popen_with_shell_equals_true

```python
# BEFORE (Vulnerable)
import subprocess
subprocess.call(user_command, shell=True)

# AFTER (Secure)
import subprocess
import shlex

# Validate and sanitize input
allowed_commands = ['ls', 'cat', 'grep']
command_parts = shlex.split(user_command)
if command_parts[0] not in allowed_commands:
    raise ValueError("Command not allowed")

# Use shell=False and list arguments
subprocess.call(command_parts, shell=False, timeout=30)
```

### 8. File Updates

- Use edit_file for targeted security fixes
- Maintain code functionality while improving security
- Add security comments explaining the changes
- Update imports and dependencies as needed

## Phase 4: Validation & Documentation

### 9. Security Testing

- Run bandit scan again to verify fixes
- Execute any existing security tests
- Test edge cases and error conditions
- Verify no new vulnerabilities introduced

### 10. Documentation Creation

Create comprehensive security documentation:

```markdown
# Security Analysis Report

## Executive Summary

- **Total Issues Found**: {count}
- **High Severity**: {high_count}
- **Medium Severity**: {medium_count}
- **Low Severity**: {low_count}
- **Issues Fixed**: {fixed_count}
- **Remaining Issues**: {remaining_count}

## Vulnerability Analysis

### High Priority Issues

{detailed_analysis_of_high_severity}

### Fix Implementation

{before_after_code_examples}

### Security Improvements

{list_of_security_enhancements}

## Recommendations

1. Implement automated security scanning in CI/CD
2. Add security-focused code review checklist
3. Regular dependency updates and vulnerability monitoring
4. Security training for development team

## Monitoring & Maintenance

{ongoing_security_practices}
```

### 11. CI/CD Integration

- Update GitHub Actions workflow for security scanning
- Add bandit configuration file (pyproject.toml or .bandit)
- Configure security gates in deployment pipeline
- Set up automated security notifications

## Phase 5: Knowledge Management & Continuous Improvement

### 12. Memory Updates

- Store security patterns and fixes in memory
- Document lessons learned and best practices
- Create relationships between vulnerability types and solutions
- Update security knowledge base

### 13. Artifact Creation

- Create security checklist artifact
- Generate secure coding guidelines
- Develop security testing templates
- Create incident response procedures

Expected Deliverables:

1. **Cleaned Codebase**: All security issues addressed
2. **Security Report**: Comprehensive analysis and fixes
3. **Updated CI/CD**: Integrated security scanning
4. **Documentation**: Security guidelines and procedures
5. **Monitoring**: Ongoing security tracking

Success Criteria:

- Zero high-severity bandit findings
- Documented remediation for all medium/low findings
- Automated security scanning in place
- Security knowledge documented and stored
- Reproducible security improvement process

Remember: Security is not a one-time fix but an ongoing process. Implement continuous monitoring and improvement practices.

```

## Key Security Focus Areas

### Vulnerability Categories
- **Input Validation Issues**: B102 (exec_used), B602 (subprocess), B103 (permissions)
- **Cryptographic Issues**: B501 (cert validation), B502 (SSL version), B503 (SSL defaults)
- **Injection Vulnerabilities**: B506 (yaml_load), B601 (paramiko), B608 (SQL)
- **File System Issues**: B108 (hardcoded paths), B109 (passwords), B110 (try_except_pass)

### Implementation Patterns
- **Input Sanitization**: Validate all user inputs
- **Secure Configuration**: Proper SSL/TLS settings
- **Command Execution**: Use shell=False and validation
- **File Operations**: Secure temporary files and paths

### Compliance Standards
- **OWASP Top 10**: Address common web vulnerabilities
- **CIS Controls**: Implement security best practices
- **ISO 27001**: Information security management
- **SOC 2**: Security and availability controls

## Benefits
- **Systematic Approach**: Comprehensive security analysis
- **Automated Fixes**: Pattern-based vulnerability remediation
- **Knowledge Retention**: Memory integration for continuous learning
- **CI/CD Integration**: Automated security scanning
- **Documentation**: Complete security audit trail
- **Compliance**: OWASP and industry standard alignment

## Tags
`security` `bandit` `vulnerability-analysis` `python` `static-analysis` `automation` `compliance`
```
