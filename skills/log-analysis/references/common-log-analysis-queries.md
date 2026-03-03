# Common Log Analysis Queries

## Common Log Analysis Queries

```yaml
Find errors in past hour:
  timestamp: last_1h AND level: ERROR

Track user activity:
  user_id: 12345 AND action: *

Find slow requests:
  duration_ms: >1000 AND level: INFO

Analyze error rate by service:
  level: ERROR | stats count by service

Find failed database operations:
  error.type: "DatabaseError" | stats count

Trace request flow:
  trace_id: "abc123" | sort by timestamp

---

Checklist:

[ ] Structured logging implemented
[ ] All errors logged with context
[ ] Request IDs/trace IDs used
[ ] Sensitive data not logged (passwords, tokens)
[ ] Log levels used appropriately
[ ] Log retention policy set
[ ] Log sampling for high-volume events
[ ] Alerts configured for errors
[ ] Dashboards created
[ ] Regular log review scheduled
[ ] Log analysis tools accessible
[ ] Team trained on querying logs
```
