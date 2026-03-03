# Debugging Tools & Techniques

## Debugging Tools & Techniques

```yaml
Tools:

curl:
  curl -v https://api.example.com
  curl -H "Authorization: Bearer token" https://api.example.com
  curl -X POST -d '{"key": "value"}' https://api.example.com

Postman:
  - GUI for request testing
  - Collection of requests
  - Environment variables
  - Pre/post request scripts
  - Mock servers

Network Inspector:
  - Browser DevTools Network tab
  - Real request/response viewing
  - Request filtering
  - Timing analysis

Traffic Analysis:
  - Charles Proxy (HTTP/HTTPS)
  - Fiddler
  - Wireshark (packet level)
  - tcpdump

---

Analysis Steps:

1. Reproduce Issue
  - Clear cache
  - Disable plugins
  - Disable extensions
  - Try incognito mode

2. Capture Traffic
  - Open Network tab
  - Clear current requests
  - Perform action
  - Observe requests

3. Analyze Requests
  - Check status codes
  - Review headers
  - Inspect payload
  - Check response time

4. Identify Pattern
  - Failed request pattern
  - Timing correlation
  - Specific conditions
  - Data size impact

5. Test Fix
  - Make change
  - Clear cache
  - Reproduce
  - Verify fix
```
