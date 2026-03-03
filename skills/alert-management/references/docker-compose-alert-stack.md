# Docker Compose Alert Stack

## Docker Compose Alert Stack

```yaml
# docker-compose.yml
version: "3.8"
services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  alertmanager:
    image: prom/alertmanager:latest
    ports:
      - "9093:9093"
    volumes:
      - ./alertmanager.yml:/etc/alertmanager/alertmanager.yml
    environment:
      SLACK_WEBHOOK_URL: ${SLACK_WEBHOOK_URL}
      PAGERDUTY_SERVICE_KEY: ${PAGERDUTY_SERVICE_KEY}
    depends_on:
      - prometheus

  alert-handler:
    build: .
    environment:
      PAGERDUTY_API_TOKEN: ${PAGERDUTY_API_TOKEN}
      SLACK_WEBHOOK_URL: ${SLACK_WEBHOOK_URL}
    ports:
      - "3000:3000"
    depends_on:
      - alertmanager
```
