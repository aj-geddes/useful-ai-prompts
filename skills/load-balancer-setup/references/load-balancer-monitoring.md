# Load Balancer Monitoring

## Load Balancer Monitoring

```yaml
# prometheus-scrape-config.yaml
scrape_configs:
  - job_name: "haproxy"
    static_configs:
      - targets: ["localhost:8404"]
    metrics_path: "/stats;csv"
    scrape_interval: 15s

  - job_name: "alb"
    cloudwatch_sd_configs:
      - region: us-east-1
        port: 443
    relabel_configs:
      - source_labels: [__meta_aws_cloudwatch_namespace]
        action: keep
        regex: "AWS/ApplicationELB"
```
