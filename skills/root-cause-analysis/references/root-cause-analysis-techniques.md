# Root Cause Analysis Techniques

## Root Cause Analysis Techniques

```yaml
Fishbone Diagram:

Main problem: Slow API Response

Branches:

  Code:
    - Inefficient algorithm
    - Missing cache
    - Unnecessary queries

  Data:
    - Large dataset
    - Missing index
    - Slow database

  Infrastructure:
    - Low CPU capacity
    - Slow network
    - Disk I/O bottleneck

  Process:
    - No monitoring
    - No load testing
    - Manual deployments

  People:
    - Lack of knowledge
    - Lack of tools
    - No peer review

---

Systemic vs. Individual Causes:

Individual: "Developer used inefficient code"
  Fix: Training
  Risk: Happens again with different person

Systemic: "No code review process"
  Fix: Implement mandatory code review
  Risk: Prevents similar issues

Prefer systemic solutions for prevention
```
