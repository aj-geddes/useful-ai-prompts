# Checklist

## Checklist

```yaml
Network Debugging Checklist:

Connection:
  [ ] Internet connectivity verified
  [ ] Firewall allows connection
  [ ] VPN not blocking
  [ ] Proxy configured if needed
  [ ] DNS resolving correctly

Request:
  [ ] Correct URL
  [ ] Correct HTTP method
  [ ] Required headers present
  [ ] Authorization correct
  [ ] Request body valid

Response:
  [ ] Status code expected
  [ ] Response headers correct
  [ ] Content-Type appropriate
  [ ] Response body valid
  [ ] No parsing errors

Performance:
  [ ] DNS lookup <50ms
  [ ] Connection <100ms
  [ ] TTFB <500ms
  [ ] Download reasonable
  [ ] Total time acceptable

Monitoring:
  [ ] Error logging enabled
  [ ] Network metrics tracked
  [ ] Alerts configured
  [ ] Baseline established
```
