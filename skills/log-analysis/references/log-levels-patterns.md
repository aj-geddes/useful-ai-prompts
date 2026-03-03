# Log Levels & Patterns

## Log Levels & Patterns

```yaml
Log Levels:

DEBUG: Detailed diagnostic info
  - Variable values
  - Function entry/exit
  - Intermediate calculations
  - Use: Development only

INFO: General informational messages
  - Startup/shutdown
  - User actions
  - Configuration changes
  - Use: Production (normal operations)

WARN: Warning messages (potential issues)
  - Deprecated API usage
  - Performance degradation
  - Resource limits approaching
  - Use: Production (investigate soon)

ERROR: Error conditions
  - Failed operations
  - Exceptions
  - Failed requests
  - Use: Production (action required)

FATAL/CRITICAL: System unusable
  - Critical failures
  - Out of memory
  - Data corruption
  - Use: Production (immediate action)

---

Log Patterns:

Request Logging:
  - Request ID (trace_id)
  - Method + Path
  - Status code
  - Duration
  - Request size / response size

Error Logging:
  - Error type/code
  - Error message
  - Stack trace
  - Context (user_id, session_id)
  - Timestamp

Business Events:
  - Event type
  - User involved
  - Impact/importance
  - Timestamp
  - Relevant context
```
