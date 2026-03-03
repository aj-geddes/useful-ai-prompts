# Filebeat Configuration

## Filebeat Configuration

```yaml
# filebeat.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/app/*.log
    fields:
      app: myapp
      environment: production
    multiline.pattern: '^\['
    multiline.negate: true
    multiline.match: after

  - type: docker
    enabled: true
    hints.enabled: true
    hints.default_config:
      enabled: true
      type: container
      paths:
        - /var/lib/docker/containers/${data.docker.container.id}/*.log

  - type: log
    enabled: true
    paths:
      - /var/log/syslog
      - /var/log/auth.log
    fields:
      service: system
      environment: production

processors:
  - add_docker_metadata:
      host: "unix:///var/run/docker.sock"
  - add_kubernetes_metadata:
      in_cluster: true
  - add_host_metadata:
  - add_fields:
      target: ""
      fields:
        environment: production

output.elasticsearch:
  hosts: ["elasticsearch:9200"]
  index: "filebeat-%{+yyyy.MM.dd}"

logging.level: info
logging.to_files: true
logging.files:
  path: /var/log/filebeat
  name: filebeat
  keepfiles: 7
  permissions: 0640
```
