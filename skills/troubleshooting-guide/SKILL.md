---
name: troubleshooting-guide
description: >
  Create comprehensive troubleshooting guides, FAQ documents, known issues
  lists, and debug guides. Use when documenting common problems, error messages,
  or debugging procedures.
---

# Troubleshooting Guide

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Create structured troubleshooting documentation that helps users and support teams quickly diagnose and resolve common issues.

## When to Use

- FAQ documentation
- Common error messages
- Debug guides
- Known issues lists
- Error code reference
- Performance troubleshooting
- Configuration issues
- Installation problems

## Quick Start

- Installation problems

````markdown
# Troubleshooting Guide

## Quick Diagnosis

### Is the Service Working?

Check our [Status Page](https://status.example.com) first.

### Quick Health Checks

```bash
# 1. Check service is running
curl https://api.example.com/health

# 2. Check your API key
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.example.com/api/v1/status

# 3. Check network connectivity
ping api.example.com

# 4. Check DNS resolution
nslookup api.example.com
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Issue: "Authentication Failed"](references/issue-authentication-failed.md) | Issue: "Authentication Failed" |
| [Issue: "Rate Limit Exceeded"](references/issue-rate-limit-exceeded.md) | Issue: "Rate Limit Exceeded" |
| [Issue: "Connection Timeout"](references/issue-connection-timeout.md) | Issue: "Connection Timeout" |
| [Issue: "Invalid JSON Response"](references/issue-invalid-json-response.md) | Issue: "Invalid JSON Response" |
| [Issue: "Slow Performance"](references/issue-slow-performance.md) | Issue: "Slow Performance" |

## Best Practices

### ✅ DO

- Start with most common issues
- Include error messages verbatim
- Provide step-by-step diagnostics
- Show expected vs actual output
- Include code examples
- Document error codes
- Add screenshots/videos
- Link to related documentation
- Keep solutions up-to-date
- Include workarounds
- Test all solutions

### ❌ DON'T

- Use vague descriptions
- Skip diagnostic steps
- Forget to show examples
- Assume technical knowledge
- Skip verification steps
- Forget edge cases
