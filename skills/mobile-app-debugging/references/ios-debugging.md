# iOS Debugging

## iOS Debugging

```yaml
Xcode Debugging:

Attach Debugger:
  - Xcode → Run on device
  - Set breakpoints in code
  - Step through execution
  - View variables
  - Console logs

View Logs:
  - Xcode → Window → Devices & Simulators
  - Select device → View Device Logs
  - Filter by app name
  - Check system logs for crashes

Inspect Memory:
  - Xcode → Debug → View Memory Graph
  - Identify retain cycles
  - Check object count
  - Monitor allocation growth

---
Common iOS Issues:

App Crash (SIGABRT):
  Cause: Exception in Objective-C
  Solution: Check console for error message
  Debug: Set breakpoint on exception

Memory Warning (SIGKILL):
  Cause: Too much memory usage
  Solution: Reduce memory footprint
  Optimize: Image caching, data structures

Networking:
  Issue: Network requests fail on device
  Check: Network connectivity status
  Solution: Implement Network Link Conditioner
  Test: Throttle network in Xcode
```
