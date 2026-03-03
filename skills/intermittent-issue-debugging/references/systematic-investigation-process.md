# Systematic Investigation Process

## Systematic Investigation Process

```yaml
Step 1: Understand the Pattern
  Questions:
    - How often does it occur? (1/100, 1/1000?)
    - When does it occur? (time of day, load, specific user?)
    - What are the conditions? (network, memory, load?)
    - Is it reproducible? (deterministic or random?)
    - Any recent changes?

  Analysis:
    - Review error logs
    - Check error rate trends
    - Identify patterns
    - Correlate with changes

Step 2: Reproduce Reliably
  Methods:
    - Increase test frequency (run 1000 times)
    - Stress test (heavy load)
    - Simulate poor conditions (network, memory)
    - Run on different machines
    - Run in production-like environment

  Goal: Make issue consistent to analyze

Step 3: Add Instrumentation
  - Add detailed logging
  - Add monitoring metrics
  - Add trace IDs
  - Capture errors fully
  - Log system state

Step 4: Capture the Issue
  - Recreate scenario
  - Capture full context
  - Note system state
  - Document conditions
  - Get reproduction case

Step 5: Analyze Data
  - Review logs
  - Look for patterns
  - Compare normal vs error cases
  - Check timing correlations
  - Identify root cause

Step 6: Implement Fix
  - Based on root cause
  - Verify with reproduction case
  - Test extensively
  - Add regression test
```
