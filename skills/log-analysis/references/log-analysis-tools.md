# Log Analysis Tools

## Log Analysis Tools

```yaml
Log Aggregation:

ELK Stack (Elasticsearch, Logstash, Kibana):
  - Logstash: Parse and process logs
  - Elasticsearch: Search and analyze
  - Kibana: Visualization and dashboards
  - Use: Large scale, complex queries

Splunk:
  - Comprehensive log management
  - Real-time search and analysis
  - Dashboards and alerts
  - Use: Enterprise (expensive)

CloudWatch (AWS):
  - Integrated with AWS services
  - Log Insights for querying
  - Dashboards
  - Use: AWS-based systems

Datadog:
  - Application performance monitoring
  - Log management
  - Real-time alerts
  - Use: SaaS monitoring

---
Log Analysis Techniques:

Grep/Awk: grep "ERROR" app.log
  awk '{print $1, $4}' app.log

Filtering: Filter by timestamp
  Filter by service
  Filter by error type
  Filter by user

Searching: Search for error patterns
  Search for user actions
  Search trace IDs
  Search IP addresses

Aggregation: Count occurrences
  Group by error type
  Calculate duration percentiles
  Rate of errors over time
```
