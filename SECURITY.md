# Security Policy

## Scope

This repository contains a library of AI prompts designed for professional workflows. Unlike traditional software repositories, there is no executable code that could contain conventional security vulnerabilities such as buffer overflows, SQL injection, or authentication bypasses.

However, prompt libraries have their own unique security considerations related to content safety and prompt integrity.

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |

Only the current `main` branch is actively maintained. We do not provide security updates for historical commits or branches.

## What Constitutes a Security Issue

For a prompt library, security issues may include:

### High Priority
- **Prompt injection attacks**: Prompts designed to manipulate AI systems into bypassing safety guidelines or performing unintended actions
- **Malicious content**: Prompts that encourage or facilitate harmful, illegal, or unethical activities
- **Data exfiltration prompts**: Content designed to trick AI systems into revealing sensitive information

### Medium Priority
- **Jailbreak attempts**: Prompts crafted to circumvent AI safety measures
- **Deceptive prompts**: Content that misrepresents its purpose or contains hidden instructions
- **Social engineering templates**: Prompts designed to manipulate users or third parties

### Lower Priority
- **Biased or discriminatory content**: Prompts that promote unfair treatment of individuals or groups
- **Misinformation templates**: Prompts designed to generate false or misleading content

## Reporting a Vulnerability

If you discover a security issue in this prompt library, please report it through one of the following channels:

### Preferred: GitHub Security Advisories

1. Navigate to the [Security tab](../../security) of this repository
2. Click "Report a vulnerability"
3. Provide a detailed description of the issue

### Alternative: Private Issue

If you cannot use GitHub Security Advisories:

1. Open a new issue with the title prefix `[SECURITY]`
2. Provide minimal details publicly
3. Request a private communication channel for full disclosure

**Please do not:**
- Publicly disclose the full details of security issues before they are addressed
- Submit security reports for issues that do not fall within the scope defined above

## What to Include in Your Report

- Location of the problematic prompt (file path and line numbers if applicable)
- Description of the security concern
- Potential impact or harm that could result
- Any suggested remediation steps

## Response Timeline

| Action | Expected Timeframe |
| ------ | ------------------ |
| Initial acknowledgment | Within 48 hours |
| Preliminary assessment | Within 5 business days |
| Resolution for high-priority issues | Within 14 days |
| Resolution for medium/lower priority | Within 30 days |

These timelines are targets and may vary based on the complexity of the issue and maintainer availability.

## Our Commitment

We take the safety and integrity of this prompt library seriously. When a valid security issue is reported, we will:

1. Acknowledge receipt of your report promptly
2. Investigate the issue thoroughly
3. Remove or remediate problematic content
4. Credit reporters (unless anonymity is requested) in our changelog
5. Communicate transparently about the resolution

## Questions

For general questions about this security policy, please open a standard issue in the repository.
