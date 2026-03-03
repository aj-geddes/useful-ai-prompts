# Logstash Pipeline Configuration

## Logstash Pipeline Configuration

```conf
# logstash.conf
input {
  # Receive logs via TCP/UDP
  tcp {
    port => 5000
    codec => json
  }

  # Read from files
  file {
    path => "/var/log/app/*.log"
    start_position => "beginning"
    codec => multiline {
      pattern => "^%{TIMESTAMP_ISO8601}"
      negate => true
      what => "previous"
    }
  }

  # Read from Kubernetes
  kubernetes {
    kubernetes_url => "https://kubernetes.default"
    ca_file => "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
  }
}

filter {
  # Parse JSON logs
  json {
    source => "message"
    target => "parsed"
  }

  # Extract fields
  grok {
    match => {
      "message" => "%{TIMESTAMP_ISO8601:timestamp} \[%{LOGLEVEL:level}\] %{GREEDYDATA:message}"
    }
  }

  # Add timestamp
  date {
    match => ["timestamp", "ISO8601"]
    target => "@timestamp"
  }

  # Add metadata
  mutate {
    add_field => {
      "environment" => "production"
      "datacenter" => "us-east-1"
    }
    remove_field => ["host"]
  }

  # Drop debug logs in production
  if [level] == "DEBUG" {
    drop { }
  }

  # Tag errors
  if [level] =~ /ERROR|FATAL/ {
    mutate {
      add_tag => ["error"]
    }
  }
}

output {
  # Send to Elasticsearch
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "logs-%{+YYYY.MM.dd}"
    document_type => "_doc"
  }

  # Also output errors to console
  if "error" in [tags] {
    stdout {
      codec => rubydebug
    }
  }
}
```
