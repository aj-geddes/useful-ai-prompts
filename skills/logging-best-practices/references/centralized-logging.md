# Centralized Logging

## Centralized Logging

### ELK Stack (Elasticsearch, Logstash, Kibana)

```yaml
# docker-compose.yml
version: "3"
services:
  elasticsearch:
    image: elasticsearch:8.0.0
    environment:
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ports:
      - "9200:9200"

  logstash:
    image: logstash:8.0.0
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    ports:
      - "5000:5000"
    depends_on:
      - elasticsearch

  kibana:
    image: kibana:8.0.0
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch
```

```conf
# logstash.conf
input {
  tcp {
    port => 5000
    codec => json
  }
}

filter {
  # Parse timestamp
  date {
    match => ["timestamp", "ISO8601"]
  }

  # Add geo-location if IP present
  if [ip] {
    geoip {
      source => "ip"
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "app-logs-%{+YYYY.MM.dd}"
  }
}
```

### Ship Logs to ELK

```typescript
// winston-elk.ts
import winston from "winston";
import "winston-logstash";

const logger = winston.createLogger({
  transports: [
    new winston.transports.Logstash({
      port: 5000,
      host: "logstash",
      node_name: "user-service",
      max_connect_retries: -1,
    }),
  ],
});
```

### AWS CloudWatch Logs

```typescript
// cloudwatch-logger.ts
import winston from "winston";
import WinstonCloudWatch from "winston-cloudwatch";

const logger = winston.createLogger({
  transports: [
    new WinstonCloudWatch({
      logGroupName: "/aws/lambda/user-service",
      logStreamName: () => {
        const date = new Date().toISOString().split("T")[0];
        return `${date}-${process.env.LAMBDA_VERSION}`;
      },
      awsRegion: "us-east-1",
      jsonMessage: true,
    }),
  ],
});
```
