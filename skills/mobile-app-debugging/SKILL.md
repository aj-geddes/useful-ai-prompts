---
name: mobile-app-debugging
description: >
  Debug issues specific to mobile applications including platform-specific.
  Use when app crashes on mobile, performance issues on device, platform-specific bugs, or network connectivity issues.
  problems, device constraints, and connectivity issues.
---

# Mobile App Debugging

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Mobile app debugging addresses platform-specific issues, device hardware limitations, and mobile-specific network conditions.

## When to Use

- App crashes on mobile
- Performance issues on device
- Platform-specific bugs
- Network connectivity issues
- Device-specific problems

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [iOS Debugging](references/ios-debugging.md) | iOS Debugging |
| [Android Debugging](references/android-debugging.md) | Android Debugging |
| [Cross-Platform Issues](references/cross-platform-issues.md) | Cross-Platform Issues |
| [Mobile Testing & Debugging Checklist](references/mobile-testing-debugging-checklist.md) | Mobile Testing & Debugging Checklist |

## Best Practices

### ✅ DO

- Test on real devices across OS versions — simulators miss GPU, memory, and thermal throttling behavior
- Use platform-specific profilers (Xcode Instruments, Android Studio Profiler) to measure CPU, memory, and energy impact
- Reproduce crashes by symbolizing crash logs and matching to the exact build version and device model
- Test under degraded network conditions (airplane mode toggle, 3G throttling, high latency) to catch connectivity edge cases
- Check for retain cycles (iOS) and Activity/Context leaks (Android) as a routine part of debugging memory issues

### ❌ DON'T

- Assume behavior on one OS version applies to all — API deprecations and permission changes break across versions
- Block the main/UI thread with synchronous network calls, heavy computation, or large database reads
- Ignore low-memory warnings (`didReceiveMemoryWarning`, `onTrimMemory`) — the OS will terminate unresponsive apps
- Test only on high-end devices — budget devices with limited RAM and slower CPUs expose real-world performance issues
