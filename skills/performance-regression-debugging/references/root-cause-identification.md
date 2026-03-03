# Root Cause Identification

## Root Cause Identification

```yaml
Systematic Search:

Step 1: Identify Changed Code
  - Check git commits between versions
  - Review code review comments
  - Identify risky changes
  - Prioritize by likelyhood

Step 2:
  Binary Search (Bisect)
  - Start with suspected change
  - Disable the change
  - Re-measure performance
  - If improves → this is the issue
  - If not → disable other changes

  git bisect start
  git bisect bad HEAD
  git bisect good v1.0.0
  # Test each commit

Step 3: Profile the Change
  - Run profiler on old vs new code
  - Compare flame graphs
  - Identify expensive functions
  - Check allocation patterns

Step 4: Analyze Impact
  - Code review the change
  - Understand what changed
  - Check for O(n²) algorithms
  - Look for new database queries
  - Check for missing indexes

---
Common Regressions:

N+1 Query:
  Before: 1 query (10ms)
  After: 1000 queries (1000ms)
  Caused: Removed JOIN, now looping
  Fix: Restore JOIN or use eager loading

Missing Index:
  Before: Index Scan (10ms)
  After: Seq Scan (500ms)
  Caused: New filter column, no index
  Fix: Add index

Memory Leak:
  Before: 50MB memory
  After: 500MB after 1 hour
  Caused: Listener not removed, cache grows
  Fix: Clean up properly

Bundle Size:
  Before: 150KB gzipped
  After: 250KB gzipped
  Caused: Added library without tree-shaking
  Fix: Use lighter alternative or split

Algorithm Efficiency:
  Before: O(n) = 1ms for 1000 items
  After: O(n²) = 1000ms for 1000 items
  Caused: Nested loops added
  Fix: Use better algorithm
```
