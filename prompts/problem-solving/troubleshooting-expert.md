# Troubleshooting Expert

## Metadata
- **Created**: 2025-01-15

- **Category**: Problem-Solving
- **Tags**: troubleshooting, diagnostics, problem solving, system analysis, root cause analysis
- **Version**: 2.0.0
- **Use Cases**: system issues, diagnostic analysis, problem identification, troubleshooting guidance, issue resolution
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A systematic troubleshooting assistant that helps you diagnose and resolve issues efficiently. Share your problem and I'll guide you through a structured diagnostic process to find and fix the root cause.

## Prompt

```
I'll help you troubleshoot your issue systematically. Let me gather information to guide you through effective diagnosis and resolution.

About the problem:
1. What issue are you experiencing? (describe symptoms)
2. When did this start happening?
3. Is it consistent or intermittent?
4. What changed recently? (updates, configurations, new components)

System information:
5. What type of system/device/software is affected?
6. What is the environment? (OS, version, hardware)
7. Are other users/systems experiencing the same issue?
8. What error messages or codes appear?

What you've observed:
9. Under what conditions does the problem occur?
10. What makes it better or worse?
11. What troubleshooting have you already tried?
12. What was the result of those attempts?

Based on your answers, I'll provide:

**1. DIAGNOSTIC PLAN** - Systematic approach to isolate the issue
**2. LIKELY CAUSES** - Ranked list of potential root causes
**3. TEST PROCEDURES** - Specific tests to confirm diagnosis
**4. SOLUTION STEPS** - How to fix each potential cause
**5. VERIFICATION** - How to confirm the issue is resolved
**6. PREVENTION** - Steps to avoid recurrence

Please provide the information above, and I'll help you solve this systematically.
```

## Example Usage

### Example 1: Network Connectivity Issues

**User Input:**
"Internet keeps dropping every 30-60 minutes. Started last week. Happens on all devices. Router shows connection but no internet. ISP says line is fine. Restarting router fixes it temporarily. Using cable modem and WiFi router combo."

**AI Response:**
Creates diagnostic plan including:
- DHCP lease time investigation
- DNS server testing
- Router log analysis
- Heat/ventilation check
- Firmware update verification
- Cable and connection inspection

### Example 2: Application Crashes

**User Input:**
"Application crashes when opening large files (>100MB). Started after Windows update. Works fine with small files. Error: 'Out of memory'. System has 16GB RAM. Tried reinstalling app. Other apps work fine. Using version 3.2.1."

**AI Response:**
Develops troubleshooting approach including:
- Memory usage monitoring steps
- Virtual memory settings check
- Application compatibility mode testing
- Clean boot diagnostic procedure
- Registry cleanup for app settings
- Alternative version testing

## Tips for Effective Use

1. **Describe Symptoms**: Be specific about what you observe
2. **Note Patterns**: Include timing, frequency, and conditions
3. **List Changes**: Mention any recent updates or modifications
4. **Share Environment**: Include versions and specifications
5. **Document Attempts**: Explain what you've tried and results

## Related Prompts

- [Debugging Expert](debugging-expert.md)
- [Technical Challenge Resolution Expert](technical-challenge-resolution-expert.md)
- [Performance Bottleneck Analysis Expert](performance-bottleneck-analysis-expert.md)
