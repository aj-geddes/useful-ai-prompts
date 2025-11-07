---
category: technical-workflows
date: '2025-08-18'
description: Comprehensive Python security analysis using Bandit with systematic vulnerability remediation and best practices implementation
layout: prompt
prompt: |
  I'll help you analyze and fix security vulnerabilities in your Python codebase using Bandit. Let me understand your project:

  ## Understanding Your Security Analysis Needs

  **Project Information:**
  - What Python project should I analyze?
  - Do you have an existing Bandit report (bandit.json)?
  - What is the current state of security in your codebase?
  - Are there known security issues or concerns?

  **Security Requirements:**
  - What security standards must you meet? (OWASP, PCI-DSS, HIPAA)
  - Are there specific vulnerability types you're concerned about?
  - Do you have security policies or guidelines to follow?
  - Are there compliance or audit requirements?

  **Fix Strategy:**
  - Should I fix all issues or prioritize by severity?
  - Are there vulnerabilities you want to suppress with justification?
  - Do you need approval before implementing fixes?
  - Should fixes be committed immediately or reviewed first?

  **Testing Requirements:**
  - Do you have tests that need to pass after fixes?
  - Should I validate fixes don't break functionality?
  - Are there performance considerations?
  - Do you need backward compatibility maintained?

  **Code Context:**
  - What are the main use cases of the application?
  - Are there external APIs or services integrated?
  - What data does the application handle? (PII, financial, health)
  - What is the deployment environment? (cloud, on-premises, hybrid)

  ---

  Based on your answers, I'll provide:

  ## 1. Comprehensive Security Analysis

  Systematic vulnerability assessment:
  - **Bandit Report Parsing**: JSON report analysis and categorization
  - **Severity Classification**: High, medium, low issue prioritization
  - **Vulnerability Grouping**: Issues categorized by type (B101, B102, B501, etc.)
  - **Pattern Recognition**: Recurring security issues identification
  - **Risk Assessment**: Exploitability and impact evaluation
  - **Business Context**: Exposure analysis based on application context

  ## 2. Memory and Research Integration

  Knowledge-enhanced analysis:
  - **Memory Retrieval**: Previous security patterns and fix strategies
  - **Web Research**: Latest security advisories for identified issues
  - **OWASP Guidelines**: Current recommendations for vulnerability types
  - **CVE Database**: Cross-reference with known vulnerabilities
  - **Best Practices**: Authoritative secure coding patterns
  - **Knowledge Update**: Store findings in memory for future reference

  ## 3. Strategic Fix Planning

  Prioritized remediation approach:
  - **Risk-Based Prioritization**: Severity, exploitability, impact, exposure
  - **Dependency Analysis**: Identify fix dependencies and ordering
  - **Backward Compatibility**: Ensure existing functionality preserved
  - **Testing Strategy**: Validation approach for each fix
  - **Rollback Planning**: Recovery procedures if fixes cause issues

  ## 4. Project Context Analysis

  Codebase understanding:
  - **Structure Analysis**: lc-project-context for macro understanding
  - **File Examination**: lc-get-files for affected code review
  - **Pattern Detection**: Root cause identification
  - **Documentation**: Current implementation for comparison
  - **Impact Assessment**: Changes affect on other components

  ## 5. Vulnerability-Specific Fixes

  Comprehensive security remediation:

  **B102 - exec_used:**
  - Replace exec() with safer alternatives
  - Use ast.literal_eval() for safe evaluation
  - Implement proper sandboxing if exec needed
  - Validate and sanitize all inputs

  **B103 - set_bad_file_permissions:**
  - Implement least-privilege file permissions
  - Use 0o600 for sensitive files, 0o644 for public
  - Document permission requirements
  - Add validation for permission changes

  **B104-B110 - Hardcoded Bindings:**
  - Move bindings to configuration files
  - Use environment variables for sensitive values
  - Implement proper secret management
  - Add validation for configuration loading

  **B201-B202 - Flask Debug Mode:**
  - Disable debug in production environments
  - Use environment-based configuration
  - Implement proper error handling
  - Add logging for production debugging

  **B301-B324 - Unsafe Deserialization:**
  - Replace pickle with safer alternatives (JSON, MessagePack)
  - Implement input validation and sanitization
  - Use cryptographic signatures for data integrity
  - Add version control for serialized data

  **B401-B413 - Weak Cryptography:**
  - Replace MD5/SHA1 with SHA-256 or better
  - Use secrets module for random generation
  - Implement proper key management
  - Use industry-standard libraries (cryptography, PyNaCl)

  **B501-B507 - SSL/TLS Issues:**
  - Enforce TLS 1.2 or higher
  - Validate certificates properly
  - Implement certificate pinning where appropriate
  - Use secure cipher suites

  **B601-B611 - Injection Vulnerabilities:**
  - Use parameterized queries for SQL
  - Implement input validation and sanitization
  - Use subprocess with shell=False
  - Escape outputs properly for context

  ## 6. Testing and Validation

  Quality assurance for fixes:
  - **Pre-Fix Testing**: Capture current test status
  - **Fix Implementation**: Apply security improvements
  - **Post-Fix Testing**: Validate functionality preserved
  - **Security Revalidation**: Confirm vulnerabilities fixed
  - **Performance Testing**: Ensure no degradation
  - **Integration Testing**: Validate with dependencies

  ## 7. Documentation and Reporting

  Comprehensive documentation:
  - **Fix Summary**: What was changed and why
  - **Before/After Comparison**: Code changes with explanations
  - **Security Improvements**: Risk reduction achieved
  - **Testing Results**: Validation outcomes
  - **Known Issues**: Any remaining concerns
  - **Recommendations**: Future security improvements

  ## 8. Git Integration

  Version control for security fixes:
  - **Branch Creation**: Security fix branch
  - **Incremental Commits**: Logical fix grouping
  - **Descriptive Messages**: Clear commit descriptions
  - **Code Review**: PR creation for team review
  - **Audit Trail**: Complete fix history

  ## 9. Compliance Validation

  Standards adherence verification:
  - **OWASP Top 10**: Coverage assessment
  - **CWE Mapping**: Common weakness enumeration
  - **Regulatory Requirements**: Industry-specific compliance
  - **Security Policies**: Organizational standard adherence
  - **Audit Preparation**: Documentation for compliance reviews

  ## 10. Best Practices Implementation

  Secure coding standards:
  - **Input Validation**: All user input sanitized
  - **Output Encoding**: Context-appropriate escaping
  - **Authentication**: Strong credential management
  - **Authorization**: Proper access controls
  - **Cryptography**: Industry-standard implementations
  - **Error Handling**: Secure error messages
  - **Logging**: Security event tracking

  ## 11. Prevention Strategies

  Long-term security improvement:
  - **Pre-Commit Hooks**: Bandit integration in development
  - **CI/CD Integration**: Automated security scanning
  - **Developer Training**: Secure coding practices
  - **Code Review Guidelines**: Security checklist
  - **Security Champions**: Team security advocates
  - **Regular Audits**: Periodic security assessments

  ## 12. Edge Case Handling

  Comprehensive coverage:
  - **Legacy Code**: Gradual improvement strategies
  - **Third-Party Libraries**: Dependency security
  - **Configuration Files**: Secure defaults
  - **Environment Variables**: Proper secret management
  - **Error Conditions**: Secure failure modes

  ## 13. Success Metrics

  Validation criteria:
  - All high-severity issues addressed
  - Medium/low issues prioritized and tracked
  - Tests passing after fixes
  - No functionality regression
  - Documentation complete
  - Team approval obtained
  - Compliance requirements met

  ## 14. Continuous Improvement

  Ongoing security enhancement:
  - **Metrics Tracking**: Security issue trends
  - **Tool Updates**: Latest Bandit versions
  - **Pattern Library**: Common fix patterns
  - **Knowledge Sharing**: Team learning
  - **Process Refinement**: Workflow improvements

  Tell me about your Python project and I'll perform a comprehensive security analysis with systematic vulnerability remediation using Bandit!
slug: bandit-security-analysis
tags:
- technical
- security
- python
- vulnerability-analysis
title: Bandit Security Analysis and Remediation
version: 1.0.0
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
---
