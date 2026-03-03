# Systematic RCA Process

## Systematic RCA Process

```yaml
Step 1: Gather Facts
  - When did issue occur?
  - Who detected it?
  - How many users affected?
  - What error messages?
  - What system changes deployed?
  - Check logs, metrics, alerts
  - Determine impact scope

Step 2: Reproduce
  - Can we reproduce consistently?
  - What are the exact steps?
  - What environment (prod, staging)?
  - Can we isolate to component?
  - Set up test case

Step 3: Identify Contributing Factors
  - Direct cause
  - Indirect/enabling factors
  - System vulnerabilities
  - Procedural gaps
  - Knowledge gaps

Step 4: Determine Root Cause
  - Use 5 Whys technique
  - Ask "why did this control fail?"
  - Look for systemic issues
  - Separate root cause from symptoms

Step 5: Develop Solutions
  - Immediate: Fix the symptom
  - Short-term: Prevent recurrence
  - Long-term: Systemic fix
  - Prioritize by impact/effort

Step 6: Implement & Verify
  - Implement solutions
  - Test in staging
  - Deploy carefully
  - Verify improvement
  - Monitor metrics

Step 7: Document & Share
  - Write RCA report
  - Document lesson learned
  - Share with team
  - Update procedures
  - Training if needed
```
