# Browser Network Tools

## Browser Network Tools

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
  - Slow 3G: 400 Kbps down, 400 Kbps up
  - Offline: No network connection

Custom Settings:
  - Simulate real network speeds
  - Test mobile performance
  - Identify bottlenecks
  - Verify error handling

---
Request Analysis:

Headers:
  - Request headers (what browser sent)
  - Response headers (server response)
  - Cookies (session data)
  - Authorization (tokens)

Preview:
  - JSON formatted view
  - Response data inspection
  - Parse errors highlighted

Response:
  - Full response body
  - Raw vs formatted view
  - File download option

Timing:
  - Detailed timing breakdown
  - Identify slow components
  - DNS lookup time
  - Connection establishment
```
