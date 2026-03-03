# Cross-Platform Issues

## Cross-Platform Issues

```yaml
React Native Debugging:

Console Logs:
  - Run app with: react-native run-android
  - View logs: adb logcat | grep ReactNativeJS
  - Or use remote debugger

Remote Debugging:
  - Shake device → Enable Remote Debugging
  - Chrome DevTools debugging
  - Set breakpoints in JS
  - Inspect state

Performance:
  - Perf Monitor: Shake → Perf Monitor
  - Shows FPS, RAM, Bridge traffic
  - Identify frame drops
  - Check excessive bridge calls

---
Flutter Debugging:

Device Logs: flutter logs
  Shows all device and app output

Debugging: flutter run --debug
  Set breakpoints in IDE
  Step through code

Hot Reload: Useful for rapid iteration
  Hot restart for full reload
  Useful for debugging UI changes

---
Common Mobile Issues:

Network Connectivity:
  Issue: App works on WiFi, fails on cellular
  Solution: Test on both networks
  Debug: Use network throttler
  Implement: Retry logic, offline support

Device Specific:
  Issue: Works on simulator, fails on device
  Solution: Always test on real device
  Causes:
    - Memory constraints
    - Performance differences
    - Platform differences
    - Screen size issues

Battery/Memory:
  Issue: Excessive battery drain
  Debug: Use power profiler
  Optimize: Reduce background work
  Monitor: Location tracking, networking
```
