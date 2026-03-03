# Kibana Dashboard and Alerts

## Kibana Dashboard and Alerts

```json
{
  "dashboard": {
    "title": "Application Logs Overview",
    "panels": [
      {
        "title": "Error Rate by Service",
        "query": "level: ERROR",
        "visualization": "bar_chart",
        "groupBy": ["service"],
        "timeRange": "1h"
      },
      {
        "title": "Top 10 Error Messages",
        "query": "level: ERROR",
        "visualization": "table",
        "fields": ["message", "count"],
        "sort": [{ "count": "desc" }],
        "size": 10
      },
      {
        "title": "Request Latency Distribution",
        "query": "duration: *",
        "visualization": "histogram"
      },
      {
        "title": "Errors Over Time",
        "query": "level: ERROR",
        "visualization": "line_chart",
        "dateHistogram": "1m"
      }
    ]
  },
  "alerts": [
    {
      "name": "High Error Rate",
      "query": "level: ERROR",
      "threshold": 100,
      "window": "5m",
      "action": "slack"
    },
    {
      "name": "Critical Exceptions",
      "query": "level: FATAL",
      "threshold": 1,
      "window": "1m",
      "action": "email"
    }
  ]
}
```
