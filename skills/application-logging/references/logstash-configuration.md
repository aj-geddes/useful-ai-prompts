# Logstash Configuration

## Logstash Configuration

```conf
# logstash.conf
input {
  tcp {
    port => 5000
    codec => json
  }
}

filter {
  date {
    match => [ "timestamp", "YYYY-MM-dd HH:mm:ss" ]
    target => "@timestamp"
  }

  mutate {
    add_field => { "[@metadata][index_name]" => "logs-%{+YYYY.MM.dd}" }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "%{[@metadata][index_name]}"
  }
}
```
