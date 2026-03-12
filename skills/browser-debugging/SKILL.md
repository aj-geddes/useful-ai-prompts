---
name: browser-debugging
description: >
  Debug client-side issues using browser developer tools. Identify JavaScript.
  Use when javascript errors, layout/styling issues, performance problems, or user interaction issues.
  errors, styling issues, and performance problems in the browser.
---

# Browser Debugging

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Browser debugging tools help identify and fix client-side issues including JavaScript errors, layout problems, and performance issues.

## When to Use

- JavaScript errors
- Layout/styling issues
- Performance problems
- User interaction issues
- Network request failures
- Animation glitches

## Quick Start

Minimal working example:

```yaml
Chrome DevTools Tabs:

Elements/Inspector:
  - Inspect HTML structure
  - Edit HTML/CSS in real-time
  - View computed styles
  - Check accessibility tree
  - Modify DOM

Console:
  - View JavaScript errors
  - Execute JavaScript
  - View console logs
  - Monitor messages
  - Clear errors

Sources/Debugger:
  - Set breakpoints
  - Step through code
  - Watch variables
  - Call stack view
  - Conditional breakpoints

Network:
  - View all requests
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Browser DevTools Fundamentals](references/browser-devtools-fundamentals.md) | Browser DevTools Fundamentals |
| [Debugging Techniques](references/debugging-techniques.md) | Debugging Techniques |
| [Common Issues & Solutions](references/common-issues-solutions.md) | Common Issues & Solutions |
| [Performance Debugging](references/performance-debugging.md) | Performance Debugging |

## Best Practices

### ✅ DO

- Use conditional and logpoint breakpoints instead of littering code with `console.log`
- Reproduce issues in an incognito window to rule out extension interference
- Check the Network tab for failed requests, CORS errors, and unexpected response codes before debugging JS logic
- Use the Performance panel's flame chart to pinpoint long tasks blocking the main thread
- Inspect the Accessibility tree alongside the Elements panel when debugging layout for screen readers
- Preserve logs across navigations when debugging redirect-related issues

### ❌ DON'T

- Leave `debugger` statements or verbose `console.log` calls in committed code
- Ignore the Console warnings and deprecation notices — they often foreshadow breakage
- Test only in one browser; verify across Chrome, Firefox, and Safari for cross-browser issues
- Disable cache in DevTools and forget to re-enable it — this masks caching bugs in production
