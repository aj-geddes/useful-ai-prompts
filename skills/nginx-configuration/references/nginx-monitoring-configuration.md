# Nginx Monitoring Configuration

## Nginx Monitoring Configuration

```nginx
# /etc/nginx/conf.d/monitoring.conf
server {
    listen 127.0.0.1:8080;
    server_name localhost;

    # Stub status for monitoring
    location /nginx_status {
        stub_status on;
        access_log off;
        allow 127.0.0.1;
        allow ::1;
        deny all;
    }

    # Prometheus metrics
    location /metrics {
        access_log off;
        proxy_pass http://127.0.0.1:8081/metrics;
        allow 127.0.0.1;
        allow ::1;
        deny all;
    }
}
```
