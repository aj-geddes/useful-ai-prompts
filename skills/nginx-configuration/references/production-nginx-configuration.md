# Production Nginx Configuration

## Production Nginx Configuration

```nginx
# /etc/nginx/nginx.conf
user nginx;
worker_processes auto;
worker_rlimit_nofile 65535;
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
    worker_connections 4096;
    use epoll;
    multi_accept on;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Logging
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

    log_format upstream_time '$remote_addr - $remote_user [$time_local] '
                            '"$request" $status $body_bytes_sent '
                            '"$http_referer" "$http_user_agent" '
                            'rt=$request_time uct="$upstream_connect_time" '
                            'uht="$upstream_header_time" urt="$upstream_response_time"';

    access_log /var/log/nginx/access.log upstream_time buffer=32k flush=5s;

    # Performance optimizations
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    client_max_body_size 20M;

    # Gzip compression
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml text/javascript
               application/json application/javascript application/xml+rss
               application/rss+xml application/atom+xml image/svg+xml;
    gzip_disable "msie6";

    # Rate limiting
    limit_req_zone $binary_remote_addr zone=general:10m rate=10r/s;
    limit_req_zone $binary_remote_addr zone=api:10m rate=100r/m;
    limit_conn_zone $binary_remote_addr zone=connections:10m;

    # Upstream servers
    upstream backend {
        least_conn;
        server backend1.internal:8080 weight=5 max_fails=3 fail_timeout=30s;
        server backend2.internal:8080 weight=5 max_fails=3 fail_timeout=30s;
        server backend3.internal:8080 weight=3 max_fails=3 fail_timeout=30s;
        keepalive 32;
    }

    upstream api_backend {
        least_conn;
        server api1.internal:3000;
        server api2.internal:3000;
        server api3.internal:3000;
        keepalive 64;
    }

    # Caching
    proxy_cache_path /var/cache/nginx/general levels=1:2 keys_zone=general_cache:10m max_size=1g inactive=60m use_temp_path=off;
    proxy_cache_path /var/cache/nginx/api levels=1:2 keys_zone=api_cache:10m max_size=500m inactive=30m use_temp_path=off;

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
```
