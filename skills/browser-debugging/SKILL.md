---
name: browser-debugging
description: >
  Debug client-side issues using browser developer tools. Identify JavaScript
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

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
