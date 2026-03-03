# Android Debugging

## Android Debugging

```yaml
Android Studio:

Attach Debugger:
  - Run → Debug
  - Set breakpoints
  - Step through code
  - Watch variables
  - Evaluate expressions

Logcat:
  - Displays all app logs
  - Filter by tag
  - Filter by process
  - Show errors and warnings

Device Monitor:
  - Memory profiler
  - CPU profiler
  - Network profiler
  - Battery usage

---
Common Android Issues:

App Crash (ANR):
  Cause: Long-running operation on main thread
  Solution: Move to background thread
  Example: Use AsyncTask or coroutines

Memory Leak:
  Cause: Activity not garbage collected
  Solution: Clear references in onDestroy
  Debug: Android Profiler shows retained objects

Networking:
  Issue: Network requests timeout
  Check: Network connectivity
  Solution: Implement timeout and retry
  Test: Simulate poor network
```
