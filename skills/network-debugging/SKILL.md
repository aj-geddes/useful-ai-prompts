---
name: network-debugging
description: >
  Debug network issues using browser tools and network analysis. Diagnose.
  Use when slow loading times, failed requests, intermittent connectivity, or cors errors.
  connection problems, latency, and data transmission issues.
---

# Network Debugging

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Network debugging identifies connectivity issues, latency problems, and data transmission errors that impact application performance.

## When to Use

- Slow loading times
- Failed requests
- Intermittent connectivity
- CORS errors
- SSL/TLS issues
- API communication problems

## Quick Start

Minimal working example:

```yaml
Chrome DevTools Network Tab:

Columns:
  - Name: Request file/endpoint
  - Status: HTTP status code
  - Type: Resource type (xhr, fetch, etc)
  - Initiator: What triggered request
  - Size: Resource size / transferred size
  - Time: Total time to complete
  - Waterfall: Timeline visualization

Timeline Breakdown:
  - Queueing: Waiting in queue
  - DNS: Domain name resolution
  - Initial connection: TCP handshake
  - SSL: SSL/TLS negotiation
  - Request sent: Time to send request
  - Waiting (TTFB): Time to first byte
  - Content Download: Receiving response

---
Network Conditions:

Throttling Presets:
  - Fast 3G: 1.6 Mbps down, 750 Kbps up
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Browser Network Tools](references/browser-network-tools.md) | Browser Network Tools |
| [Common Network Issues](references/common-network-issues.md) | Common Network Issues |
| [Debugging Tools & Techniques](references/debugging-tools-techniques.md) | Debugging Tools & Techniques |
| [Checklist](references/checklist.md) | Checklist |

## Best Practices

### ✅ DO

- Isolate whether the issue is DNS, TLS, connection, or application layer before diving into code
- Use `curl -w` timing breakdowns or browser DevTools waterfall to pinpoint which phase (DNS, TTFB, download) is slow
- Test with throttled connections and high latency to reproduce issues users experience on mobile or congested networks
- Check CORS preflight responses (`OPTIONS`) separately — a missing header there blocks the actual request silently
- Capture and compare HAR files before and after changes to verify network-level impact of fixes

### ❌ DON'T

- Assume a timeout means the server is down — it could be DNS resolution, a firewall rule, or a proxy misconfiguration
- Ignore certificate chain errors in development by disabling TLS verification — this hides real deployment issues
- Debug network problems solely from the client side; check server access logs, load balancer metrics, and upstream health simultaneously
- Retry failed requests indefinitely without exponential backoff and jitter — this amplifies outages with thundering herd effects
